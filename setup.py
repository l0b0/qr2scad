#!/usr/bin/env python
"""
Setup configuration

Prerequisites: PIL
"""

from setuptools import find_packages, setup
from qr2scad.qr2scad import __doc__ as module_doc

setup(
    name = 'qr2scad',
    version = '0.6.2',
    description = 'QR code to OpenSCAD converter',
    long_description = module_doc,
    url = 'http://github.com/l0b0/qr2scad',
    keywords = 'QR code QRcode convert converter OpenSCAD SCAD',
    packages = find_packages(exclude=['tests']),
    install_requires = ['PIL'],
    entry_points = {
        'console_scripts': ['qr2scad = qr2scad.qr2scad:main']},
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
    ],
    test_suite = 'tests.tests',
    author = 'Victor Engmark',
    author_email = 'victor.engmark@gmail.com',
    maintainer = 'Victor Engmark',
    maintainer_email = 'victor.engmark@gmail.com',
    download_url = 'http://github.com/l0b0/qr2scad',
    platforms = ['POSIX', 'Windows'],
    license = 'GPL v3 or newer',
    )
