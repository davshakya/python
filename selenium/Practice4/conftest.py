import pytest
# @pytest.fixture(scope="class")
# def setup():
#     print("This will run the fixture first...")
#     yield
#     print("This will run in end...")
    
@pytest.fixture(scope="module")
def setup():
    print("This will run the fixture first...")
    yield
    print("This will run in end...")
    
def pytest_html_report_title(report):
    report.title="My very own report" 

from py.xml import html
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("Hello it is prefix")])
    summary.extend([html.p("Hello it is summary")])
    postfix.extend([html.p("Hello it is postfix")])
    
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        extra.append(pytest_html.extras.url("http://www.example.com/"))
        # extra.append(pytest_html.extra.image('test.jpg'))
        
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            extra.append(pytest_html.extra.image('test.jpg'))
            
            
        report.extra = extra
    