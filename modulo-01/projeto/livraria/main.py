from rich.console import Console
from view.view_principal import menu

console = Console()


def main() -> None:

    menu()
    console.input("\n[bold red]Pressione enter para finalizar...")
    console.clear()


if __name__ == "__main__":
    main()
