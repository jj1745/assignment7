'''
Created on Nov 2, 2015

@author: jj1745
'''

import numpy as np

class FirstQuestion(object):
    '''
    The class for the first question
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.initial_array =  np.zeros((5,3))

        for i in range(5):
            for j in range(3):
                self.initial_array[i,j] = (i+1) + 5*j
                
    def printOneA(self):
        '''
        print the answer for first question part (a)
        '''
        array_a = np.zeros((2,3))
        array_a[0] = self.initial_array[1]
        array_a[1] = self.initial_array[3]
        print "1. Part(a): \n", array_a 
        
    def printOneB(self):
        '''
        print the answer for first question part (b)
        '''
        array_b = self.initial_array[:,1]
        print "1. Part(b): \n", array_b
        
    def printOneC(self):
        '''
        print the answer for first question part (c)
        '''
        array_c = self.initial_array[1:4,:3]
        print "1. Part(c): \n", array_c
        
    def printOneD(self):
        '''
        print the answer for first question part (d)
        '''
        list_d = []
        for element in self.initial_array.flat:
            if element >= 3 and element <= 11:
                list_d.append(element)
        array_d = np.array(list_d)
        print "1. Part(d): \n", array_d  