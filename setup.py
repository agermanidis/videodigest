#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='videodigest',
    version='0.0.1',
    description='Command-line utility for generating summaries of subtitled videos using automatic text summarization',
    author='Anastasis Germanidis',
    author_email='agermanidis@gmail.com',
    url='https://github.com/agermanidis/videodigest',
    scripts=['videodigest'],
    install_requires=[
        'sumy>=0.3.0',
        'moviepy>=0.2.2.11',
        'pysrt>=1.0.1',
    ],
    license=open("LICENSE").read()
)
