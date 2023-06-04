Feature: Dropbox API

  Scenario: Verify Dropbox API
    Given I have a valid access token
      Then I should get a valid response

  Scenario: Upload file to Dropbox
    Given I have a valid access token
      When I upload a file to Dropbox
        Then I should see the file in my Dropbox folder

  Scenario: Get file metadata
    Given I have a valid access token
      Then I should see the file metadata

  Scenario: Download file from Dropbox
    Given I have a valid access token
      When I download a file from Dropbox
        Then I should see the file in my local folder

  Scenario: Delete file from Dropbox
    Given I have a valid access token
      When I delete a file from Dropbox
        Then I should not see the file in my Dropbox folder

  Scenario: Delete file from local folder
    Given I delete a file from my local folder
        Then I should not see the file in my local folder
