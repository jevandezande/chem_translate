from .convertor import Convertor


class LatexConvertor(Convertor):
    """
    Converts a string to latex
    >>> LatexConvertor.convert("H2O + NH3 -> OH- + NH4+")
    'H$_2$O + NH$_3$ -> OH$^-$ + NH$_4^+$'
    """

    @classmethod
    def mol_convertor(cls, string: str) -> str:
        """
        Converts a molecular formula to the desired format
        >>> LatexConvertor.mol_convertor("H2O")
        'H$_2$O'
        >>> LatexConvertor.mol_convertor("(NH4)(PO4)^2-")
        '(NH$_4$)(PO$_4$)$^{2-}$'
        >>> LatexConvertor.mol_convertor("(MgO2)2(PbCl32)3^2-")
        '(MgO$_2$)$_2$(PbCl$_32$)$_3^{2-}$'
        """
        return super().mol_convertor(string)

    @classmethod
    def finalize(cls, string: str) -> str:
        """
        Removes double dollar signs
        >>> LatexConvertor.finalize("$123$$456$")
        '$123456$'
        """
        return string.replace("$$", "")

    @classmethod
    def subscript_number(cls, number: str) -> str:
        """
        Converts a number to subscript
        >>> LatexConvertor.subscript_number("123")
        '$_123$'
        """
        return f"$_{number}$"

    @classmethod
    def superscript_number_charge(cls, number: str, charge: str) -> str:
        """
        Converts a number and charge to superscript
        >>> LatexConvertor.superscript_number_charge("123", "-")
        '$^{123-}$'
        >>> LatexConvertor.superscript_number_charge("", "+")
        '$^+$'
        """
        return f"$^{{{number}{charge}}}$" if number else f"$^{charge}$"
