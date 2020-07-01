# End-to-End-Selenium-Automation-Testcase-with-Python
Fully functional web automation testcase done with Pytest. Signup, Login and Rent items pages are automated and tested with Pytest.
Logging and Html report system have been generated.
To get specific test results, instead of smoke I have tested specific cases with (-k) input in the terminal. For example, py.test -k (any class or function name).
Some bugs have been found and successfully reported with log and HTML report.
Sql injection verified by using True validation, for example: (‘ or ‘abc‘=‘abc‘;–) and came negative.
For signup page, personal informations have been parameterized.
Fixture is used to simplify the test cases.
