from homework.homework2.pages.app import App

import sys
sys.path.append('..')
class Test_Contact :
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        self.app.stop()

    def test_addcontact(self):
        username = "13911111118"
        phonenum = "13911111118"
        self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_member(username, phonenum).verify_ok().goto_personalpage().goto_detailspage().goto_editpage().del_person()

    # def test_addcontact1(self):
    #     username = "13911111117"
    #     phonenum = "13911111117"
    #     self.main.goto_contactlistpage().goto_addmemberpage().addmember_bymenual().edit_member(username, phonenum).verify_ok()