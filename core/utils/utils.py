import re

"""
Este módulo contém funções utilitárias para o projeto de web scraping.
Inclui funções para normalização de strings e formatação de URLs.
"""

def normalize_title_to_link(title: str) -> str:
    """
    Normaliza o título de um produto para ser usado em uma URL (slug).

    Args:
        title (str): O título original do produto.

    Returns:
        str: O título normalizado, contendo apenas caracteres alfanuméricos,
             hífens, e em letras minúsculas.
    """
    # Remove caracteres que não sejam alfanuméricos, espaços ou hífens
    normalized = re.sub(r"[^a-zA-Z0-9\s-]", "", title)

    # Substitui espaços por hífens
    normalized = normalized.replace(" ", "-")

    # Substitui múltiplos hífens consecutivos por um único hífen
    normalized = re.sub(r"-{2,}", "-", normalized)

    # Converte para minúsculas
    normalized = normalized.lower()

    # Remove hífens do início e do fim da string
    normalized = normalized.strip("-")

    return normalized
