import multiprocessing as mp
import time

from src.requestClient import RequestClient

client = RequestClient() 

def worker(queue):
    # Get the current worker's name
    worker_name = mp.current_process().name

    while True:
        if queue.empty():
            # print("queue is empty")
            break
        else:
            # print("get data in worker " + worker_name)
            data = queue.get()
            client.post(data)


def createQueue(dataset):
    queue = mp.Manager().Queue()
    for data in dataset:
        queue.put(data)
    return queue

def createProcesses(workers, queue):
    processes = []
    for c in range(workers): 
        p = mp.Process(target=worker, args=((queue),))
        p.name = 'worker ' + str(c)
        processes.append(p)
        p.start()
    return processes

def syncProcesses(processes):
    for p in processes:
        p.join()


def execute(dataset, workers):   
    startTime = int(time.time())

    queue = createQueue(dataset) 
    processes = createProcesses(workers, queue)
    syncProcesses(processes)
    
    finishTime = int(time.time())
    return finishTime - startTime
        