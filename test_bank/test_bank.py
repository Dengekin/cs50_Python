import bank

def test_qnb ():
    assert bank.value("Hello") == 0

def test_garanti ():
    assert bank.value("Hi") == 20

def test_fiba ():
    assert bank.value("ekin") == 100
