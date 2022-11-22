from project import encrypt, decrypt, paranoid_uriel_encode, paranoid_urieldecrypt
import pytest


def test_encrypt():
    with pytest.raises(TypeError):
        encrypt(2)
        encrypt(33.3)
        encrypt(True)
        encrypt(False)
        encrypt(None)


def test_decrypt():
    assert decrypt("d 5 h 0") == "cs50"
    assert decrypt("s f 6 y f 6 3") == "harvard"
    assert decrypt("s f 6 y f 6 3?") == "harvard?"
    assert decrypt("s f 6 y f 6 3 ?") == "harvard ?"
    assert decrypt("s f 6 y f 6 3   d 5 h 0!") == "harvard  cs50!"


def test_decrypt_errors():
    with pytest.raises(ValueError):
        decrypt(2)
        decrypt(33.3)
        decrypt(True)
        decrypt(False)
        decrypt(None)


def test_encode():
    assert paranoid_uriel_encode("d 5 h 0") == "ZCA1IGggMA=="
    assert paranoid_uriel_encode("s f 6 y f 6 3?") == "cyBmIDYgeSBmIDYgMz8="
    assert paranoid_uriel_encode("s f 6 y f 6 3   d 5 h 0!") == "cyBmIDYgeSBmIDYgMyAgIGQgNSBoIDAh"


def test_encode_errors():
    with pytest.raises(ValueError):
        decrypt(2)
        decrypt(33.3)
        decrypt(True)
        decrypt(False)
        decrypt(None)


def test_decode_decrypt():
    assert paranoid_urieldecrypt("ZCA1IGggMA==") == "d 5 h 0"
    assert paranoid_urieldecrypt("cyBmIDYgeSBmIDYgMz8=") == "s f 6 y f 6 3?"
    assert paranoid_urieldecrypt("cyBmIDYgeSBmIDYgMyAgIGQgNSBoIDAh") == "s f 6 y f 6 3   d 5 h 0!"


def test_decc_dec_errors():
    with pytest.raises(ValueError):
        decrypt(2)
        decrypt(33.3)
        decrypt(True)
        decrypt(False)
        decrypt(None)
