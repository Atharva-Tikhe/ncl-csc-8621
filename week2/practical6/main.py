from car import Car


def main():
    car = Car(2025, 'toyota')

    car.get_speed()
    for _ in range(5):
        car.accelerate()
        print(car.get_speed())

    for _ in range(5):
        print(car.get_speed())
        car.brake()

    print(car.get_speed())

main()