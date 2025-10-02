from car import Car
from car_manager import CarManager


def main():
    car = Car(2005, "toyota")

    car.get_speed()
    for _ in range(5):
        car.accelerate()
        print(car.get_speed())

    for _ in range(5):
        print(car.get_speed())
        car.brake()

    print(car.get_speed())

    cm = CarManager("./cars.csv")
    print(cm.get_car_list())
    print(cm.get_cars_older_than(10))
    print(cm.get_cars_of_category("hatchback"))


main()
