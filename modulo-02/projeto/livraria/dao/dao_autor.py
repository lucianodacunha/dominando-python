from model.model_autor import Autor
from exception.exceptions import RegistroNaoEncontradoException
from util.connection_factory import ConnectionFactory


class AutorDAO:
    def __init__(self) -> None:
        ...

    def inserir(self, autor: Autor) -> Autor:
        nome = autor.nome
        email = autor.email
        telefone = autor.telefone
        bio = autor.bio        
        sql = """INSERT INTO livraria.autores (nome, email, telefone, bio)
            VALUES (%s, %s, %s, %s)"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome, email, telefone, bio))
            connection.commit()
            registro_inserido = cursor.rowcount
            if not registro_inserido:
                raise Exception(f"Nenhum registro inserido")            
        except Exception as e:
            raise Exception(f"Falha ao inserir, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def listar(self) -> dict[int, Autor]:
        sql = "SELECT id, nome, email, telefone, bio FROM livraria.autores;"
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            autores = cursor.fetchall()
            if not autores:
                raise RegistroNaoEncontradoException("Nenhum registro cadastrado")
            return autores
        except RegistroNaoEncontradoException as e:
            raise RegistroNaoEncontradoException(f"{e}")
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def atualizar(self, id: int, nome: str, email: str, telefone: str, bio: str) -> None:
        # TODO: Atualizar update alterando informações de categoria, autor e editora
        sql = """UPDATE livraria.autores
                SET nome = %s, email = %s, telefone = %s, bio = %s  
                WHERE id = %s;"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome, email, telefone, bio, id))
            connection.commit()
            registro_atualizado = cursor.rowcount
            if not registro_atualizado:
                raise Exception(f"Nenhum registro atualizado")            
        except Exception as e:
            raise Exception(f"Falha ao atualizar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)

    def excluir(self, id: int) -> None:
        sql = "DELETE FROM livraria.autores WHERE id = %s"
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

    def listar_por_id(self, id: int) -> Autor:
        sql = """SELECT id, nome, email, telefone, bio 
                    FROM livraria.autores 
                    WHERE id = %s;"""
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            autor = cursor.fetchone()
            if not autor:
                raise RegistroNaoEncontradoException(f"Nenhum registro cadastrado")
            return autor
        except RegistroNaoEncontradoException as e:
            raise RegistroNaoEncontradoException(f"{e}")
        except Exception as e:
            raise Exception(f"Falha ao consultar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)
