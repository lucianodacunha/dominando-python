from model.model_autor import Autor
from dao.dao_autores import AutorDAO
from util.validators import validator


class AutorController:

    def __init__(self) -> None:
        self.dao = AutorDAO()

    def inserir(self, autor_info: dict) -> dict:
        try:
            validator(autor_info)
            nome = autor_info["nome"]
            biografia = autor_info["biografia"]
            autor = Autor(nome, biografia)

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
            biografia = autor_info["biografia"]
            autor = Autor(nome, biografia)
            autor = self.dao.atualizar(id, nome, biografia)
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

    def buscar_por_id(self, autor_info: dict):
        try:
            id = int(autor_info["id"])
            autor = self.dao.buscar_por_id(id)
            return {"success": True, "message": autor}
        except Exception as e:
            return {"success": False, "error": str(e)}
