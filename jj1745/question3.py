'''
Created on Nov 2, 2015

@author: jj1745
'''

import numpy as np

class ThirdQuestion(object):
    '''
    The class for the third question
    '''


    def __init__(self):
        '''
        Constructor
        '''
        np.random.seed(100)
        self.random_matrix = np.random.rand(10,3)
        
    def printThree(self):
        '''
        print the answer for question 3
        '''
        half_matrix = np.ones((10,3)) / 2
        difference = np.absolute(self.random_matrix - half_matrix)

        sorted_matrix = np.argsort(difference, axis = 1)

        output = self.random_matrix[sorted_matrix == 0]
    
        print "3. \n", np.array(output)