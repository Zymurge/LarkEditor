from larktree import LarkTree
from anytree import Node

class LarkEdit:

    def __init__(self, text):
        super().__init__()
        self.text = text
        self.tree = LarkTree(text)

    def Validate(self, rules):
        result = ""
        for i in range(len(self.tree.lines)):
            valid = True
            for rule in rules:
                if not rule(self.tree.lines[i], self.tree.nodes[i]):
                    valid = False
                    print("Rule fail: {} for line '{}': ".format(rule.__name__, self.tree.lines[i]))
                    break
            result += self.tree.lines[i] + ("<good>" if valid else "<bad>")
            result += "\n" if i < len(self.tree.lines)-1 else ""
        return result

    @staticmethod
    def Rule_L_Length(line, node):
        return len( line.strip() ) <= 80

    @staticmethod
    def Rule_L_Children_Count(line, node):
        # print("Rule_L_Children_Count: depth {}, children {} for '{}'".format(node.depth, len(node.children), line))
        if(node.depth%2):
            return len(node.children) < 3
        else:
            return True