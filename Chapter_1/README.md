# knowledge

## 测试结果类型

+ PASSED(.):测试通过
+ FAILED(F):测试失败
+ SKIPPED(s): 测试未执行
+ XFAIL(x):预期测试失败
+ XPASS(X):预期测试失败，但实际上运行通过，不符合预期
+ ERROR(E): 测试用例之外的代码触发了异常

## 命令行选项

```shell
(.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest --help
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

positional arguments:
  file_or_dir

general:
  -k EXPRESSION         Only run tests which match the given substring expression. An expression is a Python evaluable expression where all names are substring-  
                        matched against test names and their parent classes. Example: -k 'test_method or test_other' matches all test functions and classes whose 
                        name contains 'test_method' or 'test_other', while -k 'not test_method' matches those that don't contain 'test_method' in their names. -k 
                        'not test_method and not test_other' will eliminate the matches. Additionally keywords are matched to classes and functions containing    
                        extra names in their 'extra_keyword_matches' set, as well as functions which have names assigned directly to them. The matching is case-  
                        insensitive.
  -m MARKEXPR           Only run tests matching given mark expression. For example: -m 'mark1 and not mark2'.
  --markers             show markers (builtin, plugin and per-project ones).
  -x, --exitfirst       Exit instantly on first error or failed test
  --fixtures, --funcargs
                        Show available fixtures, sorted by plugin appearance (fixtures with leading '_' are only shown with '-v')
  --fixtures-per-test   Show fixtures per test
  --pdb                 Start the interactive Python debugger on errors or KeyboardInterrupt
  --pdbcls=modulename:classname
                        Specify a custom interactive Python debugger for use with --pdb.For example: --pdbcls=IPython.terminal.debugger:TerminalPdb
  --trace               Immediately break when running each test
  --capture=method      Per-test capturing method: one of fd|sys|no|tee-sys
  -s                    Shortcut for --capture=no
  --runxfail            Report the results of xfail tests as if they were not marked
  --lf, --last-failed   Rerun only the tests that failed at the last run (or all if none failed)
  --ff, --failed-first  Run all tests, but run the last failures first. This may re-order tests and thus lead to repeated fixture setup/teardown.
  --nf, --new-first     Run tests from new files first, then the rest of the tests sorted by file mtime
```

### --collect-only

该选项可以展示在给定的配置下哪些测试用例会被运行
```shell
(.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest . --collect-only
===================================================================================== test session starts =====================================================================================
platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
collected 6 items                                                                                                                                                                               

<Dir Chapter_1>
  <Module test_four.py>
    <Function test_asdict>
    <Function test_replace>
  <Module test_one.py>
    <Function test_passing>
  <Module test_three.py>
    <Function test_defaults>
    <Function test_member_access>
  <Module test_two.py>
    <Function test_failing>
    ================================================================================= 6 tests collected in 0.02s ================================================================================== 
```

### -k

使用表达式去指定希望运行的测试用例
```shell
(.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest -k "asdict or defaults" --collect-only 
====================================================================================== test session starts =======================================================================================
platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0
rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
collected 6 items / 4 deselected / 2 selected

<Dir Chapter_1>
  <Module test_four.py>
    <Function test_asdict>
  <Module test_three.py>
    <Function test_defaults>

========================================================================== 2/6 tests collected (4 deselected) in 0.02s =========================================================================== 
```

### -m

用mark来标记测试并分组，以便快速选中并运行
```python
@pytest.mark.run_these_please
def test_member_access():

@pytest.mark.run_these_please    
def test_replace():

```
```
(.venv) PS D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1> pytest -m run_these_please -v             
====================================================================================== test session starts =======================================================================================
platform win32 -- Python 3.12.0, pytest-8.2.1, pluggy-1.5.0 -- d:\project\mypythonproject\python_howto\PracticeOfPytest\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\project\mypythonproject\python_howto\PracticeOfPytest\Chapter_1
collected 6 items / 4 deselected / 2 selected                                                                                                                                                      

test_four.py::test_replace PASSED                                                                                                                                                           [ 50%] 
test_three.py::test_member_access PASSED                                                                                                                                                    [100%] 
========================================================================== 2 passed, 4 deselected, 2 warnings in 0.02s ===========================================================================
```

-m 'mark1 and mar2' 选中同时带有俩个标记的用例

-m 'mark1 and not mark2' 选中带有mark1 去掉带有mark2的用例

-m 'mark1 or mark2' 带有mark1或者mark2的用例

### -x 选项

通常在运行测试用例时候遇到失败的用例会标记失败继续运行剩余的用例，但是在debug的时候我们希望失败时候就停下来
-x 选项在遇到失败后便不会运行剩余的测试用例

### --maxfail=num

-x 就是 --maxfail=1
该选项允许你遇到失败几次后再停止测试

### --lf

运行上次失败的最后一个用例

### --ff

与--lf 一样但是会运行剩余的测试用例

### -v 

测试结果会更详细， 每个测试用例都会占一行

### -q

保留核心信息 更加聚焦

### -l (--showlocals)

失败测试用例会显示局部变量和他的值

### --tb=style

+ --tb=short 仅输出assert的一行以及系统判定内容（不显示上下文）
+ --tb=line 只使用一行输出显示所有的错误信息
+ --tb=no 直接屏蔽所有的回溯信息
+ --tb=long 输出最为详细的回溯信息
+ --tb=auto 默认值仅打印第一个和最后一个失败用例的回溯信息
+ --tb=native 只打印python标准库的回溯信息

### --duration=N

统计测试过程中哪几个阶段是最慢的（包括每个测试用例的call、setup、teardown）

### --version -h

试一下 不写了 累了 没劲了







