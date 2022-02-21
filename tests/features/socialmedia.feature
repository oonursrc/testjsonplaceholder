Feature: Manage social media with fake APIs

    Scenario: Server is running
        Given Server is up and running

    Scenario: Find a user
        When Send request to query all users
        Then There are 10 users listed
        And User with username Delphine is exists

    Scenario: Find user posts
        When Send request to query user posts
        Then There are 10 posts listed

    Scenario: Search user post
        When Search user posts with the title sapiente omnis fugit eos
        Then There are 1 posts listed the title sapiente omnis fugit eos

    Scenario: Validate email of comments for each user post
        Then Email for each comment is in proper format

    Scenario: Delete user post by title
        When Delete user posts with the title sapiente omnis fugit eos
        And Send request to query user posts
        Then There are 9 posts listed

    Scenario Outline: Add a new post
        When Add user a post with the title <title> body <body> for user <user>
        And Send request to query user posts
        Then There are 11 posts listed
        Examples:
            | title     | body      | user      |
            | NewTitle  | NewBody   | Delphine  |

