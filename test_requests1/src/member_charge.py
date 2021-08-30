import requests

from test_requests1.src.base import Base


class TestMemberCharge(Base):
    def test_add(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            "userid": "zhangsan",
            "name": "张三",
            "mobile": "+86 13800000000",
            "department": [1],
        }
        # json 代表把数据转为 json 进行发送
        r = requests.post(url, json=data)
        return r.json()

    def test_delete(self):
        userid = 'zhangsan'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}'
        r = requests.get(url)
        return r.json()

    def test_update(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}'
        data = {
            "userid": "zhangsan",
            "name": "李四",
        }
        r = requests.post(url, json=data)
        return r.json()

    def test_find(self):
        userid = 'zhangsan'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}'
        r = requests.get(url)
        return r.json()
