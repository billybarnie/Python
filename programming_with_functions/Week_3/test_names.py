from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Ian", "Barnie") == "Barnie; Ian"
    assert make_full_name("Nova", "Barnie") == "Barnie; Nova"
    assert make_full_name("L", "Jack") == "Jack; L"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    assert extract_family_name("Barnie; Ian") == "Barnie"
    assert extract_family_name("Barnie; Nova") == "Barnie"
    assert extract_family_name("Jack; L") == "Jack"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    assert extract_given_name("Barnie; Ian") == "Ian"
    assert extract_given_name("Barnie; Nova") == "Nova"
    assert extract_given_name("Jack; L") == "L"
    assert extract_given_name("; ") == ""

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
