Feature: Test EPAM website

  Scenario: Verify Homepage Title
    Given I am on the EPAM homepage
      When I retrieve the page title
      Then the title should be "EPAM | Software Engineering & Product Development Services"

  Scenario: Search for Careers
    Given I am on the EPAM homepage
      When I click on the search icon
      Given I enter "Careers" in the search bar
      Given I click on the search submit
      Given I click on the "Careers" link in the search results
      Then I should be redirected to the careers page

  Scenario: Verify Social Media Icons
    Given I am on the EPAM homepage
      When I check the social media section
        Then I should see icons for Facebook, Twitter, LinkedIn, and Instagram

  Scenario: Navigate to Services Page
    Given I am on the EPAM homepage
      When I click on the "Services" link in the navigation menu
        Then I should be redirected to the services page

  Scenario: Contact EPAM
    Given I am on the EPAM homepage
      When I click on the "Contact" link in the navigation menu
        Then I should see a contact form

  Scenario: Verify Footer Links
    Given I am on the EPAM homepage
      When I scroll to the bottom of the page
        Then I should see links for "About", "Services", "Industries", "Insights", "Careers", and "Contact" in the footer

  Scenario: Verify Language Options
    Given I am on the EPAM homepage
      When I click on the language selector in the header
        Then I should see options to switch between English, SNG, and Ukrainian

  Scenario: Verify homepage slider
    Given I am on the EPAM homepage
        Then I should see a slider with 3 images

  Scenario: Close Browser
    Given I am on the EPAM homepage
      When I close the browser
        Then The browser should close
