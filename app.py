import pandas as pd
import numpy as np
import sys
sys.path.append('./functions/')
#from mainFunction import knn
from ConfigReader import ReadConfig
from importDataset import ImportAllDatasets
from gridsearch import *
from randomizedSearch import *
from mainFunction import *


# This is the main module the user calls

# The bulk of it goes below
def main():
    #Loading all csv files as datasets
    datasets=ImportAllDatasets()
#    print(type(datasets))

    # Load the configuration params
    k,interval,searchAlgo,optimization_Type,typeOfClassifier,radius,weight=ReadConfig()

    # TODO: create knn classifier
    # For now I have a placeholder
    #knn = KNeighborsClassifier(n_neighbors=100, n_jobs=-1)
    #print(knn)
    # TODO: this changes based on the config file


    # TODO: 1 optimize parameters

    # TODO: 1.1 Grid search
    #print(gridSearch([datasets[0][1]], knn))
    # for value in datasets:
    #     print(type(value))
    #     for thing in value:
    #         print(type(thing))

    # print(type(datasets[0][0]))

    # TODO: 1.2 Randomized search
    print(randomSearch([datasets[1]],5))
    

    #print(randomSearch([datasets[1]]),5)
    # TODO: 1.3 OurImplementation for brute force arround sqrt(n)

    # TODO: export report


   # print(knn)
    #print(knn.get_params())

    #lodf = grdSearch(datasets, knn)
    #print(lodf)


# TODO: tie the functions together

# TODO: produce the report

if __name__ == "__main__":
    main()

#%%
