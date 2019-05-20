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
  Scenario: Account is not editable
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "name": "*random string(10)*",
      "account_id": 586658
    }
    """
    When I do an api PUT request
    Then I should have 403 as status code
    And response body should match with content
    """
    {
      "code": "unauthorized_operation",
      "kind": "error",
      "error": "Authorization failure.",
      "requirement": "You must be a project creator on the destination account."
    }
    """

  @AT-PRO-05 @create_instance_projects
  Scenario: Delete a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>"
    When I do an api DELETE request
    Then I should have 204 as status code
    When I do an api GET request
    Then I should have 403 as status code
    And response body should match with content
    """
    {
      "code": "unauthorized_operation",
      "kind": "error",
      "error": "Authorization failure.",
      "general_problem": "You aren't authorized to access the requested resource.",
      "possible_fix": "Your project permissions are determined on the Project Membership page. If you are receiving this error you may be trying to access the wrong project, or the project API access is disabled, or someone listed as the project's Owner needs to change your membership type."
    }
    """

  @AT-PRO-06
  Scenario: Get a non-existent project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/wrongid"
    When I do an api GET request
    Then I should have 404 as status code
    And response body should match with content
    """
    {
      "code": "unfound_resource",
      "kind": "error",
      "error": "The object you tried to access could not be found.  It may have been removed by another user, you may be using the ID of another object type, or you may be trying to access a sub-resource at the wrong point in a tree."
    }
    """

  @AT-PRO-07 @create_instance_full_projects @In-Progress
  Scenario: Delete a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>"
    When I do an api DELETE request
    Then I should have 204 as status code


  @AT-PRO-08 @create_instance_projects @In-Progress
  Scenario: Archive a project
    Given I have the next endpoint "projects"
    And I have the next endpoint "projects/<id>/archive"
    When I do an api POST request
    Then I should have 302 as status code

  @AT-PRO-09 @create_instance_projects
  Scenario: Get all projects
    Given I remove all projects from dashboard
    And I have the next endpoint "projects"
    When I have the body payload below
    """
    {
      "name": "First",
      "iteration_length": 1,
      "week_start_day": "Monday",
      "point_scale": "0,1,2,3,5,8",
      "point_scale_is_custom": false,
      "bugs_and_chores_are_estimatable": false,
      "automatic_planning": true,
      "enable_tasks": true,
      "time_zone": {
          "olson_name": "America/New_York",
          "offset": "-04:00"
      },
      "number_of_done_iterations_to_show": 4,
      "has_google_domain": false,
      "enable_incoming_emails": true,
      "initial_velocity": 10,
      "public": true,
      "atom_enabled": false,
      "project_type": "public",
      "enable_following": true
    }
    """
    And I do an api POST request
    Then I should have 200 as status code
    When I have the body payload below
    """
    {
      "name": "Second",
      "iteration_length": 1,
      "week_start_day": "Tuesday",
      "point_scale": "0,1,2,3,5,8",
      "point_scale_is_custom": false,
      "bugs_and_chores_are_estimatable": false,
      "automatic_planning": true,
      "enable_tasks": false,
      "time_zone": {
          "olson_name": "America/New_York",
          "offset": "-04:00"
      },
      "number_of_done_iterations_to_show": 4,
      "has_google_domain": false,
      "enable_incoming_emails": true,
      "initial_velocity": 15,
      "public": true,
      "atom_enabled": false,
      "project_type": "public",
      "enable_following": true
    }
    """
    And I do an api POST request
    Then I should have 200 as status code
    When I do an api GET request
    Then I should have 200 as status code
    And I should get a list records tha contains
    """
    [
      {
        "name": "First",
        "iteration_length": 1,
        "week_start_day": "Monday",
        "point_scale": "0,1,2,3,5,8",
        "point_scale_is_custom": false,
        "bugs_and_chores_are_estimatable": false,
        "automatic_planning": true,
        "enable_tasks": true,
        "time_zone": {
            "kind": "time_zone",
            "olson_name": "America/New_York",
            "offset": "-04:00"
        },
        "number_of_done_iterations_to_show": 4,
        "has_google_domain": false,
        "enable_incoming_emails": true,
        "initial_velocity": 10,
        "public": true,
        "atom_enabled": false,
        "project_type": "public",
        "enable_following": true
      },
      {
        "name": "Second",
        "iteration_length": 1,
        "week_start_day": "Tuesday",
        "point_scale": "0,1,2,3,5,8",
        "point_scale_is_custom": false,
        "bugs_and_chores_are_estimatable": false,
        "automatic_planning": true,
        "enable_tasks": false,
        "time_zone": {
            "kind": "time_zone",
            "olson_name": "America/New_York",
            "offset": "-04:00"
        },
        "number_of_done_iterations_to_show": 4,
        "has_google_domain": false,
        "enable_incoming_emails": true,
        "initial_velocity": 15,
        "public": true,
        "atom_enabled": false,
        "project_type": "public",
        "enable_following": true
      }
    ]
    """