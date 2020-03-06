from string_calculator.calculator import *
import pytest

def test_empty_string():

	assert add(" ") == 0

def test_add_two_numbers():
	
	assert add("1, 2") == 3

def test_add_multiple_numbers():
	
	assert add("1, 2, 3") == 6

def test_new_line_as_delimiter():
	
	assert add('1\n2,3') == 6

def test_different_delimiters():
	assert add('//;\n1;2') == 3

def test_negative_numbers_exception():
	
	with pytest.raises(Exception) as err:
		assert add("//;\n-1;2,-3") 
		assert str(err.value) == "negetives not allowed: -1,-3"

def test_bigger_than_1000():
	
	assert add('//;\n1000,1;2') == 3

def test_delimiters_any_length():
	
	assert add('//[***]\n1***2***3') == 6

def test_multiple_delimiters():
	
	assert add('//[*][%]\n1*2%3') == 6