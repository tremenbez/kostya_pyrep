from typing import Union
import doctest

class Automobile:
    """
    Родительский класс автомобилей.
    Атрибуты сделаны непубличными (protected), чтобы предотвратить их прямое изменение извне и обеспечить контроль через методы.

    Атрибуты:
        _name (str): Название марки автомобиля.
        _engine (str): Модель двигателя.
        _wheels (int): Количество колес.
        _distance (Union[int, float]): Пройденный километраж.

    Методы:
        set_name(new_name: str) -> None: Устанавливает название марки автомобиля.
        set_distance(new_distance: Union[int, float]) -> None: Устанавливает пройденный километраж.
        drive(additional_distance: Union[int, float]) -> None: Увеличивает пройденный километраж.

    Примеры:
        >>> auto = Automobile("Audi", "12F3249G91", 4, 123)
        >>> auto.distance
        123
        >>> auto.drive(100)
        >>> auto.distance
        223
        >>> auto.distance = 500
        >>> auto.distance
        500
    """
    def __init__(self, name: str, engine: str, wheels: int, distance: Union[int, float]):
        self._name = None
        self.set_name(name)
        self._engine = engine
        self._wheels = wheels
        self._distance = None
        self.set_distance(distance)

    def __str__(self):
        return f"Марка автомобиля: '{self.name}', Модель двигателя: '{self.engine}', Количество колес: {self.wheels}, Километраж: {self.distance} км."

    def __repr__(self):
        return f"{self.__class__.__name__} (name={self.name!r}, engine={self.engine!r}, wheels={self.wheels!r}, distance={self.distance!r})"

    @property
    def name(self):
        return self._name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Марка автомобиля должна быть типа str.")
        self._name = new_name

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, new_engine: str) -> None:
        if not isinstance(new_engine, str):
            raise TypeError("Модель двигателя должна быть типа str.")
        self._engine = new_engine

    @property
    def wheels(self):
        return self._wheels

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, new_distance: Union[int, float]) -> None:
        self.set_distance(new_distance)

    def set_distance(self, new_distance: Union[int, float]) -> None:
        """
        Устанавливает пройденный километраж.

        Аргументы:
            new_distance (Union[int, float]): Новое значение пройденного километража.

        Raises:
            TypeError: Если new_distance не является int или float.
            ValueError: Если new_distance не является положительным числом.

        Примеры:
            >>> auto = Automobile("Audi", "12F3249G91", 4, 123)
            >>> auto.set_distance(200)
            >>> auto.distance
            200
        """
        if not isinstance(new_distance, (int, float)):
            raise TypeError("Пройденный километраж должен быть типа int или float")
        if new_distance <= 0:
            raise ValueError("Пройденный километраж должен быть положительным числом")
        self._distance = new_distance

    def drive(self, additional_distance: Union[int, float]) -> None:
        """
        Увеличивает пройденный километраж.

        Аргументы:
            additional_distance (Union[int, float]): Дополнительное расстояние.

        Raises:
            TypeError: Если additional_distance не является int или float.
            ValueError: Если additional_distance не является положительным числом.

        Примеры:
            >>> auto = Automobile("Audi", "12F3249G91", 4, 123)
            >>> auto.drive(100)
            >>> auto.distance
            223
        """
        if not isinstance(additional_distance, (int, float)):
            raise TypeError("Дополнительное расстояние должно быть типа int или float")
        if additional_distance <= 0:
            raise ValueError("Дополнительное расстояние должно быть положительным числом")
        self._distance += additional_distance


class Car(Automobile):
    """
    Дочерний класс легковых автомобилей.

    Атрибуты::
        _backseats (int): Количество задних мест.

    Методы:
        check_backseats(new_backseats: int) -> None: Устанавливает количество задних мест в автомобиле.
        set_distance(new_distance: Union[int, float]) -> None: Переопределенный метод для установки пройденного расстояния.

    Примеры:
        >>> car = Car("Mercedes", "67249G91", 4, 12333, 2)
        >>> car.backseats
        2
        >>> car.set_distance(200000)
        >>> car.distance
        200000
    """
    def __init__(self, name: str, engine: str, wheels: int, distance: float, backseats: int):
        super().__init__(name, engine, wheels, distance)
        self._backseats = None
        self.check_backseats(backseats)

    def __str__(self):
        return f"Марка автомобиля: '{self.name}', Модель двигателя: '{self.engine}', Количество колес: {self.wheels}, Километраж: {self.distance} км, Количество задних мест: {self.backseats}."

    def __repr__(self):
        return f"{self.__class__.__name__} (name={self.name!r}, engine={self.engine!r}, wheels={self.wheels!r}, distance={self.distance!r}, backseats={self.backseats!r})"

    @property
    def backseats(self):
        return self._backseats

    def set_distance(self, new_distance: Union[int, float]) -> None:
        """
        Переопределенный метод для установки пройденного расстояния.
        Добавлена дополнительная проверка: расстояние не может превышать 300 000 км, что обуславливается ТИПОМ автомобиля.

        Аргументы:
            new_distance (Union[int, float]): Новое значение пройденного километража.

        Raises:
            TypeError: Если new_distance не является int или float.
            ValueError: Если new_distance не является положительным числом или превышает 300 000 км.

        Примеры:
            >>> car = Car("Mercedes", "67249G91", 4, 12333, 2)
            >>> car.set_distance(200000)
            >>> car.distance
            200000
        """
        if not isinstance(new_distance, (int, float)):
            raise TypeError("Пройденный километраж должен быть типа int или float")
        if new_distance <= 0:
            raise ValueError("Пройденный километраж должен быть положительным числом")
        if new_distance > 300_000:
            raise ValueError("Пройденный километраж не может превышать 300 000 км")
        self._distance = new_distance

    def check_backseats(self, new_backseats: int) -> None:
        """
        Устанавливает количество задних мест в автомобиле.

        Аргументы:
            new_backseats (int): Новое количество задних мест.

        Raises:
            TypeError: Если new_backseats не является int.
            ValueError: Если new_backseats не является положительным числом.

        Примеры:
            >>> car = Car("Mercedes", "67249G91", 4, 12333, 2)
            >>> car.check_backseats(3)
            >>> car.backseats
            3
        """
        if not isinstance(new_backseats, int):
            raise TypeError("Количество задних мест должно быть типа int")
        if new_backseats <= 0:
            raise ValueError("Количество задних мест должно быть положительным числом")
        self._backseats = new_backseats


class Truck(Automobile):
    """
    Дочерний класс грузовых автомобилей.

    Атрибуты::
        _volume (Union[int, float]): Вместимость кузова в кубических метрах.

    Методы:
        check_volume(new_volume: Union[int, float]) -> None: Устанавливает вместимость кузова.
        set_distance(new_distance: Union[int, float]) -> None: Переопределенный метод для установки пройденного расстояния - теперь 800 000 км, что обуславливается ТИПОМ автомобиля.

    Примеры:
        >>> truck = Truck("Камаз", "12491", 6, 8833, 10)
        >>> truck.volume
        10
        >>> truck.set_distance(70_000)
        >>> truck.distance
        70000

    """
    def __init__(self, name: str, engine: str, wheels: int, distance: float, volume: Union[int, float]):
        super().__init__(name, engine, wheels, distance)
        self._volume = None
        self.check_volume(volume)

    def __str__(self):
        return f"Марка автомобиля: '{self.name}', Модель двигателя: '{self.engine}', Количество колес: {self.wheels}, Километраж: {self.distance} км, Вместимость кузова: {self.volume} куб. м."

    def __repr__(self):
        return f"{self.__class__.__name__} (name={self.name!r}, engine={self.engine!r}, wheels={self.wheels!r}, distance={self.distance!r}, volume={self.volume!r})"

    @property
    def volume(self):
        return self._volume

    def set_distance(self, new_distance: Union[int, float]) -> None:
        """
        Переопределенный метод для установки пройденного расстояния.
        Добавлена дополнительная проверка: расстояние не может превышать 800 000 км.

        Аргументы:
            new_distance (Union[int, float]): Новое значение пройденного километража.

        Raises:
            TypeError: Если new_distance не является int или float.
            ValueError: Если new_distance не является положительным числом или превышает 800 000 км.

        Примеры:
            >>> truck = Truck("Камаз", "12491", 6, 8833, 10)
            >>> truck.set_distance(700_000)
            >>> truck.distance
            700000
        """
        if not isinstance(new_distance, (int, float)):
            raise TypeError("Пройденный километраж должен быть типа int или float")
        if new_distance <= 0:
            raise ValueError("Пройденный километраж должен быть положительным числом")
        if new_distance > 800_000:
            raise ValueError("Пройденный километраж не может превышать 800 000 км")
        self._distance = new_distance

    def check_volume(self, new_volume: Union[int, float]) -> None:
        """
        Устанавливает вместимость кузова.

        Аргументы:
            new_volume (Union[int, float]): Новая вместимость кузова.

        Raises:
            TypeError: Если new_volume не является int или float.
            ValueError: Если new_volume не является положительным числом.

        Примеры:
            >>> truck = Truck("Камаз", "12491", 6, 8833, 10)
            >>> truck.check_volume(15)
            >>> truck.volume
            15
        """
        if not isinstance(new_volume, (int, float)):
            raise TypeError("Вместимость кузова должна быть типа int или float")
        if new_volume <= 0:
            raise ValueError("Вместимость кузова должна быть положительным числом")
        self._volume = new_volume


if __name__ == "__main__":
    doctest.testmod()