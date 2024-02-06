import logging
import argparse

FORMAT = '{levelname} - {asctime}. {msg}'

logging.basicConfig(filename='rectangle_info.txt', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)




class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if width <= 0:
            logger.error(f'Не удалось создать прямоугольник. Ширина должна быть положительной, а не {width}')
            return
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                logger.error(f'Не удалось создать прямоугольник. Высота должна быть положительной, а не {height}')
                return

            self._height = height
        logger.info(f'Создан прямоугольник с шириной {self.width} и высотой {self.height}. ')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
            logger.info(f'Значение ширины изменено. Прямоугольник с шириной {self.width} и высотой {self.height}')
        else:
            logger.error(f'Не удалось изменить ширину. Ширина должна быть положительной, а не {value}')
            return

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
            logger.info(f'Значение высоты изменено. Прямоугольник с шириной {self.width} и высотой {self.height}')
        else:
            logger.error(f'Не удалось изменить высоту. Ширина должна быть положительной, а не {value}')
            return

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self._width + self._height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """

        return self._width * self._height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


def rectangle_parser():
    parser = argparse.ArgumentParser(prog='Rectangle()', description='Создание экземпляра класса Rectangle(прямоугольник).')
    parser.add_argument('-w', '--width', help="Задайте ширину прямоугольника", type=int)
    parser.add_argument('-H', '--height', help="Задайте высоту прямоугольника", type=int)
    args = parser.parse_args()
    return Rectangle(args.width, args.height)


if __name__ == '__main__':
    # rectangle_1 = Rectangle(5, 4)
    # rectangle_2 = Rectangle(5, -4)
    # rectangle_3 = Rectangle(3)
    # rectangle_4 = rectangle_1 + rectangle_3
    # rectangle_5 = rectangle_1 - rectangle_3
    # rectangle_6 = Rectangle(4, 5)
    # rectangle_7 = rectangle_1 - rectangle_6
    # rectangle_3.width = -10
    # rectangle_5.height = 8

    rectangle_parser()

