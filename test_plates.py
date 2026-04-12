from plates import is_valid


def test_is_valid_starts_with_alpha():
    assert is_valid("HE") is True
    assert is_valid("12") is False
    assert is_valid("H") is False


def test_is_valid_size_limit():
    assert is_valid("AB") is True
    assert is_valid("AAA222") is True
    assert is_valid("AAA2222") is False


def test_is_valid_number_placement():
    assert is_valid("AAA22A") is False
    assert is_valid("AAA222") is True
    assert is_valid("AAA022") is False


def test_is_valid_punctuation_check():
    assert is_valid("CS512!") is False
    assert is_valid("PI3.14") is False
    assert is_valid("PI3 14") is False
