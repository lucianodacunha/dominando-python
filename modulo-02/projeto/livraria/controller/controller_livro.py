from model.model_livro import Livro
from dao.dao_livro import LivroDAO
from util.validators import validator


class LivroController:

    def __init__(self) -> None:
        self.dao = LivroDAO()

    def inserir(self, livro_info: dict) -> dict:
        try:
            validator(livro_info)
            titulo = livro_info["titulo"]
            resumo = livro_info["resumo"]
            ano = livro_info["ano"]
            paginas = livro_info["paginas"]
            isbn = livro_info["isbn"]
            livro = Livro(titulo, resumo, ano, paginas, isbn)

            self.dao.inserir(livro)
            return {"success": True, "message": "Registro inserido com sucesso"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def listar(self) -> dict:
        try:
            livros = self.dao.listar()
            return {"success": True, "message": livros}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def atualizar(self, livro_info: dict) -> dict:
        try:
            id = int(livro_info["id"])
            titulo = livro_info["titulo"]
            resumo = livro_info["resumo"]
            ano = livro_info["ano"]
            paginas = livro_info["paginas"]
            isbn = livro_info["isbn"]

            livro = self.dao.atualizar(id, titulo, resumo, ano, paginas, isbn)
            return {"success": True, "message": livro}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def excluir(self, livro_info: dict) -> dict:
        try:
            id = int(livro_info["id"])

            livro = self.dao.excluir(id)
            return {"success": True, "message": livro}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def buscar_por_id(self, livro_info: dict):
        try:
            id = int(livro_info["id"])
            livro = self.dao.buscar_por_id(id)
            return {"success": True, "message": livro}
        except Exception as e:
            return {"success": False, "error": str(e)}
