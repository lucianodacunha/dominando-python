class Autor:
    __slots__ = ("__id", "__nome", "__email", "__telefone", "__bio")

    def __init__(self, nome: str, bio: str) -> None:
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.bio = bio

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id) -> None:
        """Método setter da propriedade id"""
        self.__id = id

    @property
    def nome(self) -> str:
        """Método getter da propriedade nome"""
        return self.__nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self.__nome = nome

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email) -> None:
        self.__email = email

    @property
    def telefone(self) -> str:
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone) -> None:
        self.__telefone = telefone

    @property
    def bio(self) -> str:
        return self.__bio

    @bio.setter
    def bio(self, bio: str) -> None:
        self.__bio = bio

    def __str__(self) -> str:
        return f"{str(self.id).zfill(2)} - {self.nome}"
