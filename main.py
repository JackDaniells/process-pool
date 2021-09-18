import datetime

from src.dataset import Dataset

import parallel, sequential


def compareExecutions(datasetName):
    dataset = Dataset(datasetName).getData()

    print("-----------------------------------------")
    print("Start sending data from dataset " + datasetName + " to cloud....")

    sequentialTime = sequential.execute(dataset)

    print("Sequential time: " + str(datetime.timedelta(seconds=sequentialTime)))

    parallelTwoWorkersTime = parallel.execute(dataset, 2)

    print("Parallel with 2 threads: " + str(datetime.timedelta(seconds=parallelTwoWorkersTime)))

    parallelFourWorkersTime = parallel.execute(dataset, 4)

    print("Parallel with 4 threads: " + str(datetime.timedelta(seconds=parallelFourWorkersTime)))

    # speedup = sequentialTime / parallelTime
    # eficiency = speedup / workers

    # print("Speedup: " + str(speedup))
    # print("Eficiency: " + str(eficiency))
    print("-----------------------------------------")


if __name__ == '__main__':

    compareExecutions('D1')
    compareExecutions('D2')
    compareExecutions('D3')
    compareExecutions('D4')


    



    