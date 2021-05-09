import pytest
import yaml

from homework.homework2.pages.app import App

import sys
sys.path.append('..')

def get_datas():
    with open("./datas.yaml", encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

class Test_Contact :
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('username, phonenum', get_datas()['data']['creat'] )
    #@pytest.mark.parametrize('phonenum', get_datas()['data']['phonenum'])
    def test_addcontact(self, username, phonenum):
        self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_member(username, phonenum).verify_ok().goto_personalpage().goto_detailspage(username).goto_editpage().del_person()

    # def test_addcontact1(self):
    #     username = "13911111117"
    #     phonenum = "13911111117"
    #     self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_member(username, phonenum).verify_ok()