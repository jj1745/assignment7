'''
Created on Oct 30, 2015

@author: jj1745
'''

from question1 import FirstQuestion
from question2 import SecondQuestion
from question3 import ThirdQuestion

if __name__ == '__main__':
    '''
    This is the main program the prints answers for all questions
    '''
    # Create an FirstQuestion object. Call the ''print solution'' function
    q1 = FirstQuestion()
    q1.printOneA()
    q1.printOneB()
    q1.printOneC()
    q1.printOneD()
    
    # Create an SecondQuestion object. 
    print "\n"
    q2 = SecondQuestion()
    q2.printTwo()
    
    # Create an ThirdQuestion object.
    print "\n"
    q3 = ThirdQuestion()
    q3.printThree()
    
    print "\n"
    print "4. Please see mandelbrot.png"
    
    