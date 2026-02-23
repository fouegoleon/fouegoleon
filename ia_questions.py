#!/usr/bin/env python3
"""Assistant IA simple en ligne de commande qui répond à des questions en français."""

from __future__ import annotations

import datetime as _dt
import re


def repondre(question: str) -> str:
    """Retourne une réponse simple basée sur l'intention détectée."""
    q = question.strip().lower()

    if not q:
        return "Pose-moi une question et je ferai de mon mieux pour te répondre."

    if any(mot in q for mot in ["bonjour", "salut", "coucou"]):
        return "Bonjour 👋 Je suis une IA simple. Pose-moi une question."

    if "heure" in q:
        maintenant = _dt.datetime.now().strftime("%H:%M")
        return f"Il est actuellement {maintenant}."

    if "date" in q:
        aujourd_hui = _dt.date.today().strftime("%d/%m/%Y")
        return f"Nous sommes le {aujourd_hui}."

    if "qui es-tu" in q or "tu es qui" in q:
        return "Je suis une intelligence artificielle de démonstration qui répond à des questions simples."

    # Petit mode calcul: ex. "combien font 12 + 7"
    calcul = re.search(r"(-?\d+)\s*([+\-*/])\s*(-?\d+)", q)
    if calcul:
        a, op, b = calcul.groups()
        x, y = int(a), int(b)
        if op == "+":
            return f"{x} + {y} = {x + y}"
        if op == "-":
            return f"{x} - {y} = {x - y}"
        if op == "*":
            return f"{x} * {y} = {x * y}"
        if op == "/":
            if y == 0:
                return "Impossible de diviser par zéro."
            return f"{x} / {y} = {x / y}"

    return (
        "Je n'ai pas encore la réponse précise à cette question. "
        "Essaie une question sur la date, l'heure, ou un calcul simple (ex: 12 + 7)."
    )


def main() -> None:
    print("IA Q&R (écris 'quit' pour quitter)")
    while True:
        entree = input("Toi : ")
        if entree.strip().lower() in {"quit", "exit", "q"}:
            print("IA : À bientôt !")
            break
        print("IA :", repondre(entree))


if __name__ == "__main__":
    main()
