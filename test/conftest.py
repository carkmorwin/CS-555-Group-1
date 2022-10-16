import random
from datetime import datetime, timedelta

import pytest
from gedcom.family import Family
from gedcom.individual import Individual


@pytest.fixture
def future_date():
    return datetime.now().date() + timedelta(days=random.randint(0, 10000))


@pytest.fixture
def previous_date():
    return datetime.now().date() + timedelta(days=-random.randint(0, 10000))


@pytest.fixture
def today():
    return datetime.now().date()


@pytest.fixture
def individual():
    return Individual("I" + str(random.randint(0, 10000)))


@pytest.fixture
def family():
    return Family("F" + str(random.randint(0, 10000)))


@pytest.fixture
def make_individual():
    def make_individual():
        return Individual("I" + str(random.randint(0, 10000)))

    return make_individual


@pytest.fixture
def husband(make_individual):
    husband = make_individual()
    husband.sex = "M"

    return husband


@pytest.fixture
def wife(make_individual):
    wife = make_individual()
    wife.sex = "F"

    return wife


@pytest.fixture
def family_with_husband_and_wife(family, husband, wife):
    family.husband_id = husband.id
    family.wife_id = wife.id
    family.married = True

    return (family, husband, wife)


@pytest.fixture
def add_siblings_to_family():
    def add_siblings(family, num_siblings):
        for _ in range(num_siblings):
            family.children_ids.append("I" + str(random.randint(0, 10000)))

    return add_siblings
