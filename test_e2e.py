import unittest
import io
from larkedit import LarkEdit

class TestE2E(unittest.TestCase):
    def test_external_file(self):
        test_file = "test_input.txt"
        with open(test_file) as tf:
            data = tf.read()
            results = LarkEdit(data).Validate([LarkEdit.Rule_L_Length, LarkEdit.Rule_L_Children_Count])
        for line in results.split("\n"):
            if len(line) < 1:
                continue
            expect, text, actual = line.split("::")
            expect = expect.strip()
            expectTag = "<good>" if expect == "g" else "<bad>"
            self.assertEqual(actual, expectTag, "incorrect tag for line: {}".format(text) )