import pytest
import yaml

from homework.homework1.page.main_page import Main


def get_datas():
    with open("./department.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas


class TestAddDepart:

    def setup(self):
        self.main = Main()



    @pytest.mark.parametrize('department', get_datas()['data']['department'])
    def test_adddepart(self, department):
        #主页 1.点击添加成员 2.点击添加部门 3.返回通讯录界面 4.验证
        self.main.goto_add_member().goto_add_depart().goto_contact(department).get_depart_list()

    @pytest.mark.parametrize('department', get_datas()['data']['department'])
    def test_con_test_adddepart(self, department):
        #主页 1.通讯录录 2.点击添加部门 3.返回通讯录界面 4.验证
        self.main.goto_contact().goto_add_depart().goto_contact(department).get_depart_list()