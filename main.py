import datetime

from src.dataset import Dataset

import parallel, sequential

TWO_WORKERS = 2
FOUR_WORKERS = 4


def compareExecutions(datasetName):
    dataset = Dataset(datasetName).getData()

    print("-----------------------------------------")
    print("Start sending data from dataset " + datasetName + " to cloud....")

    sequentialTime = sequential.execute(dataset)

    print("Sequential time: " + str(datetime.timedelta(seconds=sequentialTime)))



    parallelTwoWorkersTime = parallel.execute(dataset, TWO_WORKERS)

    print("Parallel with 2 processes: " + str(datetime.timedelta(seconds=parallelTwoWorkersTime)))
    speedupTwoWorkers = sequentialTime / parallelTwoWorkersTime
    eficiencyTwoWorkers = speedupTwoWorkers / TWO_WORKERS

    print("Speedup: " + str(speedupTwoWorkers))
    print("Eficiency: " + str(eficiencyTwoWorkers))



    parallelFourWorkersTime = parallel.execute(dataset, FOUR_WORKERS)

    print("Parallel with 4 processes: " + str(datetime.timedelta(seconds=parallelFourWorkersTime)))

    speedupFourWorkers = sequentialTime / parallelFourWorkersTime
    eficiencyFourWorkers = speedupFourWorkers / FOUR_WORKERS

    print("Speedup: " + str(speedupFourWorkers))
    print("Eficiency: " + str(eficiencyFourWorkers))
    print("-----------------------------------------")


if __name__ == '__main__':

    compareExecutions('D1')
    compareExecutions('D2')
    compareExecutions('D3')
    compareExecutions('D4')


    



    