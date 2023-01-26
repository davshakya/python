def test_1():
    x=30
    y=20
    assert x==y
    
def test_2():
    name="Selenium"
    title="Selenium for web automation"
    assert name in title
    
def test_3():
    name="jenkins"
    title="Jenkins is CI server"
    assert name in title,"Title not matched"
        
    
    