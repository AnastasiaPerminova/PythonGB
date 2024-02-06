import logging
import argparse

FORMAT = '{asctime}. {msg}'
logging.basicConfig(filename='employee_info.txt', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)


class Person:
    """
    класс Person имеeт атрибуты : Фамилия, Имя, Отчество, Возраcт
    методы:
    birthday() - увеличивает возраст  на 1 год;
    full_name() - возвращает полное имя : Фамилия Имя Отчество
    get_age() - возвращает возраст
    """


    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    """
    класс Employee наследует от класса Person имеeт атрибуты : Фамилия, Имя, Отчество, Возраcт, должность, зарплата
    методы:
    raise_salary() - повышает зарплату на указанное число процентов,
    __str__ - возвращает полное имя и должность
    """

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary
        logger.info(
            f'Employee : Фамилия : {self.last_name} Имя: {self.first_name} Отчество: {self.patronymic} Возраст: {self.get_age()}\t'
            f'Должность: {self.position} Зарплата:{self.salary}')

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)
        logger.info(
            f'Работнику  {self.last_name}  {self.first_name} {self.patronymic} ({self.position}) увеличена зарплата на {percent} процентов. Зарплата: {self.salary}')

    def __str__(self):
        return f'{self.full_name()} ({self.position})'


def employee_parser():
    parser = argparse.ArgumentParser(prog='Employee()',
                                     description='Создание экземпляра класса Employee(работник).')
    parser.add_argument('-ln', '--last_name', help="Фамилия", type=str)
    parser.add_argument('-fn', '--first_name', help="Имя", type=str)
    parser.add_argument('-p', '--patronymic', help="Отчество", type=str)
    parser.add_argument('-a', '--age', help="Возраст", type=int)
    parser.add_argument('-pos', '--position', help="Должность", type=str)
    parser.add_argument('-s', '--salary', help="Зарплата", type=float)
    args = parser.parse_args()
    return Employee(args.last_name, args.first_name, args.patronymic, args.age, args.position, args.salary)


if __name__ == '__main__':

    employee_1 = Employee('Иванов', 'Иван', 'Иванович', 30, 'менеджер проекта', 200000)
    employee_1.raise_salary(30)
    employee_2 = Employee('Cидоров', 'Аристарх', 'Иванович', 55, 'начальник отдела', 350000)
    employee_parser()
