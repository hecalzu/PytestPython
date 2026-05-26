Feature: Order Transaction
    Test realted to Order Transactions

    Scenario Outline: Verify Order success message shown in details page
        Given place the item order with user credentials <username> and <password>
        And the user is on login page
        When when I login with username <username> and password <password>
        And navigate to orders page
        And select the order id
        Then order message is successfully shown in details page
        Examples:
            | username         | password   |
            | hf1788@gmail.com | Redfive5.. |