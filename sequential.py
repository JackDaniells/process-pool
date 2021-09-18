import time

from src.requestClient import RequestClient

def execute(dataset):
    client = RequestClient()

    startTime = int(time.time())

    for row in dataset:
        client.post(row)

    finishTime = int(time.time())
    return finishTime - startTime
        