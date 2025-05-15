from model.model_autor import Autor

autores: list[Autor] = list()


def listar_autores() -> list[Autor]:
    return autores


def excluir_autor(id: int) -> Autor:
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break
    return autores.pop(idx)


def listar_autor_por_id(id: int) -> Autor:
    for idx, autor in enumerate(autores):
        if autor.id == id:
            break

    return autores[idx]


def cadastrar_autores(autor: Autor) -> None:
    autores.append(autor)


def editar_autor(id: int, autor: Autor) -> Autor:
    for idx, _autor in enumerate(autores):
        if _autor.id == id:
            break

    _autor = autores[idx]
    _autor.nome = autor.nome
    _autor.biografia = autor.biografia
    return _autor
