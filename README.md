# OZ Upgradeable Mix

This repos show how to use OZ hardhat's upgradeable library with Brownie-based project. Tests will be done in Brownie to enabling Property-Based Testing and Stateful Testing, while deployment will be done through OZ hardhat's upgradeable to enabling safe upgrade.

## Get Started

For consistency among collaborators, use the fixed node version. (Optional, but recommend)
```
$ nvm use
```

Install Brownie
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install eth-brownie
```

Install Ganache CLI, as Brownie depends on this
```
$ yarn global add ganache-cli
```

Install node dependencies for Typechain Compilation and Hardhat Deployment
```
$ yarn
$ git submodule init
```

If you get everything right, you should be able to do `Contract Compilation`, and `Running Unit Test`

### Contract Compilation
To compile for Typechain, along with its CommonJS
```
$ yarn run compile
```

### Running Unit Test
To run unit test
```
$ brownie test
```
