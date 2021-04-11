import pytest

from homework.calculator import Caculator


@pytest.fixture()
def calculate():
    print("开始计算")
    cal =Caculator()
    yield cal
    print("结束计算")