from viberUser import ViberUser


class ViberReaction():
    def __init__(self, emoji: str, user: ViberUser):
        if isinstance(emoji, str) and emoji in ["sunglases", "heart", "smile", "like", "sad"]:
            self.__emoji = emoji
        else:
            raise ValueError("Invalid emoji!")

        if isinstance(user, ViberUser):
            self.__user = user
        else:
            raise ValueError("Invalid user!")

    # Getters:

    def get_emoji(self):
        return self.__emoji

    def get_user(self):
        return self.__user

    # Setters:

    def set_emoji(self, emoji: str):
        if isinstance(emoji, str) and emoji in ["sunglases", "heart", "smile", "like", "sad"]:
            self.__emoji = emoji
        else:
            raise ValueError("Invalid emoji!")

    def set_user(self, user: ViberUser):
        if isinstance(user, ViberUser):
            self.__user = user
        else:
            raise ValueError("Invalid user!")

    # Additional methods:
    def print(self):
        print(
            f"{self.__emoji} from {self.__user.get_name()} {self.__user.get_lastName()}")
