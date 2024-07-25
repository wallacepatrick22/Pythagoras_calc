import pytest
import Pythagoras.source as source

# test sqrt function for scenario where input is an even number
def test_sqrt_even():
    input = 4
    expected_output = 2.0
    output = source.sqrt(input)
    assert output == expected_output
 
 # test sqrt function for scenario where input is an odd number   
def test_sqrt_odd():
    input = 9
    expected_output = 3.0
    output = source.sqrt(input)
    assert output == expected_output
    
# test sqrt function for scenario where input is a negative number    
def test_sqrt_odd():
    input = -9
    expected_output = 3.0
    output = source.sqrt(input)
    assert output == expected_output
    
# test hypot function



