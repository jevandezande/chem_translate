def get_num(string: str, decimal: bool = False) -> str:
    """
    Retrieve the first full number
    :param string: the string to read
    :param decimal: indicates if the number should allow a decimal

    >>> get_num("123HELLO")
    '123'
    >>> get_num("123")
    '123'
    >>> get_num("12.3HELLO", decimal=True)
    '12.3'
    >>> get_num("12.3HELLO", decimal=False)
    '12'
    >>> get_num("")
    ''
    >>> get_num("HELLO")
    ''
    >>> get_num("HELLO123")
    ''
    """
    i = 0
    for i, char in enumerate(string):
        if not char.isnumeric():
            if char != "." or decimal:
                break
            decimal = False
    return string[:i]
