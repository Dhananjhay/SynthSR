#!/usr/bin/env python

import sys
import setuptools

python_version = sys.version[:3]

if python_version != '3.6':
    raise Exception('Setup.py only works with python version 3.6'.format(python_version))

else:

    with open('requirements.txt') as f:
        required_packages = [line.strip() for line in f.readlines()]

    print(setuptools.find_packages())

    setuptools.setup(name='SynthSR',
                     version='2.0',
                     license='Apache 2.0',
                     description='Domain-agnostic segmentation of brain scans',
                     author='Benjamin Billot',
                     url='https://github.com/BBillot/SynthSR',
                     keywords=['super-resolution', 'modality synthesis', 'domain-agnostic', 'brain'],
                     packages=setuptools.find_packages(),
                     python_requires='>=3.6',
                     install_requires=required_packages,
                     include_package_data=True)
