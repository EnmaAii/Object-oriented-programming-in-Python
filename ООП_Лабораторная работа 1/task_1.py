# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
class Cat:
    def __init__(self, color: str, ears: str):
        """
        Класс описывает кота
        :param color: окрас кота
        :param ears: тип ушей кота

        >>> cat1 = Cat("grey", "lop-eared")
        >>> cat2 = Cat("brown", "straight")
        >>> print(cat1.color, cat1.ears)
        grey lop-eared
        >>> print(cat2.color, cat2.ears)
        brown straight

        """
        if not isinstance(color, str):
            raise TypeError("Окрас должен быть типа string")
        if ears not in ["straight", "lop-eared"]:
            raise ValueError("ears must be straight or lop-eared")
        self.color = color
        self.ears = ears

        def sleep(self) -> str:
            """
            Кот спит

            >>> cat = Cat("brown", "straight")
            >>> cat.sleep()
            'Zzz...'
            """
            return "Zzz..."

        def play(self) -> str:
            """
            Кот играет

            >>> cat = Cat("grey", "lop-eared")
            >>> cat.play()
            'Playing with a toy!'
            """
            return "Playing with a toy!"

class Ball:
    """
    Уже определен класс кота. Коты играют с мячиками. Определим класс Мяч

    :param color: цвет мяча
    :param capacity_volume: максимальный объем мяча
    :occupied_volume: насколько мяч заполнен воздухом

    >>> ball = Ball("blue", 3.0, 2.0)
    >>> ball.inflate_ball(1.0)
    >>> ball.deflate_ball(0.5)
    >>> print(ball.occupied_volume)
    2.5
    """
    def __init__(self, color, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(color, str):
            raise TypeError("Цвет мяча должен быть типа string")

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем мяча должен быть int, float")
        if capacity_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем мяча должен быть int, float")
        if occupied_volume < 0:
            raise ValueError
        if occupied_volume > capacity_volume:
            raise ValueError("Мяч лопнул")
        self.occupied_volume = occupied_volume

    def inflate_ball(self, delta: Union[int, float]):
        """
        Увеличивает объем воздуха в мяче.

        :param delta: величина увеличения объема воздуха

        >>> ball = Ball("blue", 5, 3)
        >>> ball.inflate_ball(1)
        >>> print(ball.occupied_volume)
        4
        >>> ball.inflate_ball(2)
        Traceback (most recent call last):
            ...
        ValueError: Мяч лопнул
        """
        if not isinstance(delta, (int, float)):
            raise TypeError("Величина увеличения объема воздуха должна быть int или float")
        if delta < 0:
            raise ValueError("Величина увеличения объема воздуха должна быть неотрицательным числом")

        new_occupied_volume = self.occupied_volume + delta

        if new_occupied_volume > self.capacity_volume:
            raise ValueError("Мяч лопнул")
        self.occupied_volume = new_occupied_volume

    def deflate_ball(self, delta: Union[int, float]):
        """
        Уменьшает объем воздуха в мяче.

        :param delta: величина уменьшения объема воздуха

        >>> ball = Ball("blue", 5, 3)
        >>> ball.deflate_ball(1)
        >>> print(ball.occupied_volume)
        2
        >>> ball.deflate_ball(3)
        Traceback (most recent call last):
            ...
        ValueError: Невозможно сдуть мяч на такое число
        """
        if not isinstance(delta, (int, float)):
            raise TypeError("Величина уменьшения объема воздуха должна быть int или float")
        if delta < 0:
            raise ValueError("Величина уменьшения объема воздуха должна быть неотрицательным числом")

        new_occupied_volume = self.occupied_volume - delta

        if new_occupied_volume < 0:
            raise ValueError("Невозможно сдуть мяч на такое число")

        self.occupied_volume = new_occupied_volume

class Owner:
    """
    Замечательно, если у кота будет хозяин

    >>> owner = Owner("Female", 25, "Lenina", 5, 45)
    >>> print(owner.sex, owner.age, owner.street, owner.number_street, owner.flat)
    Female 25 Lenina 5 45
    """
    def __init__(self, sex: str, age: int, street: str, number_street: int, flat: int):
        if not isinstance(sex, str):
            raise TypeError("Пол хозяина должен быть типа строка")
        if sex not in ["Male", "Female", "Other"]:
            raise ValueError("Пол может быть Male, Female, Other")
        self.sex = sex

        if not isinstance(age, int):
            raise TypeError("Введите сколько полных лет, возраст должен быть типа int")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if age > 150:
            raise ValueError("Введите настоящий возраст")
        self.age = age

        if not isinstance(street, str):
            raise TypeError("Улица должна быть типа строка")
        self.street = street

        if not isinstance(number_street, int):
            raise TypeError("Номер улицы должен быть типа int")
        if number_street < 0:
            raise ValueError("Номер улицы не может быть отрицательным")
        self.number_street = number_street

        if not isinstance(flat, int):
            raise TypeError("Номер квартиры должен быть типа int")
        if flat < 0:
            raise ValueError("Номер квартиры не может быть отрицательным")
        self.flat = flat

        def feed_cat(self) -> str:
            """
            Хозяин кормит кота

            >>> owner = Owner("Female", 25, "Lenina", 5, 45)
            >>> owner.feed_cat()
            'Feeding the cat!'
            """
            return "Feeding the cat!"

        def play_with_cat(self) -> str:
            """
            Хозяин играет с котом

            >>> owner = Owner("Male", 30, "Pushkin", 10, 22)
            >>> owner.play_with_cat()
            'Playing with the cat!'
            """
            return "Playing with the cat!"

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
