Feature: Book avaliablity
  In order to buy a book
  I want to check the book avaliablity


Scenario: Book is available
    Given I have provided book id OL3386321M
    When I fetch data
    Then the status should be 200 which indicate the book is avaliable
    

    

  