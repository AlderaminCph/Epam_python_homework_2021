import datetime

import pytest

from homework5.task1 import Homework, Student, Teacher


def student_init():
    student = Student(
        "Petrov",
        "Roman",
    )
    return student


def teacher_init():
    teacher = Teacher("Ivanov", "Ivan")
    return teacher


def homework_init():
    homework = Homework("Learn OOP", 10, datetime.datetime.now())
    return homework


def test_homework_access_attributes():
    test_homework = Homework(
        "Learn functions", 14, datetime.datetime(2021, 8, 8, 11, 59, 14, 311745)
    )
    assert test_homework.text == "Learn functions"
    assert test_homework.deadline == 14
    assert test_homework.created == datetime.datetime(2021, 8, 8, 11, 59, 14, 311745)


def test_homework_is_active():
    active_homework = homework_init()
    assert active_homework.is_active() is True


def test_homework_is_expired():
    active_homework = Homework(
        "tasks to do", 10, datetime.datetime(2015, 8, 8, 11, 59, 14, 311745)
    )
    assert active_homework.is_active() is False


def test_student_access_attributes():
    test_student = student_init()
    assert test_student.first_name == "Roman"
    assert test_student.last_name == "Petrov"


def test_teacher_access_attributes():
    test_teacher = teacher_init()
    assert test_teacher.first_name == "Ivan"
    assert test_teacher.last_name == "Ivanov"


def test_student_do_homework():
    test_student = student_init()
    test_homework = homework_init()
    assert test_student.do_homework(test_homework) == test_homework


def test_student_do_homework_late(capfd):
    test_student = student_init()
    test_homework = Homework(
        "homework task", 8, datetime.datetime(2015, 8, 8, 11, 59, 14, 311745)
    )
    test_student.do_homework(test_homework)
    stdout, stderr = capfd.readouterr()
    assert test_student.do_homework(test_homework) is None
    assert stdout == "You are late\n"
    assert stderr == ""
