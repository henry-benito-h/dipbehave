# Created by Henry Benito at 3/23/2019
@Smoke
Feature: API Availability
  As an admin
  I want to get a response from api service.
  So I should get 200 OK response


  Scenario: Test service availability for project
    And I have the next endpoint "projects"
    When I do an api GET request
    Then I should have 200 as status code
