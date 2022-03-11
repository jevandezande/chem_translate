from .latex_convertor import LatexConvertor
from .unicode_convertor import UnicodeConvertor

convertors = {
    "latex": LatexConvertor,
    "unicode": UnicodeConvertor,
}


def translate(string: str, to: str = "unicode") -> str:
    convertor = convertors.get(to.lower(), None)
    if convertor is None:
        raise ValueError(f"{to=} is not a supported translation, choose one of {set(convertors)}.")

    return convertor.convert(string)
