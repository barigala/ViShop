Feature: Account Page Navigation

  Scenario: Navigate to Account Page and verify sections
    Given I see Account Button
    When I click on the Account button
    Then I should see the Account page title
    When I navigate to "Credit Cards"
    Then I should return to the Account page
    When I navigate to "Coupons"
    Then I should return to the Account page
    When I navigate to "Orders"
    Then I should return to the Account page
    When I navigate to "Saved Payments"
    Then I should return to the Account page
