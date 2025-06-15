from model.model_livro import Livro
from exception.exceptions import RegistroNaoEncontradoException
from util.connection_factory import ConnectionFactory

class LivroDAO:

    def __init__(self) -> None:
        ...

    def inserir(self, livro: Livro) -> None:
        # TODO: Corrigir inserção com id_categoria, editora e autor
        titulo = livro.titulo
        resumo = livro.resumo
        ano = livro.ano
        paginas = livro.paginas
        isbn = livro.isbn
        sql = """INSERT INTO livraria.livros (titulo, resumo, ano, paginas, isbn)
            VALUES (%s, %s, %s, %s, %s)"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (titulo, resumo, ano, paginas, isbn))
            connection.commit()
            registro_inserido = cursor.rowcount
            if not registro_inserido:
                raise Exception(f"Nenhum registro inserido")            
        except Exception as e:
            raise Exception(f"Falha ao inserir, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def listar(self) -> list[tuple[Livro]]:
        # TODO: Atualizar consulta trazendo informações de categoria, autor e editora
        sql = "SELECT id, titulo, resumo, ano, paginas, isbn FROM livraria.livros;"
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            livros = cursor.fetchall()
            if not livros:
                raise RegistroNaoEncontradoException("Nenhum livro cadastrado")
            return livros
        except RegistroNaoEncontradoException as e:
            raise RegistroNaoEncontradoException(f"{e}")
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def atualizar(self, id: int, titulo: str, resumo: str, ano: int, 
        paginas: int, isbn: str) -> None:        
        # TODO: Atualizar update alterando informações de categoria, autor e editora
        sql = """UPDATE livraria.livros 
            SET titulo = %s, resumo = %s, ano = %s, paginas = %s, isbn = %s
            WHERE id = %s;"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (titulo, resumo, ano, paginas, isbn, id))
            connection.commit()
            registro_atualizado = cursor.rowcount
            if not registro_atualizado:
                raise Exception(f"Nenhum registro atualizado")            
        except Exception as e:
            raise Exception(f"Falha ao atualizar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def excluir(self, id: int) -> Livro:
        sql = "DELETE FROM livraria.livros WHERE id = %s"
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
            registro_excluido = cursor.rowcount
            if not registro_excluido:
                raise Exception(f"Nenhum registro excluido")            
        except Exception as e:
            raise Exception(f"Falha ao excluir, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def buscar_por_id(self, id: int) -> Livro:
        sql = """SELECT 
            id, titulo, resumo, ano, paginas, isbn 
            FROM livraria.livros WHERE id = %s;"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            livro = cursor.fetchone()
            if not livro:
                raise RegistroNaoEncontradoException(f"Nenhum livro cadastrado")
            return livro
        except RegistroNaoEncontradoException as e:
            raise RegistroNaoEncontradoException(f"{e}")
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)
