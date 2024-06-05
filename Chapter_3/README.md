# knowledge

@pytest.fixture()可以装饰一个函数用来声明这个函数是一个fixture
如果测试函数中有fixture 则会运行这个fixture 将他的返回值返回给测试函数（测试函数获取到的是fixture的返回值）

在公共目录中创建conftest.py（视为本地插件库） 在其中添加fixture 来共享给测试用例

--setup-show  回溯fixture的执行过程

```python
@pytest.fixture(scope='xxx')
scope='founction' 默认值
scope='class'
scope='module'
scope='session'


@pytest.mark.usefixtures('fixture1', 'fixture2')
使用usefixture和测试方法中添加fixture参数 区别是后者可以使用fixture的返回值

@pytest.fixture(autouse=True, scope='module')
使作用域中的测试函数都运行该fixture

@pytest.fixture(name='new_name')
对fixture重命名
```


```python
@pytest.fixture(params=datas)
def task(request):
    return request.param

def test_task(task):
    pass

该fixture 会将datas中的一个元素返回 如如果有多个则测试用例会执行多次

```

