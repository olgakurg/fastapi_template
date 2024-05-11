from msgspec import Struct, json


class MsgOutput(Struct):
    res: int

    def decode(self, msg):
        return json.decode(msg=msg, type=self.__class__.__name__)

    def encode(self):
        return json.encode(self)
