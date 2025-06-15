from model.model_categoria import Categoria
from dao.dao_categoria import CategoriaDAO
from util.validators import validator


class CategoriaController:
    def __init__(self) -> None:
        self.dao = CategoriaDAO()

    def inserir(self, categoria_info: dict) -> dict:
        try:
            validator(categoria_info)
            categoria = Categoria(**categoria_info)

            self.dao.inserir(categoria)
            return {"success": True, "message": "Registro inserido com sucesso"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def listar(self) -> dict:
        try:
            categorias = self.dao.listar()
            return {"success": True, "message": categorias}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def atualizar(self, categoria_info: dict) -> dict:
        try:
            validator(categoria_info)
            categoria = Categoria(**categoria_info)
            categoria = self.dao.atualizar(categoria)
            return {"success": True, "message": categoria}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def excluir(self, categoria_info: dict) -> dict:
        try:
            id = int(categoria_info["id"])
            categoria = self.dao.excluir(id)
            return {"success": True, "message": categoria}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def buscar_por_id(self, categoria_info: dict):
        try:
            id = int(categoria_info["id"])
            categoria = self.dao.buscar_por_id(id)
            return {"success": True, "message": categoria}
        except Exception as e:
            return {"success": False, "error": str(e)}
