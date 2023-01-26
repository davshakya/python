import pytest


@pytest.fixture(scope="module")
def setup():
    print("This will run first")
    yield
    print("This will run in the end")
    
def pytest_html_report_title(report):
    report.title = "My very own title!"
    
# from py.xml import html

# def pytest_html_results_summary(prefix, summary, postfix):
#     prefix.extend([html.p("Prefix_Start")])
#     postfix.extend([html.p("Postfix_end")])
  



