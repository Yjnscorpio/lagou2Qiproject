import unittest


# class TestClass(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("这是测试整个类前要执行的方法")
#
#     def setUp(self) -> None:
#         print("这是每一个测试方法前面运行的方法")
#
#     def tearDown(self) -> None:
#         print("这是每一个测试方法后面运行的方法")
#
#     def test_first(self):
#         print("这是测试方法1")
#
#     @unittest.skip("这次不想执行这个测试")
#     def test_second(self):
#         print("这是测试方法2")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("这是测试整个类之后要执行的方法")

class demo(unittest.TestCase):
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("tearDown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")  # 保证传入的两个参数是相等的
        self.assertIn('h', 'this', "判断是否包含在内")


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print("test_demo1 case0")

    def test_demo1_case1(self):
        print("test_demo1 case1")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(demo("test_case01"))
    suite.addTest(demo1("test_demo1_case0"))

    unittest.TextTestRunner().run(suite)
