from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

runner = HttpRunner()
summary = runner.run("testcases/verify_code_login.yml",dot_env_path="conf/.env")
# summary = runner.run("/api/account/GET_verify-code.yml",dot_env_path="conf/.env")
gen_html_report(summary)

