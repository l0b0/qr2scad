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
from StringIO import StringIO
import sys
import unittest

from qr2scad import qr2scad

EXAMPLE_FILE = os.path.join(os.path.dirname(__file__), './example.png')

class TestConvert(unittest.TestCase):
    """Framework for testing file conversion."""
    # pylint: disable-msg=R0904

    def setUp(self):
        """Set stdin and stdout."""
        # pylint: disable-msg=C0103
        self.stdin_backup = sys.stdin

        self.stdout_backup = sys.stdout
        self.output_stream = StringIO()
        sys.stdout = self.output_stream
        
        self.output_file = None


    def test_standard_file(self):
        """Check that a simple QR code results in some data."""
        sys.stdin = open(EXAMPLE_FILE)
        qr2scad.main()
        self.assertNotEqual(
            self.output_stream.getvalue(),
            '')


    def tearDown(self):
        """Restore stdin and stdout."""
        # pylint: disable-msg=C0103
        sys.stdin = self.stdin_backup
        sys.stdout = self.stdout_backup


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
