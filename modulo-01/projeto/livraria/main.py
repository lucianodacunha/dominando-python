from rich.console import Console
from view.view_principal import menu_principal

console = Console()


def main() -> None:

    menu_principal()
    console.input("\n[red]Pressione enter para finalizar...")
    console.clear()


if __name__ == "__main__":
    main()
