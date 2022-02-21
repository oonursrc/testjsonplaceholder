def create_add_user_post_body(title: str, body: str, user_id: int):
    """Creates body for adding new user post

    Parameters:
    title: str type, title of the post
    body: str type, body of the post
    user_id: int type, id of the user

    Return:
        body as json
    """
    return {
        "userId": user_id,
        "title": title,
        "body": body
    }

