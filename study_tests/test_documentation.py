# -*- coding: utf-8 -*-

import pytest

def add(left: '左項', right: '右項') -> '和':
  return left + right

def test_annotation():
  assert 10 == add(4, 6)
