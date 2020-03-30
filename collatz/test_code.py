from collatz.code import Number


def test_can_step_1():
    start = Number(4, 1, 3)
    expected = {Number(12, 1, 10)}
    result = start.step()
    assert expected == result
