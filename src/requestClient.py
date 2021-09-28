from random import randint
import time

class RequestClient:
    # simulates an HTTP request
    def post(self, data):
        t = randint(2, 6) / 10 # 200ms to 600ms delay in requests
        time.sleep(t)

        # simulate errors in request
        e = randint(0, 99)
        if e < 3: # 2% error rate
            return True 
        else:
            return False