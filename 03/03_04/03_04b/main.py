user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    user_pref2={}
    for key,value in user_pref.items():
        if value is not None:
            user_pref2[key]=value
    return user_pref2


print(update_preferences(user_preferences))
