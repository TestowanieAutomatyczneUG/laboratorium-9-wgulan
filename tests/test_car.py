from src.sample.Car import Car
from unittest.mock import *
from unittest import TestCase, main


class TestCar(TestCase):
    def test_needs_fuel(self):
        # prepare mock
        test_car = Car()
        test_car.needsFuel = Mock(name='needs_fuel')
        test_car.needsFuel.return_value = True

        # testing
        self.assertEqual(test_car.needsFuel(), True, 'return value from needsFuel incorrect')

    def test_get_engine_temperature(self):
        # prepare mock
        test_car = Car()
        test_car.getEngineTemperature = Mock(name='getEngineTemperature')
        test_car.getEngineTemperature.return_value = 85

        # testing
        self.assertEqual(test_car.getEngineTemperature(), 85, 'return value from getEngineTemperature incorrect')

    def test_drive_to(self):
        # prepare mock
        test_car = Car()
        test_car.driveTo = Mock(name='driveTo')
        test_car.driveTo.side_effect = lambda destination: f'Destination: {destination}'

        # testing
        self.assertEqual(test_car.driveTo("Moscow"), f"Destination: Moscow")


if __name__ == '__main__':
    main()
