from typing import Union
import doctest

print("""Выберите один вариант работ для IphoneRepairCenter:
1. Чистка динамика, микрофонов от пыли
2. Замена экрана
3. Замена аккумулятора
4. Восстановление после попадания влаги
""")

class IphoneRepairCenter:
    def __init__(self, model: Union[str, int], ios_version: float, problem: int) -> None:
        """
        Создание и подготовка к работе нашего сервисного центра)

        :param model: Модель телефона
        :param ios_version: Версия прошивки телефона
        :param problem: Код неисправности

        Примеры:
        >>> First_phone = IphoneRepairCenter("11 Pro Max",16, 3) # Инициализация экземпляра класса
        """
        if not isinstance(model,(str, int)):
            raise TypeError ("Модель должна записываться либо строкой, либо int числом")
        if not isinstance(problem,int):
            raise TypeError ("Вариант работ должен быть int числом")
        if problem not in (1, 2, 3, 4):
            raise TypeError("Выберите из списка существующих работ")
        self.model = model
        self.ios_version = ios_version

    def check_last_version(self) -> Union[int,float]:
        """
        Проверяет последнюю поддерживаемую версию для твоего телефона и возвращает ее.

        :return: Выводит последнюю доступную версию IOS для указанной модели.

        Примеры:
        >>> First_phone = IphoneRepairCenter(16,18.1, 1)
        >>> First_phone.check_last_version()
        """
        ...

    def repair_time_cost(self) -> dict[str, Union[int, float]]:
        """
        Показывает цену и время ремонта для выбранной модели телефона.

        :return: Словарь с ключами 'time' (время ремонта в часах) и 'cost' (стоимость ремонта в рублях).

        Примеры:
        >>> First_phone = IphoneRepairCenter("13 Pro",18.01, 2)
        >>> First_phone.repair_time_cost()
        """
        ...

class BatteryService:
    def __init__(self, battery_health: int, charge_cycles: int) -> None:
        """
        Создание и подготовка объекта "Сервис батареи"

        :param battery_health: Состояние батареи (в процентах, от 0 до 100)
        :param charge_cycles: Количество циклов зарядки

        Примеры:
        >>> battery_service = BatteryService(85, 300) # Инициализация экземпляра класса
        """
        if not (0 <= battery_health <= 100):
            raise ValueError("Состояние батареи должно быть в диапазоне от 0 до 100")
        if charge_cycles < 0:
            raise ValueError("Количество циклов зарядки не может быть отрицательным")
        self.battery_health = battery_health
        self.charge_cycles = charge_cycles

    def needs_replacement(self) -> bool:
        """
        Проверяет, требуется ли замена батареи.

        :return: True, если батарея требует замены, иначе False.

        Примеры:
        >>> battery_service = BatteryService(50, 500)
        >>> battery_service.needs_replacement()
        """
        ...

    def remaining_life(self) -> float:
        """
        Оценивает оставшийся срок службы батареи в процентах.

        :return: Оставшийся срок службы батареи (от 0 до 100%).

        Примеры:
        >>> battery_service = BatteryService(85, 300)
        >>> battery_service.remaining_life()
        """
        ...

class WaterDamageAssessment:
    def __init__(self, water_level: int, is_power_on: bool) -> None:
        """
        Создание и подготовка объекта "Диагностика повреждений от воды"

        :param water_level: Уровень повреждения водой (от 0 до 10)
        :param is_power_on: Флаг, включается ли устройство после повреждения водой

        Примеры:
        >>> water_damage = WaterDamageAssessment(7, False) # Инициализация экземпляра класса
        """
        if not (0 <= water_level <= 10):
            raise ValueError("Уровень воды должен быть в диапазоне от 0 до 10")
        self.water_level = water_level
        self.is_power_on = is_power_on

    def is_repairable(self) -> bool:
        """
        Определяет, можно ли отремонтировать устройство.

        :return: True, если ремонт возможен, иначе False.

        Примеры:
        >>> water_damage = WaterDamageAssessment(5, True)
        >>> water_damage.is_repairable()
        """
        ...

    def estimated_cost(self) -> float:
        """
        Оценивает стоимость ремонта в зависимости от уровня повреждений.

        :return: Примерная стоимость ремонта (в рублях).

        Примеры:
        >>> water_damage = WaterDamageAssessment(7, False)
        >>> water_damage.estimated_cost()
        """
        ...

if __name__ == "__main__":
    doctest.testmod() # тестирование примеров, которые находятся в документации