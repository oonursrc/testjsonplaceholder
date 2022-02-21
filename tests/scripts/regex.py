import re

regex = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'


def check_if_email_is_in_proper_format(email: str):
    """Verifies if email is in proper format

    Parameters:
    email: str type, email of the in the comment to be checked

    Return:
    True if email is in proper format otherwise False
    """
    return True if (re.search(regex, email)) else False
