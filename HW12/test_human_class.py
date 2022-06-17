import pytest


class Test_Human:
    def setup(self):
        self.human = Human(name='Sofia', age=24, gender='female')


    def test_human_grow01(self):
        self.human.grow()
        assert self.human.age == 25, f'\n Age not as expected\n Actual Result: {self.human.age}\nExpected: 25'

    def test_human_grow02(self):
        self.human.grow()
        assert self.human.age != 27, f'\n Age not as expected\n Actual Result: {self.human.age}\nExpected: 25'
Bezzub6498qwe5