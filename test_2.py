from example2 import reverse_string

def test_reverse_string_basic():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_palindrome():
    assert reverse_string("madam") == "madam"

def test_reverse_numbers():
    assert reverse_string("12345") == "54321"
