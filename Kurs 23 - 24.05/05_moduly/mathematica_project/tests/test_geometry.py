from mathematica.geometry.matrices import square_area, triangle_area


def test_square_area():
    assert square_area(4) == 16
    assert square_area(3) == 9

def test_triangle_area():
    assert triangle_area(4, 6) == 12
    assert triangle_area(1, 2) == 1