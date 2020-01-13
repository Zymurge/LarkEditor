from interface import implements, Interface

class Rule(Interface):

    @staticmethod
    def Name() -> str:
        pass

    @staticmethod
    def Validate(line, nodes) -> bool:
        pass


class Length(implements(Rule)):

    @staticmethod
    def Name() -> str:
        return "length"

    @staticmethod
    def Validate(line, nodes):
        return len( line.strip() ) <= 80
