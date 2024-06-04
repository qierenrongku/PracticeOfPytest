# knowledge

### 目录结构

```shell
D:\PROJECT\MYPYTHONPROJECT\PYTHON_HOWTO\PRACTICEOFPYTEST\TASKS_PROJ
│  CHANGELOG.rst
│  LICENSE
│  MANIFEST.in
│  setup.py
│
├─src   # 源码
│  └─tasks
│          api.py
│          cli.py
│          config.py
│          tasksdb_pymongo.py
│          tasksdb_tinydb.py
│          __init__.py
│
└─tests # 测试代码
    │  conftest.py  # pytest 的本地插件 可以包含hook和fixture
    │  pytest.ini  #  pytest 在该项目的配置文件
    │
    ├─func  # 功能测试
    │      test_add.py
    │      __init__.py
    │
    └─unit  # 单元测试
            test_task.py
            __init__.py
```
使用skip 和 skipif 会直接跳过测试用例而不会执行，xfail标记会告诉pytest运行此测试 预期是失败的

```python
@pytest.mark.skip(reason='哈哈哈哈')
def test_1():
    pass

@pytest.mark.skipif(1 < 2,reason='哈哈哈哈')
def test_2():
    pass

@pytest.mark.xfail()
def test_3():
    pass

```
参数化测试
```python
@pytest.mark.parametrize('a, b, c', [(1, 2, 3), (2, 3, 4), (3, 4, 5)])
def test_1(a, b, c):
    pass
```
如果放在类上会传递给所有的方法