# knowledge

## 内置fixture

### tmpdir and tmpdir_factory

tmpdir 的作用范围是函数级别 tmpdir_factory 范围是会话级别

可以利用tmpdir_factory 来创建一个fixture 来达到模块级别或者class级别

### pytestconfig

内置的pytestconfig可以通过命令行参数、选项、配置文件、插件、运行目录等方式来控制pytest。pytestconfig是request.config的快捷方式，它在pytest的文档里有时候被称为pytest配置对象

### cache

cache 的作用是存储一段测试会话的信息，在下一段测试会话中使用 （--lf， --ff）

--cache-show 来显示存储的信息
测试会话开始前传入--clear-cache来清空缓存

### capsys

允许使用代码读取stdout和stderr可以临时禁止抓取日志输出

### monkeypatch

monkeypatch 可以在运行期间对类和模块进行动态修改
+ setattr(target, name, value=<notset>, raising=True):设置一个属性
+ delattr(target, name=<notest>, raising=True): 删除一个属性
+ setitem(dic, name, value): 设置字典中的一条记录
+ setenv(name, value, prepend=True):设置一个环境变量
+ delenv(name, raising=True):删除一个环境变量
+ syspath_prepend(path): 将路径path加入到sys.path的最前面，sys.path是python导入系统路径列表
+ chdir(path): 改变当前工作目录

raising:指示pytest是否在记录不存在时抛出异常
setenv中的prepend可以是一个字符那么环境变量的值就是 value + prepend + <old value>


