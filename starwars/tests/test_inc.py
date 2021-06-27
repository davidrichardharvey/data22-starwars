# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 15:44:10 2021

@author: Andrew Rothwell
"""

'''
Two functions to test if I can correctly call the function "inc" in the "app"
module.

Firstly, the "test_incPass" function will assert a correct answer, and then
"test_incFail" will assert an incorrect one. Assuming they both return the
expected answers I can assume I have correctly implemented these unit tests
using the PyTest module.
'''

from starwars.app.inc import inc

def test_incPass():
    
    assert inc(3) == 4
    
def test_incFail():
    
    assert inc(3) == 5

