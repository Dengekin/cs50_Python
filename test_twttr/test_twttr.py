from twttr.twttr import shorten

def main():
    test_spacex()

"""
def test_elon():
    try:
        assert shorten(vowel) == "vwl"
    except AssertionError:
        print("ERROR")
"""
def test_spacex():
    assert shorten("ekin") == "kn"
    assert shorten("deng") == "dng"

main()
