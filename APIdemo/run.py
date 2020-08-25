from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

runner = HttpRunner(log_level="DEBUG")
# summary = runner.run("testcases/verify_code_login.yml",dot_env_path="conf/.env")
summary = runner.run("api/mall/back-end/car-item/GET_tree.yml",dot_env_path="conf/.env")
gen_html_report(summary)

