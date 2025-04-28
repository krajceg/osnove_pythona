from autor import Autor


class Knjiga():
    def __init__(self, isbn: str = None, naziv: str = None, godinaIzdavanja: int = None, autor: Autor = None):
        if isbn is None or isinstance(isbn, str):
            self.__isbn = isbn
        else:
            raise ValueError("ISBN mora biti string!")

        if naziv is None or isinstance(naziv, str):
            self.__naziv = naziv
        else:
            raise ValueError("Naziv knjige mora biti string!")

        if godinaIzdavanja is None or isinstance(godinaIzdavanja, int):
            self.__godinaIzdavanja = godinaIzdavanja
        else:
            raise ValueError("Godina izdavanja mora biti broj!")

        if autor is None or isinstance(autor, Autor):
            self.__autor = autor
        else:
            raise ValueError("Autor mora biti objekat klase Autor!")

    # Getters:
    def get_isbn(self):
        return self.__isbn

    def get_naziv(self):
        return self.__naziv

    def get_godinaIzdavanja(self):
        return self.__godinaIzdavanja

    def get_autor(self):
        return self.__autor

    # Setters:
    def set_isbn(self, isbn: str):
        if isinstance(isbn, str):
            self.__isbn = isbn
        else:
            raise ValueError("ISBN mora biti broj!")

    def set_naziv(self, naziv: str):
        if isinstance(naziv, str):
            self.__naziv = naziv
        else:
            raise ValueError("Naziv knjige mora biti string!")

    def set_godinaIzdavanja(self, godinaIzdavanja: int):
        if isinstance(godinaIzdavanja, int):
            self.__godinaIzdavanja = godinaIzdavanja
        else:
            raise ValueError("Godina izdavanja mora biti broj!")

    def set_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            self.__autor = autor
        else:
            raise ValueError("Autor mora biti objekat klase Autor!")

    # Additional methods:
    def print(self):
        print(self.__isbn)
        print(f"{self.__naziv} - {self.__godinaIzdavanja}")
        print("Autor: ", end="")
        self.__autor.print()
