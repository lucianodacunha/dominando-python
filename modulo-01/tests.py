
from rich.console import Console


console = Console()

console.clear()
nome: str = console.input("[green]Informe seu nome: ")
console.print(f"[yellow]Olá {nome}")

console.input("\n[red]Pressione enter para continuar...")
console.clear()