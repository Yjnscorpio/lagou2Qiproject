# 作业：创建模块，模块里面创建方法，定义有参数，和无参，有返回值和无返回值 的情况，并说明 无返回值的默认返回值。
class Person():
    def __init__(self, name, age, gender, position, work):
        self.name = name
        self.age = age
        self.gender = gender
        self.position = position
        self.work = work

    # 有返回值
    def Person_info(self):
        Person_info = self.name + ":" + str(self.age) + " " + self.gender + " " + self.position
        return Person_info

    # 无返回值
    def do_work(self):
        print(f"{self.name} 是否正在工作：{self.work}")

    # 默认参数
    def set_att(self, value, name="张三"):
        self.value = value
        print(f"{name} 身材是{self.value}")


# 传参数
Person = Person("Tom", 26, "男", "测试工程师", "写代码")
get_info = Person.Person_info()
print(get_info)
Person.do_work()
Person.set_att("胖")
