def add(x, y):
    """test pytest

    Args:
        x (float): float numbers
        y (float): float numbers

    Returns:
        float: sum of x and y
    """
    return x + y

def test_add():
    assert add(1, 2) == 3