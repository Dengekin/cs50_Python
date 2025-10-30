import fuel
import pytest

# convert() testleri
def test_convert_valid():
    assert fuel.convert("1/2") == 50
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/100") == 1  
    assert fuel.convert("99/100") == 99

def test_convert_invalid():
    # paydanın sıfır olması
    with pytest.raises(ZeroDivisionError):
        fuel.convert("1/0")
    # pay > payda
    with pytest.raises(ValueError):
        fuel.convert("2/1")
    # format hatalı
    with pytest.raises(ValueError):
        fuel.convert("abc")
    with pytest.raises(ValueError):
        fuel.convert("1/a")

# gauge() testleri
def test_gauge_empty_full():
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

def test_gauge_middle():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(75) == "75%"

