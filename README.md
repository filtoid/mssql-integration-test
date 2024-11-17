# mssql-integration-test
A library for creating an integration testing db object, for an actual database.

### Introduction

This is designed to be a drop in replacement for the [MySql PyPi Project](https://pypi.org/project/mssql/): [Github](https://github.com/JoseRoberts87/mssql/tree/master), for use within a specific project - [Pyway](https://github.com/jasondcamp/pyway). There's no reason it won't work for other projects, but that was the original reason for creating this.

### Installation
As of now it is not installed in PyPi so you have install from Github:
`pip install git+https://github.com/filtoid/mssql-integration-tests`

### Usage
```python
from mssql-integration-tests import MsSql

mssql = MsSql(host="<HOSTNAME>", port=<PORT>, db_name="<DATABASE_NAME>", username="<USER>", password="<PASSWORD>", driver="<DRIVER>")

```
