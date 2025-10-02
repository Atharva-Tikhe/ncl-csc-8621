from car import Car


class CarManager:

    def __init__(self, csv_path):
        self.__csv_path = csv_path
        self.__input_list = []
        self.__cars = []
        self.__populate_cars_list()

    def __populate_cars_list(self):
        with open(self.__csv_path, "r") as f:
            self.__input_list = f.readlines()
            f.close()

        for car in self.__input_list:
            try:
                make, year, model, category, color = car.strip().split(",")
                temp_car_obj = Car(year, make)
                temp_car_obj.set_category(category)
                temp_car_obj.set_color(color)
                self.__cars.append(temp_car_obj)
            except ValueError:
                print("columns missing... skipping")

    def get_car_list(self):
        return self.__cars

    def get_cars_older_than(self, years):
        older_than = []
        for car in self.__cars:
            if car.age >= years:
                older_than.append(car)
        return older_than

    def get_cars_of_category(self, category):
        selected_category = []
        for car in self.__cars:
            if car.get_category() == category:
                selected_category.append(car)

        return selected_category
