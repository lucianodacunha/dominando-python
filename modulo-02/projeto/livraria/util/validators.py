def validator(infos: dict) -> bool:
    keys = infos.keys()

    for key in keys:
        match key:
            case "nome" | "biografia" | "titulo" | "resumo" | "isbn":
                if not isinstance(infos[key], str):
                    raise ValueError(f"{key}, tipo incorreto!")
                if len(infos[key]) <= 1:
                    raise ValueError(f"{key}, tamanho incorreto!")
                return True
            case "ano":
                try:
                    int(infos["ano"])
                    return True
                except:
                    raise Exception(f"{key}, tipo incorreto")
            case "id":
                try:
                    int(infos["id"])
                    return True
                except:
                    raise Exception(f"{key}, tipo incorreto")
            case _:
                return True
