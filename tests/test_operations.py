#!/usr/bin/env python
# coding: utf-8

import io
import os
import sys
import uuid
import json
import logging
import argparse
import unittest
import string
import random
import copy
import datetime
import tempfile
import typing

from collections import namedtuple
from unittest import mock

pkg_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # noqa
sys.path.insert(0, pkg_root)  # noqa

# from tests.util import CaptureStdout, SwapStdin
# from tests import skip_on_travis
# from tests.infra import testmode

from eastwood.clint import EastwoodOperationsCommandDispatch
from eastwood.clint import movies


def setUpModule():
    pass


class TestOperations(unittest.TestCase):
    def test_dispatch(self):
        with self.subTest("dispatch without mutually exclusive arguments"):
            self._test_dispatch()

        with self.subTest("dispatch with mutually exclusive arguments"):
            self._test_dispatch(mutually_exclusive=True)

        with self.subTest("dispatch with action overrides"):
            self._test_dispatch(action_overrides=True)

    def _test_dispatch(self, mutually_exclusive=None, action_overrides=False):
        dispatch = EastwoodOperationsCommandDispatch()
        target = dispatch.target(
            "my_target",
            arguments={
                "foo": dict(default="george", type=int),
                "--argument-a": None,
                "--argument-b": dict(default="bar"),
            },
            mutually_exclusive=(["--argument-a", "--argument-b"] if mutually_exclusive else None),
        )

        if action_overrides:

            @target.action("my_action", arguments={"foo": None, "--bar": dict(default="bars")})
            def my_action(argv, args):
                self.assertEqual(args.argument_b, "LSDKFJ")
                self.assertEqual(args.foo, "24")
                self.assertEqual(args.bar, "bars")

        else:

            @target.action("my_action")
            def my_action(argv, args):
                self.assertEqual(args.argument_b, "LSDKFJ")
                self.assertEqual(args.foo, 24)

        dispatch(["my_target", "my_action", "24", "--argument-b", "LSDKFJ"])


# # Check write to output file
# temp_prefix = "dss-test-operations-iam-aws-list-roles-temp-output"
# f, fname = tempfile.mkstemp(prefix=temp_prefix)
# with open(fname, "r") as f:
#     output = f.read()


#    def test_secrets_crud(self):
#        # CRUD (create read update delete) test procedure:
#        # - create new secret
#        # - list secrets and verify new secret shows up
#        # - get secret value and verify it is correct
#        # - update secret value
#        # - get secret value and verify it is correct
#        # - delete secret
#        which_stage = os.environ["Eastwood_DEPLOYMENT_STAGE"]
#        which_store = os.environ["Eastwood_SECRETS_STORE"]
#
#        secret_name = random_alphanumeric_string()
#        testvar_name = f"{which_store}/{which_stage}/{secret_name}"
#        testvar_value = "Hello world!"
#        testvar_value2 = "Goodbye world!"
#
#        unusedvar_name = f"{which_store}/{which_stage}/admin_user_emails"
#
#        with self.subTest("Create a new secret"):
#            # Monkeypatch the secrets manager
#            with mock.patch("dss.operations.secrets.sm_client") as sm:
#                # Creating a new variable will first call get, which will not find it
#                sm.get_secret_value = mock.MagicMock(return_value=None, side_effect=ClientError({}, None))
#                # Next we will use the create secret command
#                sm.create_secret = mock.MagicMock(return_value=None)
#
#                # Create initial secret value:
#                # Dry run first
#                with SwapStdin(testvar_value):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=True, infile=None, quiet=True, force=True
#                        ),
#                    )
#
#                # Provide secret via stdin
#                with SwapStdin(testvar_value):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=False, infile=None, quiet=True, force=True
#                        ),
#                    )
#
#                # Provide secret via infile
#                with tempfile.NamedTemporaryFile(prefix='dss-test-operations-new-secret-temp-input', mode='w') as f:
#                    f.write(testvar_value)
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=False, infile=f.name, force=True, quiet=True
#                        ),
#                    )
#
#                # Check error-catching with non-existent infile
#                mf = 'this-file-is-not-here'
#                with self.assertRaises(RuntimeError):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=False, infile=mf, force=True, quiet=True
#                        ),
#                    )
#
#        with self.subTest("List secrets"):
#            with mock.patch("dss.operations.secrets.sm_client") as sm:
#                # Listing secrets requires creating a paginator first,
#                # so mock what the paginator returns
#                class MockPaginator(object):
#                    def paginate(self):
#                        # Return a mock page from the mock paginator
#                        return [{"SecretList": [{"Name": testvar_name}, {"Name": unusedvar_name}]}]
#                sm.get_paginator.return_value = MockPaginator()
#
#                # Non-JSON output first
#                with CaptureStdout() as output:
#                    secrets.list_secrets([], argparse.Namespace(json=False))
#                self.assertIn(testvar_name, output)
#
#                # JSON output
#                with CaptureStdout() as output:
#                    secrets.list_secrets([], argparse.Namespace(json=True))
#                all_secrets_output = json.loads("\n".join(output))
#                self.assertIn(testvar_name, all_secrets_output)
#
#        with self.subTest("Get secret value"):
#            with mock.patch("dss.operations.secrets.sm_client") as sm:
#                # Requesting the variable will try to get secret value and succeed
#                sm.get_secret_value.return_value = {"SecretString": testvar_value}
#                # Now run get secret value in JSON mode and non-JSON mode
#                # and verify variable name/value is in both.
#
#                # New output file
#                with tempfile.NamedTemporaryFile(prefix='dss-test-operations-get-secret-temp-output', mode='w') as f:
#                    # Try to overwrite outfile without --force
#                    with self.assertRaises(RuntimeError):
#                        secrets.get_secret(
#                            [], argparse.Namespace(secret_name=testvar_name, outfile=f.name, force=False)
#                        )
#
#                    # Overwrite outfile with --force
#                    secrets.get_secret(
#                        [], argparse.Namespace(secret_name=testvar_name, outfile=f.name, force=True)
#                    )
#                    with open(f.name, 'r') as fr:
#                        file_contents = fr.read()
#                    self.assertIn(testvar_value, file_contents)
#
#                # Output secret to stdout
#                with CaptureStdout() as output:
#                    secrets.get_secret(
#                        [], argparse.Namespace(secret_name=testvar_name, outfile=None, force=False)
#                    )
#                self.assertIn(testvar_value, "\n".join(output))
#
#        with self.subTest("Update existing secret"):
#            with mock.patch("dss.operations.secrets.sm_client") as sm:
#                # Updating the variable will try to get secret value and succeed
#                sm.get_secret_value = mock.MagicMock(return_value={"SecretString": testvar_value})
#                # Next we will call the update secret command
#                sm.update_secret = mock.MagicMock(return_value=None)
#
#                # Update secret:
#                # Dry run first
#                with SwapStdin(testvar_value2):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=True, infile=None, force=True, quiet=True
#                        ),
#                    )
#
#                # Use stdin
#                with SwapStdin(testvar_value2):
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=False, infile=None, force=True, quiet=True
#                        ),
#                    )
#
#                # Use input file
#                with tempfile.NamedTemporaryFile(prefix='dss-test-operations-update-secret-temp-input', mode='w') as f:
#                    f.write(testvar_value2)
#                    secrets.set_secret(
#                        [],
#                        argparse.Namespace(
#                            secret_name=testvar_name, dry_run=False, infile=f.name, force=True, quiet=True
#                        ),
#                    )
#
#        with self.subTest("Delete secret"):
#            with mock.patch("dss.operations.secrets.sm_client") as sm:
#                # Deleting the variable will try to get secret value and succeed
#                sm.get_secret_value = mock.MagicMock(return_value={"SecretString": testvar_value})
#                sm.delete_secret = mock.MagicMock(return_value=None)
#
#                # Delete secret
#                # Dry run first
#                secrets.del_secret(
#                    [], argparse.Namespace(secret_name=testvar_name, force=True, dry_run=True, quiet=True)
#                )
#
#                # Real thing
#                secrets.del_secret(
#                    [], argparse.Namespace(secret_name=testvar_name, force=True, dry_run=False, quiet=True)
#                )
#
#    def test_ssmparams_utilities(self):
#        prefix = f"/{os.environ['Eastwood_PARAMETER_STORE']}/{os.environ['Eastwood_DEPLOYMENT_STAGE']}"
#        gold_var = f"{prefix}/dummy_variable"
#
#        var = "dummy_variable"
#        new_var = fix_ssm_variable_prefix(var)
#        self.assertEqual(new_var, gold_var)
#
#        var = "/dummy_variable"
#        new_var = fix_ssm_variable_prefix(var)
#        self.assertEqual(new_var, gold_var)
#
#        var = f"{prefix}/dummy_variable"
#        new_var = fix_ssm_variable_prefix(var)
#        self.assertEqual(new_var, gold_var)
#
#        var = f"{prefix}/dummy_variable/"
#        new_var = fix_ssm_variable_prefix(var)
#        self.assertEqual(new_var, gold_var)
#
#    def test_ssmparams_crud(self):
#        # CRUD (create read update delete) test for setting environment variables in SSM param store
#        testvar_name = random_alphanumeric_string()
#        testvar_value = "Hello world!"
#
#        # Assemble environment to return
#        old_env = {"DUMMY_VARIABLE": "dummy_value"}
#        new_env = dict(**old_env)
#        new_env[testvar_name] = testvar_value
#        ssm_new_env = self._wrap_ssm_env(new_env)
#
#        with self.subTest("Print the SSM environment"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm:
#                # listing params will call ssm.get_parameter to get the entire environment
#                ssm.get_parameter = mock.MagicMock(return_value=ssm_new_env)
#
#                # Now call our params.py module. Output var=value on each line.
#                with CaptureStdout() as output:
#                    lambda_params.ssm_environment([], argparse.Namespace(json=False))
#                self.assertIn(f"{testvar_name}={testvar_value}", output)
#
#    def test_lambdaparams_crud(self):
#        # CRUD (create read update delete) test for setting lambda function environment variables
#        testvar_name = random_alphanumeric_string()
#        testvar_value = "Hello world!"
#        testvar_value2 = "Goodbye world!"
#
#        # Assemble an old and new environment to return
#        old_env = {"DUMMY_VARIABLE": "dummy_value"}
#        new_env = dict(**old_env)
#        new_env[testvar_name] = testvar_value
#
#        ssm_old_env = self._wrap_ssm_env(old_env)
#        ssm_new_env = self._wrap_ssm_env(new_env)
#
#        lam_old_env = self._wrap_lambda_env(old_env)
#        lam_new_env = self._wrap_lambda_env(new_env)
#
#        with self.subTest("Create a new lambda parameter"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm, \
#                    mock.patch("dss.operations.lambda_params.lambda_client") as lam:
#
#                # If this is not a dry run, lambda_set in params.py
#                # will update the SSM first, so we mock those first.
#                # Before we have set the new test variable for the
#                # first time, we will see the old environment.
#                ssm.put_parameter = mock.MagicMock(return_value=None)
#                ssm.get_parameter = mock.MagicMock(return_value=ssm_old_env)
#
#                # The lambda_set func in params.py will update lambdas,
#                # so we mock the calls that those will make too.
#                lam.get_function = mock.MagicMock(return_value=None)
#                lam.get_function_configuration = mock.MagicMock(return_value=lam_old_env)
#                lam.update_function_configuration = mock.MagicMock(return_value=None)
#
#                with SwapStdin(testvar_value):
#                    lambda_params.lambda_set(
#                        [], argparse.Namespace(name=testvar_name, dry_run=True, quiet=True)
#                    )
#
#                with SwapStdin(testvar_value):
#                    lambda_params.lambda_set(
#                        [], argparse.Namespace(name=testvar_name, dry_run=False, quiet=True)
#                    )
#        with self.subTest("List lambda parameters"):
#            with mock.patch("dss.operations.lambda_params.lambda_client") as lam:
#                # The lambda_list func in params.py calls get_deployed_lambas, which calls lam.get_function()
#                # using daemon folder names (this function is called only to ensure no exception is thrown)
#                lam.get_function = mock.MagicMock(return_value=None)
#                # Next we call get_deployed_lambda_environment(), which calls lam.get_function_configuration
#                # (this returns the mocked new env vars json)
#                lam.get_function_configuration = mock.MagicMock(return_value=lam_new_env)
#                # Used to specify a lambda by name
#                stage = os.environ["Eastwood_DEPLOYMENT_STAGE"]
#
#                # Non-JSON fmt
#                with CaptureStdout() as output:
#                    lambda_params.lambda_list([], argparse.Namespace(json=False))
#                # Check that all deployed lambdas are present
#                for lambda_name in lambda_params.get_deployed_lambdas(quiet=True):
#                    self.assertIn(f"{lambda_name}", output)
#
#                # JSON fmt
#                with CaptureStdout() as output:
#                    lambda_params.lambda_list([], argparse.Namespace(json=True))
#                # Check that all deployed lambdas are present
#                all_lams_output = json.loads("\n".join(output))
#                for lambda_name in lambda_params.get_deployed_lambdas(quiet=True):
#                    self.assertIn(lambda_name, all_lams_output)
#
#        with self.subTest("Get environments of each lambda function"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm, \
#                    mock.patch("dss.operations.lambda_params.lambda_client") as lam:
#
#                # lambda_environment() function in dss/operations/lambda_params.py calls get_deployed_lambdas()
#                #   (which only does local operations)
#                # then it calls get_deployed_lambda_environment() on every lambda,
#                #   which calls lambda_client.get_function() (only called to ensure no exception is thrown)
#                lam.get_function = mock.MagicMock(return_value=None)
#                #   then calls lambda_client.get_function_configuration()
#                lam.get_function_configuration = mock.MagicMock(return_value=lam_new_env)
#
#                # TODO: reduce copypasta
#
#                # Non-JSON, no lambda name specified
#                with CaptureStdout() as output:
#                    lambda_params.lambda_environment([], argparse.Namespace(lambda_name=None, json=False))
#                # Check that all deployed lambdas are present
#                output = "\n".join(output)
#                for lambda_name in lambda_params.get_deployed_lambdas(quiet=True):
#                    self.assertIn(lambda_name, output)
#
#                # Non-JSON, lambda name specified
#                with CaptureStdout() as output:
#                    lambda_params.lambda_environment([], argparse.Namespace(lambda_name=f"dss-{stage}", json=False))
#                output = "\n".join(output)
#                self.assertIn(f"dss-{stage}", output)
#
#                # JSON, no lambda name specified
#                with CaptureStdout() as output:
#                    lambda_params.lambda_environment([], argparse.Namespace(lambda_name=None, json=True))
#                # Check that all deployed lambdas are present
#                all_lams_output = json.loads("\n".join(output))
#                for lambda_name in lambda_params.get_deployed_lambdas(quiet=True):
#                    self.assertIn(lambda_name, all_lams_output)
#
#                # JSON, lambda name specified
#                with CaptureStdout() as output:
#                    lambda_params.lambda_environment([], argparse.Namespace(lambda_name=f"dss-{stage}", json=True))
#                all_lams_output = json.loads("\n".join(output))
#                self.assertIn(f"dss-{stage}", all_lams_output)
#
#        with self.subTest("Update (set) existing lambda parameters"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm, \
#                    mock.patch("dss.operations.lambda_params.lambda_client") as lam:
#                # Mock the same way we did for create new param above.
#                # First we mock the SSM param store
#                ssm.get_parameter = mock.MagicMock(return_value=ssm_new_env)
#                ssm.put_parameter = mock.MagicMock(return_value=None)
#                # Next we mock the lambda client
#                lam.get_function = mock.MagicMock(return_value=None)
#                lam.get_function_configuration = mock.MagicMock(return_value=lam_new_env)
#                lam.update_function_configuration = mock.MagicMock(return_value=None)
#
#                # Dry run then real (mocked) thing
#                with SwapStdin(testvar_value2):
#                    lambda_params.lambda_set(
#                        [], argparse.Namespace(name=testvar_name, dry_run=True, quiet=True)
#                    )
#                with SwapStdin(testvar_value2):
#                    lambda_params.lambda_set(
#                        [], argparse.Namespace(name=testvar_name, dry_run=False, quiet=True)
#                    )
#
#        with self.subTest("Update lambda environment stored in SSM store under $Eastwood_DEPLOYMENT_STAGE/environment"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm, \
#                    mock.patch("dss.operations.lambda_params.lambda_client") as lam, \
#                    mock.patch("dss.operations.lambda_params.es_client") as es, \
#                    mock.patch("dss.operations.lambda_params.sm_client") as sm, \
#                    mock.patch("dss.operations.lambda_params.set_ssm_environment") as set_ssm:
#                # If we call lambda_update in dss/operations/lambda_params.py,
#                #   it calls get_local_lambda_environment()
#                #   (local operations only)
#                # lambda_update() then calls set_ssm_environment(),
#                #   which we mocked above into set_ssm
#                set_ssm = mock.MagicMock(return_value=None) # noqa
#
#                ssm.put_parameter = mock.MagicMock(return_value=None)
#
#                # get_elasticsearch_endpoint() calls es.describe_elasticsearch_domain()
#                es_endpoint_secret = {
#                    "DomainStatus": {
#                        "Endpoint": "this-invalid-es-endpoint-value-comes-from-dss-test-operations"
#                    }
#                }
#                es.describe_elasticsearch_domain = mock.MagicMock(
#                    return_value=es_endpoint_secret
#                )
#
#                # get_admin_emails() calls sm.get_secret_value() several times:
#                # - google service acct secret (json string)
#                # - admin email secret
#                # use side_effect when returning multiple values
#                google_service_acct_secret = json.dumps(
#                    {"client_email": "this-invalid-email-comes-from-dss-test-operations"}
#                )
#                admin_email_secret = "this-invalid-email-list-comes-from-dss-test-operations"
#
#                # Finally, we call set_ssm_environment
#                # which calls ssm.put_parameter()
#                # (mocked above).
#
#                # If we also update deployed lambdas:
#                # get_deployed_lambdas() -> lam_client.get_function()
#                # get_deployed_lambda_environment() -> lam_client.get_function_configuration()
#                # set_deployed_lambda_environment() -> lam_client.update_function_configuration()
#                lam.get_function = mock.MagicMock(return_value=None)
#                lam.get_function_configuration = mock.MagicMock(return_value=lam_new_env)
#                lam.update_function_configuration = mock.MagicMock(return_value=None)
#
#                # The function sm.get_secret_value() must return things in the right order
#                # Re-mock it before each call
#                email_side_effect = [
#                    self._wrap_secret(google_service_acct_secret),
#                    self._wrap_secret(admin_email_secret),
#                ]
#
#                # Dry run, then real (mocked) thing
#                sm.get_secret_value = mock.MagicMock(side_effect=email_side_effect)
#                lambda_params.lambda_update(
#                    [], argparse.Namespace(update_deployed=False, dry_run=True, force=True, quiet=True)
#                )
#                sm.get_secret_value = mock.MagicMock(side_effect=email_side_effect)
#                lambda_params.lambda_update(
#                    [], argparse.Namespace(update_deployed=False, dry_run=False, force=True, quiet=True)
#                )
#                sm.get_secret_value = mock.MagicMock(side_effect=email_side_effect)
#                lambda_params.lambda_update(
#                    [], argparse.Namespace(update_deployed=True, dry_run=False, force=True, quiet=True)
#                )
#
#        with self.subTest("Unset lambda parameters"):
#            with mock.patch("dss.operations.lambda_params.ssm_client") as ssm, \
#                    mock.patch("dss.operations.lambda_params.lambda_client") as lam:
#                # If this is not a dry run, lambda_set in params.py
#                # will update the SSM first, so we mock those first.
#                # Before we have set the new test variable for the
#                # first time, we will see the old environment.
#                ssm.put_parameter = mock.MagicMock(return_value=None)
#                # use deepcopy here to prevent delete operation from being permanent
#                ssm.get_parameter = mock.MagicMock(return_value=copy.deepcopy(ssm_new_env))
#
#                # The lambda_set func in params.py will update lambdas,
#                # so we mock the calls that those will make too.
#                lam.get_function = mock.MagicMock(return_value=None)
#                # use side effect here, and copy the environment for each lambda, so that deletes won't be permanent
#                lam.get_function_configuration = mock.MagicMock(
#                    side_effect=[copy.deepcopy(lam_new_env) for j in get_deployed_lambdas()]
#                )
#                lam.update_function_configuration = mock.MagicMock(return_value=None)
#
#                lambda_params.lambda_unset([], argparse.Namespace(name=testvar_name, dry_run=True, quiet=True))
#                lambda_params.lambda_unset([], argparse.Namespace(name=testvar_name, dry_run=False, quiet=True))
#
#    def test_events_operations_journal(self):
#        with self.subTest("Should forward to lambda when `starting_journal_id` is `None`"):
#            self._test_events_operations_journal(None, 0, 2)
#
#        with self.subTest("Should execute journaling when `starting_journal_id` is not `None`"):
#            self._test_events_operations_journal("blah", 1, 0)
#
#    def _test_events_operations_journal(self,
#                                        starting_journal_id: str,
#                                        expected_journal_flashflood_calls: int,
#                                        expected_sqs_messenger_calls: int):
#        sqs_messenger = mock.MagicMock()
#        with mock.patch("dss.operations.events.SQSMessenger", return_value=sqs_messenger), \
#                mock.patch("dss.operations.events.list_new_flashflood_journals"), \
#                mock.patch("dss.operations.events.journal_flashflood") as journal_flashflood, \
#                mock.patch("dss.operations.events.monitor_logs"):
#            args = argparse.Namespace(prefix="pfx",
#                                      number_of_events=5,
#                                      starting_journal_id=starting_journal_id,
#                                      job_id=None)
#            events.journal([], args)
#            self.assertEqual(expected_journal_flashflood_calls, len(journal_flashflood.mock_calls))
#            self.assertEqual(expected_sqs_messenger_calls, len(sqs_messenger.mock_calls))
#
#    def _wrap_ssm_env(self, e):
#        """
#        Package up the SSM environment the way AWS returns it.
#        :param dict e: the dict containing the environment to package up and send to SSM store at
#            $Eastwood_DEPLOYMENT_STAGE/environment.
#        """
#        # Value should be serialized JSON
#        ssm_e = {"Parameter": {"Name": "environment", "Value": json.dumps(e)}}
#        return ssm_e
#
#    def _wrap_lambda_env(self, e):
#        """
#        Package up the lambda environment (a.k.a. function configuration) the way AWS returns it.
#        :param dict e: the dict containing the lambda function's environment variables
#        """
#        # Value should be a dict (NOT a string)
#        lam_e = {"Environment": {"Variables": e}}
#        return lam_e
#
#    def _wrap_secret(self, val):
#        """
#        Package up the secret the way AWS returns it.
#        """
#        return {"SecretString": val}


if __name__ == "__main__":
    unittest.main()
