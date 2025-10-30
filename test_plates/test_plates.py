import plates

def test_reno():
    assert plates.is_valid("AA")
    assert plates.is_valid("AABB89CC") == False


# 1) Başlangıçta iki harf olmalı
def test_begins_with_letters_valid():
    assert plates.is_valid("CS") is True
    assert plates.is_valid("CS50") is True

def test_begins_with_letters_invalid():
    assert plates.is_valid("1S50") is False   # ilk karakter rakam
    assert plates.is_valid("C550") is False   # ikinci karakter rakam

# 2) Uzunluk 2–6
def test_length_valid():
    assert plates.is_valid("PI") is True      # 2
    assert plates.is_valid("CS50") is True    # 4
    assert plates.is_valid("ABCDEF") is True  # 6

def test_length_invalid():
    assert plates.is_valid("P") is False        # 1 -> kısa
    assert plates.is_valid("OUTATIME") is False # 7 -> uzun

# 3) Sadece alfanümerik
def test_alphanumeric():
    assert plates.is_valid("CS50") is True
    assert plates.is_valid("CS 50") is False
    assert plates.is_valid("CS-50") is False
    assert plates.is_valid("CS.50") is False
    assert plates.is_valid("CS!50") is False

# 4) Rakamlar (varsa) sonda olmalı
def test_number_placement():
    assert plates.is_valid("AAA222") is True
    assert plates.is_valid("CS50") is True
    assert plates.is_valid("CS50P") is False   # rakamdan sonra harf
    assert plates.is_valid("AA2A2") is False   # karışık

# 5) İlk rakam 0 olamaz
def test_zero_placement():
    assert plates.is_valid("CS05") is False
    assert plates.is_valid("AA0") is False

# 6) Hiç rakam yoksa da geçerli olabilir
def test_no_digits():
    assert plates.is_valid("AAA") is True
    assert plates.is_valid("AA") is True
