Feature: Web UI Automation

  Scenario: Login to the application
    Given I am on the login page
      When I enter username and password
        When I click on login button
          Then I should see the Dashboard page

  Scenario: Add new job
    Given I am on the admin page
      When I go to the jobs page
        When I click on add new job button
          When I enter job details
            Then I click on save button

  Scenario: Delete my job
    Given I am on the admin page
      When I go to the jobs page
        When I should find and delete my job
          Then I should not see my job in the list

  Scenario: Logout from the application and close the browser
    Given I am on the admin page
      When I click on logout button
        When I should see the login page
          Then I close the browser
