`qr2scad` QR code to OpenSCAD converter
=======================================

Why use this? If someone sees the QR code on your thing in real life, they can find the design and make their own copies with just a photo of it. Theoretically, you could even assign this job to a machine, looking around the web (or your tool box) for things that can be duplicated.

Installation / upgrade
----------------------

    pip install --upgrade https://github.com/l0b0/qr2scad/tarball/master

To install a specific version `X.Y.Z` (only 0.6.2 onward):

    pip install https://github.com/l0b0/qr2scad/tarball/vX.Y.Z

How to use
----------

1. Create an OpenSCAD file with your QR code:

        qr2scad < qr_code.png > qr_code.scad
2. [`include`](http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/Include_Statement) `qr_code.scad` in your OpenSCAD file.
3. [`difference`](http://en.wikibooks.org/wiki/OpenSCAD_User_Manual/CSG_Modelling#difference) the `qr_code` module from a flat surface.
4. Create the thing.
5. Use a marker, paint or other substance to fill the holes with a contrasting color.
6. Clean off excess color to get a crisp, scannable QR code.
