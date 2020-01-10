import unittest
from larkedit import LarkEdit
from anytree import Node

class TestCtor(unittest.TestCase):
    def test_positive(self):
        dataset = [
            (
                "L1\n\tL1-B1\n\tL1-B2",
                "L1<good>\n\tL1-B1<good>\n\tL1-B2<good>"
            ),
            (
                "L1\n\tL1-B1\n\tL1-B2\nL2\n\tL2-B1\n\t\tL1-B2-L1\n\t\tL1-B2-L2\nL3\n\tL3-B1\n\tL3-B2\n",
                "L1<good>\n\tL1-B1<good>\n\tL1-B2<good>\nL2<good>\n\tL2-B1<good>\n\t\tL1-B2-L1<good>\n\t\tL1-B2-L2<good>\nL3<good>\n\tL3-B1<good>\n\tL3-B2<good>"
            )
        ]
        self.Validate(dataset)

    def test_validation(self):
        dataset = [
            (
                "L1\nL2 FAIL\n\tL2-B1 FAIL\n\tL2-B2\nL3",
                "L1<good>\nL2 FAIL<bad>\n\tL2-B1 FAIL<bad>\n\tL2-B2<good>\nL3<good>"
            ),
            (   "L1\n\tL1-B1\n\t\tL1-B1-L1\n\t\t\tL1-B1-L1-B1\n\t\t\tL1-B1-L1-B2\n\t\t\tL1-B1-L1-B3\n\tL1-B2\nL2",
                "L1<good>\n\tL1-B1<good>\n\t\tL1-B1-L1<bad>\n\t\t\tL1-B1-L1-B1<good>\n\t\t\tL1-B1-L1-B2<good>\n\t\t\tL1-B1-L1-B3<good>\n\tL1-B2<good>\nL2<good>"
            )
        ]
        def Rule_FAIL(line, nodes):
            result = False if line.find("FAIL") > -1 else True
            return result

        rules = [LarkEdit.Rule_L_Length, LarkEdit.Rule_L_Children_Count, Rule_FAIL]
        self.Validate(dataset, rules)

    def Validate(self, dataset, rules=[]):
        for case in dataset:
            testdata, expect = case
            # print("Validating:\n" + testdata)
            lark = LarkEdit(testdata)
            result = lark.Validate(rules)
            self.assertEqual(result, expect)
            self.assertNotEqual(result[:0], "\n", "Should not append a closing blank line")
            lark = ""