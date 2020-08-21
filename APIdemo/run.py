from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

runner = HttpRunner()
# summary = runner.run("api/account/GET_verify-code.yml")
summary = runner.run("testcase/verify_code_login.yml")

gen_html_report(summary)