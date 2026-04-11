from bank import value


def test_hello():
    assert value("hello") == 0


def test_first_letter():
    assert value("hey gurl") == 20


def test_no_h_greet():
    assert value("i am that i am") == 100


def test_cap():
    assert value("Hllo") == 20
