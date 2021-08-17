import datetime

import pytest

from homework5.task1 import Homework, Student, Teacher


@pytest.fixture()
def student_init():
    student = Student(
        "Petrov",
        "Roman",
    )
    return student


@pytest.fixture()
def teacher_init():
    teacher = Teacher("Ivanov", "Ivan")
    return teacher


@pytest.fixture()
def homework_init():
    homework = Homework(
        "Learn OOP", 10, datetime.datetime(2021, 8, 8, 11, 59, 14, 311745)
    )
    return homework


def test_homework_access_attributes(homework_init):
    assert homework_init.text == "Learn OOP"
    assert homework_init.deadline == 10
    assert homework_init.created == datetime.datetime(2021, 8, 8, 11, 59, 14, 311745)


def test_homework_is_active(homework_init):
    assert homework_init.is_active() is True


def test_homework_is_expired():
    active_homework = Homework(
        "tasks to do", 10, datetime.datetime(2015, 8, 8, 11, 59, 14, 311745)
    )
    assert active_homework.is_active() is False


def test_student_access_attributes(student_init):
    assert student_init.first_name == "Roman"
    assert student_init.last_name == "Petrov"


def test_teacher_access_attributes(teacher_init):
    assert teacher_init.first_name == "Ivan"
    assert teacher_init.last_name == "Ivanov"


def test_student_do_homework(student_init, homework_init):
    assert student_init.do_homework(homework_init) == homework_init


def test_student_do_homework_late(capfd, student_init):
    test_homework = Homework(
        "homework task", 8, datetime.datetime(2015, 8, 8, 11, 59, 14, 311745)
    )
    student_init.do_homework(test_homework)
    stdout, stderr = capfd.readouterr()
    assert student_init.do_homework(test_homework) is None
    assert stdout == "You are late\n"
    assert stderr == ""
