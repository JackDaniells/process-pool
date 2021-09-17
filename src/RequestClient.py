import time

class RequestClient:
    def __init__(self, timeout):
        self.timeout = timeout

    def sendData(self, data):
        time.sleep(self.timeout)
