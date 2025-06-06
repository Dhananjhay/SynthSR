#!/usr/bin/env python

import sys
import os
import shutil
import setuptools

python_version = sys.version[:3]
if python_version != '3.6':
    raise Exception("Setup.py only works with python version 3.6")

# Read install_requires from requirements.txt
with open('requirements.txt') as f:
    required_packages = [line.strip() for line in f.readlines()]

# Copy models/ and scripts/ into SynthSR/ so they are packaged properly
for folder in ['models', 'scripts']:
    dest = os.path.join('SynthSR', folder)
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(folder, dest)

setuptools.setup(
    name="SynthSR",
    version="2.0",
    license="Apache 2.0",
    description="Domain-agnostic segmentation of brain scans",
    author="Benjamin Billot",
    url="https://github.com/BBillot/SynthSR",
    keywords=["super-resolution", "modality synthesis", "domain-agnostic", "brain"],

    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=required_packages,

    include_package_data=True,
    package_data={
        'SynthSR': ['models/*', 'scripts/*.py'],
    },
)
