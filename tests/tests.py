#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
qr2scad test suite

Default syntax:

./tests.py
    Run all unit tests
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

from doctest import testmod
from os.path import join, dirname
import unittest

from qr2scad import qr2scad

EXAMPLE_BIG = join(dirname(__file__), './example_big.png')
EXAMPLE_BW = join(dirname(__file__), './example_bw.png')
EXAMPLE_RGB = join(dirname(__file__), './example_rgb.png')


class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""
    # pylint: disable-msg=R0904

    def test_black_and_white(self):
        """Check that a black-and-white image gives output."""
        result = qr2scad.qr2scad(open(EXAMPLE_BW))
        self.assertNotEqual(
            result,
            '')
        self.assertNotEqual(
            result,
            'module qrcode() {\n}\nqrcode();\n')


    def test_rgb(self):
        """Check that an RGB image gives output."""
        result = qr2scad.qr2scad(open(EXAMPLE_RGB))
        self.assertNotEqual(
            result,
            '')
        self.assertNotEqual(
            result,
            'module qrcode() {\n}\nqrcode();\n')


    def test_big(self):
        """Check that a big image gives output."""
        self.input_stream = open(EXAMPLE_BIG)
        result = qr2scad.qr2scad(self.input_stream)
        self.assertNotEqual(
            result,
            '')
        self.assertNotEqual(
            result,
            'module qrcode() {\n}\nqrcode();\n')


    def test_equal(self):
        """Check that the valid examples all result in the same output."""
        result_big = qr2scad.qr2scad(open(EXAMPLE_BIG))

        result_bw = qr2scad.qr2scad(open(EXAMPLE_BW))

        result_rgb = qr2scad.qr2scad(open(EXAMPLE_RGB))

        self.assertNotEqual(
            result_big,
            '')
        self.assertNotEqual(
            result_big,
            'module qrcode() {\n}\nqrcode();\n')
        self.assertNotEqual(
            result_bw,
            '')
        self.assertNotEqual(
            result_rgb,
            '')
        self.assertEqual(
            result_bw,
            result_rgb)
        self.assertEqual(
            result_big,
            result_bw)


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(testmod(qr2scad)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
