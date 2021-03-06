# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:35:43 2018

@author: Christian
"""
import numpy as np
import pandas as pd
import math as math
import glob
from sklearn.model_selection import cross_validate
#from sklearn.cross_validation import cross_validate

def binarySearch(dataset, classifier):
    returnListDfs = []
    cols = ['Strategy', 'Dataset', 'n_instances', 'l_attributes', 'k_neighbours', 'fit_time', 'accuracy', 'f1_macro', 'f1_micro']
    returnmainDf = pd.DataFrame(columns=cols)
    for idx, data in enumerate(dataset):
        try:
            # Get the n
            n = data.shape[0]
            # Get the l
            l = data.shape[1]
            # lower/upperbounds
            lb = 1
            ub = round(2*n/3) - 1

            y = data['target']
            X = data.drop('target', axis=1)
            #'recall_macro', 'recall_micro', 'precision_macro', 'precision_micro'
            score_params = ['accuracy']

            classifier.set_params(n_neighbors = ub)
            scores = cross_validate(classifier, X, y, scoring=score_params, return_train_score=False)
            scores_ub = scores['test_accuracy'].mean()
            classifier.set_params(n_neighbors = lb)
            scores = cross_validate(classifier, X, y, scoring=score_params, return_train_score=False)
            scores_lb = scores['test_accuracy'].mean()
            k = 0
            while (ub-lb >= 1) & (abs(scores_ub-scores_lb) >= 0.01):
                if (scores_lb > scores_ub):
                    ub = round(abs(ub+lb)/2)
                    dummy = True
                    k = ub
                else:
                    lb = round(abs(ub+lb)/2)
                    dummy = False
                    k = lb
                if dummy == True:
                      print(ub)
                      classifier.set_params(n_neighbors = ub)
                      scores = cross_validate(classifier, X, y, scoring=score_params, return_train_score=False)
                      scores_ub = scores['test_accuracy'].mean()
                      print(scores_ub)
                else:
                    print(lb)
                    classifier.set_params(n_neighbors = lb)
                    scores = cross_validate(classifier, X, y, scoring=score_params, return_train_score=False)
                    scores_lb = scores['test_accuracy'].mean()
                    print(scores_lb)
        except Exception as e:
            print(e)
            continue
        score_params = ['accuracy', 'f1_macro', 'f1_micro']
        classifier.set_params(n_neighbors = k)
        scores = cross_validate(classifier, X, y, scoring=score_params, return_train_score=False)
        print(scores)
        scoreFrame = pd.DataFrame(scores)
        scoreFrame = scoreFrame.mean()
        returnDf = pd.DataFrame(scoreFrame)
        returnDf['Strategy'] = 'Binary Search'
        returnDf['Dataset'] = 'D' + str(idx)
        returnDf['n_instances'] = n
        returnDf['l_attributes'] = l
        returnDf['k_neighbours'] = k
        returnListDfs.append(returnDf)

    for dataf in returnListDfs:
        returnmainDf = returnmainDf.append(dataf)

    return returnmainDf
