# Created by Jafeth GArcia and Henry Benito at 2/20/2019
Feature: Generic steps on a basic scenario
  # Enter feature description here

  Scenario: Test an action
    Given I am authenticated as "admin"
    Given I have the next endpoint "projects"
#    And I have the body payload below
#    """
#    {
#      "message": "Requires ",
#      "documentation_url": "https://developer.github.com/v3/users/#get-the-authenticated-user"
#    }
#    """
    When I do an api GET request
    Then I should have 200 as status code