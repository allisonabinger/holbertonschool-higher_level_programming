#!/usr/bin/python3
"""Unit Tests for base.py

    Classes to test from base.py
    
        TestBase_init
        TestBase_to_json_string
        TestBase_save_to_file
        TestBase_from_json_string
        TestBase_create
        TestBase_load_from_file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_init(unittest.TestCase):
    """
    Unit Tests for testing the initialization for the base class
    """

    def test_id_attr(self):
        """asserts if id is initialized"""
        base1 = Base()
        self.assertTrue(hasattr(base1, 'id'))

    def test_id_eq_noarg(self):
        """unittest for ids: no id given"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, base2.id - 1)
    
    def test_id_neq_noarg(self):
        """unitttest for ids: no id given, using notequal"""
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)
    
    def test_id_none_arg(self):
        """unitttest for id: 'None' used as id"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)
    
    def test_id_arg_given(self):
        """unittest for id: argument given at initialization"""
        self.assertEqual(6, Base(6).id)
    
    def test_id_public_att(self):
        """unittest for id: accessing a public attribute"""
        base1 = Base(3)
        base1.id = 4
        self.assertEqual(4, base1.id)
    
    def test_float_id(self):
        """unittest for id: float given instead of int"""
        self.assertEqual(4.7, Base(4.7).id)
    
    def test_false_att(self):
        """unittest for class attribute: given a false attribute"""
        with self.assertRaises(AttributeError):
            print(Base(1).__nb_instance)
    
    def test_private_att(self):
        """unittest for class attribute: access private attribute"""
        with self.assertRaises(AttributeError):
            print(Base().__nb_objects)

class TestBase_to_json_string(unittest.TestCase):
    """
    Unit testing for the to_json_string method in the Base Class
    """

    def test_ld_is_None(self):
        """unittest for json string: if method returns a string"""
       
        r = Rectangle(10, 8, 6, 4, 2)
        self.assertTrue(str, type(Base.to_json_string([r.to_dictionary()])))
    
    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))
    
    def test_none_list(self):
        self.assertEqual("[]", Base.to_json_string(None))
    
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

class TestBase_save_to_file(unittest.TestCase):
    """
    Unit testing for the save_to_file method in the Base class
    """

    def test_save_square(self):
        s = Square(10, 7, 2, 8, )
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
    
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

class TestBase_create(unittest.TestCase):
    """
    Unit testing for the save_to_file method in the Base
    """

    def test_create_square(self):
        square1 = Square(4, 2, 1, 3)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertEqual("[Square] (3) 2/1 - 4", str(square2))

    def test_create_square_notequal(self):
        square1 = Square(4, 2, 1, 3)
        square1_dict = square1.to_dictionary()
        square2 = Square.create(**square1_dict)
        self.assertNotEqual(square1, square2)
    
class TestBase_load_from_file(unittest.TestCase):
    """
    Unit testing for the load_from_file in the Base Class
    """

    def test_invalid_arg_num(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)
    
"""
------------------------------
Need to add more tests here
------------------------------
"""


    
    
     




    
    

  



if __name__ == '__main__':
    unittest.main()
