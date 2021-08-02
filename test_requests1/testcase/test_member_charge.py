from test_requests1.src.member_charge import MemberCharge


class TestMemberCharge:
    def setup(self):
        self.member = MemberCharge()

    def test_add(self):
        r = self.member.add()
        assert r.get('errcode') == 60104
        print(r)

    def test_delete(self):
        r = self.member.delete()
        print(r)

    def test_update(self):
        r = self.member.update()
        print(r)

    def test_find(self):
        r = self.member.find()
        print(r)