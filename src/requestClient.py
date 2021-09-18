from random import randint
import time

class RequestClient:
    def post(self, data):
        t = randint(2, 6) / 10
        time.sleep(t)
        return