from httprunner.api import HttpRunner
from httprunner.report import gen_html_report

# runner = HttpRunner(log_level="DEBUG")
runner = HttpRunner()
# summary = runner.run("testcases/verify_code_login.yml",dot_env_path="conf/.env")
# summary = runner.run("api/auth/POST_login.yml",dot_env_path="conf/.env")
summary = runner.run("testsuites/order.yml",dot_env_path="conf/.env")
gen_html_report(summary)

