from viberUser import ViberUser
from viberReaction import ViberReaction
from datetime import datetime


class ViberMessage():
    def __init__(self, text, sender: ViberUser, receiver: ViberUser, reaction: ViberReaction = None):
        self.__text = str(text)

        if isinstance(sender, ViberUser):
            self.__sender = sender
        else:
            raise ValueError("Invalid sender!")

        if isinstance(receiver, ViberUser):
            self.__receiver = receiver
        else:
            raise ValueError("Invalid receiver!")

        if reaction is None or isinstance(reaction, ViberReaction):
            self.__reaction = reaction
        else:
            raise ValueError("Invalid reaction!")

        self.__time = datetime.now().replace(microsecond=0)

    # Getters:

    def get_text(self):
        return self.__text

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_reaction(self):
        return self.__reaction

    def get_time(self):
        return self.__time

    # Setters:

    def set_text(self, text):
        self.__text = str(text)

    def set_sender(self, sender: ViberUser):
        if isinstance(sender, ViberUser):
            self.__sender = sender
        else:
            raise ValueError("Invalid sender!")

    def set_receiver(self, receiver: ViberUser):
        if isinstance(receiver, ViberUser):
            self.__receiver = receiver
        else:
            raise ValueError("Invalid receiver!")

    def set_reaction(self, reaction: ViberReaction):
        if isinstance(reaction, ViberReaction):
            self.__reaction = reaction
        else:
            raise ValueError("Invalid reaction!")

    # Addition methods:

    def show_message(self):
        print(
            f"From: {self.__sender.get_name()} {self.__sender.get_lastName()} * ", end="")
        if self.__sender.get_active():
            print("Active Now - ", end="")
        else:
            print("Not Active - ", end="")
        print(f"at {self.get_time()}")
        print(
            f"To: {self.__receiver.get_name()} {self.__receiver.get_lastName()}")
        if self.__reaction is None:
            print(self.__text)
        else:
            print(f"{self.__text} : ", end="")
            self.__reaction.print()
