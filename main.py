import multiprocessing as mp
import pandas as pd
import numpy as np
import time, datetime
from random import randint

DATASET = 'D1'
WORKERS = 4

# ------
class RequestClient:
    def sendData(self, data):
        t = randint(2, 6) / 10
        time.sleep(t)
        return

requestClient = RequestClient()

# ------
def do_work(queue):
    # Get the current worker's name
    worker_name = mp.current_process().name

    while True:
        if queue.empty():
            # print("queue is empty")
            break
        else:
            # print("get data in worker " + worker_name)
            data = queue.get()
            requestClient.sendData(data)
        
   

def fillQueue(dataset, queue):
    for data in dataset:
        queue.put(data)


def sendDataParallel(dataset, workers):
    m = mp.Manager()
    pqueue = m.Queue()
    processes = []

    startTime = int(time.time())

    fillQueue(dataset, pqueue) 

    for c in range(workers): 
        p = mp.Process(target=do_work, args=((pqueue),))
        p.name = 'worker ' + str(c)
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    finishTime = int(time.time())
    return finishTime - startTime


def sendDataSequential(dataset):
    startTime = int(time.time())

    for row in dataset:
        requestClient.sendData(row)

    finishTime = int(time.time())
    return finishTime - startTime


# ------
if __name__ == '__main__':


    # get dataset
    df = pd.read_csv('datasets/' + DATASET + '.csv')
    dataset = df.to_numpy()

    print("Start sending data to cloud....")

    parallelTime = sendDataParallel(dataset, WORKERS)

    print("Parallel time: " + str(datetime.timedelta(seconds=parallelTime)))

    sequentialTime = sendDataSequential(dataset)

    print("Sequential time: " + str(datetime.timedelta(seconds=sequentialTime)))

    print("All data was sended!")

    speedup = sequentialTime / parallelTime
    eficiency = speedup / WORKERS

    print("Speedup: " + str(speedup))
    print("Eficiency: " + str(eficiency))



    