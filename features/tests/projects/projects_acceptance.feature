# Created by Henry Benito at 3/23/2019
@acceptance
Feature: Projects
  As an admin
  I want to do the main CRUD operations with projects resources
  So non 4XX code should be displayed

  Background:
#    Given I am authenticated as "admin"
    Given I have the next endpoint "projects"

  Scenario: Create a new project
    Given I remove all projects from dashboard
    Given I have the next endpoint "projects"
    And I have the body payload below
    """
    {
      "name": "*random string(10)*"
    }
    """
    When I do an api POST request
    Then I should have 200 as status code
    And The response body should have an id
    And the response body should contain previous content
    And the response body should contain previous content and
    """
    {
      "project_type": "private",
      "week_start_day": "Monday",
      "atom_enabled": false,
      "automatic_planning": true,
      "bugs_and_chores_are_estimatable": false
    }
    """
    And the response body should be equal to GET body


  Scenario: Create a new project
    Given I have the next endpoint "projects"
    And I have the body payload below
    """
    {
      "name": "*random string(10)*",
      "project_type": "public",
      "week_start_day": "*random week day*"
    }
    """
    When I do an api POST request
    Then I should have 200 as status code
    And The response body should have an id
    And the response body should contain previous content
    And the response body should contain previous content and
    """
    {
      "atom_enabled": false,
      "automatic_planning": true,
      "bugs_and_chores_are_estimatable": false
    }
    """
    And the response body should be equal to GET body

  Scenario: Edit a project
    Given I have the next endpoint "projects"
    Given I have a record already created with this content
    """
    {
      "name": "*random string(10)*"
    }
    """
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "name": "*random string(10)*",
      "project_type": "public",
      "week_start_day": "*random week day*"
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    And The response body should have an id
    And the response body should contain previous content
    And the response body should contain previous content and
    """
    {
      "atom_enabled": false,
      "automatic_planning": true,
      "bugs_and_chores_are_estimatable": false
    }
    """
    And the response body should be equal to GET body


    Scenario: Delete a project
    Given I have the next endpoint "projects"
    Given I have a record already created with this content
    """
    {
      "name": "*random string(10)*"
    }
    """
    Given I have the next endpoint "projects/<id>"
    When I do an api DELETE request
    Then I should have 204 as status code