from setuptools import find_packages, setup
import sys
import os

sys.path.insert(0, os.path.abspath( os.path.dirname(__file__)))


requirements_path="requirements.txt"
with open(requirements_path) as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    name="generic_analysis",
    version="0.0.1",
    description = "Generic analysis",
    long_description="Analysing with Python.",
    url="https://github.com/j-oshi/docker-jupyter-notebook",
    author= "J Oshin",
    packages= find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires =">= 3.0.*",
)