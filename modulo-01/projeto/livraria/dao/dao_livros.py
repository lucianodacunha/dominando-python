from model.model_livro import Livro

livros: list[Livro] = list()


def listar() -> list[Livro]:
    return livros


def cadastrar(livro: Livro) -> None:
    livros.append(livro)


def excluir(id: int) -> None:
    for idx, livro in enumerate(livros):
        if livro.id == id:
            break
    return livros.pop(idx)


def listar_por_id(id: int) -> None:
    for idx, livro in enumerate(livros, start=1):
        if livro.id == id:
            break

    return livros[idx]


def editar(id: int, livro: Livro) -> None:
    _livro = listar_por_id(id)
    _livro.nome = livro.nome
    _livro.biografia = livro.biografia
    return _livro
