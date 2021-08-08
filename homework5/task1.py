"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """Homework class.

    Attributes:
        text (str): Text of task.
        deadline (:obj:'int'): Number of days to complete the task.
        created (datetime): Exact date and time of creation.
    """

    def __init__(self, text: str, deadline: int, created: datetime):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self):
        """Checks if the time for the task has expired.

        Returns:
            boolean
        """
        return datetime.datetime.now() < (
            self.created + datetime.timedelta(days=self.deadline)
        )


class Person:
    """Class Person

    Attributes:
        last_name (str): Last Name.
        first_name (str): First Name.
    """

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """Class Student inherit the properties from the Person class.

    Attributes:
        last_name (str): Last Name.
        first_name (str): First Name.
    """

    @staticmethod
    def do_homework(homework: Homework):
        """Takes a Homework object and returns it,
        if the job is already overdue, it prints 'You are late' and returns None.

        Args:
            homework: Homework object
        Returns:
            None if job is iverdue otherwise return homework object.
        """
        return homework if homework.is_active() else print("You are late")


class Teacher(Person):
    """Class Teacher inherit the properties from the Person class.

    Attributes:
        last_name (str): Last Name.
        first_name (str): First Name.
    """

    @staticmethod
    def create_homework(text, deadline):
        """Creates homework object.
        Args:
            text: the text of the task
            deadline: the number of days for this task
        Returns:
            an instance of Homework
        """
        return Homework(text, deadline, datetime.datetime.now())
