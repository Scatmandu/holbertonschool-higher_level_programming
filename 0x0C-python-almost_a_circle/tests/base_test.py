#!/usr/bin/python3
"""This modules contains unittests for Base Class"""


import unittest
from unittest import result
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing Base Class"""

    @classmethod
    def create_class(cls):
        """create class"""
        cls.b1 = Base()
        cls.b2 = Base(1)
        cls.b3 = Base(2)
        cls.b4 = Base(3)
        cls.b5 = Base()

    @classmethod
    def destroy_class(cls):
        """destroy class"""
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5

    def test_instantation(self):
        """Testing init"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 5)

    def test_ID(self):
        """Testing id's"""
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def testToJsonString(self):
        """Testing to json string"""
        dict_list = [{'id': None}, {'id': 1}, {'id': 2}, {'id': 3}]
        self.assertEqual(Base.to_json_string(
            dict_list), '[{"id": null}, {"id": 1}, {"id": 2}, {"id": 3}]')

    def testFromJsonString(self):
        """Testing from json"""
        json_string = Base.to_json_string(
            [{'id': None}, {'id': 1}, {'id': 2}, {'id': 3}])
        self.assertEqual(Base.from_json_string(json_string),
                         [{"id": None}, {"id": 1}, {"id": 2}, {"id": 3}])
