from math import pi

import pytest
from src.area import Figure, Triangle, Circle


@pytest.mark.parametrize('sides, expected', [
    ((2, 3, 2), 1.984313483298443),
    ((5, 9, 9), 21.614520582238228),
    ((11, 45, 36), 126.8857754044952),
])
def test_triangle_area(sides, expected):
    assert Triangle(*sides).get_area() == expected


@pytest.mark.parametrize('sides, expected', [
    ((2, 3, 2), 'Треугольник неправильный'),
    ((5, 12, 13), 'Треугольник правильный'),
    ((11, 45, 36), 'Треугольник неправильный'),
    ((5, 3, 4), 'Треугольник правильный')
])
def test_triangle_is_right(sides, expected):
    assert Triangle(*sides).is_right() == expected


@pytest.mark.parametrize('sides, expected', [
    ((2, 3, 6), 'There is no triangle with the specified sides'),
    ((2, 3, 'Value'), 'Unexpected type of values'),
    ((11, 45, -36), 'There is no triangle with the specified sides'),
    ((5, '3', 4), 'Unexpected type of values')
])
def test_triangle_exceptions(sides, expected):
    with pytest.raises(ValueError) as exc:
        Triangle(*sides)
    assert str(exc.value) == expected


@pytest.mark.parametrize('radius, expected', [
    (6, 113.09733552923255),
    (8, 201.06192982974676),
    (5, 78.53981633974483),
])
def test_circle_area(radius, expected):
    assert Circle(radius).get_area() == expected


@pytest.mark.parametrize('radius, exception, expected', [
    ((2, 3), ValueError, 'Unexpected type of values'),
    (-6, ValueError, 'There is no circle with the specified radius'),
    ('Value', ValueError, 'Unexpected type of values'),
    ('3', ValueError, 'Unexpected type of values')
])
def test_circle_exceptions(radius, exception, expected):
    with pytest.raises(exception) as exc:
        Circle(radius)
    assert str(exc.value) == expected


@pytest.mark.parametrize('sides, expected', [
    ((3,), 28.274333882308138),
    ((5,), 78.53981633974483),
    ((8,), 201.06192982974676),
    ((3, 4, 5), 6.0),
    ((5, 9, 9), 21.614520582238228),
    ((11, 45, 36), 126.8857754044952),
])
def test_abstract_figure_area(sides: tuple[float], expected: float):
    assert Figure.get_abstract_area(*sides) == expected


@pytest.mark.parametrize('sides, exception, expected', [
    ((2, 3), TypeError, 'A figure with this number of sides is not defined'),
    ((-6,), ValueError, 'There is no circle with the specified radius'),
    (('Value',), ValueError, 'Unexpected type of values'),
    ((2, 3, 6), ValueError, 'There is no triangle with the specified sides')
])
def test_figure_exceptions(sides, exception, expected):
    with pytest.raises(exception) as exc:
        Figure.get_abstract_area(*sides)
    assert str(exc.value) == expected


