from ahorcado.main import Ahorcado
import pytest


def test_disallows_numbers():
    with pytest.raises(TypeError):
        Ahorcado('123')


def test_disallows_empty_words():
    with pytest.raises(TypeError):
        Ahorcado('')


def test_spots_misses_correctly():
    ahorcado = Ahorcado('Banana')
    assert ahorcado.check_ifexists('X') is False
    assert ahorcado.check_ifexists('B') is True


def test_spots_if_letter_was_already_used_correctly():
    ahorcado = Ahorcado('Peach')
    ahorcado.check_ifexists('B')
    assert ahorcado.already_used('X') is False
    assert ahorcado.already_used('B') is True


def test_doesnt_strike_if_letter_was_already_used():
    ahorcado = Ahorcado('Strawberry')
    for _ in range(50):
        ahorcado.check_ifexists('W')
    assert ahorcado.hung() is False


def test_letters_are_case_insensitive():
    ahorcado = Ahorcado('Yay')
    ahorcado.check_ifexists('y')
    ahorcado.check_ifexists('A')
    assert ahorcado.freed()


def test_knows_if_man_is_still_alive():
    ahorcado = Ahorcado('XYZ')
    assert ahorcado.hung() is False

    assert_not_hung_after_trying('A', ahorcado)
    assert_not_hung_after_trying('B', ahorcado)
    assert_not_hung_after_trying('C', ahorcado)
    assert_not_hung_after_trying('D', ahorcado)
    assert_not_hung_after_trying('E', ahorcado)
    assert_not_hung_after_trying('F', ahorcado)
    assert_not_hung_after_trying('G', ahorcado)
    assert_not_hung_after_trying('H', ahorcado)

    ahorcado.check_ifexists('I')
    assert ahorcado.hung() is True


def assert_not_hung_after_trying(letter, ahorcado):
    ahorcado.check_ifexists(letter)
    assert ahorcado.hung() is False
