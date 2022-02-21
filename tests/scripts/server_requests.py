import os
import json
import configparser
import requests as req
from os.path import dirname

from tests.scripts.body import create_add_user_post_body
from tests.scripts.headers import get_header

ROOT_DIR = os.path.dirname(dirname(dirname(__file__)))  # Project root dir

cf = configparser.ConfigParser()
cf.read(ROOT_DIR + "/config/config.ini")


def verify_server_is_running():
    """Verifies if server is up & running"""
    resp = req.get(cf["URLs"]['MAIN_URL'])
    assert resp.status_code == int(cf["RESP_CODES"]["SUCCESS"])


def query_all_users():
    """Queries all users

    Return:
        response body as json
    """
    resp = req.get(cf["URLs"]['MAIN_URL'] + cf["URLs"]['USERS_URL'])
    assert resp.status_code == int(cf["RESP_CODES"]["SUCCESS"])
    return json.loads(resp.content.decode("utf-8"))


def query_all_posts_of_user(context):
    """Queries all post of an user

    Return:
        response body as json
    """
    resp = req.get(cf["URLs"]['MAIN_URL'] + cf["URLs"]['USERS_URL'] + str(context["user_id"]) + cf["URLs"]['POSTS_URL'])
    assert resp.status_code == int(cf["RESP_CODES"]["SUCCESS"])
    return json.loads(resp.content.decode("utf-8"))


def query_all_comments_of_a_post(id: int):
    """Queries all comments of a post

    Parameters:
    id: int type, id of the post

    Return:
        response body as json
    """
    resp = req.get(cf["URLs"]['MAIN_URL'] + cf["URLs"]['POSTS_URL'] + str(id) + cf["URLs"]['COMMENTS_URL'])
    assert resp.status_code == int(cf["RESP_CODES"]["SUCCESS"])
    return json.loads(resp.content.decode("utf-8"))


def delete_post_by_title(context, title: str):
    """Deletes post by title

    Parameters:
    title: str type, title of the post

    Return:
        response body as json
    """
    for post in range(len(context["user_posts"])):
        if context["user_posts"][post]["title"] == title:
            resp = req.delete(cf["URLs"]['MAIN_URL'] + cf["URLs"]['POSTS_URL'] + str(context["user_posts"][post]["id"]))
            assert resp.status_code == int(cf["RESP_CODES"]["SUCCESS"])
            return json.loads(resp.content.decode("utf-8"))


def add_post(title: str, body: str, user_id: int):
    """Adds new post for an user
    Parameters:
    title: str type, title of the user post to be added
    body: str type, body of the user post to be added
    user_id: str type, id of the user
    """
    header = get_header()
    body = create_add_user_post_body(title, body, user_id)
    payload = { header, body }
    resp = req.post(cf["URLs"]['MAIN_URL'] + cf["URLs"]['POSTS_URL'], params=payload)
    assert resp.status_code == int(cf["RESP_CODES"]["CREATED"])

