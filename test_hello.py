from hello import hello

# best ptactice to return a val and not have side effects like say print()


def test_default():
    assert hello() == "Hello World"


def test_arg():
    assert hello("Fijabi") == "Hello Fijabi"
