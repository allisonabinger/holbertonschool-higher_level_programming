#!/usr/bin/python3
"""Unit Tests for base.py

    Classes to test from base.py
    
        TestBase_inst
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

class TestBase_inst(unittest.TestCase):
    """
    Unit Tests for testing the instantiation for the base class
    """

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
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)
  



if __name__ == '__main__':
    unittest.main()
