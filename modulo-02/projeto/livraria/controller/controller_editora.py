from model.model_editora import Editora
from dao.dao_editora import EditoraDAO
from util.validators import validator


class EditoraController:

    def __init__(self) -> None:
        self.dao = EditoraDAO()

    def inserir(self, editora_info: dict) -> dict:
        try:
            validator(editora_info)
            nome = editora_info["nome"]
            endereco = editora_info["endereco"]
            telefone = editora_info["telefone"]
            editora = Editora(nome, endereco, telefone)

            self.dao.inserir(editora)
            return {"success": True, "message": "Registro inserido com sucesso"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def listar(self) -> dict:
        try:
            editoras = self.dao.listar()
            return {"success": True, "message": editoras}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def atualizar(self, editora_info: dict) -> dict:
        try:
            id = int(editora_info["id"])
            nome = editora_info["nome"]
            endereco = editora_info["endereco"]
            telefone = editora_info["telefone"]
            editora = self.dao.atualizar(id, nome, endereco, telefone)
            return {"success": True, "message": editora}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def excluir(self, editora_info: dict) -> dict:
        try:
            id = int(editora_info["id"])
            editora = self.dao.excluir(id)
            return {"success": True, "message": editora}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def buscar_por_id(self, editora_info: dict):
        try:
            id = int(editora_info["id"])
            editora = self.dao.buscar_por_id(id)
            return {"success": True, "message": editora}
        except Exception as e:
            return {"success": False, "error": str(e)}
