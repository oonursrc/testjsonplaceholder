"""Manage Social Media feature tests."""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)

from tests.scripts.common import (
    verify_user_count,
    verify_user_exists,
    verify_user_post_count,
    get_user_id,
    verify_user_post_exists,
    verify_if_email_of_a_comment_is_proper,
    verify_if_post_deleted_by_title,
    verify_user_post_count_by_title,
    add_new_user_post,
)
from tests.scripts.server_requests import (
    verify_server_is_running,
    query_all_users,
    query_all_posts_of_user,
    query_all_comments_of_a_post,
)
import config.conditions as condition


@scenario('../features/socialmedia.feature', 'Server is running')
def test_server_is_running():
    """Server is running."""


@scenario('../features/socialmedia.feature', 'Find a user')
def test_find_a_user():
    """Find a user."""


@scenario('../features/socialmedia.feature', 'Find user posts')
def test_find_user_posts():
    """Find user posts."""


@scenario('../features/socialmedia.feature', 'Search user post')
def test_search_user_post():
    """Search user post."""


@scenario('../features/socialmedia.feature', 'Validate email of comments for each user post')
def test_validate_emails_of_comments_for_each_user_post():
    """Validate emails of comments for each user post."""


@scenario('../features/socialmedia.feature', 'Delete user post by title')
def test_delete_user_post_by_title():
    """Delete user post by title."""


@scenario('../features/socialmedia.feature', 'Add a new post')
def test_add_a_new_post():
    """Add a new post."""


@given('Server is up and running')
def step():
    verify_server_is_running()


@when('Send request to query all users')
def step(context):
    context["user_list"] = query_all_users()


@then(parsers.parse('There are {count:d} {option} listed'))
def step(context, count, option):
    if option == condition.Conditions.USERS.value:
        verify_user_count(context, count)
    elif option == condition.Conditions.POSTS.value:
        verify_user_post_count(context, count)
    else:
        pass  # can be implemented if needed


@then(parsers.parse('There are {count:d} posts listed the title {title}'))
def step(context, count, title):
    verify_user_post_count_by_title(context, count, title)


@then(parsers.parse('User with username {username} is exists'))
def step(context, username):
    verify_user_exists(context, username)
    context["user_id"] = get_user_id(context, username)


@when('Send request to query user posts')
def step(context):
    context["user_posts"] = query_all_posts_of_user(context)


@when(parsers.parse('{operation} user {option} with the title {title}'))
def step(context, operation, option, title):
    if operation == condition.Operations.SEARCH.value:
        if option == condition.Conditions.POSTS.value:
            verify_user_post_exists(context, title)
        elif option == condition.Conditions.COMMENTS.value:
            pass  # can be implemented if needed
    if operation == condition.Operations.DELETE.value:
        verify_if_post_deleted_by_title(context, title)


@then('Email for each comment is in proper format')
def step(context):
    for post in range(len(context["user_posts"])):
        comments = query_all_comments_of_a_post(context["user_posts"][post]["id"])
        for comment in range(len(comments)):
            verify_if_email_of_a_comment_is_proper(comments[comment]["email"])


@when(parsers.parse('When Add user a post with the title {title} body {body} for user {username}'))
def step(context, title, body, username):
    add_new_user_post(context, title, body, username)
