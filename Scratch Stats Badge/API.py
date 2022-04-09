from requests import get


def get_user_data(username, data_type):
    _default_types = ["id", "username", "scratchteam",
                      "joined", "status", "bio", "country"]
    _scratch_db_data = ["loves", "favorites",
                        "comments", "views", "followers", "following"]
    _other = ["messages"]
    try:
        if data_type in _default_types:
            data = get(f"https://api.scratch.mit.edu/users/{username}").json()
            if data_type in ["id", "username", "scratchteam"]:
                return data[data_type]
            elif data_type == _default_types[3]:
                return data["history"]["joined"]
            elif data_type in _default_types[4:]:
                return data["profile"][data_type]
        elif data_type in _scratch_db_data:
            data = get(
                f"https://scratchdb.lefty.one/v3/user/info/{username}").json()["statistics"]
            return data[data_type]
        elif data_type in _other:
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"}
            data = get(
                f"https://api.scratch.mit.edu/users/{username}/messages/count", headers=headers).json()["count"]
            return data
        else:
            return False
    except KeyError:
        return False


def get_studio_data(id, data_type):
    _default_types = ["id", "title", "comments",
                      "followers", "managers", "projects"]
    try:
        if data_type in _default_types:
            data = get(f"https://api.scratch.mit.edu/studios/{id}/").json()
            if data_type in ["id", "title"]:
                return data[data_type]
            elif data_type in _default_types[2:]:
                return data["stats"][data_type]
        else:
            return False
    except KeyError:
        return False


def get_project_data(id, data_type):
    _default_types = ["id", "title", "views",
                      "loves", "favorites", "remixes"]
    try:
        if data_type in _default_types:
            data = get(f"https://api.scratch.mit.edu/projects/{id}/").json()
            if data_type in ["id", "title"]:
                return data[data_type]
            elif data_type in _default_types[2:]:
                return data["stats"][data_type]
        else:
            return False
    except KeyError:
        return False
