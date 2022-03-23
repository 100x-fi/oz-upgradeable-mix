from brownie import (
    Contract,
    ZERO_ADDRESS
)
import pytest


@pytest.fixture(scope="function")
def proxy_admin(ProxyAdmin, accounts):
  return ProxyAdmin.deploy({'from': accounts[0]})


@pytest.fixture(scope="function")
def upgradeable_erc20(TransparentUpgradeableProxy, UpgradeableErc20, proxy_admin, accounts):
  impl = UpgradeableErc20.deploy({'from': accounts[0]})
  proxy = TransparentUpgradeableProxy.deploy(impl.address, proxy_admin.address, impl.initialize.encode_input(
      "Some Upgradeable Erc20", "SERC20"), {'from': accounts[0]})
  return Contract.from_abi("UpgradeableErc20", proxy.address, UpgradeableErc20.abi)
