from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

runner = HttpRunner()
# summary = runner.run("testcases/verify_code_login.yml",dot_env_path="conf/.env")
summary = runner.run("api/mall/back-end/GET_car-items.yml",dot_env_path="conf/.env")
gen_html_report(summary)

