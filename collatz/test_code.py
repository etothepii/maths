from collatz.code import Number


def test_can_step_1():
    start = Number(4, 1, 3)
    expected = {Number(12, 1, 10)}
    result = start.step()
    assert expected == result


def test_can_step_2():
    start = Number(12, 1, 10)
    expected = {Number(6, 1, 5)}
    result = start.step()
    assert expected == result


def test_can_step_3():
    start = Number(9, 1, 8)
    expected = {Number(9, 2, 4), Number(27, 1, 25)}
    result = start.step()
    assert expected == result
