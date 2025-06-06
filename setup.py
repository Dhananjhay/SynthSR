#!/usr/bin/env python

import sys
import os
import setuptools

python_version = sys.version[:3]
if python_version != '3.6':
    raise Exception("Setup.py only works with python version 3.6")
else:
    # Read install_requires from requirements.txt
    with open('requirements.txt') as f:
        required_packages = [line.strip() for line in f.readlines()]

    # Find the files inside models/ and scripts/ so we can install them
    def collect_all_files(top_dir):
        """
        Walk through top_dir (e.g. "models" or "scripts") and return a list
        of all file paths (relative to the repo root). We'll feed these
        into data_files so they get copied into site-packages/SynthSR/<top_dir>.
        """
        all_files = []
        for root, _, files in os.walk(top_dir):
            for fn in files:
                # Join root + filename
                rel_path = os.path.join(root, fn)
                all_files.append(rel_path)
        return all_files

    # Collect everything under models/ and scripts/
    model_files = collect_all_files("models")
    script_files = collect_all_files("scripts")

    data_files = [
        ("SynthSR/models", model_files),
        ("SynthSR/scripts", script_files),
    ]

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

        data_files=data_files,
    )
