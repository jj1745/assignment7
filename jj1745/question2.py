'''
Created on Nov 2, 2015

@author: jj1745
'''

import numpy as np

class SecondQuestion(object):
    '''
    The class for the second question
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.a = np.arange(25).reshape(5,5)
        self.b = np.array([1.,5.,10.,15.,20.])
        
    def printTwo(self):
        '''
        print the answer for question 2
        '''
        c = np.zeros((5,5))
        
        for i in range(5):
            for j in range(5):
                c[i,j] = self.a[i,j] / self.b[i]   
    
        print "2. \n", c
        