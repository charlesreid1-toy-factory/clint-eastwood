"""
Facts about Dirty Harry (via clinteastwood.net)
"""
import os
import sys
import json
import random
import logging
import argparse

from eastwood.clint import dispatch


logger = logging.getLogger(__name__)


facts = dispatch.target("dirty-harry-facts", arguments={}, help=__doc__)


# Set up dicts with common flag options for all the actions below
json_flag_options = dict(
    default=False, dest='_json', action="store_true", help="format the output as JSON if this flag is present"
)
shout_flag_options = dict(
    default=False, dest='_shout', action="store_true", help="shout the Dirty Harry facts"
)


def print_facts(argv, args, descr, facts):
    if args._shout:
        descr = descr.upper()
        facts = [f.upper() for f in facts]
    if args._json:
        data = dict(descr=descr, facts=facts)
        print(json.dumps(data, indent=4))
    else:
        print()
        print(descr)
        print()
        for fact in facts:
            print(f" - {fact}")
        print()


@facts.action(
    "partner",
    arguments={
        "--json": json_flag_options,
        "--shout": shout_flag_options,
    },
)
def facts_partner(argv, args):
    """
    Facts about Dirty Harry's partner
    """
    descr = "In each Dirty Harry film, Harry's partner is either injured or killed."
    facts = [
        "In 1968 Harry's partner Fanduchi was killed.",
        "In 1971 Harry's partner Dietrick was hospitalized.",
        "Also in 1971, Harry's new partner, Chico Gonzales, was injured and hospitalized after a gun fight with Scorpio. He saved Harry's life. Chico retired from the force and became a school teacher. Frank De Georgio became Harry's partner.",
        "In 1973, Harry was assigned a new partner named Early Smith. Smith was killed when a bomb detonated in his mail box. The bomb was planted by the vigilante cops. De Georgio became Harry's partner again.",
        "In 1976, after being demoted to personnel but before being assigned a new partner Harry's former partner Frank De Georgio, was killed by Bobby Maxwell during a robbery.",
        "In 1976, Harry was assigned a new partner. As the Mayor was trying to boost his popularity he began a new policy of having women on the police force. Harry's new partner was Kate Moore. Kate Moore died on Alcatraz while trying to save the mayor.",
        "In 1983 Harry's partner was Horace King. Harry and Horace were good friends and when Harry got sent to San Paolo, Horace went to visit him. Horace was killed in Harry's apartment.",
        "Until 1988 Harry worked without a partner. After testifying at the Jannero trial, Jannero wanted Harry killed. After an attempt on Harry's life where Harry killed his attackers he was assigned a new partner to cover his back. Al Quan moved into homicide to help Harry. Quan was injured when their car was partially blown up by the Dead Pool killer.",
    ]
    print_facts(argv, args, descr, facts)


@facts.action(
    "zoom",
    arguments={
        "--json": json_flag_options,
        "--shout": shout_flag_options,
    },
)
def facts_zoom(argv, args):
    """
    Facts about zooming in during Dirty Harry films
    """
    descr = "All Dirty Harry films end with the camera zooming out from the action."
    facts = [
        "In Dirty Harry, the camera zooms out as Harry walks away from killing Scorpio and throwing his badge in the water.",
        "In Magnum Force, the camera zooms out as Harry walks away from the burning car of Lieutenant Briggs.",
        "In The Enforcer, the camera zooms out as Harry walks away from the Mayor on Alcatraz Island.",
        "In Sudden Impact, the camera zooms away as Harry and Jennifer Spencer walk away from the amusement park rides.",
        "In The Dead Pool, the camera zooms away as Harry and Samantha Walker leave the pier.",
    ]
    print_facts(argv, args, descr, facts)


@facts.action(
    "fivemin",
    arguments={
        "--json": json_flag_options,
        "--shout": shout_flag_options,
    },
)
def facts_fivemin(argv, args):
    """
    Facts about the first five minutes of Dirty Harry films
    """
    descr = "In each Dirty Harry movie someone is killed within the first 5 minutes."
    facts = [
        "In Dirty Harry, an unknown women is killed by Scorpio while swimming in a rooftop pool.",
        "In Magnum Force, four gangsters are killed after leaving court by a vigilante cop.",
        "In The Enforcer, two gas men are killed by Bobby Maxwell in order to get their uniforms and truck.",
        "In Sudden Impact, a man is killed by Jennifer Spencer as an act of revenge.",
        "In The Dead Pool, Harry kills four gangsters who are ordered by Lou Jannero to kill him.",
    ]
    print_facts(argv, args, descr, facts)


@facts.action(
    "water",
    arguments={
        "--json": json_flag_options,
        "--shout": shout_flag_options,
    },
)
def facts_water(argv, args):
    """
    Facts about bodies of water in the Dirty Harry films
    """
    descr = "Each Dirty Harry film ends near water."
    facts = [
        "In Dirty Harry, Harry shoots Scorpio and sends his body splashing into the water.",
        "In Magnum Force, Harry ends his battle with the two of the vigilante cops on mothballed aircraft carriers in Alameda.",
        "In The Enforcer, Harry blows up Bobby Maxwell in the lighthouse on Alcatraz Island in the middle of San Francisco Bay.",
        "In Sudden Impact, Harry kills Jennifer Spencer's kidnappers on the amusement park boardwalk.",
        "In The Dead Pool, Harry kills Rook on a pier with a harpoon gun.",
    ]
    print_facts(argv, args, descr, facts)
