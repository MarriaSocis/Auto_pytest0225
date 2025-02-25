class CommonUtil:

      # 前四个方法是类方法，用做前后置处理

      def setup_class(self):
          print("每个类之前执行一次")


      def teardown_class(self):
          print("每个类之后执行一次")


      def setup_method(self):
          print("每个用例之前执行一次")


      def teardown_method(self):
          print("每个用例之后执行一次")