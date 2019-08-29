# 1. 参数值的引用

在python中strings、tuples、和numbers是不可变对象，而list、set、dict等是可变对象。当把一个引用传递给函数，函数调用完成返回的时候。不可变对象不会改变，而可变对象会改变。

# 2.python中的元类如何理解

元类是类的类。在python中，类也是一种对象，类定义类的实例（对象）的方法。而元类就定义了类的方法。type就是Python中用来动态创建类的元类。

当你使用以下代码创建了一个类后。
```python
class Myclass(object):
    pass
```

在这背后当检测到关键字class后，实际调用了以下代码使用元类type创建了Myclass
```python
type('Mycalsss',(),{})
#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
```

# 3.python中的方法
事实上python里面的方法有三种：
- 实例方法（普通的方法）
- 静态方法（staticmethod）
- 类方法（classmethod）

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x

a=A()
```
### 实例方法。
实例方法接受一个参数(self),self指向类A本身。通过self参数实例方法可以访问、修改同一对象下的属性和方法。
### 类方法。
类方法接受一个参数(cls),通过cls参数，类方法可以访问类的属性和方法，但是不可以访问实例的变量（self.变量名）
### 静态方法
静态方法不需要绑定

# 4.静态变量，实例变量
类变量是可以在类的说有的实例间进行共享的变量。
实例变量是属于每个实例的。
```python
class Foo:
    num = 0 #类变量
    self.num2 = 3 #实例变量
```

# 5.python的自省
自省就是面向对象的语言所写的程序在运行时,所能知道对象的类型.简单一句就是运行时能够获得对象的类型.比如type(),dir(),getattr(),hasattr(),isinstance().

# 6.字典推导式
```python
dict = {ket:value for key, value in iterable}
```

# 7.python里面单下划线和双下划线的用处
_foo   单下划线只是约定熟成的，用来指定私有变量。
__foo  双下划线有实际意义，双下划线开头的名字，解释器会使用前面加上类名 _calssname__foo 来替代__foo，以防止直接访问，但是还是可以通过_classname__foo来访问

# 8.字符串格式化
- %
- format

format
- "{ } { }".format()
- "{1} {2}".format()
- "{a} {b}".format(a=， b=)
- dict = {key1:value1, key2:value2} "{key1} {key2}".format(**dict)
- list = [....] "{[0]} {[1]}".format(list)
- 传入对象：
```python
class Foo:
    def __init__(self,value):
        self.value = value
foo = Foo(6)
"value is {0.value}".format(foo)
```
# 9. 迭代器、生成器
迭代器(iterator)就是实现了__iter__() 和__next__()方法的对象。
可迭代对象(iterable)，是实现了__iter__()方法，iterable的__iter__()方法会返回一个iterator，返回的iterator的__next__()方法会返回下一个iterator。同时，iterator也是一种iterable（可迭代对象）所以也要实现__iter__()，iterator的__iter__只需要返回自己就行。

生成器(generator)。生成器是一种迭代器，是一种只能迭代一次的迭代器。生成器不会生成所有的值，而是会动态的生成。yield 是一个类似return的关键字，它会返回一个generator。
```python
def createGenerator():
    my_list = range(3)
    for i in my_list:
       yield i

mygeneroator = createGeneroator()
for i in mygenerator:
    print(i)
```
!将列表生成式中[]改成() 之后从列表生成式变为生成器

# 10. *args  和 **kwargs
*args.可以传递任意数量的参数,它是一个tuple
**kwargs允许你使用没有事先定义的参数名,表示关键字参数，是一个dict

# 11.面向切面编程AOP， 和装饰器
AOP:这种在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。装饰器就是经典的AOP
装饰器的用途：插入日志、性能测试、事务处理。
装饰器的作用就是为已经存在的对象添加额外的功能

```python
#简单装饰器写法
def foo(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

#带参数装饰器
def foo_have_parameter(parameter):
    def foo(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return foo
```
# 12. 新式类和旧式类
```python
#新式类
class C(object):
    pass
#旧式类
class B:
    pass
```
新式类是继承自object对象
object定义的一系列特殊方法

__new__() __init__()
__new__是一个静态方法,而__init__是一个实例方法.
__new__用来创建实例，__init__用来创建实例后的初始化。
__new__() 原型是object.__new__(cls,[,...])
当调用C(*args, **kwargs)创建一个实例的时候，实际上内部调用的：
```python
c = C__new__(cls, *args, **kwargs)
if isinstance(c,C): #判断c是不是C的实例
    C.__init__(c, *args, **kwargs)
```
__metaclass__是创建类时起作用.所以我们可以分别使用__metaclass__,__new__和__init__来分别在类创建,实例创建和实例初始化的时候做一些小手脚

__delattr__()、 __getattribute__()、__setattr__()
这几个用来处理属性的访问

__repr__() __str__()
print(object)打印一个对象会调用__str__() 如果__str__()没有定义则会调用__repr__() 。直接输出对象，调用__repr__()，__repr__()是用于显示给开发人员

```python
class A():
    def foo1(self):
        print "A"
class B(A):
    def foo2(self):
        pass
class C(A):
    def foo1(self):
        print "C"
class D(B, C):
    pass

d = D()
d.foo1()
```
按照经典类的查找顺序从左到右深度优先的规则，在访问d.foo1()的时候,D这个类是没有的..那么往上查找,先找到B,里面没有,深度优先,访问A,找到了foo1(),所以这时候调用的是A的foo1()，从而导致C重写的foo1()被绕过.
新式类中采用的是广度优先的算法

# 13.单例模式
1. 使用__new__方法
```python
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
class Foo(Singleton):
    pass
```
2. 共享属性
创建实例的时候，把所有的__dict__指向同一个字典，这样它们就具有同样的属性和方法
```python
class Singleton(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        ob = super(Singleton, cls).__new__(cls, *args, **kwargs)
        ob.__dict__ = cls._state
        return ob
class Foo(Singleton):
    psss
```
3. 装饰器实现
```python
def Singleton(cls):
    _instance = {}
    def getinstance(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*atrgs, **kwargs)
        return _instance[cls]
    return getinstance

@Singleton
class myclass:
    pass
```
4. import方法 
import是天然的单例模式
```python
#mysingleton.py
class Singleton(object):
    def foo(slef):
        pass
my_singleton = My_Singleton()
#
from mysingleton import my_singleton
my_single.foo()
```
# 14.GIL线程全局锁
线程全局锁就是指，cpu一个核在同一时刻只能运行一个线程。
在做I/O操作时，不需要cpu，这时python解释器会释放全局锁。python中会有一个执行指令的计数器，一个线程执行了一定数量的计算后，就会切换线程。对于io密集型任务python的多线程可以起到作用。但是在cpu密集型任务的时候，会因为线程的切换，导致浪费资源。

# 15.协程
子程序就是协程的一种特例
协程的特点在于是一个线程内执行，没有线程之间切换的开销
协程只有一个线程，不需多线程的锁机制
协程的切换由用户自己管理和调度
通过创建协程将异步编程同步化

python2可以通过yield实现协程，python3通过async/await实现协程
- yield实现
```python
def consumer():
    message = ''
    while True:
        n = yield message
        if not n:
            return
        print(n)
        message = 'ok'

def productor(c):
    c.next
    n = 0
    while n < 5:
        n = n + 1
        r = c.send(n)
        print(r)
    c.close()

c = consumer()
productor(c)
```
comsumer函数是一个生成器，把这个生成器传给productor后，通过c.next启动生成器。一但生产力东西，通过c.send()切换到consumer执行。consumer通过yield拿到消息。又通过yield 把结果传回。productor拿到consumer返回的东西后，继续生产下一个。生产完成后，通过c.close()关闭协程
- async/await
```python
import asynico

async def productor(queue):
    n = 0
    while n < 5:
        n = n + 1
        await queue.put(n)
        print(n)

async def consumer(queue):
    while True:
        e = await.get()
        print(e)
        queue.task_done()

def main():
    queue = asynico.Queue()
    productor1 = productor(queue)
    consumer1 = consumer(queue)
    loop = asynic.get_event_loop()
    loop.run_until_complete(asynic.gather*[productor1,consumer1])

if __name__ == '__main__':
    main()
```
# 16.闭包
必须有一个内嵌函数
内嵌函数必须引用外部函数中的变量
外部函数的返回值必须是内嵌函数
```python
def print_msg(x):
    # print_msg 是外围函数
    def printer(y):
        # printer 是嵌套函数
        print(x + y)
    return printer

another = print_msg(3)
# 输出 zen of python
another(4)
```
调用print_msg时产生了一个闭包printer,闭包对外部变量x进行了引用。当函数print_msg生命周期结束后，x变量依然存在。
闭包的目的：保存函数的状态信息，使函数的局部变量信息依然可以保存下来
闭包的应用：装饰器

# 17.lambda 匿名函数
语法：lambda [arg1 [, agr2,.....argn]] : expression
```python
lambda x,y,z :(x + y)*z

add = lambda x, y : x+y
add(1,2)
```
# 18. 函数式编程：
map()函数接受两个参数，一个是函数，一个是列表list,将函数依次作用到list的每个元素上，并把结果作为新的list返回

reduce()函数，把一个函数作用在一个list上，这一个函数必须接受两个参数。 reduce函数把计算结果和list的下一个元素进行累计计算reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

filter()函数用来过滤列表list，filter函数接受一个函数和一个list然后把函数作用到list的每一个参数上，根据返回值是True还是False,来决定保留还是舍弃该元素

sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。

```python
sorted(list1, key=lambda x: abs(x))
map(lambda x: x > 5, a)
reduce(lambda x,y: x*y, range(1,4))
```

# 19.垃圾回收机制

1. 引用计数

   每个对象都有字段记载被引用次数当被引用次数减小为零的时候，就会被回收

2. 标记清除

   从根对象（全局变量、调用栈、寄存器）出发，以对象为节点，以引用为边，遍历所有的对象。访问过的就会被标记，没有访问过的就会被清除。

3. 分代

   分代回收基于标记清楚维护三个集合，根据存活时间不同划分到三个集合里面，集合不同垃圾回收的频率不同。

   

# 20. is

is是对比地址,==是对比值

# 21.read,readline和readlines

- read 读取整个文件
- readline 读取一行
- readlines 读取整个文件到一个list, 使用for .. in ..访问

# 22.python2 和 python3 的区别

- print函数

  python3中print是一个函数，所以使用的时候，必须括起来 print('hello world')
  python2中print是class 类 print'hello woeld'

- 整除

  python3中/表示真除 %表示取余 //表示地板除
  python2根据除数和被除数的小数位得到结果 %表示取余 //表示地板除

- range

  python3中range是可迭代对象，惰性求值 xrange不存在
  python2中range直接生成列表 xrange才是可迭代对象

- input

  python3中input输入的是字符
  python2的input输入数字的是int类型的

- 编码

  python2默认以ASCII码
  python3默认为Unicode

- 不等式

  python2有 != 和 <>
  python3只有!=

- try except

  ```python
  try:
      pass
  except Exception,e:
      pass
  #python3
  try：
      pass
  except Exception as e:
      pass
  ```

- For循环变量和全局命名空间泄漏

  ```python
  #python2
  i = 1
  print 'before: i =', i  #1
  print 'comprehension: ', [i for i in range(5)]
  print 'after: i =', i  #4
  #python3
  i = 1
  print('before: i =', i)  #1
  print('comprehension:', [i for i in range(5)])
  print('after: i =', i)  #1
  ```

# 23.Restful架构

1）每一个URI代表一种资源；

2）客户端和服务器之间，传递这种资源的某种表现层；

3）客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"。

# 24.去除列表重复元素

```python
l1 = ['b','c','d','b','c','a','a']
#1
list(set(l1))
#2
l2 = {}.fromkeys(l1).keys()
#3
l2 = list(set(l1))
l2.sort(key=l1.index)
#4
l2 = []
[l2.append(i) fro i in l1 if not in l2]

```

# 25.合并有序链表

```python
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])
```

# 26. 算法

```python
#二分查找
def binary_searsh(list, item):
    low = 0
    high = len(list) - 1
    while low < high:
        mid = (low + high)/2
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess > item:
            low = mid + 1
        else:
            return mid
    return None
#快排
def quicksort(list):
    if len(list) < 2:
        return None
    else:
        mid = list[0]
        less = [i for i in list[1:] if i <= mid]
        bigger = [i for i in list[1:] if i > mid]
        finallylist = quicksort(less) + [mid] + quicksort(biger)
        return finallylist
#冒泡    
def bubblesort(list):
    for j in range(len(list)):
        for i in range(0, len(list) - 1 - j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1],list[i]
    return list

#选择排序
def selectsort(list):
    for i in range(list):
        for j in range(len(list)-i):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list

#直接插入排序
def insertsort(list):
    for i in range(1,len(list)):
        for j in range(i):
            if list[i] < list[j]:
                list[j].insert(list[i])
                list.pop(i + 1)
    return list
```

