import pytest

from homework6.task1 import instances_counter


def test_get_created_instances_without_inheritance_with_attributes():
    @instances_counter
    class User:
        pass

    assert User.get_created_instances() == 0  # 0
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3  # 3


def test_get_created_instances_inheritance_with_attributes():
    @instances_counter
    class User:
        pass

    class AnotherUser(User):
        def __init__(self, name):
            self.name = name
            super().__init__()

    zero = AnotherUser.get_created_instances()  # 0
    AnotherUser("UserName")
    assert AnotherUser.get_created_instances() == 1  # 1


def test_reset_instances_counter():
    @instances_counter
    class User:
        pass

    user, _, _ = User(), User(), User()
    assert User.reset_instances_counter() == 3  # 3
    assert User.get_created_instances() == 0  # 0
