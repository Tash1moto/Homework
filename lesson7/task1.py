# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.passenger_seats = count_passenger_seats
        self.baby_seat = is_baby_seat
        self.busy = False

    def __str__(self):
        return (f"Car color={self.color}, Number of passenger seats={self.passenger_seats}, "
                f"with seat for baby={self.baby_seat}, availability of car={self.busy}")


car1 = Car(color="Red", count_passenger_seats=10, is_baby_seat=True)
print(car1.__str__())
