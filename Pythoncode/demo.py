name = 'tome'


def fun():
    print(f"func {name}")


fun()  # 上面只是定义了方法，但是没有调用，不调用的话是什么都打印不出来的

a = 1


def func():
    a = 2  # 这里的a只是这个方法里面的一个局部变量
    print(f"func {a}")


print(a)  # 这里打印的东西仅仅是之前定义的a，并不是在方法中重新定义的a
func()
