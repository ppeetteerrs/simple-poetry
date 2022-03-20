#!/usr/bin/env python

from dunamai import Version
from setuptools import find_packages, setup

setup(
    author="Peter Yuen",
    author_email="ppeetteerrsx@gmail.com",
    python_requires=">=3.8",
    description="A clean, automated setup for publishing simple Python packages to PyPI and Anaconda.",
    install_requires=[
        x.strip() for x in open("requirements.txt").readlines() if x.strip() != ""
    ],
    license="MIT license",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="simple-pypackage",
    name="simple-pypackage",
    packages=find_packages(
        include=["simple_pypackage", "simple_pypackage.*"],
        exclude=["docs"],
    ),
    package_data={
        "": ["*.txt"],
    },
    test_suite="tests",
    url="https://github.com/ppeetteerrs/simple-pypackage",
    version=Version.from_any_vcs().serialize(),
    zip_safe=False,
    options={"bdist_wheel": {"universal": True}},
)
