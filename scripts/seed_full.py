"""
Seed definitivo — 980 figuritas álbum Panini Mundial 2026.
  1   → código '00'   : Logo Panini / Trofeo FIFA
  19  → FWC1-FWC19    : Especiales torneo
  960 → 48 países × 20 figuritas cada uno
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import SessionLocal, engine, Base
import app.models  # noqa: F401

Base.metadata.create_all(bind=engine)

# ── Nombre oficial de cada selección ─────────────────────────────
COUNTRY_NAMES = {
    # UEFA (16)
    "GER": "Alemania",           "AUT": "Austria",
    "BEL": "Bélgica",            "BIH": "Bosnia y Herzegovina",
    "CRO": "Croacia",            "SCO": "Escocia",
    "ESP": "España",             "FRA": "Francia",
    "ENG": "Inglaterra",         "NOR": "Noruega",
    "NED": "Países Bajos",       "POR": "Portugal",
    "CZE": "República Checa",    "SWE": "Suecia",
    "SUI": "Suiza",              "TUR": "Turquía",
    # CAF (10)
    "ALG": "Argelia",            "CPV": "Cabo Verde",
    "CIV": "Costa de Marfil",    "EGY": "Egipto",
    "GHA": "Ghana",              "MAR": "Marruecos",
    "COD": "Rep. Dem. Congo",    "SEN": "Senegal",
    "RSA": "Sudáfrica",          "TUN": "Túnez",
    # AFC (9)
    "KSA": "Arabia Saudita",     "AUS": "Australia",
    "QAT": "Catar",              "KOR": "Corea del Sur",
    "IRN": "Irán",               "IRQ": "Irak",
    "JOR": "Jordania",           "JPN": "Japón",
    "UZB": "Uzbekistán",
    # CONMEBOL (6)
    "ARG": "Argentina",          "BRA": "Brasil",
    "COL": "Colombia",           "ECU": "Ecuador",
    "PAR": "Paraguay",           "URU": "Uruguay",
    # CONCACAF (6)
    "CAN": "Canadá",             "USA": "Estados Unidos",
    "MEX": "México",             "CUW": "Curazao",
    "HAI": "Haití",              "PAN": "Panamá",
    # OFC (1)
    "NZL": "Nueva Zelanda",
}

# Orden exacto de los 48 países
COUNTRIES = [
    # UEFA
    "GER","AUT","BEL","BIH","CRO","SCO","ESP","FRA",
    "ENG","NOR","NED","POR","CZE","SWE","SUI","TUR",
    # CAF
    "ALG","CPV","CIV","EGY","GHA","MAR","COD","SEN","RSA","TUN",
    # AFC
    "KSA","AUS","QAT","KOR","IRN","IRQ","JOR","JPN","UZB",
    # CONMEBOL
    "ARG","BRA","COL","ECU","PAR","URU",
    # CONCACAF
    "CAN","USA","MEX","CUW","HAI","PAN",
    # OFC
    "NZL",
]
assert len(COUNTRIES) == 48, f"Se esperan 48 países, hay {len(COUNTRIES)}"

# ── Jugadores reales para las potencias ─────────────────────────
# Clave = número de posición (1-20)
# pos 1  → Escudo (Brillante)   is_special=True
# pos 13 → Foto de Equipo       is_special=False
KNOWN: dict[str, dict[int, str]] = {
    "ARG": {
         1: "Escudo Argentina (Brillante)",
         2: "Emiliano Martínez",       3: "Nahuel Molina",
         4: "Cristian Romero",         5: "Nicolás Otamendi",
         6: "Nicolás Tagliafico",      7: "Leonardo Balerdi",
         8: "Enzo Fernández",          9: "Alexis Mac Allister",
        10: "Rodrigo De Paul",        11: "Exequiel Palacios",
        12: "Leandro Paredes",        13: "Foto de Equipo - Selección Argentina",
        14: "Nico Paz",               15: "Franco Mastantuono",
        16: "Nicolás González",       17: "Lionel Messi",
        18: "Lautaro Martínez",       19: "Julián Álvarez",
        20: "Giuliano Simeone",
    },
    "BRA": {
         1: "Escudo Brasil (Brillante)",
         2: "Alisson",                 3: "Danilo",
         4: "Marquinhos",              5: "Gabriel Magalhães",
         6: "Guilherme Arana",         7: "Bruno Guimarães",
         8: "João Gomes",              9: "Lucas Paquetá",
        10: "Rodrygo",                11: "Raphinha",
        12: "Vinícius Júnior",        13: "Foto de Equipo - Selección Brasil",
        14: "Endrick",                15: "Savinho",
        16: "Gabriel Martinelli",     17: "Pedro",
        18: "André",                  19: "Éder Militão",
        20: "Bento",
    },
    "FRA": {
         1: "Escudo Francia (Brillante)",
         2: "Mike Maignan",            3: "Jules Koundé",
         4: "Dayot Upamecano",         5: "William Saliba",
         6: "Théo Hernandez",          7: "Aurélien Tchouaméni",
         8: "Eduardo Camavinga",       9: "N'Golo Kanté",
        10: "Antoine Griezmann",      11: "Ousmane Dembélé",
        12: "Kylian Mbappé",          13: "Foto de Equipo - Selección Francia",
        14: "Marcus Thuram",          15: "Bradley Barcola",
        16: "Warren Zaïre-Emery",     17: "Benjamin Pavard",
        18: "Adrien Rabiot",          19: "Randal Kolo Muani",
        20: "Brice Samba",
    },
    "ESP": {
         1: "Escudo España (Brillante)",
         2: "Unai Simón",              3: "Dani Carvajal",
         4: "Robin Le Normand",        5: "Aymeric Laporte",
         6: "Marc Cucurella",          7: "Rodri",
         8: "Pedri",                   9: "Fabián Ruiz",
        10: "Dani Olmo",              11: "Lamine Yamal",
        12: "Nico Williams",          13: "Foto de Equipo - Selección España",
        14: "Álvaro Morata",          15: "Alejandro Grimaldo",
        16: "Martin Zubimendi",       17: "Mikel Oyarzabal",
        18: "Ferran Torres",          19: "Pau Cubarsí",
        20: "David Raya",
    },
    "URU": {
         1: "Escudo Uruguay (Brillante)",
         2: "Sergio Rochet",           3: "Nahitan Nández",
         4: "Ronald Araújo",           5: "José María Giménez",
         6: "Mathías Olivera",         7: "Federico Valverde",
         8: "Manuel Ugarte",           9: "Nicolás de la Cruz",
        10: "Giorgian de Arrascaeta", 11: "Facundo Pellistri",
        12: "Darwin Núñez",           13: "Foto de Equipo - Selección Uruguay",
        14: "Maximiliano Araújo",     15: "Brian Rodríguez",
        16: "Rodrigo Bentancur",      17: "Sebastián Cáceres",
        18: "Matías Viña",            19: "Luciano Rodríguez",
        20: "Santiago Mele",
    },
}


def get_name(code: str, pos: int) -> str:
    """Devuelve el nombre para (país, posición)."""
    country_name = COUNTRY_NAMES[code]
    if code in KNOWN:
        return KNOWN[code][pos]
    # Auto-generado para los 43 países restantes
    if pos == 1:
        return f"Escudo {country_name} (Brillante)"
    if pos == 13:
        return f"Foto de Equipo - Selección {country_name}"
    return f"Jugador {pos} de {country_name}"


def build_catalog() -> list[dict]:
    catalog = []

    # ── 1. Ítem de apertura ──────────────────────────────────────
    catalog.append({
        "code": "00",
        "section": "Apertura",
        "player_name": None,
        "description": "Logo Panini / Trofeo FIFA (Brillante)",
        "is_special": True,
    })

    # ── 2. Especiales FWC (FWC1 - FWC19) ───────────────────────
    for n in range(1, 20):          # 1 a 19 inclusive → 19 figuritas
        catalog.append({
            "code": f"FWC{n}",
            "section": "Especiales FWC",
            "player_name": None,
            "description": f"Especial Torneo FWC {n}",
            "is_special": True,
        })

    # ── 3. Bloque de selecciones (48 × 20 = 960) ────────────────
    for code in COUNTRIES:
        country_name = COUNTRY_NAMES[code]
        for pos in range(1, 21):    # 1 a 20 inclusive → 20 figuritas
            name = get_name(code, pos)
            is_escudo = (pos == 1)
            is_foto   = (pos == 13)
            catalog.append({
                "code": f"{code}{pos}",
                "section": country_name,
                "player_name": None if (is_escudo or is_foto) else name,
                "description": name if (is_escudo or is_foto) else None,
                "is_special": is_escudo,
            })

    return catalog


# ── Ejecución directa ────────────────────────────────────────────
def run_seed():
    catalog = build_catalog()
    total = len(catalog)

    if total != 980:
        raise ValueError(
            f"ERROR de conteo: se generaron {total} figuritas, se esperan 980.\n"
            f"  Apertura : 1\n"
            f"  FWC      : 19\n"
            f"  Países   : 48 × 20 = 960\n"
            f"  Total    : 980"
        )

    db = SessionLocal()
    try:
        from app.models.sticker import Sticker
        from app.models.inventory import UserSticker

        existing = db.query(Sticker).count()
        if existing > 0:
            print(f"Limpiando {existing} figuritas y su inventario asociado...")
            db.query(UserSticker).delete()
            db.query(Sticker).delete()
            db.commit()

        stickers = [
            Sticker(
                code=s["code"],
                section=s["section"],
                player_name=s.get("player_name"),
                description=s.get("description"),
                is_special=s.get("is_special", False),
            )
            for s in catalog
        ]
        db.add_all(stickers)
        db.commit()

        inserted = db.query(Sticker).count()
        if inserted != 980:
            raise AssertionError(f"Se insertaron {inserted} registros, se esperaban 980.")

        print(f"\n{'='*45}")
        print(f"  SEED EXITOSO: {inserted} figuritas cargadas.")
        print(f"  Apertura : 1  |  FWC : 19  |  Países : 960")
        print(f"  Total    : {inserted} / 980")
        print(f"{'='*45}\n")

    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
