@Acceptance
Feature: Projects Acceptance
  As an admin
  I want to do the main CRUD operations with projects resources
  So non 4XX code should be displayed

  @AT-PRO-01
  Scenario: Create a new project with required values
    Given I remove all projects from dashboard
    And I have the next endpoint "projects"
    When I have the body payload below
    """
    {
      "name": "*random string(10)*"
    }
    """
    And I do an api POST request
    Then I should have 200 as status code
    And The response body should have an id
    And the response body should contain previous content
    And the response body should contain previous content and
    """
    {
      "public": false,
      "project_type": "private"
    }
    """
    And the response body should be equal to GET body

  @AT-PRO-02
  Scenario: Create a new project with required values from ui
    Given I have the next endpoint "projects"
    And I have the body payload below
    """
    {
      "name": "*random string(10)*",
      "public": true,
      "project_type": "public"
    }
    """
    When I do an api POST request
    Then I should have 200 as status code
    And The response body should have an id
    And the response body should contain previous content
    And the response body should contain previous content and
    """
    {
      "public": true,
      "project_type": "public"
    }
    """
    And the response body should be equal to GET body

  @AT-PRO-03 @create_instance_projects
  Scenario: Edit a project
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
    And the response body should be equal to GET body

  @AT-PRO-04 @create_instance_projects
  Scenario: Delete a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>"
    When I do an api DELETE request
    Then I should have 204 as status code

  @AT-PRO-05 @create_instance_full_projects @wip
  Scenario: Delete a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>"
    When I do an api DELETE request
    Then I should have 204 as status code

  @AT-PRO-06 @create_instance_projects @wip
  Scenario: Archive a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>/archive"
    When I do an api POST request
    Then I should have 302 as status code
