import unittest
from larktree import LarkTree
from anytree import Node

class TestLevelFromLeadingTabCount(unittest.TestCase):
    def test_positive(self):
        dataset = [
            ("I have not leading tabs", 1),
            ("\tOne tab here", 2),
            ("\t\t\tthree tabs anybody?", 4)
        ]
        for case in dataset:
            input, expect = case
            result = LarkTree.LevelFromLeadingTabCount(input)
            self.assertEqual(result, expect)

    def test_negative(self):
        dataset = [
            ("", None),
            ("\tOne tab\tplus embedded", 2),
            ("\t\t\t", None)
        ]
        for case in dataset:
            input, expect = case
            result = LarkTree.LevelFromLeadingTabCount(input)
            self.assertEqual(result, expect)

class TestLastNodeAtLevel(unittest.TestCase):
    def test_positive(self):
        tree = TestTree()
        dataset = [
            (4, tree.nodes[9]),
            (3, tree.nodes[8]),
            (1, tree.nodes[2]),
            (0, tree.root)
        ]
        for case in dataset:
            input, expect = case
            result = tree.LastNodeAtLevel(input)
            self.assertEqual(result, expect)

    def test_negative(self):
        tree = TestTree()
        dataset = [
            (5, tree.nodes[9])
        ]
        for case in dataset:
            input, expect = case
            result = tree.LastNodeAtLevel(input)
            self.assertEqual(result, expect)
            
class TestStringFromNode(unittest.TestCase):
    def test_positive(self):
        tree = TestTree()
        dataset = [
            (tree.nodes[9], "\t\t\tL3,2,3 - 9"),
            (tree.nodes[0], "L:1 - 0"),
            (tree.root, None)
        ]
        for case in dataset:
            input, expect = case
            result = tree.StringFromNode(input)
            self.assertEqual(result, expect)

class TestParse(unittest.TestCase):
    def test_positive(self):
        dataset = [
            ("blah,blah,blah", 1),  # Single row
            ("row one\nrow two\nrow three", 3), # three level 1 rows
            ("L1\n\tL1-B1,\t\nL1-B2,\n\t\tL1-B2-L1\n\t\t\tL1-B2-L1-B1", 5), # simple nesting
            ("row one\nrow two\nrow three\n", 3), # trailing return should be ignored
            ("L1\n\nafter blank\nrow three\n\t\t\nafter blank with tabs\n\tfiller", 5) # embedded blank lines should be ignored, with or without tabs
        ]
        for case in dataset:
            input, expect = case
            result = LarkTree(input)
            self.assertEqual(len(result.lines), expect)

def TestTree():
    text = \
"""L:1 - 0
\tL1,1 - 1
L:2 - 2
\tL2,1 - 3
\t\tL3,1 - 4
\t\tL:3,2 - 5
\t\t\tL:3,2,1 - 6
\t\t\tL:3,2,2 - 7
\t\tL3,2 - 8
\t\t\tL3,2,3 - 9
\tL2,2 - 10
\tL2,3 - 11
\tL2,4 - 12"""
    return LarkTree(text)        

if __name__ == '__main__':
    unittest.main()