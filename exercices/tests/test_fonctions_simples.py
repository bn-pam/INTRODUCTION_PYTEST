from exercices.src.fonctions_simples import add, divide, add_integer, alea_uniform
import pytest

def test_add():
    assert add (1,2) == 3


def test_add_negative():
    assert add (-1,2) == 1

#def divide_by_zero_error():
 #   with pytest.raises(ValueError): #equivalent de l'assertion d'une erreur
 #       divide(1,0)

def test_divide():
    assert divide (1,1) == 1

def test_error_when_integer():
    with pytest.raises(TypeError): #equivalent de l'assertion d'une erreur
        add_integer(1.1,2.1)

# def test_alea_uniform():
#     assert alea_uniform not isinstance(element, float):
#         raise TypeError("Vous devez passer une chaîne de caractères")

def test_alea_uniform():
    assert isinstance (alea_uniform(0,10), float) 
    assert alea_uniform(0,10) >= 0 
    assert alea_uniform(0,10) <=10
    
def test_alea_uniform_error():
    with pytest.raises(TypeError):
        alea_uniform(0,"a")


####### CORRIGE #######

#### test add ####
def test_add_int():
    assert add (1,2) == 3
    assert add (0,0) == 0
    assert add (-1,1) == 0
    assert add (-1,-1) == -2

def test_add_floats():
    assert add (1.0,2.0) == 3.0
    assert add (0.0,0.0) == 0.0
    assert add (-1.0,1.0) == 0.0
    assert add (-1.0,-1.0) == -2.0

def test_add_integer_floats():
    assert add (1,2.0) == 3.0

def test_add_strings():
    assert add ("a","b") == "ab"
    assert add ("","") == ""
    assert add ("","b") == "b"
    assert add ("a","") == "a"

def test_add_list():
    assert add ([1,2,3], [4,5,6]) == [1,2,3,4,5,6]
    assert add ([1,2,3], [])== [1,2,3]
    assert add ([], [4,5,6]) == [4,5,6]
    assert add ("a","") == "a"

#### test divide ####
def test_divide_ok():
    assert divide(1,1) == 1
    assert divide(1,2) == 0.5
    assert divide(2.2,2) == 1.1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError): #cas particulier de l'erreur générée par une division par zero
        divide(8,0) #donner un cas pour lequel on a une division par zero


