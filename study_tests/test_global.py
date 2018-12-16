# -*- coding: utf-8 -*-

import pytest

gvar = 'global variable'

def define_local_variable():
  gvar = 'local variable'
  return gvar

def use_global_variable():
  global gvar
  gvar = 'used global variable'
  return gvar

def outer():
  var1 = '外側の変数'
  var2 = 'これも外側の変数'

  def inner():
    nonlocal var1 # var1を外側の変数と宣言し、値を変更できるようにする
    var1 = '内側で変更'
    var3 = '内側の変数'
    return (var1, var2, var3)
  
  return inner()

def test_global_variable():
  assert 'global variable' == gvar
  assert 'local variable' == define_local_variable()
  assert 'used global variable' == use_global_variable()

  assert ('内側で変更', 'これも外側の変数', '内側の変数') == outer()
