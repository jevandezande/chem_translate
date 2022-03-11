from .convertor import Convertor


class UnicodeConvertor(Convertor):
    """
    Converts a string to unicode
    >>> UnicodeConvertor.convert("H2O + NH3 -> OH- + NH4+")
    'H₂O + NH₃ -> OH⁻ + NH₄⁺'
    """

    @classmethod
    def subscript_number(cls, number: str) -> str:
        """
        Converts a number to subscript
        >>> UnicodeConvertor.subscript_number("123")
        '₁₂₃'
        """
        return str.translate(number, UNICODE_SUBSCRIPT_TRANSLATION)

    @classmethod
    def superscript_number_charge(cls, number: str, charge: str) -> str:
        """
        Converts a number and charge to superscript
        >>> UnicodeConvertor.superscript_number_charge("123", "-")
        '¹²³⁻'
        >>> UnicodeConvertor.superscript_number_charge("", "+")
        '⁺'
        """
        out = str.translate(number, UNICODE_SUPERSCRIPT_TRANSLATION) if number else ""
        return out + str.translate(charge, UNICODE_CHARGES_TRANSLATION)


UNICODE_SUPERSCRIPT_TRANSLATION = {ord(str(i)): v for i, v in enumerate("⁰¹²³⁴⁵⁶⁷⁸⁹")}
UNICODE_SUBSCRIPT_TRANSLATION = {ord(str(i)): v for i, v in enumerate("₀₁₂₃₄₅₆₇₈₉")}
UNICODE_CHARGES_TRANSLATION = {ord("+"): "⁺", ord("-"): "⁻"}
