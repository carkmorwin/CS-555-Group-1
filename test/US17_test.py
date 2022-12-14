from os import path

import random
from datetime import datetime, timedelta

import pytest
from gedcom.parser import Parser
from gedcom import US17
from gedcom.family import Family
from gedcom.individual import Individual


@pytest.fixture
def individuals():
    INPUT_FILE_PATH = path.join(
        path.dirname(path.realpath(__file__)), "..", "input2.ged"
    )
    OUTPUT_FILE_PATH = path.join(
        path.dirname(path.realpath(__file__)), "..", "results.txt"
    )

    with open(INPUT_FILE_PATH) as infile:
        parser = Parser(infile)
        parser.parse()

    return parser.individuals

    # return Individual("I" + str(random.randint(0, 10000)));


@pytest.fixture
def families():
    INPUT_FILE_PATH = path.join(
        path.dirname(path.realpath(__file__)), "..", "input2.ged"
    )
    OUTPUT_FILE_PATH = path.join(
        path.dirname(path.realpath(__file__)), "..", "results.txt"
    )

    with open(INPUT_FILE_PATH) as infile:
        parser = Parser(infile)
        parser.parse()

    return parser.families

    # return Family("F" + str(random.randint(0, 10000)));


# No bigamy
class TestUS17:
    def test_individual_no_bigamy(self, individuals, families):
        # INPUT_FILE_PATH = path.join(path.dirname(path.realpath(__file__)), "..\input2.ged");
        # OUTPUT_FILE_PATH = path.join(path.dirname(path.realpath(__file__)), "..\results.txt");

        # with open(INPUT_FILE_PATH) as infile:
        #    parser = Parser(infile);
        #    parser.parse();

        # errors = US17.US17({}, {family.id: family})
        # errors = US17.US17({}, hParser.individuals, hParser.families).US17_Problems;
        errors = US17.US17_ex(individuals, families)
        assert len(errors) == 0