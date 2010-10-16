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

import doctest
import os
from cStringIO import StringIO
import sys
import unittest

from qr2scad import qr2scad

EXAMPLE_BW = os.path.join(os.path.dirname(__file__), './example_bw.png')
EXAMPLE_RGB = os.path.join(os.path.dirname(__file__), './example_rgb.png')


class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""
    # pylint: disable-msg=R0904

    def setUp(self):
        """Set streams."""
        # pylint: disable-msg=C0103
        self.input_stream = None
        self.stdin = sys.stdin
 
        self.output_stream = StringIO()
        self.stdout = sys.stdout


    def test_black_and_white(self):
        """Check that a black-and-white image gives output."""
        try:
            sys.stdout = self.output_stream
            self.input_stream = open(EXAMPLE_BW)
            sys.stdin = self.input_stream
            qr2scad.main()
            result = self.output_stream.getvalue()
            self.assertNotEqual(
                result,
                '')
        finally:
            sys.stdin = self.stdin
            sys.stdout = self.stdout
            self.input_stream.close()


    def test_rgb(self):
        """Check that an RGB image gives output."""
        try:
            sys.stdout = self.output_stream
            self.input_stream = open(EXAMPLE_RGB)
            sys.stdin = self.input_stream
            qr2scad.main()
            result = self.output_stream.getvalue()
            self.assertNotEqual(
                result,
                '')
        finally:
            sys.stdin = self.stdin
            sys.stdout = self.stdout
            self.input_stream.close()


    def test_bw_rgb(self):
        """Check that an RGB image gives the same output as for the equivalent
        black-and-white image."""
        try:
            sys.stdout = self.output_stream
            self.input_stream = open(EXAMPLE_BW)
            sys.stdin = self.input_stream
            qr2scad.main()
            result_bw = self.output_stream.getvalue()
        finally:
            sys.stdin = self.stdin
            sys.stdout = self.stdout
            self.input_stream.close()
            self.output_stream.close()

        try:
            self.output_stream = StringIO()
            sys.stdout = self.output_stream
            self.input_stream = open(EXAMPLE_RGB)
            sys.stdin = self.input_stream
            qr2scad.main()
            result_rgb = self.output_stream.getvalue()
        finally:
            sys.stdin = self.stdin
            sys.stdout = self.stdout
            self.input_stream.close()

        self.assertNotEqual(
            result_bw,
            '')
        self.assertNotEqual(
            result_rgb,
            '')
        self.assertEqual(
            result_bw,
            result_rgb)


    def tearDown(self):
        """Close streams."""
        # pylint: disable-msg=C0103
        self.input_stream.close()
        sys.stdin = self.stdin

        self.output_stream.close()
        sys.stdout = self.stdout


class TestDoc(unittest.TestCase):
    """Test Python documentation strings."""
    def test_doc(self):
        """Documentation tests."""
        self.assertEqual(doctest.testmod(qr2scad)[0], 0)


def main():
    """Run tests"""
    unittest.main()


if __name__ == '__main__':
    main()
