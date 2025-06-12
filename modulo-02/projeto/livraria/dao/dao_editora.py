from model.model_editora import Editora
from exception.exceptions import RegistroNaoEncontradoException
from dao.connection_factory import ConnectionFactory

class EditoraDAO:
    def __init__(self):
        ...
        # self.__editoras: dict[int, Editora] = dict()
        # self.__sequence: int = 1

    def inserir(self, editora: Editora) -> Editora:
        sql = "INSERT INTO livraria.editoras (nome, endereco, telefone) values (%s, %s, %s);"
        nome = editora.nome
        endereco = editora.endereco
        telefone = editora.telefone

        try:
            conn = ConnectionFactory.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (nome, endereco, telefone))
            conn.commit()
            cursor.close()
            # novo_id = cursor.fetchone()[0]

            return None #novo_id
        except Exception as e:
            print(f"Erro durante o insert: {e}")

        # editora.id = self.__sequence
        # self.__editoras[editora.id] = editora
        # self.__sequence += 1
        # return self.__editoras[editora.id]

    def listar(self) -> dict[int, Editora]:
        sql = "SELECT nome, endereco, telefone FROM livraria.editoras;"
        try:
            conn = ConnectionFatory.get_connection()
            cursor = conn.cursor()
            cursor.execute(sql)
            registros = cursor.fetchall()
            return list(registros)
        except Exception as e:
            print(f"Erro ao consultar: {e}")

        # if not self.__editoras:
        #     raise RegistroNaoEncontradoException("Nenhum autor cadastrado")
        # return self.__editoras.values()

    def atualizar(self, id: int, nome: str, endereco: str, telefone: str) -> Editora:
        editora = self.buscar_por_id(id)
        editora.nome = nome
        editora.endereco = endereco
        editora.telefone = telefone
        return editora

    def excluir(self, id: int) -> Editora:
        if self.__editoras.get(id, 0):
            return self.__editoras.pop(id, 0)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")

    def buscar_por_id(self, id: int) -> Editora:
        if self.__editoras.get(id, 0):
            return self.__editoras.get(id)
        else:
            raise RegistroNaoEncontradoException("Registro não encontrado")
