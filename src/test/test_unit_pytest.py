import pytest
from .Src import Car
from ..blah import Bar

car_speed=[45,50,60,120]

@pytest.mark.parametrize("speed_brake", car_speed)
def test_car_brake(speed_brake):
    car = Bar(50)

    car.brake()
    assert car.speed == speed_brake


def test_car_speed():
    car = Bar(60)
    expected = 65

    assert car.accelerate() == expected
