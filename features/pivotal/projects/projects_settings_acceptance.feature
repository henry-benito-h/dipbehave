@AcceptanceSettings
Feature: Projects Settings Acceptance
  As an admin
  I want to do the make basic changes with projects settings
  So no 4XX and 5XX codes should be displayed

  @ATS-PRO-01 @create_instance_projects
  Scenario: Enable tasks on a project
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "enable_tasks": true
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"Exhaust ports are ray shielded"
    }
    """
    When I do an api POST request
    Then I should have 200 as status code
    And I save the id as "story_id"
    When I have the next endpoint "projects/<id>/stories/*get var(story_id)*/tasks"
    And I have the body payload below
    """
    {
      "description":"Some task"
    }
    """
    And I do an api POST request
    Then I should have 200 as status code

  @ATS-PRO-02 @create_instance_projects
  Scenario: Disable tasks on a project
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "enable_tasks": false
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"Exhaust ports are ray shielded"
    }
    """
    When I do an api POST request
    Then I should have 200 as status code
    And I save the id as "story_id"
    When I have the next endpoint "projects/<id>/stories/*get var(story_id)*/tasks"
    And I have the body payload below
    """
    {
      "description":"Some task"
    }
    """
    And I do an api POST request
    Then I should have 400 as status code

  @ATS-PRO-03 @create_instance_projects
  Scenario: Feature are estimated when Bugs and Chores May Be Given Points are disabled
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "bugs_and_chores_are_estimatable": true
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "story_type":"feature",
      "estimate": 3
    }
    """
    And I do an api POST request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "bugs_and_chores_are_estimatable": false
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "story_type":"feature",
      "estimate": 3
    }
    """
    And I do an api POST request
    Then I should have 200 as status code

  @ATS-PRO-04 @create_instance_projects
  Scenario: Bugs and Chores May Be Given Points
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "bugs_and_chores_are_estimatable": true
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "story_type":"bug",
      "estimate": 3
    }
    """
    And I do an api POST request
    Then I should have 200 as status code


  @ATS-PRO-05 @create_instance_projects
  Scenario: Bugs and Chores are not pointed
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "bugs_and_chores_are_estimatable": false
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "story_type":"bug",
      "estimate": 3
    }
    """
    And I do an api POST request
    Then I should have 400 as status code

  @ATS-PRO-06 @create_instance_projects
  Scenario: Modify random start day
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "week_start_day": "*random_week_day*"
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    And the response body should contain previous content

 @ATS-PRO-07 @create_instance_projects
  Scenario: Create history with scale point
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "point_scale": "0,1,2,4,8",
      "point_scale_is_custom": false
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "estimate": 4
    }
    """
    And I do an api POST request
    Then I should have 200 as status code

  @ATS-PRO-08 @create_instance_projects
  Scenario: Create history with custom scale point
    Given I have the next endpoint "projects/<id>"
    And I have the body payload below
    """
    {
      "point_scale": "0,1,6,7,13",
      "point_scale_is_custom": true
    }
    """
    When I do an api PUT request
    Then I should have 200 as status code
    When I have the next endpoint "projects/<id>/stories"
    And I have the body payload below
    """
    {
      "name":"*random string*",
      "estimate": 7
    }
    """
    And I do an api POST request
    Then I should have 200 as status code
