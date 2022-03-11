from abc import ABC, abstractmethod

from .tools import get_num


class Convertor(ABC):
    """
    Converts a chemical formula into the desired format
    """

    OPERATIONS = {"+", "=", ";", "->", "<-", "<>"}

    @classmethod
    def convert(cls, string: str) -> str:
        out = []

        chunks = [c for chunk in string.split() for c in chunk.split(";")]
        for chunk in chunks:
            if chunk in cls.OPERATIONS or len(chunk) == 1:
                out.append(chunk)
                continue

            out.append(cls.mol_convertor(chunk))

        return " ".join(out)

    @classmethod
    def mol_convertor(cls, string: str) -> str:
        """
        Converts a molecular formula to the desired format
        """
        out = ""

        # Leading number: stoichiometric ratio
        if string[0].isnumeric():
            number = get_num(string)
            out += f"{number}$\\cdot$"
            string = string[len(number) :]

        while string:
            increment = 1
            if (char := string[0]).isnumeric():
                number = get_num(string)
                increment = len(number)
                out += cls.subscript_number(number)
            elif char == "^":
                number = get_num(string[1:])
                increment = len(number) + 2
                charge = string[len(number) + 1]
                assert charge in ["-", "+"]
                out += cls.superscript_number_charge(number, charge)
            elif char in ["-", "+"]:
                out += cls.superscript_number_charge("", char)
            else:
                out += char

            string = string[increment:]

        return cls.finalize(out)

    @classmethod
    @abstractmethod
    def subscript_number(cls, number: str) -> str:
        pass

    @classmethod
    @abstractmethod
    def superscript_number_charge(cls, number: str, charge: str) -> str:
        pass

    @classmethod
    def finalize(cls, string: str) -> str:
        return string
