import multiprocessing as mp
import pandas as pd
import numpy as np
import time, datetime
from random import randint


class RequestClient:
    def sendData(self, data):
        t = randint(2, 6) / 10
        time.sleep(t)
        return

requestClient = RequestClient()

def request_worker(chunk):
    for row in chunk:
        requestClient.sendData(row)
    return

def request_worker_queue(queue):
    while True:
        data = queue.get()
        requestClient.sendData(data)

def fillQueue(dataset, queue):
    for data in dataset:
        queue.put(data)


def sendDataParallel(dataset, workers):
    startTime = int(time.time())

    pool = mp.Pool(processes=workers)
    result = pool.map(request_worker, [(chunk) 
        for chunk in np.array_split(dataset, workers)])
    pool.close()
    pool.join()

    finishTime = int(time.time())
    return finishTime - startTime

def sendDataSequential(dataset):
    startTime = int(time.time())

    request_worker(dataset)

    finishTime = int(time.time())
    return finishTime - startTime


# ------
if __name__ == '__main__':

    workers = 4

    # get dataset
    # df = pd.read_csv('datasets/beach-water-quality-automated-sensors-1.csv')
    df = pd.read_csv('datasets/dataset.csv')
    dataset = df.to_numpy()

    print("Start sending data to cloud....")

    sequentialTime = sendDataSequential(dataset)

    print("Sequential time: " + str(datetime.timedelta(seconds=sequentialTime)))

    parallelTime = sendDataParallel(dataset, workers)

    print("Parallel time: " + str(datetime.timedelta(seconds=parallelTime)))

    print("All data was sended!")

    speedup = sequentialTime / parallelTime
    eficiency = speedup / workers

    print("Speedup: " + str(speedup))
    print("Eficiency: " + str(eficiency))



    