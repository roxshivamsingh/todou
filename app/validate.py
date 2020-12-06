from app.models import User


def username(val):
    if(val != ""):
        if(User(username=val.lower()).exist()):
            return 0
        else:
            return 1
    else:
        return 0
