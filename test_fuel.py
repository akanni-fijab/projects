from fuel import convert, gauge
import pytest


def test_convert():
    with pytest.raises(ValueError):
        convert("a/3")
    with pytest.raises(ValueError):  # one test per pyraise
        convert("0.3/4")
    with pytest.raises(ValueError):
        convert("-1/200")
    with pytest.raises(ValueError):
        convert("200/10")

    with pytest.raises(ZeroDivisionError):
        convert("2/0")

    assert convert("99/100") == 99


def test_gauge():
    assert gauge(0.9) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(67) == "67%"
