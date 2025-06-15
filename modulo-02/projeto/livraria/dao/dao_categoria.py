from model.model_categoria import Categoria
from exception.exceptions import RegistroNaoEncontradoException
from util.connection_factory import ConnectionFactory


class CategoriaDAO:
    def __init__(self) -> None:
        ...
        
    def inserir(self, categoria: Categoria) -> None:
        nome = categoria.nome
        sql = "INSERT INTO livraria.categorias (nome) VALUES (%s);"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome,))
            connection.commit()
            registro_inserido = cursor.rowcount
            if not registro_inserido:
                raise Exception("Nenhum registro inserido")
        except Exception as e:
            raise Exception(f"Falha ao inserir, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def listar(self) -> list[Categoria]:
        sql = "SELECT id, nome FROM livraria.categorias;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            categorias = cursor.fetchall()
            if not categorias:
                raise RegistroNaoEncontradoException("Nenhum registro encontrado")
            return categorias
        except RegistroNaoEncontradoException as e:
            raise RegistroNaoEncontradoException(f"{e}")
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def atualizar(self, id: int, nome: str) -> None:
        sql = "UPDATE livraria.categorias SET nome = %s WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome, id))
            connection.commit()
            registros_atualizados = cursor.rowcount
            if not registros_atualizados:
                raise Exception("Nenhum registro atualizado")
        except Exception as e:
            raise Exception(f"Falha ao atualizar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def excluir(self, id: int) -> Categoria:
        sql = "DELETE FROM livraria.categorias WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
            registros_excluidos = cursor.rowcount
            if not registros_excluidos:
                raise Exception("Nenhum registro excluido")
        except Exception as e:
            raise Exception(f"Falha ao excluir, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def buscar_por_id(self, id: int) -> Categoria:
        sql = "SELECT id, nome FROM livraria.categorias WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            categoria = cursor.fetchone()            
            if not categoria:
                raise Exception("Nenhum registro encontrado")
            return categoria
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)
