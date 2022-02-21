from enum import Enum


class Conditions(Enum):
    USERS = "users"
    POSTS = "posts"
    COMMENTS = "comments"


class Operations(Enum):
    SEARCH = "Search"
    DELETE = "Delete"
    Update = "Update"
