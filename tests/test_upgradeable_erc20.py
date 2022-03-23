import pytest

def test_init(upgradeable_erc20, accounts):
  assert upgradeable_erc20.name() == "Some Upgradeable Erc20"
  print("hello")