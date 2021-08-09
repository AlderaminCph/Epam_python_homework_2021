"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
"""


def instances_counter(cls):
    """Decorator to class. Applies to any class and adds 2 methods to it.

    Methods:
        get_created_instances: Returns the number of created class instances.
        reset_instances_counter: Reset the instance counter, returns
        the value before reset.
    """

    class CountInstance(cls):
        instances = 0

        @classmethod
        def init_counter(cls):
            if "instances" not in cls.__dict__:
                cls.instances = 0

        def __init__(self, *args, **kwargs):
            self.init_counter()
            super().__init__(*args, **kwargs)
            self.__class__.instances += 1

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls.instances

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            try:
                return cls.instances
            finally:
                cls.instances = 0

    return CountInstance
