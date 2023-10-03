#!/usr/bin/python3
"""
----------------------
Unit Tests for rectangle.py
----------------------

** Methods in rectangle.py tested as Classes:

    ----------------------------------
        TestBase_init
        TestBase_to_json_string
        TestBase_save_to_file
        TestBase_from_json_string
        TestBase_create
        TestBase_load_from_file
    ----------------------------------

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle_init(unittest.TestCase):
    """
    Unit Tests for testing the initialization for the rectangle class
    """

    def test_init_compare_rectangles_width(self):
        r1 = Rectangle(5, 4, 0, 0, None)
        r2 = Rectangle(5, 3, 0, 0, None)
        self.assertEqual(r1.width, r2.width)

    def test_init_compare_rectangles_height(self):
        r1 = Rectangle(4, 7, 0, 0, None)
        r2 = Rectangle(2, 7, 0, 0, None)
        self.assertEqual(r1.height, r2.height)

    def test_different_id(self):
        r1 = Rectangle(5, 4, 3, 2, None)
        r2 = Rectangle(5, 4, 3, 2, None)
        self.assertNotEqual(r1.id, r2.id)
    
    def test_width_getter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        self.assertEqual(5, r1.width)

    def test_width_setter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        r1.width = 3
        self.assertEqual(3, r1.width)
    
    def test_height_getter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        self.assertEqual(4, r1.height)

    def test_height_setter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        r1.height = 3
        self.assertEqual(3, r1.height)
    
    def test_x_getter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        self.assertEqual(4, r1.x)
    
    def test_x_setter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        r1.x = 2
        self.assertEqual(2, r1.x)

    def test_y_getter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        self.assertEqual(4, r1.x)

    def test_x_getter(self):
        r1 = Rectangle(5, 4, 4, 4, 1)
        r1.y = 3
        self.assertEqual(4, r1.x)
        

class TestRectangle_width(unittest.TestCase):
    """
    Unit test for the width attribute in the Rectangle
    """

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.4, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle('4', 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(["one", "two"], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"one", "two"}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(("one", "two"), 2)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 2)

class TestRectangle_height_attr(unittest.TestCase):
    """
    Unit test for the height attribute in the Rectangle
    """

    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 5.4)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, '4')

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"a": 1, "b": 2})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, False)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, ["one", "two"])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {"one", "two"})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, ("one", "two"))

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2,complex(4))

class TestRectangle_x_attr(unittest.TestCase):
    """
    Unittests for testing x attribute
    """

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)


class TestRectangle_y(unittest.TestCase):
    """
    Unittests for testing y attribute
    """

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))



"""
-----------------
Need more test here.
-----------------
"""


if __name__ == '__main__':
    unittest.main()
