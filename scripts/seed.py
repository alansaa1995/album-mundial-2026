"""
Script de semilla — carga el catálogo base de figuritas del Mundial 2026.
Ejecutar desde la raíz del proyecto: python scripts/seed.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import SessionLocal, engine, Base
import app.models  # noqa: F401

Base.metadata.create_all(bind=engine)

STICKER_CATALOG = [
    # Argentina (ARG) — 19 figuritas
    *[{"code": f"ARG{i}", "section": "Argentina", "player_name": name, "is_special": False}
      for i, name in enumerate([
          "Lionel Messi", "Ángel Di María", "Rodrigo De Paul", "Julián Álvarez",
          "Emiliano Martínez", "Nicolás Otamendi", "Leandro Paredes", "Alexis Mac Allister",
          "Nahuel Molina", "Marcos Acuña", "Germán Pezzella", "Paulo Dybala",
          "Lautaro Martínez", "Exequiel Palacios", "Enzo Fernández", "Thiago Almada",
          "Valentín Carboni", "Facundo Medina", "Walter Kannemann",
      ], start=1)],

    # Brasil (BRA) — 19 figuritas
    *[{"code": f"BRA{i}", "section": "Brasil", "player_name": name, "is_special": False}
      for i, name in enumerate([
          "Vinicius Jr.", "Rodrygo", "Neymar Jr.", "Raphinha",
          "Alisson Becker", "Marquinhos", "Casemiro", "Bruno Guimarães",
          "Eder Militão", "Alex Sandro", "Thiago Silva", "Richarlison",
          "Fred", "Antony", "Gabriel Martinelli", "Endrick",
          "Lucas Paquetá", "Danilo", "Éder Militão",
      ], start=1)],

    # Francia (FRA) — 19 figuritas
    *[{"code": f"FRA{i}", "section": "Francia", "player_name": name, "is_special": False}
      for i, name in enumerate([
          "Kylian Mbappé", "Antoine Griezmann", "Ousmane Dembélé", "Marcus Thuram",
          "Hugo Lloris", "Raphaël Varane", "N'Golo Kanté", "Aurélien Tchouaméni",
          "Benjamin Pavard", "Theo Hernández", "William Saliba", "Eduardo Camavinga",
          "Adrien Rabiot", "Olivier Giroud", "Christopher Nkunku", "Randal Kolo Muani",
          "Youssouf Fofana", "Jules Koundé", "Mike Maignan",
      ], start=1)],

    # Estadios — sección especial
    {"code": "EST1", "section": "Estadios", "player_name": None, "description": "MetLife Stadium - Nueva York/Nueva Jersey", "is_special": True},
    {"code": "EST2", "section": "Estadios", "player_name": None, "description": "AT&T Stadium - Dallas", "is_special": True},
    {"code": "EST3", "section": "Estadios", "player_name": None, "description": "SoFi Stadium - Los Ángeles", "is_special": True},
    {"code": "EST4", "section": "Estadios", "player_name": None, "description": "Hard Rock Stadium - Miami", "is_special": True},
    {"code": "EST5", "section": "Estadios", "player_name": None, "description": "Levi's Stadium - San Francisco", "is_special": True},

    # Escudos (foil especiales)
    {"code": "ESC_ARG", "section": "Escudos", "player_name": None, "description": "Escudo Argentina - Foil", "is_special": True},
    {"code": "ESC_BRA", "section": "Escudos", "player_name": None, "description": "Escudo Brasil - Foil", "is_special": True},
    {"code": "ESC_FRA", "section": "Escudos", "player_name": None, "description": "Escudo Francia - Foil", "is_special": True},
]


def run_seed():
    db = SessionLocal()
    try:
        from app.models.sticker import Sticker
        existing = db.query(Sticker).count()
        if existing > 0:
            print(f"El catálogo ya tiene {existing} figuritas. Seed omitido.")
            return

        stickers = [
            Sticker(
                code=s["code"].upper(),
                section=s["section"],
                player_name=s.get("player_name"),
                description=s.get("description"),
                is_special=s.get("is_special", False),
            )
            for s in STICKER_CATALOG
        ]
        db.add_all(stickers)
        db.commit()
        print(f"Seed completado: {len(stickers)} figuritas cargadas.")
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
