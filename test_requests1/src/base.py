from test_requests1.src.token import Token


class Base:
    #类变量是指， 多个实例，类可以共用这个类
    token = None

    def __init__(self):
        if self.token is None:
            self.token = Token.get_token()