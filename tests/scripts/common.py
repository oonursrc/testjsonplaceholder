from tests.scripts.regex import check_if_email_is_in_proper_format
from tests.scripts.schema import validate_json
from tests.scripts.server_requests import delete_post_by_title, add_post


def verify_user_count(context, count: int):
    """Verifies if user count is equal to given number

    Parameters:
    context: context object of pytest
    count: int type, value to compare with count of users
    """

    list_length = len(context["user_list"])
    assert list_length == count, f"Values {list_length} and {count} are expected to be equal"


def verify_user_exists(context, username: str):
    """Verifies if given user in user list

    Parameters:
    context: context object of pytest
    username: str type, username to check if it is exists
    """

    flag = False

    for user in range(len(context["user_list"])):
        if context["user_list"][user]["username"] == str(username):
            validate_json(context["user_list"][user])
            flag = True
            break

    assert flag, f"User {username} is expected to be in user list"


def get_user_id(context, username: str):
    """Gets user id of given username

    Parameters:
        context: context object of pytest
        username: str type, username to get its id

    Return:
        user id as int
    """

    for user in range(len(context["user_list"])):
        if context["user_list"][user]["username"] == str(username):
            return context["user_list"][user]["id"]


def verify_user_post_count(context, count: int):
    """Verifies if user count is equal to given number

    Parameters:
    context: context object of pytest
    count: int type, value to compare with count of user posts
    """

    list_length = len(context["user_posts"])
    assert list_length == count, f"Values {list_length} and {count} are expected to be equal"


def verify_user_post_count_by_title(context, count: int, title: str):
    """Verifies if user has post with given title

    Parameters:
    context: context object of pytest
    count: int type, quantity of post
    title: str type, title of user comment to be checked
    """
    post_count = 0
    for post in range(len(context["user_posts"])):
        if context["user_posts"][post]["title"] == str(title):
            post_count = post_count + 1

    assert (post_count == count , f"Values {post_count} and {count} are expected to be equal")


def verify_user_post_exists(context, title: str):
    """Verifies if user has post with given title

    Parameters:
    context: context object of pytest
    title: str type, title of user comment to be checked
    """
    flag = False

    for post in range(len(context["user_posts"])):
        if context["user_posts"][post]["title"] == str(title):
            flag = True
            break
    assert flag, f"Post with title \"{title}\" is expected to be in user posts"


def verify_if_email_of_a_comment_is_proper(email: str):
    """Verifies if email is in proper format

    Parameters:
    email: str type, email of the in the comment to be checked
    """
    check_if_email_is_in_proper_format(email)


def verify_if_post_deleted_by_title(context, title: str):
    """Verifies if post is deleted by title

    Parameters:
    title: str type, title of the user comment to be deleted
    """
    ret = delete_post_by_title(context, title)
    assert (len(ret) == 0, "Delete operation is not successful")


def add_new_user_post(context, title: str, body: str, username: str):
    """Adds user post

    Parameters:
    title: str type, title of the user post to be added
    body: str type, body of the user post to be added
    username: str type, username of the user
    """
    context["user_id"] = get_user_id(context, username)
    add_post(title, body, context["user_id"])
