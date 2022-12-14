from gedcom.parser import Parser
from gedcom.Tests.US22 import *

class TestUS22:
    def test_empty_roles(self):
        parser = Parser(None)
        
        US22_Test(parser)
        assert US22_Problems


    def test_unique_ids(self, individual, family):
        parser = Parser(None)
        
        unique_individual_id, unique_family_id = ["I10001", "I10002",], ["F21000", "F210001"]

        parser.individuals = {
            individual.id: unique_individual_id,
            family.id: unique_family_id
        }

        US22_Test(parser)
        assert US22_Problems


    def test_duplicate_ids(self, individual, family):
        parser = Parser(None)
        
        duplicate_individual_id, duplicate_family_id = ["I10001", "I10001",], ["F21000", "F210000"]

        parser.individuals = {
            individual.id: duplicate_individual_id,
            family.id: duplicate_family_id
        }

        US22_Test(parser)
        assert US22_Problems
        


