#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
NAME
    qr2scad.py

SYNOPSIS
    qr2scad.py < input_file

DESCRIPTION
    Convert QR code images to OpenSCAD.

    The result can be used in an existing OpenSCAD file as follows:
    1. Remove the QR code from a flat surface using the difference() function.
    2. After printing, splash some removable paint or ink on the QR code holes.
    3. Remove the residue around the holes with a piece of cloth, leaving the color in the holes intact.

EXAMPLE
    ./qr2scad.py < example.png > example.scad

BUGS
    Please email bugs to victor dot engmark at gmail dot com.
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

import os
from PIL import Image
import signal
import sys

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""

def qr2scad():
    img = Image.open(sys.stdin)
    width, height = img.size

    # Convert image to boolean matrix (black is True)
    img_matrix = img.load()
    print 'module qrcode() {'
    for row in range(height):
        for column in range(width):
            if img_matrix[column, row] == (0, 0, 0) or img_matrix[column, row] == 0:
                print '    translate([%(x)s, -%(y)s, -1])' % {
                    'x': column,
                    'y': row
                }, 'cube();'
    print "}"
    print 'qrcode();'

def main(argv = None):
    qr2scad()

if __name__ == '__main__':
    main()
