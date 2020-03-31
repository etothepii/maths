from collatz.code import Number


def test_can_step_1():
    start = Number(4, 1, 3)
    expected = {Number(12, 1, 10, 7)}
    result = start.step()
    assert expected == result, "Even, Odd"


def test_can_step_2():
    start = Number(12, 1, 10, 7)
    expected = {Number(6, 1, 5, 7)}
    result = start.step()
    assert expected == result, "Even, Even"


def test_can_step_3():
    start = Number(9, 1, 8, 7)
    expected = {Number(9, 2, 4, 7), Number(27, 1, 25, 7)}
    result = start.step()
    assert expected == result, "Odd, Even"


def test_can_step_4():
    start = Number(27, 1, 25, 7)
    expected = {Number(27, 2, 26, 7), Number(81, 1, 76, 7)}
    result = start.step()
    assert expected == result, "Odd, Odd"


def test_can_terminate():
    start = Number(9, 4, 2, 7)
    expected = set()
    result = start.step()
    assert expected == result, "Can Terminate"
