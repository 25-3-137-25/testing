from main import *


def test_to2():
    assert to2(8) == "1000"


def test_puzirek():
    assert puzirek([1, 4, 5, 2, 9, 7]) == [1, 2, 4, 5, 7, 9]


def test_viborka():
    assert viborka([1, 4, 5, 2, 9, 7]) == [1, 2, 4, 5, 7, 9]


def test_vstavka():
    assert vstavka([1, 4, 5, 2, 9, 7]) == [1, 2, 4, 5, 7, 9]


def test_to8():
    assert to8(19) == "23"


def test_fibonacci():
    assert fibonacci(19) == 4181


def test_gosdolg():
    assert gosdolg(19) == "госдолг сша больше, чем ваше кол-во долларов"


def test_prostoe():
    assert prostoe(19) == True