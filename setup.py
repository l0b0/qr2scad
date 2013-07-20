#!/usr/bin/env python
"""
Setup configuration
"""

from setuptools import setup
from qr2scad import (
    __package__,
    __version__,
    __doc__,
    __url__,
    __author__,
    __email__,
    __maintainer__,
    __license__,
)

setup(
    name=__package__,
    version=__version__,
    description='QR code to OpenSCAD converter',
    long_description=__doc__,
    url=__url__,
    keywords='QR code QRcode convert converter OpenSCAD SCAD CAD',
    packages=[__package__],
    install_requires=['pillow'],
    entry_points={
        'console_scripts': ['qr2scad=qr2scad.qr2scad:main']},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Artistic Software',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion'
    ],
    test_suite='tests.tests',
    author=__author__,
    author_email=__email__,
    maintainer=__maintainer__,
    maintainer_email=__email__,
    download_url='https://github.com/l0b0/qr2scad/tarball/v' + __version__,
    platforms=['POSIX', 'Windows'],
    license=__license__,
)
