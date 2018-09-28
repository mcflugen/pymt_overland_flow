from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import OverlandFlow

OverlandFlow = bmi_factory(OverlandFlow)

del bmi_factory
