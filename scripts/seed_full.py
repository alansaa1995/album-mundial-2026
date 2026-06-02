"""
Catálogo completo — 980 figuritas del álbum oficial Panini Mundial 2026.
Estructura por equipo: [COD]1=Escudo · [COD]2=Foto equipo · [COD]3-19=Jugadores

Ejecutar desde la raíz del proyecto:
    python scripts/seed_full.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import SessionLocal, engine, Base
import app.models  # noqa: F401

Base.metadata.create_all(bind=engine)

# ─────────────────────────────────────────────────────────────────
#  SECCIONES ESPECIALES
# ─────────────────────────────────────────────────────────────────

FWC_STICKERS = [
    # Presentación del torneo — FWC1-FWC20
    ("FWC1",  "FIFA World Cup 2026", None, "Portada oficial del álbum",                  True),
    ("FWC2",  "FIFA World Cup 2026", None, "El trofeo FIFA World Cup",                    True),
    ("FWC3",  "FIFA World Cup 2026", None, "Mapa de sedes — USA · Canada · Mexico",       True),
    ("FWC4",  "FIFA World Cup 2026", None, "Historia del Mundial (1930-2022)",             False),
    ("FWC5",  "FIFA World Cup 2026", None, "Campeones históricos",                         False),
    ("FWC6",  "FIFA World Cup 2026", None, "Goleadores históricos del torneo",             False),
    ("FWC7",  "FIFA World Cup 2026", None, "Grupo A — tabla",                              False),
    ("FWC8",  "FIFA World Cup 2026", None, "Grupo B — tabla",                              False),
    ("FWC9",  "FIFA World Cup 2026", None, "Grupo C — tabla",                              False),
    ("FWC10", "FIFA World Cup 2026", None, "Grupo D — tabla",                              False),
    ("FWC11", "FIFA World Cup 2026", None, "Grupo E — tabla",                              False),
    ("FWC12", "FIFA World Cup 2026", None, "Grupo F — tabla",                              False),
    ("FWC13", "FIFA World Cup 2026", None, "Grupo G — tabla",                              False),
    ("FWC14", "FIFA World Cup 2026", None, "Grupo H — tabla",                              False),
    ("FWC15", "FIFA World Cup 2026", None, "Grupo I — tabla",                              False),
    ("FWC16", "FIFA World Cup 2026", None, "Grupo J — tabla",                              False),
    ("FWC17", "FIFA World Cup 2026", None, "Grupo K — tabla",                              False),
    ("FWC18", "FIFA World Cup 2026", None, "Grupo L — tabla",                              False),
    ("FWC19", "FIFA World Cup 2026", None, "Estadísticas 48 equipos",                      False),
    ("FWC20", "FIFA World Cup 2026", None, "Presentación oficial FIFA",                    True),
]

TROPHY_STICKERS = [
    # Historia y trofeo — TRF1-TRF10
    ("TRF1",  "Trofeo & Historia", None, "El trofeo — vista frontal",     True),
    ("TRF2",  "Trofeo & Historia", None, "El trofeo — detalle dorado",    True),
    ("TRF3",  "Trofeo & Historia", None, "Brasil 1950 — Uruguay campeón", False),
    ("TRF4",  "Trofeo & Historia", None, "Italia 1934 y 1938",            False),
    ("TRF5",  "Trofeo & Historia", None, "Brasil 1970 — El mejor equipo", False),
    ("TRF6",  "Trofeo & Historia", None, "Argentina 1978 y 1986",         False),
    ("TRF7",  "Trofeo & Historia", None, "Francia 1998 — Zidane",         False),
    ("TRF8",  "Trofeo & Historia", None, "Brasil 2002 — El Fenómeno",     False),
    ("TRF9",  "Trofeo & Historia", None, "Argentina 2022 — Messi eterno", True),
    ("TRF10", "Trofeo & Historia", None, "Ganadores de la Copa del Mundo", False),
]

MASCOT_STICKERS = [
    # Mascota oficial — MAS1-MAS5
    ("MAS1", "Mascota", None, "Mascota oficial — presentación",   True),
    ("MAS2", "Mascota", None, "Mascota con el trofeo",            True),
    ("MAS3", "Mascota", None, "Mascota — USA",                    False),
    ("MAS4", "Mascota", None, "Mascota — Canada",                 False),
    ("MAS5", "Mascota", None, "Mascota — Mexico",                 False),
]

STADIUM_STICKERS = [
    # 16 sedes del Mundial — EST1-EST16
    ("EST1",  "Estadios", None, "MetLife Stadium · East Rutherford, NJ (88.491)",   True),
    ("EST2",  "Estadios", None, "AT&T Stadium · Arlington, TX (80.000)",             True),
    ("EST3",  "Estadios", None, "SoFi Stadium · Inglewood, CA (70.240)",             True),
    ("EST4",  "Estadios", None, "Hard Rock Stadium · Miami Gardens, FL (64.767)",    True),
    ("EST5",  "Estadios", None, "Levi's Stadium · Santa Clara, CA (68.500)",         True),
    ("EST6",  "Estadios", None, "Arrowhead Stadium · Kansas City, MO (76.416)",      True),
    ("EST7",  "Estadios", None, "Lincoln Financial Field · Filadelfia, PA (69.796)", True),
    ("EST8",  "Estadios", None, "Gillette Stadium · Foxborough, MA (65.878)",        True),
    ("EST9",  "Estadios", None, "Empower Field · Denver, CO (76.125)",               True),
    ("EST10", "Estadios", None, "Lumen Field · Seattle, WA (69.000)",                True),
    ("EST11", "Estadios", None, "Estadio Azteca · Ciudad de México (87.523)",        True),
    ("EST12", "Estadios", None, "Estadio AKRON · Guadalajara (49.850)",              True),
    ("EST13", "Estadios", None, "Estadio BBVA · Monterrey (53.500)",                 True),
    ("EST14", "Estadios", None, "BC Place · Vancouver (54.500)",                     True),
    ("EST15", "Estadios", None, "BMO Field · Toronto (45.736)",                      True),
    ("EST16", "Estadios", None, "Stade Olympique · Montréal (61.004)",               True),
]

IDOL_STICKERS = [
    # Estrellas del torneo — IDL1-IDL17 (foil especial)
    ("IDL1",  "Ídolos", "Lionel Messi",        "Argentina — El mejor de todos",   True),
    ("IDL2",  "Ídolos", "Kylian Mbappé",       "Francia — La nueva leyenda",      True),
    ("IDL3",  "Ídolos", "Vinicius Jr.",         "Brasil — El rey del dribbling",   True),
    ("IDL4",  "Ídolos", "Erling Haaland",      "Noruega — La máquina de goles",   True),
    ("IDL5",  "Ídolos", "Jude Bellingham",     "Inglaterra — El mediocampista total", True),
    ("IDL6",  "Ídolos", "Pedri",               "España — El futuro del fútbol",   True),
    ("IDL7",  "Ídolos", "Lamine Yamal",        "España — La joya más joven",      True),
    ("IDL8",  "Ídolos", "Rodri",               "España — Balón de Oro 2024",      True),
    ("IDL9",  "Ídolos", "Florian Wirtz",       "Alemania — La estrella del Bayer", True),
    ("IDL10", "Ídolos", "Federico Valverde",   "Uruguay — El motor del Real Madrid", True),
    ("IDL11", "Ídolos", "Mohamed Salah",       "Egipto — El faraón del fútbol",   True),
    ("IDL12", "Ídolos", "Victor Osimhen",      "Nigeria — La pantera de Nápoles", True),
    ("IDL13", "Ídolos", "Son Heung-min",       "Corea del Sur — El capitán",      True),
    ("IDL14", "Ídolos", "Moisés Caicedo",      "Ecuador — El guerrero del Chelsea", True),
    ("IDL15", "Ídolos", "Jonathan David",      "Canadá — El goleador de Lille",   True),
    ("IDL16", "Ídolos", "Takefusa Kubo",       "Japón — La maravilla española",   True),
    ("IDL17", "Ídolos", "Hakim Ziyech",        "Marruecos — El mago",             True),
]

# ─────────────────────────────────────────────────────────────────
#  EQUIPOS — 48 selecciones × 19 figuritas = 912
#  Estructura: (sección, [17 jugadores])
#  Figurita 1 = Escudo (foil), 2 = Foto equipo, 3-19 = Jugadores
# ─────────────────────────────────────────────────────────────────

TEAMS = {
    # ═══════════════════════════════════════════
    #  CONMEBOL (6)
    # ═══════════════════════════════════════════
    "ARG": ("Argentina", [
        "Lionel Messi", "Emiliano Martínez", "Nahuel Molina",
        "Cristian Romero", "Nicolás Otamendi", "Marcos Acuña",
        "Rodrigo De Paul", "Leandro Paredes", "Alexis Mac Allister",
        "Enzo Fernández", "Thiago Almada", "Valentín Carboni",
        "Julián Álvarez", "Lautaro Martínez", "Paulo Dybala",
        "Guido Rodríguez", "Germán Pezzella",
    ]),
    "BRA": ("Brasil", [
        "Alisson Becker", "Danilo", "Éder Militão",
        "Marquinhos", "Renan Lodi", "Casemiro",
        "Bruno Guimarães", "Lucas Paquetá", "Raphinha",
        "Vinicius Jr.", "Rodrygo", "Endrick",
        "Gabriel Martinelli", "Richarlison", "Gabriel Jesus",
        "Antony", "Guilherme Arana",
    ]),
    "URU": ("Uruguay", [
        "Sergio Rochet", "Nahuel Nández", "José María Giménez",
        "Ronald Araújo", "Mathías Olivera", "Rodrigo Bentancur",
        "Manuel Ugarte", "Matías Vecino", "Federico Valverde",
        "Giorgian De Arrascaeta", "Facundo Pellistri", "Darwin Núñez",
        "Agustín Canobbio", "Nicolás De La Cruz", "Brian Rodríguez",
        "Maxi Gómez", "Sebastián Cáceres",
    ]),
    "COL": ("Colombia", [
        "Camilo Vargas", "Daniel Muñoz", "Davinson Sánchez",
        "Yerry Mina", "Johan Mojica", "Wilmar Barrios",
        "Mateus Uribe", "Richard Ríos", "James Rodríguez",
        "Cucho Hernández", "Luis Díaz", "Rafael Santos Borré",
        "Miguel Ángel Borja", "Jhon Arias", "Jhon Córdoba",
        "Lerma", "Jhon Lucumí",
    ]),
    "ECU": ("Ecuador", [
        "Hernán Galíndez", "Ángelo Preciado", "Piero Hincapié",
        "Félix Torres", "Pervis Estupiñán", "Moisés Caicedo",
        "José Cifuentes", "Carlos Gruezo", "Enner Valencia",
        "Jhegson Méndez", "Gonzalo Plata", "Jeremy Sarmiento",
        "Michael Estrada", "Djorkaeff Reasco", "Kevin Rodríguez",
        "Alan Minda", "Byron Castillo",
    ]),
    "VEN": ("Venezuela", [
        "Wuilker Faríñez", "Jon Aramburu", "Nahuel Ferraresi",
        "Alexander González", "Miguel Navarro", "Jefferson Savarino",
        "Yangel Herrera", "Tomás Rincón", "Darwin Machís",
        "Eduard Bello", "Jhon Murillo", "Rómulo Otero",
        "Salomón Rondón", "Yeferson Soteldo", "Sergio Córdova",
        "Jan Hurtado", "Adrián Martínez",
    ]),

    # ═══════════════════════════════════════════
    #  CONCACAF (6)
    # ═══════════════════════════════════════════
    "USA": ("Estados Unidos", [
        "Matt Turner", "Sergiño Dest", "Chris Richards",
        "Walker Zimmermann", "Antonee Robinson", "Tyler Adams",
        "Yunus Musah", "Weston McKennie", "Christian Pulisic",
        "Giovanni Reyna", "Tim Weah", "Ricardo Pepi",
        "Josh Sargent", "Folarin Balogun", "Brenden Aaronson",
        "Joe Scally", "Miles Robinson",
    ]),
    "CAN": ("Canadá", [
        "Milan Borjan", "Alistair Johnston", "Kamal Miller",
        "Moise Bombito", "Alphonso Davies", "Stephen Eustáquio",
        "Ismael Koné", "Jonathan Osorio", "Jonathan David",
        "Tajon Buchanan", "Liam Millar", "Cyle Larin",
        "Richie Laryea", "Theo Bair", "Derek Cornelius",
        "Samuel Piette", "Jayden Nelson",
    ]),
    "MEX": ("México", [
        "Guillermo Ochoa", "Jorge Sánchez", "César Montes",
        "Johan Vásquez", "Jesús Gallardo", "Edson Álvarez",
        "Héctor Herrera", "Luis Romo", "Hirving Lozano",
        "Alexis Vega", "Orbelín Pineda", "Santiago Giménez",
        "Raúl Jiménez", "Roberto Alvarado", "Carlos Antuna",
        "Kevin Álvarez", "Chima Laryea",
    ]),
    "PAN": ("Panamá", [
        "Luis Mejía", "Óscar Murillo", "Fidel Escobar",
        "Eric Davis", "Michael Murillo", "Adalberto Carrasquilla",
        "Édgar Bárcenas", "Cecilio Waterman", "Roderick Miller",
        "Harold Cummings", "Alberto Quintero", "Rolando Blackburn",
        "Ismael Díaz", "Freddy Góndola", "Aníbal Godoy",
        "José Luis Rodríguez", "Armando Cooper",
    ]),
    "CRC": ("Costa Rica", [
        "Keylor Navas", "Keysher Fuller", "Francisco Calvo",
        "Bryan Oviedo", "Rónald Matarrita", "Celso Borges",
        "Yeltsin Tejeda", "David Guzmán", "Joel Campbell",
        "Johan Venegas", "Manfred Ugalde", "Anthony Contreras",
        "Alonso Martínez", "Daniel Chacón", "Douglas López",
        "Orlando Galo", "Aarón Suárez",
    ]),
    "HON": ("Honduras", [
        "Luis López", "Denil Maldonado", "Marcelo Pereira",
        "Jonathan Rougier", "Kervin Arriaga", "Deybi Flores",
        "Edwin Rodríguez", "Romell Quioto", "Michaell Chirinos",
        "Alberth Elis", "Jerry Bengtson", "Antony Lozano",
        "Jorge Álvarez", "José García", "Brayan Moya",
        "Diego Rodríguez", "Rigoberto Rivas",
    ]),

    # ═══════════════════════════════════════════
    #  UEFA (16)
    # ═══════════════════════════════════════════
    "GER": ("Alemania", [
        "Manuel Neuer", "Joshua Kimmich", "Antonio Rüdiger",
        "Niklas Süle", "David Raum", "İlkay Gündoğan",
        "Leon Goretzka", "Jamal Musiala", "Florian Wirtz",
        "Leroy Sané", "Kai Havertz", "Serge Gnabry",
        "Jonas Hofmann", "Nico Schlotterbeck", "Chris Füllkrug",
        "Benjamin Henrichs", "Thomas Müller",
    ]),
    "ESP": ("España", [
        "Unai Simón", "Dani Carvajal", "Aymeric Laporte",
        "Robin Le Normand", "Alejandro Grimaldo", "Rodri",
        "Pedri", "Gavi", "Lamine Yamal",
        "Nico Williams", "Álvaro Morata", "Fermín López",
        "Fabián Ruiz", "Mikel Merino", "Martín Zubimendi",
        "Dani Olmo", "Yeremy Pino",
    ]),
    "FRA": ("Francia", [
        "Mike Maignan", "Jules Koundé", "Dayot Upamecano",
        "William Saliba", "Théo Hernández", "Aurélien Tchouaméni",
        "Eduardo Camavinga", "Youssouf Fofana", "Antoine Griezmann",
        "Kylian Mbappé", "Ousmane Dembélé", "Marcus Thuram",
        "Randal Kolo Muani", "Adrien Rabiot", "Ibrahima Konaté",
        "Benjamin Pavard", "Christopher Nkunku",
    ]),
    "ENG": ("Inglaterra", [
        "Jordan Pickford", "Kyle Walker", "John Stones",
        "Levi Colwill", "Luke Shaw", "Declan Rice",
        "Jude Bellingham", "Phil Foden", "Bukayo Saka",
        "Harry Kane", "Marcus Rashford", "Cole Palmer",
        "Trent Alexander-Arnold", "Kobbie Mainoo", "Ollie Watkins",
        "Jarrod Bowen", "Anthony Gordon",
    ]),
    "POR": ("Portugal", [
        "Diogo Costa", "João Cancelo", "Rúben Dias",
        "António Silva", "Nuno Mendes", "Vitinha",
        "Bernardo Silva", "Bruno Fernandes", "João Félix",
        "Cristiano Ronaldo", "Rafael Leão", "Pedro Neto",
        "Francisco Conceição", "Otávio", "Diogo Jota",
        "Gonçalo Inácio", "Rúben Neves",
    ]),
    "NED": ("Países Bajos", [
        "Mark Flekken", "Denzel Dumfries", "Virgil van Dijk",
        "Stefan de Vrij", "Nathan Aké", "Frenkie de Jong",
        "Ryan Gravenberch", "Tijjani Reijnders", "Xavi Simons",
        "Cody Gakpo", "Donyell Malen", "Steven Bergwijn",
        "Micky van de Ven", "Brian Brobbey", "Wout Weghorst",
        "Lutsharel Geertruida", "Teun Koopmeiners",
    ]),
    "SUI": ("Suiza", [
        "Yann Sommer", "Silvan Widmer", "Manuel Akanji",
        "Fabian Schär", "Ricardo Rodríguez", "Granit Xhaka",
        "Remo Freuler", "Michel Aebischer", "Breel Embolo",
        "Noah Okafor", "Zeki Amdouni", "Dan Ndoye",
        "Ardon Jashari", "Fabian Rieder", "Ruben Vargas",
        "Xherdan Shaqiri", "Cedric Zesiger",
    ]),
    "AUT": ("Austria", [
        "Patrick Pentz", "Stefan Posch", "Kevin Danso",
        "Maximilian Wöber", "Phillipp Mwene", "Nicolas Seiwald",
        "Konrad Laimer", "Florian Grillitsch", "Christoph Baumgartner",
        "Marcel Sabitzer", "David Alaba", "Michael Gregoritsch",
        "Marko Arnautović", "Florian Kainz", "Patrick Wimmer",
        "Sasa Kalajdzic", "Andreas Weimann",
    ]),
    "DEN": ("Dinamarca", [
        "Oliver Christensen", "Joakim Maehle", "Joachim Andersen",
        "Victor Nelsson", "Andreas Christensen", "Christian Eriksen",
        "Pierre-Emile Højbjerg", "Thomas Delaney", "Mikkel Damsgaard",
        "Rasmus Hojlund", "Andreas Skov Olsen", "Jesper Lindstrøm",
        "Simon Kjær", "Alexander Bah", "Christian Nørgaard",
        "Yussuf Poulsen", "Robert Skov",
    ]),
    "SCO": ("Escocia", [
        "Angus Gunn", "Anthony Ralston", "Grant Hanley",
        "Scott McKenna", "Andy Robertson", "John McGinn",
        "Billy Gilmour", "Callum McGregor", "Ryan Christie",
        "Che Adams", "Lyndon Dykes", "Stuart Armstrong",
        "Lawrence Shankland", "Scott McTominay", "Nathan Patterson",
        "Ryan Jack", "Kevin Nisbet",
    ]),
    "SRB": ("Serbia", [
        "Vanja Milinković-Savić", "Strahinja Pavlović", "Nikola Milenković",
        "Srđan Babić", "Miloš Veljković", "Luka Ilić",
        "Sergej Milinković-Savić", "Nemanja Gudelj", "Filip Kostić",
        "Aleksandar Mitrović", "Dušan Vlahović", "Dušan Tadić",
        "Andrija Živković", "Saša Lukić", "Darko Lazović",
        "Ivan Ilić", "Marko Grujić",
    ]),
    "CRO": ("Croacia", [
        "Dominik Livaković", "Josip Stanišić", "Duje Ćaleta-Car",
        "Joško Gvardiol", "Borna Sosa", "Mateo Kovačić",
        "Luka Modrić", "Marcelo Brozović", "Ivan Perišić",
        "Andrej Kramarić", "Bruno Petković", "Mario Pašalić",
        "Lovro Majer", "Martin Erlic", "Nikola Vlašić",
        "Josip Sutalo", "Luka Ivanušec",
    ]),
    "TUR": ("Turquía", [
        "Mert Günok", "Zeki Çelik", "Samet Akaydin",
        "Kaan Ayhan", "Ferdi Kadıoğlu", "Hakan Çalhanoğlu",
        "Salih Özcan", "Orkun Kökçü", "Arda Güler",
        "Kerem Aktürkoğlu", "Barış Alper Yılmaz", "Yusuf Yazıcı",
        "Okay Yokuşlu", "Abdülkerim Bardakcı", "Yunus Akgün",
        "Cenk Tosun", "Umut Bozok",
    ]),
    "SVK": ("Eslovaquia", [
        "Marek Rodák", "Peter Pekarík", "Milan Škriniar",
        "Denis Vavro", "Tomáš Hubočan", "Stanislav Lobotka",
        "Ondrej Duda", "Juraj Kucka", "Dávid Hancko",
        "Ivan Schranz", "Róbert Boženík", "Lukáš Haraslín",
        "Dávid Strelec", "Tomáš Suslov", "Matúš Bero",
        "Adam Obert", "Dominik Hollý",
    ]),
    "HUN": ("Hungría", [
        "Péter Gulácsi", "Ádám Fiola", "Willi Orbán",
        "Attila Szalai", "Zsolt Nagy", "Ádám Nagy",
        "Dominik Szoboszlai", "Martin Ádám", "Roland Sallai",
        "Barnabás Varga", "Kevin Csoboth", "Loïc Négo",
        "Bendegúz Bolla", "László Kleinheisler", "Miha Blanco",
        "Callum Styles", "Dániel Gazdag",
    ]),
    "NOR": ("Noruega", [
        "Ørjan Nyland", "Omar Elabdellaoui", "Andreas Hanche-Olsen",
        "Leo Ostigard", "Birger Meling", "Martin Ødegaard",
        "Sander Berge", "Patrick Berg", "Mohamed Elyounoussi",
        "Erling Haaland", "Alexander Sørloth", "Ola Solbakken",
        "Kristian Thorstvedt", "Fredrik Aursnes", "Jørgen Strand Larsen",
        "Tobias Børkeeiet", "Mathias Normann",
    ]),

    # ═══════════════════════════════════════════
    #  CAF (10)
    # ═══════════════════════════════════════════
    "MAR": ("Marruecos", [
        "Yassine Bounou", "Achraf Hakimi", "Nayef Aguerd",
        "Romain Saïss", "Noussair Mazraoui", "Sofyan Amrabat",
        "Selim Amallah", "Azzedine Ounahi", "Hakim Ziyech",
        "Youssef En-Nesyri", "Sofiane Boufal", "Abdelhamid Sabiri",
        "Ilias Chair", "Zakaria Aboukhlal", "Tarik Tissoudali",
        "Adam Aznou", "Anass Zaroury",
    ]),
    "EGY": ("Egipto", [
        "Mohamed El-Shenawy", "Ahmed Hegazi", "Ahmed El-Fotouh",
        "Karim Hafez", "Omar Kamal", "Hamdi Fathi",
        "Ahmed Sayed Zizou", "Emam Ashour", "Amr El Sulaya",
        "Mohamed Salah", "Omar Marmoush", "Mostafa Mohamed",
        "Ramadan Sobhi", "Taher Mohamed Taher", "Ahmed Abdelkader",
        "Mohamed Abdelmonem", "Ahmed Rayan",
    ]),
    "SEN": ("Senegal", [
        "Édouard Mendy", "Bouna Sarr", "Kalidou Koulibaly",
        "Abdou Diallo", "Ismail Jakobs", "Idrissa Gueye",
        "Pape Matar Sarr", "Nampalys Mendy", "Sadio Mané",
        "Ismaila Sarr", "Habib Diallo", "Nicolas Jackson",
        "Iliman Ndiaye", "Lamine Camara", "Krepin Diatta",
        "Pathé Ciss", "Dion Lopy",
    ]),
    "NGA": ("Nigeria", [
        "Francis Uzoho", "Calvin Bassey", "Leon Balogun",
        "William Troost-Ekong", "Zaidu Sanusi", "Joe Aribo",
        "Alex Iwobi", "Wilfred Ndidi", "Victor Osimhen",
        "Emmanuel Dennis", "Kelechi Iheanacho", "Moses Simon",
        "Samuel Chukwueze", "Ola Aina", "Terem Moffi",
        "Raphael Onyedika", "Cyriel Dessers",
    ]),
    "RSA": ("Sudáfrica", [
        "Ronwen Williams", "Reeve Frosler", "Rushine De Reuck",
        "Siyanda Xulu", "Terrence Mashego", "Teboho Mokoena",
        "Ethan Brooks", "Themba Zwane", "Percy Tau",
        "Lyle Foster", "Bongokuhle Hlongwane", "Keagan Dolly",
        "Jody February", "Elias Mokwana", "Fagrie Lakay",
        "Yusuf Maart", "Siyethemba Sithebe",
    ]),
    "CIV": ("Costa de Marfil", [
        "Badra Ali Sangaré", "Serge Aurier", "Odilon Kossounou",
        "Simon Deli", "Wilfried Singo", "Franck Kessié",
        "Ibrahim Sangaré", "Seko Fofana", "Amad Diallo",
        "Sébastien Haller", "Wilfried Zaha", "Maxwel Cornet",
        "Jean-Philippe Gbamin", "Nicolas Pépé", "Christian Kouamé",
        "Simon Adingra", "Gradel",
    ]),
    "CMR": ("Camerún", [
        "André Onana", "Collins Fai", "Jean-Charles Castelletto",
        "Nouhou Tolo", "Harold Moukoudi", "Samuel Oum Gouet",
        "Martin Hongla", "Pierre Kunde", "Vincent Aboubakar",
        "Karl Toko Ekambi", "Jean-Pierre Nsame", "Bryan Mbeumo",
        "Olivier Ntcham", "Jeando Fuchs", "Stéphan Bahoken",
        "Moumi Ngamaleu", "Léandre Tawamba",
    ]),
    "MLI": ("Mali", [
        "Ibrahim Mounkoro", "Hamari Traoré", "Boubacar Kouyaté",
        "Falaye Sacko", "Molla Wagué", "Amadou Haidara",
        "Yves Bissouma", "Cheick Doucouré", "El Bilal Touré",
        "Ibrahima Koné", "Lassine Sinayoko", "Sékou Koïta",
        "Mamadou Doumbia", "Adama Noss Coulibaly", "Kalifa Coulibaly",
        "Mamadou Coulibaly", "Kamory Doumbia",
    ]),
    "COD": ("Rep. Dem. Congo", [
        "Joris Kayembe", "Marcel Tisserand", "Arthur Masuaku",
        "Chancel Mbemba", "Theo Bongonda", "Cédric Bakambu",
        "Meschak Elia", "Silas Mvumpa", "Fiston Mayele",
        "Mbala Nzola", "Jonathan Bolingi", "Yannick Bolasie",
        "Nathan Ngandu", "Makengo", "Jordane Kwateng",
        "Emmanuel Lebo", "Denis Bouanga",
    ]),
    "TUN": ("Túnez", [
        "Aymen Dahmen", "Ali Maaloul", "Yassine Meriah",
        "Montassar Talbi", "Mohamed Drager", "Aïssa Laïdouni",
        "Ellyes Skhiri", "Hannibal Mejbri", "Wahbi Khazri",
        "Naïm Sliti", "Issam Jebali", "Seifeddine Jaziri",
        "Youssef Msakni", "Mohamed Ali Ben Romdhane", "Maher Hannachi",
        "Dylan Bronn", "Ahmed Khalil",
    ]),

    # ═══════════════════════════════════════════
    #  AFC (9)
    # ═══════════════════════════════════════════
    "JPN": ("Japón", [
        "Shuichi Gonda", "Yukinari Sugawara", "Ko Itakura",
        "Takehiro Tomiyasu", "Yuto Nagatomo", "Wataru Endo",
        "Hidemasa Morita", "Takumi Minamino", "Takefusa Kubo",
        "Kaoru Mitoma", "Ayase Ueda", "Ritsu Doan",
        "Daichi Kamada", "Junya Ito", "Daizen Maeda",
        "Shuto Machino", "Ao Tanaka",
    ]),
    "KOR": ("Corea del Sur", [
        "Kim Seung-gyu", "Kim Moon-hwan", "Kim Min-jae",
        "Kim Young-gwon", "Kim Jin-su", "Jung Woo-young",
        "Lee Jae-sung", "Hwang In-beom", "Son Heung-min",
        "Hwang Hee-chan", "Cho Gue-sung", "Lee Kang-in",
        "Na Sang-ho", "Oh Hyeon-gyu", "Kwon Chang-hoon",
        "Paik Seung-ho", "Bae Jun-ho",
    ]),
    "IRN": ("Irán", [
        "Alireza Beiranvand", "Sadegh Moharrami", "Majid Hosseini",
        "Morteza Pouraliganji", "Ehsan Hajsafi", "Saeid Ezatolahi",
        "Ahmad Nourollahi", "Ali Karimi", "Mehdi Taremi",
        "Sardar Azmoun", "Ali Gholizadeh", "Vahid Amiri",
        "Allahyar Sayyadmanesh", "Rouzbeh Cheshmi", "Shojae Khalilzadeh",
        "Milad Mohammadi", "Ahmad Abedzadeh",
    ]),
    "AUS": ("Australia", [
        "Mat Ryan", "Miloš Degenek", "Harry Souttar",
        "Kye Rowles", "Aziz Behich", "Jackson Irvine",
        "Aaron Mooy", "Riley McGree", "Mathew Leckie",
        "Martin Boyle", "Mitchell Duke", "Craig Goodwin",
        "Garang Kuol", "Nathaniel Atkinson", "Bailey Wright",
        "Cameron Burgess", "Marco Tilio",
    ]),
    "KSA": ("Arabia Saudita", [
        "Mohammed Al-Owais", "Sultan Al-Ghanam", "Ali Al-Bulayhi",
        "Abdulelah Al-Amri", "Yasir Al-Shahrani", "Salman Al-Faraj",
        "Mohammed Al-Khanboushi", "Sami Al-Najei", "Salem Al-Dawsari",
        "Firas Al-Buraikan", "Mohammed Al-Burayk", "Hattan Bahebri",
        "Abdullah Al-Hamdan", "Nasser Al-Dawsari", "Nawaf Al-Abed",
        "Riyadh Sharahili", "Turki Al-Ammar",
    ]),
    "UZB": ("Uzbekistán", [
        "Utkir Yusupov", "Anzur Ismailov", "Sherzod Nishonov",
        "Khurshid Tursunov", "Otabek Shukurov", "Oston Urunov",
        "Dostonbek Khamdamov", "Jaloliddin Masharipov", "Eldor Shomurodov",
        "Abbosbek Fayzullaev", "Jasurbek Yakhshiboev", "Jamshid Iskanderov",
        "Khojimat Erkinov", "Sarvarbek Abdullaev", "Shamsiddin Shomurodov",
        "Akbar Tursunov", "Temur Djurayev",
    ]),
    "JOR": ("Jordania", [
        "Yazeed Abo Laila", "Abdallah Nasib", "Ahmad Al-Salhe",
        "Ahmad Abu Eid", "Baha Abdulrahman", "Yazan Al-Naimat",
        "Musa Suleiman", "Mahmoud Al-Mardi", "Moussa Al-Taamari",
        "Ahmad Hayel Saif", "Shadi Abu Hashhash", "Salem Al-Amarat",
        "Anas Bani Yaseen", "Ali Olwan", "Obada Al-Rashdan",
        "Mohammad Al-Rayyan", "Hamza Al-Dardour",
    ]),
    "IRQ": ("Irak", [
        "Jalal Hassan", "Ali Adnan", "Saad Natiq",
        "Muhammad Qasim", "Rebin Sulaka", "Amjad Attwan",
        "Bashar Resan", "Osama Rashid", "Aymen Hussein",
        "Ahmed Yasin", "Mohanad Abdulraheem", "Humam Tariq",
        "Diya Saber", "Safaa Hadi", "Hussain Ali",
        "Ibrahim Bayesh", "Emad Mohamed",
    ]),
    "QAT": ("Catar", [
        "Meshaal Barsham", "Pedro Miguel", "Bassam Al-Rawi",
        "Abdelkarim Hassan", "Boualem Khoukhi", "Karim Boudiaf",
        "Abdelaziz Hatem", "Hassan Al-Haydos", "Akram Afif",
        "Almoez Ali", "Mohammed Muntari", "Assim Madibo",
        "Jassem Gaber", "Ismail Mohamad", "Khalid Muneer",
        "Ahmed Alaaeldin", "Tariq Salman",
    ]),

    # ═══════════════════════════════════════════
    #  OFC (1)
    # ═══════════════════════════════════════════
    "NZL": ("Nueva Zelanda", [
        "Stefan Marinovic", "Liberato Cacace", "Winston Reid",
        "Tommy Smith", "Tim Payne", "Clayton Lewis",
        "Joe Bell", "Elijah Just", "Chris Wood",
        "Oli Sail", "Marco Rojas", "Matthew Garbett",
        "Sarpreet Singh", "Ryan Thomas", "Matt Ridenton",
        "Storm Roux", "Callan Elliot",
    ]),
}


# ─────────────────────────────────────────────────────────────────
#  CONSTRUCCIÓN DEL CATÁLOGO COMPLETO
# ─────────────────────────────────────────────────────────────────

def build_catalog():
    catalog = []

    # Secciones especiales
    for code, section, player, desc, special in (
        FWC_STICKERS + TROPHY_STICKERS + MASCOT_STICKERS +
        STADIUM_STICKERS + IDOL_STICKERS
    ):
        catalog.append({
            "code": code, "section": section,
            "player_name": player, "description": desc,
            "is_special": special,
        })

    # Equipos
    for team_code, (section, players) in TEAMS.items():
        assert len(players) == 17, f"{team_code} tiene {len(players)} jugadores, se esperan 17"

        # Figurita 1: Escudo (foil)
        catalog.append({
            "code": f"{team_code}1", "section": section,
            "player_name": None,
            "description": f"Escudo {section} — Foil",
            "is_special": True,
        })
        # Figurita 2: Foto del equipo
        catalog.append({
            "code": f"{team_code}2", "section": section,
            "player_name": None,
            "description": f"Foto oficial — {section}",
            "is_special": False,
        })
        # Figuritas 3-19: Jugadores
        for i, player in enumerate(players, start=3):
            catalog.append({
                "code": f"{team_code}{i}", "section": section,
                "player_name": player,
                "description": None,
                "is_special": False,
            })

    return catalog


# ─────────────────────────────────────────────────────────────────
#  EJECUCIÓN
# ─────────────────────────────────────────────────────────────────

def run_seed():
    catalog = build_catalog()

    assert len(catalog) == 980, (
        f"ERROR: el catálogo tiene {len(catalog)} figuritas, se esperan 980.\n"
        f"  Especiales: {20+10+5+16+17} = 68\n"
        f"  Equipos:    {len(TEAMS)} × 19 = {len(TEAMS)*19}\n"
        f"  Total:      {68 + len(TEAMS)*19}"
    )

    db = SessionLocal()
    try:
        from app.models.sticker import Sticker

        existing = db.query(Sticker).count()
        if existing > 0:
            print(f"Limpiando {existing} figuritas existentes...")
            # Borrar primero el inventario (FK) antes de borrar figuritas
            from app.models.inventory import UserSticker
            db.query(UserSticker).delete()
            db.query(Sticker).delete()
            db.commit()

        stickers = [
            Sticker(
                code=s["code"].upper(),
                section=s["section"],
                player_name=s.get("player_name"),
                description=s.get("description"),
                is_special=s.get("is_special", False),
            )
            for s in catalog
        ]
        db.add_all(stickers)
        db.commit()

        # Resumen por sección
        from sqlalchemy import func
        resumen = (
            db.query(Sticker.section, func.count(Sticker.id))
            .group_by(Sticker.section)
            .order_by(func.count(Sticker.id).desc())
            .all()
        )
        print(f"\nSeed completado: {len(stickers)} figuritas cargadas.\n")
        print(f"{'Sección':<30} {'Figuritas':>9}")
        print("─" * 42)
        for section, count in resumen:
            print(f"{section:<30} {count:>9}")
        print("─" * 42)
        print(f"{'TOTAL':<30} {sum(c for _, c in resumen):>9}")

    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
