import requests


class Token:
    @staticmethod
    def get_token():
        corpid = 'ww83cdadf3ebfb5bea'
        corpsecret = 'zW-vDcnqgWooflcnPfGhvboUjlTYPYHY0lAPR9Q-0Ws'
        url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
        r = requests.get(url)
        #.text 代表取原生返回值
        print(r.text)
        # r.json 代表将原生格式转换为json格式
        access_token = r.json()["access_token"]
        return access_token