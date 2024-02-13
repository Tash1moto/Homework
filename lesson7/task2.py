# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.passenger_seats = count_passenger_seats
        self.baby_seat = is_baby_seat
        self.busy = False


class Taxi:
    def __init__(self, cars: list[Car]):
        self.cars = cars

    @staticmethod
    def find_car(a, b):
        if a+b < car1.passenger_seats or a+b == car1.passenger_seats:
            if b < car1.baby_seat or b == car1.baby_seat:
                return (f"Car color={car1.color}, Number of passenger seats={car1.passenger_seats}, "
                        f"with seat for baby={car1.baby_seat}, availability of car={car1.busy}")
            else:
                print("none")


car1 = Car(color="Red", count_passenger_seats=10, is_baby_seat=True)
a = int(input("Enter number of passengers: "))
b = bool(input("Required number of baby seats: "))
print(Taxi.find_car(a, b))
