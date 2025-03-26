import os


class TestRunner:
    def __init__(self,
                 tc_name="..\\testcases\\",
                 report_path="..\\test_report\\html",
                 raw_path="..\\test_report\\raw"):
        self.report_path = report_path
        self.raw_path = raw_path
        self.tc_name = tc_name

    def run(self):
        os.system(f"pytest {self.tc_name} --alluredir {self.raw_path}")
        os.system(
            f"allure generate {self.raw_path} -o {self.report_path} --clean")


if __name__ == '__main__':
    TestRunner().run()
