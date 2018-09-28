#! /usr/bin/env python
import os
import sys
from distutils.extension import Extension

import versioneer
from setuptools import find_packages, setup

try:
    import model_metadata
except ImportError:

    def get_cmdclass(*args, **kwds):
        return kwds.get("cmdclass", None)

    def get_entry_points(*args):
        return None


else:
    from model_metadata.utils import get_cmdclass, get_entry_points


packages = find_packages(include=["pymt_overland_flow"])
pymt_components = [("OverlandFlow=landlab.bmi.components:OverlandFlow", "meta")]

setup(
    name="pymt_overland_flow",
    author="Eric Hutton",
    description="PyMT plugin overland_flow",
    version=versioneer.get_version(),
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
