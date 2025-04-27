class tacka:
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    def stampaj(self):
        print(f"Kordinate x: {self.__x}")
        print(f"Kordinate y: {self.__y}")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            raise ValueError("X mora biti broj.")

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            raise ValueError("Y mora biti broj.")
