"""
This file provides an interface to build the Eastwood operations CLI.

Commands are defined with a target-action model.

Command arguments configured at the target level are moved into the action arguments.

e.g
```
dispatch = EastwoodOperationsCommandDispatch()

storage = dispatch.target("storage", arguments={"--replica": dict(choices=["dev", "integration", "staging", "prod"])})

@storage.action("verify-referential-integrity")
def verify_ref_integrity(argv, args):
    ...

# execution:
scripts/ops.py storage verify-referential-integrity --replica staging
```
"""
import os
import logging
import argparse
from argparse import RawTextHelpFormatter
import traceback


logger = logging.getLogger(__name__)


class _target:
    def __init__(self, target_name, dispatcher):
        self.target_name = target_name
        self.dispatcher = dispatcher

    def action(self, name: str, *, arguments: dict=None, mutually_exclusive: list=None):
        dispatcher = self.dispatcher
        arguments = arguments or dict()
        if mutually_exclusive is None:
            mutually_exclusive = dispatcher.targets[self.target_name]['mutually_exclusive'] or list()

        def register_action(obj):
            parser = dispatcher.targets[self.target_name]['subparser'].add_parser(
                name,
                help=obj.__doc__,
                formatter_class=RawTextHelpFormatter
            )
            action_arguments = dispatcher.targets[self.target_name]['arguments'].copy()
            action_arguments.update(arguments)
            for argname, kwargs in action_arguments.items():
                if argname not in mutually_exclusive:
                    parser.add_argument(argname, **(kwargs or dict()))
            if mutually_exclusive:
                group = parser.add_mutually_exclusive_group(required=True)
                for argname in mutually_exclusive:
                    kwargs = action_arguments.get(argname) or dict()
                    group.add_argument(argname, **kwargs)
            parser.set_defaults(func=obj)
            dispatcher.actions[obj] = dict(target=dispatcher.targets[self.target_name], name=name)
            return obj
        return register_action

class EastwoodOperationsCommandDispatch:
    """
    Grand central dispatch for Eastwood operations
   
                              .
                        .MMMMMP    Go ahead. Make my day.
                      .MM888MM
....                .MM88888MP
MMMMMMMMb.         d8MM8tt8MM
 MM88888MMMMc `:' dMME8ttt8MM
  MM88tt888EMMc:dMM8E88tt88MP
   MM8ttt888EEM8MMEEE8E888MC
   `MM888t8EEEM8MMEEE8t8888Mb
    "MM88888tEM8"MME88ttt88MM
     dM88ttt8EM8"MMM888ttt8MM
     MM8ttt88MM" " "MMNICKMM"
     3M88888MM"      "MMMP"
      "MNICKM"
   
    """
    targets: dict = dict()
    actions: dict = dict()

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.__doc__, formatter_class=RawTextHelpFormatter)
        self.parser_targets = self.parser.add_subparsers()

    def target(self, name: str, *, arguments: dict=None, mutually_exclusive: list=None, help=None):
        arguments = arguments or dict()
        target = self.parser_targets.add_parser(name, help=help)
        self.targets[name] = dict(subparser=target.add_subparsers(),
                                  arguments=arguments,
                                  mutually_exclusive=mutually_exclusive)
        return _target(name, self)

    def __call__(self, argv):
        try:
            args = self.parser.parse_args(argv)
            action_handler = args.func(argv, args) if isinstance(args.func, type) else args.func
            try:
                action_handler(argv, args)
            except Exception:
                logger.error(traceback.format_exc())
        except SystemExit:
            pass
        except AttributeError:
            self.parser.print_help()

dispatch = EastwoodOperationsCommandDispatch()

