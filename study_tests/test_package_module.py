# -*- coding: utf-8 -*-

import pytest

# **pytestをsample_packageディレクトリがカレントディレクトリに含まないとテストは通らない**
import sample_package
#import sample_package.sample_module
from sample_package import sample_module

def test_package_and_module():
  assert 'package' == sample_package.PACKAGE_CONST
  #assert 'module' == sample_package.sample_module.MODULE_CONST
  assert 'module' == sample_module.MODULE_CONST
