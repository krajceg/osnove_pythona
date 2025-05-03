
class ViberUser():
    def __init__(self, name: str, lastName: str, phoneNumber: int, active: bool):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Invalid name!")

        if isinstance(lastName, str) and lastName.strip():
            self.__lastName = lastName
        else:
            raise ValueError("Invalid last name!")

        if isinstance(phoneNumber, int) and len(str(phoneNumber)) >= 8:
            self.__phoneNumber = phoneNumber
        else:
            raise ValueError("Invalid phone number!")

        if isinstance(active, bool):
            self.__active = active
        else:
            raise ValueError("Invalid status!")

    # Getters:

    def get_name(self):
        return self.__name

    def get_lastName(self):
        return self.__lastName

    def get_phoneNumber(self):
        return self.__phoneNumber

    def get_active(self):
        return self.__active

    # Setters:

    def set_name(self, name: str):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Invalid name!")

    def set_lastName(self, lastName: str):
        if isinstance(lastName, str) and lastName.strip():
            self.__lastName = lastName
        else:
            raise ValueError("Invalid last name!")

    def set_phoneNumber(self, phoneNumber: int):
        if isinstance(phoneNumber, int) and len(str(phoneNumber)) >= 11:
            self.__phoneNumber = phoneNumber
        else:
            raise ValueError("Invalid phone number!")

    def set_active(self, active: bool):
        if isinstance(active, bool):
            self.__active = active
        else:
            raise ValueError("Invalid status!")
