from anytree import Node, LevelOrderIter, RenderTree

class LarkTree:

    def __init__(self, text):
        super().__init__()
        self.root = Node("root")
        self.lines = text.split('\n')
        self.nodes = []
        self.__parse(self.lines)

    def __parse(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i]
            if len(line.strip()) < 1:  # skip over and remove lines lacking any body
                lines.remove(line)
                continue 
            level = self.LevelFromLeadingTabCount(line)
            myParent = self.LastNodeAtLevel(level - 1)
            self.nodes.append( Node(i, parent=myParent) )
            i += 1

    def LastNodeAtLevel(self, level):
        """Anytree counts 1 based levels, inclusive of the root.
           I want the root to be invisible and 1 based level numbers starting from no leading tab
           Therefore levels are off by 1"""
        nodes_list = list( LevelOrderIter(self.root, maxlevel=level + 1) )
        return nodes_list[-1] if nodes_list else self.root

    def StringFromNode(self, node):
        if type(node.name) is int:
            return self.lines[node.name] 
        else:
            return None
                
    @staticmethod 
    def LevelFromLeadingTabCount(line):
        c = 0
        while c < len(line):
            if line[c] == '\t':
                c += 1
            else:
                return c + 1

def Main():
    text = "".join( [
            "\tCall me line 2\n",
            "\tAnd I'm the third\n",
            "Let's start a new node here\n",
            "\tand another\n",
            "\tone more for grins\n",
            "\t\tNew sub sub\n"
        ] )
    tree = LarkTree(text)
    #print(RenderTree(nodes[0]))
    for pre, _, node in RenderTree(tree.root):
        name = tree.StringFromNode(node).strip() if not node.is_root else "root"
        print("%s%s: %s" % (pre, node.name, name))

if __name__ == "__main__":
    Main()

