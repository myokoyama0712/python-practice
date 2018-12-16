# -*- coding: utf-8 -*-

import pytest

from . import sub_sample_module # import sub_sample_module はpytest起動場所を問わず不可
from .. import sample_module
from ..sample_module import *

def test_relative_import():
  assert 'module' == MODULE_CONST
  assert 'sub_module' == sub_sample_module.MODULE_CONST
  assert 'module' == sample_module.MODULE_CONST
