from model.model_editora import Editora
from exception.exceptions import RegistroNaoEncontradoException
from util.connection_factory import ConnectionFactory

class EditoraDAO:
    def __init__(self):
        ...

    def inserir(self, editora: Editora) -> None:
        sql = "INSERT INTO livraria.editoras (nome, endereco, telefone) VALUES (%s, %s, %s);"
        nome = editora.nome
        endereco = editora.endereco
        telefone = editora.telefone
        connection = None
        cursor = None

        try:            
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome, endereco, telefone))
            registros_inseridos = cursor.rowcount
            connection.commit()
            return None
        except Exception as e:
            connection.rollback()
            raise Exception(f"Erro durante o insert: {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)


    def listar(self) -> list[str]:
        sql = "SELECT id, nome, endereco, telefone FROM livraria.editoras;"
        connection = None
        cursor = None
        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            registros = cursor.fetchall()
            return registros
        except Exception as e:
            raise Exception(f"Erro ao consultar: {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)


    def atualizar(self, id: int, nome: str, endereco: str, telefone: str) -> None:
        sql = "UPDATE livraria.editoras SET nome = %s, endereco = %s, telefone = %s WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (nome, endereco, telefone, id))
            registros_atualizados = cursor.rowcount
            connection.commit()
            if not registros_atualizados:
                raise Exception("Id não encontrado")            
        except Exception as e:
            connection.rollback()
            raise Exception(f"Erro ao atualizar, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)


    def excluir(self, id: int) -> None:
        sql = "DELETE FROM livraria.editoras WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
            registro_excluidos = cursor.rowcount
            if not registro_excluidos:
                raise Exception(f"Id não encontrado")
        except Exception as e:
            raise Exception(f"Erro ao excluir um registro, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)


    def listar_por_id(self, id: int) -> Editora:
        sql = "SELECT id, nome, endereco, telefone FROM livraria.editoras WHERE id = %s;"
        connection = None
        cursor = None

        try:
            connection = ConnectionFactory.get_connection()
            cursor = connection.cursor()
            cursor.execute(sql, (id, ))
            editora = cursor.fetchone()
            if not editora:
                raise Exception(f"Id não encontrado") 
            return editora
        except Exception as e:
            raise Exception(f"Erro ao buscar por id, {e}")
        finally:
            ConnectionFactory.close_connection(connection, cursor)
