from typing import Union
import logging

FORMAT = '{levelname} - {asctime}. {msg}'

logging.basicConfig(filename='archive_info.txt', encoding='utf-8', level=logging.INFO, format=FORMAT, style='{')
logger = logging.getLogger(__name__)

import argparse


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
            logger.info(f'Text archive: {cls._instance.archive_text}\t'
                        f'Number archive:{cls._instance.archive_number}')
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        if len(text) > 0:
            self.text = text
        else:
            logger.error(f'Invalid text: {text}. Text should be a non-empty string.')
        try:
            number = float(number)
            if number > 0:
                self.number = number
        except ValueError:
            logger.error(f'Invalid number: {number}. Number should be a positive integer or float.')

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


if __name__ == '__main__':
    archive_1 = Archive('text1', 1)
    archive_2 = Archive('text2', 2)
    archive_3 = Archive('text3', 3)
    archive_4 = Archive('text4', 4)
    archive_5 = Archive('text5', 5)
    archive_6 = Archive('', -5)
    archive_7 = Archive('text7', '7t')
