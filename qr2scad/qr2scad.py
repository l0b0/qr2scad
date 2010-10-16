#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""qr2scad - Convert QR code images to OpenSCAD
<http://github.com/l0b0/qr2scad>

Default syntax:

qr2scad < input_file

Description:

For each black pixel in the input, it will create a cube in the output.

The result can be used in an existing OpenSCAD file as follows:
1. Remove the QR code from a flat surface using the difference() function.
2. After printing, splash some removable paint or ink on the QR code holes.
3. Remove the residue around the holes with a piece of cloth, leaving the
color in the holes intact.

This code does not optimize the output in any way. If you get a really big
result file, try to scale it down and verify that it is still readable
using <http://zxing.org/w/decode.jspx>.

Examples:

./qr2scad.py < example.png > example.scad
    Convert example.png to example.scad

<http://www.thingiverse.com/thing:4448>

Bugs:

Please email bug reports to victor dot engmark at gmail dot com.
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

import os
from PIL import Image
import signal
import sys

BLOCK_HORIZONTAL_SIZE = 0.99
"""Cubes have to be less than 1 unit wide. Otherwise you will get the message
"Object isn't a valid 2-manifold!" on STL export (see 
<http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/STL_Import_and_Export>)."""

signal.signal(signal.SIGPIPE, signal.SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""

def qr2scad():
    """Convert black pixels to OpenSCAD cubes."""

    img = Image.open(sys.stdin)
    width, height = img.size

    img_matrix = img.load()
    print 'module qrcode() {'
    for row in range(height):
        for column in range(width):
            if sum(img_matrix[column, row]) == 0:
                print '    translate([%(x)s, %(y)s, 0])' % {
                    'x': column - width / 2,
                    'y': -row + height / 2
                }, 'cube([%(horizontal_size)s, %(horizontal_size)s, 1]);' % {
                    'horizontal_size': BLOCK_HORIZONTAL_SIZE
                }
    print '}'
    print 'qrcode();'

def main(argv = None):
    qr2scad()

if __name__ == '__main__':
    sys.exit(main())
