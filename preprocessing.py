import math
import os
import multiprocessing as mp
import pandas as pd
import numpy as np
import time, datetime


# ------------------------
def _clear_worker(args):
    chunk, replacer = args
    for c in chunk:
        if not(type(c) is float) and not(type(c) is int):
            c = replacer
    return chunk

def clearDataParallel(col, replacer, workers):
    pool = mp.Pool(processes=workers)
    result = pool.map(_clear_worker, [(chunk, replacer) 
        for chunk in np.array_split(col, workers)])
    pool.close()
    pool.join()

    return pd.concat(result)

# ------------------------
def _sum_worker(chunk):
    return np.sum(chunk)

def averageParallel(col, workers):
    pool = mp.Pool(processes=workers)
    result = pool.map(_sum_worker, [(chunk) 
        for chunk in np.array_split(col, workers)])
    pool.close()
    pool.join()
    return np.sum(result) / len(col)

# ------------------------
def _variance_worker(args):
    chunk, avg = args
    calc = []
    for c in chunk:
        if np.isnan(c):
            c = 0
        di = np.power(c - avg, 2)
        calc.append(di)
    return np.sum(calc)

def varianceParallel(col, avg, workers):
    pool = mp.Pool(processes=workers)
    result = pool.map(_variance_worker, [(chunk, avg) 
        for chunk in np.array_split(col, workers)])
    pool.close()
    pool.join()
    return np.sum(result) / len(col)

def executeParallel(col, processes):
    # clear column
    cleared_col = clearDataParallel(col, 0, processes)

    # get column average
    avg = averageParallel(cleared_col, processes)
    print('Average: ' + str(avg))

    # get column variance
    variance = varianceParallel(cleared_col, avg, processes)
    print('Variance: ' + str(variance))

    # get column standart deviation
    std_dev = math.sqrt(variance)
    print('Standart deviation: ' + str(std_dev))

    # clear column
    cleared_col = _clear_worker((col, 0))

    # get column average
    avg = _sum_worker(cleared_col) / len(cleared_col)
    print('Average: ' + str(avg))

    # get column variance
    variance = _variance_worker((cleared_col, avg))
    print('Variance: ' + str(variance))

    # get column standart deviation
    std_dev = math.sqrt(variance)
    print('Standart deviation: ' + str(std_dev))


# ------
if __name__ == '__main__':


    # get dataset
    df = pd.read_csv('beach-water-quality-automated-sensors-1.csv')
    col = df['Turbidity']

    startTime = int(time.time())


    executeParallel(col, 1)

    finishTime = int(time.time())
    diffTime =  finishTime - startTime
    print(str(datetime.timedelta(seconds=diffTime)))

