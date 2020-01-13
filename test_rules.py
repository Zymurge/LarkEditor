import unittest
from rules import Rule
from anytree import Node
from interface import implements

class TestRulesInterface(unittest.TestCase):
    def test_name_method(self):
        self.assertTrue( hasattr( Rule, 'Name' ) )

    def test_validate_method(self):
        self.assertTrue( hasattr( Rule, 'Validate' ) )

class MyRule(implements(Rule)):
    @staticmethod
    def Name() -> str:
        return "myrule"

    @staticmethod
    def Validate(line, nodes) -> bool:
        return False if line.find("FAIL") > -1 else True

class TestRuleImplementation(unittest.TestCase):
    def test_name(self):
        self.assertTrue( hasattr( MyRule, 'Name' ) )
        self.assertEqual( MyRule.Name(), "myrule" )

    def test_validate(self):
        self.assertTrue( hasattr( MyRule, 'Validate' ) )
        result = MyRule.Validate("This is a good line", None)
        self.assertTrue(result, "Expect MyRule to pass for line without 'FAIL'")
        result = MyRule.Validate("This is a FAIL line", None)
        self.assertFalse(result, "Expect MyRule to fail for line with 'FAIL'")

