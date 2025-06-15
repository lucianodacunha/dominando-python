from model.model_autor import Autor
from dao.dao_autor import AutorDAO
from util.validators import validator


class AutorController:

    def __init__(self) -> None:
        self.dao = AutorDAO()

    def inserir(self, autor_info: dict) -> dict:
        try:
            validator(autor_info)
            nome = autor_info["nome"]
            email = autor_info["email"]
            telefone = autor_info["telefone"]
            bio = autor_info["bio"]
            autor = Autor(nome, email, telefone, bio)

            self.dao.inserir(autor)
            return {"success": True, "message": "Registro inserido com sucesso"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def listar(self) -> dict:
        try:
            autores = self.dao.listar()
            return {"success": True, "message": autores}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def atualizar(self, autor_info: dict) -> dict:
        try:
            id = int(autor_info["id"])
            nome = autor_info["nome"]
            email = autor_info["email"]
            telefone = autor_info["telefone"]
            bio = autor_info["bio"]
            autor = self.dao.atualizar(id, nome, email, telefone, bio)
            return {"success": True, "message": autor}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def excluir(self, autor_info: dict) -> dict:
        try:
            id = int(autor_info["id"])
            autor = self.dao.excluir(id)
            return {"success": True, "message": autor}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def listar_por_id(self, autor_info: dict):
        try:
            id = int(autor_info["id"])
            autor = self.dao.listar_por_id(id)
            return {"success": True, "message": autor}
        except Exception as e:
            return {"success": False, "error": str(e)}
