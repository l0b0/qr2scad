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
3. Remove the residue around the holes with a piece of cloth, leaving the color
in the holes intact.

Examples:

qr2scad < example.png > example.scad
    Convert example.png to example.scad

<http://www.thingiverse.com/thing:4448>

Bugs:

Please email bug reports to victor dot engmark at gmail dot com.
"""

__author__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__license__ = 'GPLv3'

from PIL import Image, ImageOps
from signal import signal, SIGPIPE, SIG_DFL
import sys

BLOCK_SIZE = 1
"""<http://www.denso-wave.com/qrcode/qrgene3-e.html> recommends at least four
dots per module, so with a 0.1mm accuracy you should use at least 0.4 +
BLOCK_PADDING.
"""

BLOCK_PADDING = 0.01
"""Cubes have to be less than 1 unit wide. Otherwise you will get the message
"Object isn't a valid 2-manifold!" on STL export (see
<http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/STL_Import_and_Export>)."""

BLOCK_SIDE = BLOCK_SIZE - BLOCK_PADDING
"""This is the actual side length of a block."""

PDP_SIDE = 7
"""The position detection patterns (PDPs) are 7x7 pixels."""

signal(SIGPIPE, SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""


def qr2scad(stream):
    """Convert black pixels to OpenSCAD cubes."""

    img = Image.open(stream)

    # Convert to black and white 8-bit
    if img.mode != 'L':
        img = img.convert('L')

    # Invert color to get the right bounding box
    img = ImageOps.invert(img)

    bbox = img.getbbox()

    # Crop to only contain contents within the PDPs
    img = img.crop(bbox)

    width, height = img.size

    assert width == height,\
        'The QR code should be a square, but we found it to be %(w)sx%(h)s' % {
            'w': width,
            'h': height
        }

    qr_side = width

    # Get the resize factor from the PDP size
    new_size = qr_side / (list(img.getdata()).index(0) / (PDP_SIDE - 1))

    # Set a more reasonable size
    img = img.resize((new_size, new_size))
    qr_side = new_size

    img_matrix = img.load()

    result = ''

    result += 'module qrcode() {\n'
    for row in range(qr_side):
        for column in range(qr_side):
            if img_matrix[column, row] != 0:
                result += '    translate([%(x)s, %(y)s, 0])' % {
                    'x': BLOCK_SIZE * column - qr_side / 2,
                    'y': -BLOCK_SIZE * row + qr_side / 2
                }
                result += ' cube([%(block_side)s, %(block_side)s, 1]);\n' % {
                    'block_side': BLOCK_SIDE
                }
    result += '}\n'
    result += 'qrcode();'

    return result


def main(argv=None):
    result = qr2scad(sys.stdin)
    print result

if __name__ == '__main__':
    sys.exit(main())
