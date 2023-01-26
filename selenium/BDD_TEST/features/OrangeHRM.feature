Feature:OrangeHRM Logo
 Scenario: Logo presence on OrangeHRM home page
    Given launch chrome browser
    When Open OrangeHRM homepage
    Then verify that the Logo present on homepage
    And close browser  
    