import allure
import pytest
import yaml



def get_datas():
    with open('Cal.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

@allure.feature("测试计算器")
class TestCalc:

    @allure.story('测试加法')
    @pytest.mark.parametrize('a,b,expect',get_datas()['data']['add'],ids=get_datas()['data']['myid'])
    def test_add(self, calculate, a,b,expect):
        assert expect ==round(calculate.add(a,b),2)

    @allure.story('测试除法')
    @pytest.mark.parametrize('a,b,expect', get_datas()['data1']['div'], ids=get_datas()['data1']['myid'])
    def test_div(self, calculate, a,b,expect):
        with pytest.raises(ZeroDivisionError):
            calculate.div(0,0)
        assert expect ==round(calculate.div(a,b),2)
