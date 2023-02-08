##### ENTITY RULER####################################################################
######################################################################################

lista_de_marcas_de_autos = [
    "audi",
    "baic",
    "bmw",
    "changan",
    "chery",
    "chevrolet",
    "chrysler",
    "citroen",
    "dodge",
    "ds",
    "ferrari",
    "fiat",
    "ford",
    "foton",
    "geely",
    "haval",
    "heibao",
    "honda",
    "hyundai",
    "isuzu",
    "jac",
    "jaguar",
    "jeep",
    "kia",
    "lexus",
    "lifan",
    "maserati",
    "mclaren",
    "mini",
    "mitsubishi",
    "nissan",
    "peugeot",
    "porsche",
    "ram",
    "renault",
    "saab",
    "seat",
    "shineray",
    "smart",
    "soueast",
    "ssangyong",
    "subaru",
    "suzuki",
    "swm",
    "toyota",
    "volkswagen",
    "volvo",
]

# Fuente https://www.acara.org.ar/guia-oficial-de-precios.php?tipo=AUTOS
marcas_autos = [
    {
        "label": "MARCA_AUTOMÓVIL",
        "pattern": [
            {"ORTH": "marca"},
            {"LOWER": {"IN": lista_de_marcas_de_autos}},
        ],
    },
    {
        "label": "MARCA_AUTOMÓVIL",
        "pattern": [{"ORTH": "marca"}, {"LOWER": "alfa"}, {"LOWER": "romeo"}],
    },
    {
        "label": "MARCA_AUTOMÓVIL",
        "pattern": [
            {"ORTH": "marca"},
            {"LOWER": "mercedes"},
            {"LOWER": "benz"},
        ],
    },
    {
        "label": "MARCA_AUTOMÓVIL",
        "pattern": [{"ORTH": "marca"}, {"LOWER": "land"}, {"LOWER": "rover"}],
    },
    {
        "label": "MARCA_AUTOMÓVIL",
        "pattern": [{"ORTH": "marca"}, {"LOWER": "great"}, {"LOWER": "wall"}],
    },
]

# Fuente del BCRA: http://www.bcra.gov.ar/pdfs/comytexord/b9195.pdf
bancos = [
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "columbia"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "bisel"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "entre"},
            {"LOWER": "ríos"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "icbc"}, {"LOWER": "argentina"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "citibank"}]},
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "masventas"}],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "rci"}, {"LOWER": "Banque"}]},
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "a.b.n."}, {"LOWER": "amro"}, {"LOWER": "bank"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "bbva"},
            {"LOWER": "banco"},
            {"LOWER": "francés"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "bank"},
            {"LOWER": "of"},
            {"LOWER": "america"},
            {"LOWER": "national"},
            {"LOWER": "association"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "bnp"}, {"LOWER": "paribas"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "the"},
            {"LOWER": "bank"},
            {"LOWER": "of"},
            {"LOWER": "tokyo"},
            {"ORTH": "-", "OP": "?"},
            {"LOWER": "mitsubishi"},
            {"LOWER": "Ufj"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": "ltd"},
            {"IS_PUNCT": True, "OP": "?"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "b"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": "i"},
            {"IS_PUNCT": True, "OP": "?"},
            {"LOWER": "creditanstalt"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "hsbc"},
            {"LOWER": "Bank"},
            {"LOWER": "argentina"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "j"},
            {"LOWER": "p"},
            {"LOWER": "Morgan"},
            {"LOWER": "Chase"},
            {"LOWER": "bank"},
            {"LOWER": "national"},
            {"LOWER": "association"},
            {"ORTH": "(", "OP": "?"},
            {"LOWER": "sucursal"},
            {"LOWER": "buenos"},
            {"LOWER": "Aires"},
            {"ORTH": ")", "OP": "?"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "american"},
            {"LOWER": "express"},
            {"LOWER": "bank"},
            {"LOWER": "ltd"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "M.B.A."},
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "inversiones"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "deutsche"}, {"LOWER": "bank"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "bacs"},
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "credito"},
            {"LOWER": "y"},
            {"LOWER": "securitizacion"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "galicia"},
            {"LOWER": "y"},
            {"LOWER": "buenos"},
            {"LOWER": "aires"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "nación"},
            {"LOWER": "argentina"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "provincia"},
            {"LOWER": "de"},
            {"LOWER": "buenos"},
            {"LOWER": "aires"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "provincia"},
            {"LOWER": "de"},
            {"LOWER": "cordoba"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "supervielle"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "ciudad"},
            {"LOWER": "de"},
            {"LOWER": "buenos"},
            {"LOWER": "aires"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "patagonia"}],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "hipotecario"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "san"},
            {"LOWER": "juan"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "do"}, {"LOWER": "brasil"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "del"},
            {"LOWER": "tucuman"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "municipal"},
            {"LOWER": "de"},
            {"LOWER": "rosario"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "santander"},
            {"LOWER": "rio"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "regional"},
            {"LOWER": "de"},
            {"LOWER": "cuyo"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "del"}, {"LOWER": "chubut"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "Santa"},
            {"LOWER": "cruz"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "pampa"},
            {"LOWER": "sociedad"},
            {"LOWER": "de"},
            {"LOWER": "economía"},
            {"LOWER": "mixta"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "corrientes"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "provincia"},
            {"LOWER": "del"},
            {"LOWER": "neuquén"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "credicoop"},
            {"LOWER": "cooperativo"},
            {"LOWER": "limitado"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "de"}, {"LOWER": "valores"}],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "roela"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "mariva"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "itau"},
            {"LOWER": "buen"},
            {"LOWER": "ayre"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "provincia"},
            {"LOWER": "de"},
            {"LOWER": "tierra"},
            {"LOWER": "del"},
            {"LOWER": "fuego"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "republica"},
            {"LOWER": "oriental"},
            {"LOWER": "del"},
            {"LOWER": "uruguay"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "saenz"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "meridian"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "macro"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "mercurio"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "comafi"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "inversion"},
            {"LOWER": "y"},
            {"LOWER": "comercio"},
            {"LOWER": "exterior"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "piano"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "finansur"}]},
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "julio"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "privado"},
            {"LOWER": "de"},
            {"LOWER": "inversiones"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "la"},
            {"LOWER": "rioja"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "del"}, {"LOWER": "sol"}],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "del"},
            {"LOWER": "chaco"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [{"LOWER": "banco"}, {"LOWER": "de"}, {"LOWER": "formosa"}],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "cmf"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "santiago"},
            {"LOWER": "del"},
            {"LOWER": "estero"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "industrial"},
            {"LOWER": "de"},
            {"LOWER": "azul"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "nuevo"},
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "santa"},
            {"LOWER": "fe"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "cetelem"},
            {"LOWER": "argentina"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "servicios"},
            {"LOWER": "financieros"},
        ],
    },
    {"label": "BANCO", "pattern": [{"LOWER": "banco"}, {"LOWER": "cofidis"}]},
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "bradesco"},
            {"LOWER": "argentina"},
        ],
    },
    {
        "label": "BANCO",
        "pattern": [
            {"LOWER": "banco"},
            {"LOWER": "de"},
            {"LOWER": "servicios"},
            {"LOWER": "y"},
            {"LOWER": "transacciones"},
        ],
    },
]

patentes = [
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "XXX ddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "XXX-ddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "XXXddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "ddd XXX"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "ddd-XXX"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "dddXXX"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "XX-ddd-XX"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "XXdddXX"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "xxx ddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "xxx-ddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "xxxddd"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "ddd xxx"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "ddd-xxx"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "dddxxx"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "xx-ddd-xx"}]},
    {"label": "PATENTE_DOMINIO", "pattern": [{"SHAPE": "xxdddxx"}]},
]


lista_de_estudios = [
    "secundarios",
    "primarios",
    "terciarios",
    "universitarios",
]

lista_de_estado = ["completos", "incompletos"]

estudios = [
    {
        "label": "ESTUDIOS",
        "pattern": [
            {"LOWER": "estudios"},
            {"LOWER": {"IN": lista_de_estudios}},
            {"LOWER": {"IN": lista_de_estado}},
        ],
    },
]

dni = [
    {"label": "NUM_DNI", "pattern": [{"SHAPE": "d.ddd.ddd"}]},
    {"label": "NUM_DNI", "pattern": [{"SHAPE": "dd.ddd.ddd"}]},
    {"label": "NUM_DNI", "pattern": [{"SHAPE": "ddd.ddd.ddd"}]},
]

telefonos = [
    {"label": "NUM_TELÉFONO", "pattern": [{"SHAPE": "dd-dddd-dddd"}]},
    {"label": "NUM_TELÉFONO", "pattern": [{"SHAPE": "dddddddddd"}]},
    {"label": "NUM_TELÉFONO", "pattern": [{"SHAPE": "dddd-dddd"}]},
    {"label": "NUM_TELÉFONO", "pattern": [{"SHAPE": "dddd-ddd-dddd"}]},
]

ips = [
    {"label": "NUM_IP", "pattern": [{"SHAPE": "ddd.ddd.ddd.ddd"}]},
    {"label": "NUM_IP", "pattern": [{"SHAPE": "ddd.dd.ddd.d"}]},
    {"label": "NUM_IP", "pattern": [{"SHAPE": "ddd.dd.ddd.dd"}]},
]

fecha_numerica = [
    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "dd/dd/dd"}]},
    #    Es problematica con otros casos
    #    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "dd/dd"}]},
    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "dd/dd/dddd"}]},
    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "d/d/dd"}]},
    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "d/d/dddd"}]},
    {"label": "FECHA_NUMÉRICA", "pattern": [{"SHAPE": "d/dd/dddd"}]},
]

cuij = [
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "CAU"}, {"IS_ASCII": True}]},
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "ICN"}, {"IS_ASCII": True}]},
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "IPP"}, {"IS_ASCII": True}]},
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "CAU"}, {"LIKE_NUM": True}]},
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "ICN"}, {"LIKE_NUM": True}]},
    {"label": "NUM_CUIJ", "pattern": [{"ORTH": "IPP"}, {"LIKE_NUM": True}]},
]

fecha = [
    {
        "label": "FECHA",
        "pattern": [
            {
                "LOWER": {
                    "IN": [
                        "enero",
                        "febrero",
                        "marzo",
                        "abril",
                        "mayo",
                        "junio",
                        "julio",
                        "agosto",
                        "septiembre",
                        "octubre",
                        "noviembre",
                        "diciembre",
                    ]
                }
            },
            {"POS": "ADP", "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"},
        ],
    },
    {
        "label": "FECHA",
        "pattern": [
            {"LOWER": "a"},
            {"LOWER": "los"},
            {"LIKE_NUM": True},
            {"LOWER": "días"},
            {"LOWER": "del", "OP": "?"},
            {"LOWER": "mes", "OP": "?"},
            {"LOWER": "de"},
            {
                "LOWER": {
                    "IN": [
                        "enero",
                        "febrero",
                        "marzo",
                        "abril",
                        "mayo",
                        "junio",
                        "julio",
                        "agosto",
                        "septiembre",
                        "octubre",
                        "noviembre",
                        "diciembre",
                    ]
                }
            },
            {"POS": "ADP", "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"},
        ],
    },
    {
        "label": "FECHA",
        "pattern": [
            {"LIKE_NUM": True},
            {"POS": "ADP"},
            {
                "LOWER": {
                    "IN": [
                        "enero",
                        "febrero",
                        "marzo",
                        "abril",
                        "mayo",
                        "junio",
                        "julio",
                        "agosto",
                        "septiembre",
                        "octubre",
                        "noviembre",
                        "diciembre",
                    ]
                }
            },
            {"POS": "ADP", "OP": "?"},
            {"LOWER": "año", "OP": "?"},
            {"LIKE_NUM": True, "OP": "?"},
        ],
    },
]

nacionalidad = [
    {
        "label": "NACIONALIDAD",
        "pattern": [
            {
                "LEMMA": {
                    "IN": [
                        "argentino",
                        "boliviano",
                        "paraguayo",
                        "colombiano",
                        "chileno",
                        "brasileño",
                        "panameño",
                        "italiano",
                        "español",
                        "mexicano",
                        "ruso",
                        "francés",
                        "inglés",
                        "venezolano",
                        "estadounidense",
                        "alemán",
                        "chino",
                        "indio",
                        "cubano",
                        "nigeriano",
                        "polaco",
                        "sueco",
                        "turco",
                        "japonés",
                        "portugués",
                        "iraní",
                        "paquistaní",
                        "costarricense",
                        "canadiense",
                        "marroquí",
                        "griego",
                        "egipcio",
                        "coreano",
                        "ecuatoriano",
                        "peruano",
                        "guatemalteco",
                        "salvadoreño",
                        "holandés",
                        "dominicano",
                    ]
                }
            }
        ],
    },
    {
        "label": "NACIONALIDAD",
        "pattern": [
            {
                "LEMMA": {
                    "IN": [
                        "argentino",
                        "boliviano",
                        "paraguayo",
                        "colombiano",
                        "chileno",
                        "brasileño",
                        "panameño",
                        "italiano",
                        "español",
                        "mexicano",
                        "ruso",
                        "francés",
                        "inglés",
                        "venezolano",
                        "estadounidense",
                        "alemán",
                        "chino",
                        "indio",
                        "cubano",
                        "nigeriano",
                        "polaco",
                        "sueco",
                        "turco",
                        "japonés",
                        "portugués",
                        "iraní",
                        "paquistaní",
                        "costarricense",
                        "canadiense",
                        "marroquí",
                        "griego",
                        "egipcio",
                        "coreano",
                        "ecuatoriano",
                        "peruano",
                        "guatemalteco",
                        "salvadoreño",
                        "holandés",
                        "dominicano",
                    ]
                }
            }
        ],
    },
]


correo_electronico = [
    {"label": "CORREO_ELECTRÓNICO", "pattern": [{"LIKE_EMAIL": True}]}
]

ley = [{"label": "LEY", "pattern": [{"LOWER": "ley"}, {"LIKE_NUM": True}]}]

cuit = [
    {
        "label": "NUM_CUIT_CUIL",
        "pattern": [
            {
                "TEXT": {
                    "REGEX": "^(20|23|27|30|33)([0-9]{9}|-[0-9]{8}-[0-9]{1})$"
                }
            }
        ],
    }
]

archivos = [
    {
        "label": "NOMBRE_ARCHIVO",
        "pattern": [
            {
                "TEXT": {
                    "REGEX": r"^[\w]+\.(jpg|png|gif|bmp|tiff|svg|doc|docx|odt|txt|pdf|mp3|avi|mp4|mkv|mpg|mpeg|mov|asf|webm|3gp|3g2|m4v)$"
                }
            }
        ],
    },
]

pasaporte = [
    {
        "label": "PASAPORTE",
        "pattern": [{"TEXT": {"REGEX": "^([a-zA-Z]{3}[0-9]{6})$"}}],
    }
]

link = [{"label": "LINK", "pattern": [{"LIKE_URL": True}]}]

cbu = [
    {
        "label": "CBU",
        "pattern": [
            {"ORTH": "CBU"},
            {"ORTH": ":", "OP": "?"},
            {"IS_DIGIT": True, "LENGTH": 22},
        ],
    }
]

usuarix = [
    {
        "label": "USUARIX",
        "pattern": [
            {"ORTH": "del"},
            {"ORTH": "usuario"},
            {"ORTH": '"'},
            {"IS_ALPHA": True, "OP": "+"},
            {"ORTH": '"'},
        ],
    }
]


def tag_array(arr, tags):
    return dict(arr=arr, tags=tags)


def fetch_ruler_patterns_by_tag(tag):
    ruler_patterns = []
    for tagged_pattern in tagged_patterns:
        if tag == "todas" or tag in tagged_pattern["tags"]:
            ruler_patterns.extend(tagged_pattern["arr"])
    return ruler_patterns


tagged_patterns = [
    tag_array(dni, ["argentina", "juzgado10"]),
    tag_array(telefonos, ["argentina", "juzgado10"]),
    tag_array(ips, ["internet", "juzgado10"]),
    tag_array(fecha_numerica, ["español", "juzgado10"]),
    tag_array(cuij, ["judicial", "juzgado10"]),
    tag_array(fecha, ["español", "juzgado10"]),
    tag_array(nacionalidad, ["español", "juzgado10"]),
    tag_array(bancos, ["argentina", "juzgado10"]),
    tag_array(patentes, ["argentina", "juzgado10"]),
    tag_array(estudios, ["argentina", "juzgado10"]),
    tag_array(marcas_autos, ["argentina", "juzgado10"]),
    tag_array(correo_electronico, ["internet", "juzgado10"]),
    tag_array(ley, ["judicial", "juzgado10"]),
    tag_array(cuit, ["argentina", "juzgado10"]),
    tag_array(archivos, ["internet", "juzgado10"]),
    tag_array(pasaporte, ["argentina", "juzgado10"]),
    tag_array(link, ["internet", "juzgado10"]),
    tag_array(cbu, ["argentina", "juzgado10"]),
    tag_array(usuarix, ["internet", "juzgado10"]),
]


##### ENTITY MATCHER ####################################################################
#########################################################################################

import logging
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.lang.es.lex_attrs import _num_words
from spacy.util import filter_spans
from spacy import Language

# Extends built-in lex_attrs from the spanish lang package
num_words = _num_words + [
    "ciento",
    "docientas",
    "docientos",
    "doscientas",
    "doscientos",
    "trecientas",
    "trecientos",
    "trescientas",
    "trescientos",
    "cuatrocientas",
    "cuatrocientos",
    "quinientas",
    "quinientos",
    "seiscientas",
    "seiscientos",
    "setecientas",
    "setecientos",
    "ochocientas",
    "ochocientos",
    "novecientas",
    "novecientos",
    "millones",
    "billones",
    "trillones",
]
page_first_left_nbors = [
    "página",
    "pag",
    "p",
    "p.",
    "pág",
    "pág.",
    "fs",
    "inciso",
    "inc",
]
page_second_left_nbors = [
    "página",
    "pag",
    "fs",
    "inciso",
    "inc",
]
measure_unit_first_right_nbors = [
    "inc",
    "metros",
    "m",
    "gr",
    "grs",
    "gramos",
    "km",
    "kg",
    "cm",
]

article_left_nbors = [
    "artículo",
    "articulo",
    "artículos",
    "articulos",
    "art",
    "arts",
]

# Violence
gender_violence_context_text = "CONTEXTO_VIOLENCIA_DE_GÉNERO"
violence_context_text = "CONTEXTO_VIOLENCIA"
violence_nbors = ["violencia", "violencias"]
violence_types = [
    "ambiental",
    "doméstica",
    "domestica",
    "económica",
    "economica",
    "física",
    "fisica",
    "patrimonial",
    "psicológica",
    "psicologica",
    "sexual",
    "simbólica",
    "simbolica",
    "social",
]
gender_violence_types = ["género", "genero"]


def filter_longer_spans(spans, *, seen_tokens=set(), preserve_spans=[]):
    """Filter a sequence of spans and remove duplicates or overlaps. Useful for
    creating named entities (where one token can only be part of one entity) or
    when merging spans with `Retokenizer.merge`. When spans overlap, the (first)
    longest span is preferred over shorter spans.

    spans (iterable): The spans to filter.
    RETURNS (list): The filtered spans.
    """

    def get_sort_key(span):
        return (span.end - span.start, -span.start)

    sorted_spans = sorted(spans, key=get_sort_key, reverse=True)
    result = preserve_spans
    _seen_tokens = seen_tokens
    for span in sorted_spans:
        # Check for end - 1 here because boundaries are inclusive
        if span.start not in _seen_tokens and span.end - 1 not in _seen_tokens:
            result.append(span)
        _seen_tokens.update(range(span.start, span.end))
    result = sorted(result, key=lambda span: span.start)
    return result


def repeat_patterns(patterns, times):
    """
    Utility function that receives a pattern to return a list that contains
    that pattern multiplied by times. The final length of the list is equal to
    len(patterns) * times.
    """
    generated_patterns = []
    for i in range(0, times):
        [generated_patterns.append(pattern) for pattern in patterns]
    return generated_patterns


class GenericMatcher(object):
    """
    GenericMatcher: Given an NLP instance, and list of patterns, generates a
    pipeline that matches tokens against each of those patterns to return an
    updated Doc object.
    """

    name = "generic_matcher"

    def __init__(self, nlp, matcher_patterns=[]):
        self.nlp = nlp
        self.matcher = Matcher(self.nlp.vocab, validate=True)
        # Adds patterns to the Matcher pipeline
        for entity_label, pattern in matcher_patterns:
            self.matcher.add(entity_label, [pattern], on_match=None)

    def __call__(self, doc):
        matches = self.matcher(doc)
        matched_spans = [
            Span(doc, start, end, self.nlp.vocab.strings[match_id])
            for match_id, start, end in matches
        ]
        # Creates a set of seen tokens so that the filter_longer_spans function
        # prioritizes those spans we are sending.
        seen_tokens = set()
        merged_matched_spans = filter_spans(matched_spans)
        for span in merged_matched_spans:
            seen_tokens.update(range(span.start, span.end))
        doc_ents = merged_matched_spans + list(doc.ents)
        # Merges adjacent entities and removes overlapped entities
        doc.ents = filter_longer_spans(
            doc_ents,
            seen_tokens=seen_tokens,
            preserve_spans=merged_matched_spans,
        )
        return doc


def exist_n_token(token_index, nbor_position, document_length):
    """
    Returns true if a token neighbor exists in a document.

    :param token_index: The document index of a token
    :param nbor_position: An integer that represents a number of characters to
    the left (negative values) or to the right (positive values)
    :param document_length: An integer that represents the number of tokens in a
    document
    """
    index = token_index + nbor_position
    return index >= 0 and index < document_length


def not_in_nbor(document_length, span, ent_name, word_list, nbor_position):
    """
    Given a span, returns true whenever then span tokene exists in the document
    and does not match a string in a word list

    :param document_length: The number of tokens in a document
    :param span: A span object to evaluate
    :param ent_name: An entity name
    :param word_list: A list of allowed words
    :param nbor_position: An integer representing a number of characters to the
    left (negative values) or to the right (positive values)
    """
    if exist_n_token(span[0].i, nbor_position, document_length):
        return (
            span.label_ == ent_name
            and span[0].nbor(nbor_position).text not in word_list
        )
    return True


def is_start_of_span_contained(span, target_span):
    return span.start >= target_span.start and span.start < target_span.end


def is_end_of_span_contained(span, target_span):
    return target_span.start >= span.start and target_span.end <= span.end


def overlaps(span, span_list):
    """
    Returns True if the given span, or part of it, is contained in a given span
    list.
    """
    for s in span_list:
        if is_start_of_span_contained(span, s) or is_end_of_span_contained(
            span, s
        ):
            return True
    return False


matcher_patterns = [
    # Multi-num tokens
    (
        "NUM",
        [
            {"LOWER": {"IN": num_words}, "OP": "+"},
            {"ORTH": "y", "OP": "*"},
            {"LOWER": {"IN": num_words}, "OP": "+"},
            {"ORTH": "y", "OP": "*"},
            {"LOWER": {"IN": num_words}, "OP": "+"},
            {"ORTH": "y", "OP": "*"},
            {"LOWER": {"IN": num_words}, "OP": "+"},
        ],
    ),
    # Single num tokens
    ("NUM", [{"LOWER": {"IN": num_words}, "OP": "+"}]),
    # Digit-like words
    ("NUM", [{"IS_DIGIT": True}]),
]


@Language.factory("EntityMatcher")
class EntityMatcher(object):
    """
    EntityMatcher: Detects and labels "NUM" entities. Matches their context to
    clean out nums that should be labeled as another entity.
    """

    name = "entity_matcher"

    def __init__(
        self,
        nlp: Language,
        name: str = "entity_matcher",
        matcher_patterns=matcher_patterns,
        *,
        after_callbacks=[],
    ):
        self.nlp = nlp
        self.matcher = Matcher(self.nlp.vocab, validate=True)
        # Adds patterns to the Matcher pipeline
        for entity_label, pattern in matcher_patterns:
            self.matcher.add(entity_label, [pattern], on_match=None)
        self.after_callbacks = after_callbacks

    def __call__(self, doc):
        matches = self.matcher(doc)
        matched_spans = [
            Span(doc, start, end, self.nlp.vocab.strings[match_id])
            for match_id, start, end in matches
        ]
        # Merges adjacent entities and removes overlapped entities
        filtered_spans = filter_spans(matched_spans)

        for span in filtered_spans:
            document_length = len(doc)

            def does_not_have_first_left_nbor(document_length, span):
                return not_in_nbor(
                    document_length,
                    span,
                    "NUM",
                    page_first_left_nbors,
                    -1,
                )

            def does_not_have_second_left_nbor(document_length, span):
                return not_in_nbor(
                    document_length,
                    span,
                    "NUM",
                    page_second_left_nbors,
                    -2,
                )

            def does_not_have_first_right_nbor(document_length, span):
                return not_in_nbor(
                    document_length,
                    span,
                    "NUM",
                    measure_unit_first_right_nbors,
                    1,
                )

            if (
                does_not_have_first_left_nbor(document_length, span)
                and does_not_have_second_left_nbor(document_length, span)
                and does_not_have_first_right_nbor(document_length, span)
            ) and not overlaps(span, doc.ents):
                doc.ents = list(doc.ents) + [span]
            else:
                # FIXME this one ent has been discarded by the nbor word lists.
                # We should consider assigning them to an entity, or filter them
                # somewhere else
                logging.info(
                    f"[FIXME] Should process this span as another ent: `{span}`"
                )

        for after_callback in self.after_callbacks:
            doc = after_callback(doc)

        return doc


@Language.factory("ArticlesMatcher")
class ArticlesMatcher(object):
    name = "articles_matcher"

    def __init__(self, nlp: Language, name: str = "articles_matcher"):
        article_patterns = self.get_article_patterns()
        self.matcher = GenericMatcher(nlp, article_patterns)

    def __call__(self, doc):
        return self.matcher(doc)

    def get_article_patterns(self):
        return [
            (
                "ARTÍCULO",
                [
                    {"LOWER": {"IN": article_left_nbors}},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"IS_DIGIT": True, "OP": "+"},
                    *repeat_patterns(
                        [
                            {"ORTH": ",", "OP": "*"},
                            {"IS_DIGIT": True, "OP": "?"},
                        ],
                        14,
                    ),
                    {"ORTH": "y", "OP": "?"},
                    {"IS_DIGIT": True, "OP": "?"},
                ],
            ),
        ]


class ViolenceContextMatcher(object):
    name = "violence_context_matcher"

    def __init__(self, nlp):
        violence_context_patterns = self.get_violence_context_patterns()
        self.matcher = GenericMatcher(nlp, violence_context_patterns)

    def __call__(self, doc):
        return self.matcher(doc)

    def get_violence_context_patterns(self):
        return [
            (
                gender_violence_context_text,
                [
                    {"LOWER": {"IN": violence_nbors}},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"ORTH": "de"},
                    {"LOWER": {"IN": gender_violence_types}},
                ],
            ),
            (
                violence_context_text,
                [
                    {"LOWER": {"IN": violence_nbors}},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LOWER": {"IN": violence_types}},
                ],
            ),
            (
                violence_context_text,
                [
                    {"LOWER": {"IN": violence_nbors}},
                    {"IS_PUNCT": True, "OP": "?"},
                    {"LOWER": {"IN": violence_types}, "OP": "?"},
                    *repeat_patterns(
                        [
                            {"ORTH": ",", "OP": "*"},
                            {"LOWER": {"IN": violence_types}, "OP": "?"},
                        ],
                        7,
                    ),
                    {"ORTH": "y", "OP": "+"},
                    {"LOWER": {"IN": violence_types}, "OP": "+"},
                ],
            ),
        ]


def tag_cb(cb, tags):
    return dict(cb=cb, tags=tags)


tagged_cbs = [
    tag_cb(ArticlesMatcher, ["judicial"]),
    tag_cb(ViolenceContextMatcher, ["judicial"]),
]


def fetch_cb_by_tag(tag):
    cbs = []
    for tagged_cb in tagged_cbs:
        if tag == "todas" or tag in tagged_cb["tags"]:
            cbs.append(tagged_cb["cb"])
    return cbs


##### ENTITY CUSTOM ####################################################################
########################################################################################

import re
from functools import partial
from spacy import Language

period_rules = [
    "segundo",
    "segundos",
    "minuto",
    "minutos",
    "hr",
    "hs",
    "hora",
    "horas",
    "año",
    "años",
    "dia",
    "día",
    "dias",
    "días",
    "mes",
    "meses",
]

law_left_nbors = [
    "ley",
    "leyes",
]

address_first_left_nbors = [
    "calle",
    "Calle",
    "dirección",
    "Dirección",
    "avenida",
    "av.",
    "Avenida",
    "Av.",
    "pasaje",
    "Pasaje",
    "Parcela",
    "parcela",
]

address_second_left_nbors = [
    "instalación",
    "contramano",
    "sita",
    "sitas",
    "sito",
    "sitos",
    "real",
    "domiciliado",
    "domiciliada",
    "constituido",
    "constituida",
    "contramano",
    "intersección",
    "domicilio",
    "ubicado",
    "registrado",
    "ubicada",
    "real",
]

address_connector = "en"

license_plate_left_nbor = [
    "patente",
    "dominio",
]

age_right_token = "años"
age_text_in_token = "edad"
number_abreviated_indicator = "nº"
case_first_left_token = "caso"
case_second_left_token = "causa"
cuij_indicator = "cuij"
actuacion_number_indicator = "nro"
actuacion_nbor_token = "actuación"
expediente_indicator = "expediente"

judge_lemma = ["juez", "jueza", "Juez", "Jueza"]
secretarix_lemma = [
    "secretario",
    "secretaria",
    "prosecretario",
    "prosecretaria",
    "Prosecretario",
    "Prosecretaria",
    "Secretario",
    "Secretaria",
]
prosecutor_lemma = ["fiscal", "fiscalía", "Fiscal", "Fiscalía"]
ombuds_person_lemma = ["defensor", "defensora", "Defensora", "Defensor"]
accused_lemma = [
    "acusado",
    "acusada",
    "imputado",
    "imputada",
    "infractor",
    "infractora",
    "Acusado",
    "Acusada",
    "Imputado",
    "Imputada",
    "Infractor",
    "Infractora",
]
advisor_lemma = ["asesor", "asesora", "Asesor", "Asesora"]
phone_lemma = ["teléfono", "tel", "celular", "número", "numerar", "telefónico"]
phone_text = ["telefono", "tel", "cel"]


def is_age(token):
    return (
        token.like_num
        and token.nbor(1).text == age_right_token
        and age_text_in_token in token.sent.text
    )


def is_caseNumber(token):
    return token.like_num and (
        (
            token.nbor(-1).lower_ == number_abreviated_indicator
            and token.nbor(-2).lower_ == case_second_left_token
        )
        or token.nbor(-1).lower_ == case_first_left_token
    )


def is_cuijNumber(token):
    return (token.is_ascii and token.nbor(-3).lower_ == cuij_indicator) or (
        token.like_num and token.nbor(-3).lower_ == cuij_indicator
    )


def is_actuacionNumber(token):
    return (
        token.nbor(-1).lower_ == ":"
        and token.nbor(-2).lower_ == actuacion_number_indicator
        and token.nbor(-3).lower_ == actuacion_nbor_token
    )


def is_expedienteNumber(token):
    return (
        token.nbor(-1).lower_ == number_abreviated_indicator
        and (
            token.nbor(-3).lower_ == expediente_indicator
            or token.nbor(-2).lower_ == expediente_indicator
        )
    ) or (token.like_num and token.nbor(-2).lower_ == expediente_indicator)


def is_place_token(token):
    # TODO Este enfoque puede generar falsos positivos
    first_left_nbors = [
        "asentamiento",
        "paraje",
        "localidad",
        "country",
        "distrito",
    ]

    return token.nbor(-1).lower_ in first_left_nbors


def is_law(ent):
    first_token = ent[0]
    return ent.label_ == "NUM" and (
        first_token.nbor(-1).lower_ in law_left_nbors
        or first_token.nbor(-2).lower_ in law_left_nbors
        or first_token.nbor(-3).lower_ in law_left_nbors
    )


def is_last(doc, token_id):
    return token_id == len(doc) - 1


def is_between_tokens(token_id, left=0, right=0):
    return token_id < right and token_id >= left


is_from_first_tokens = partial(is_between_tokens, left=0, right=3)


def is_judge(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in judge_lemma
        or first_token.nbor(-2).lemma_ in judge_lemma
        or first_token.nbor(-3).lemma_ in judge_lemma
    )


def is_period(ent):
    last_token = ent[len(ent) - 1]
    return ent.label_ in ["NUM"] and last_token.nbor(1).text in period_rules


def is_secretary(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in secretarix_lemma
        or first_token.nbor(-2).lemma_ in secretarix_lemma
        or first_token.nbor(-3).lemma_ in secretarix_lemma
    )


def is_prosecutor(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in prosecutor_lemma
        or first_token.nbor(-2).lemma_ in prosecutor_lemma
        or first_token.nbor(-3).lemma_ in prosecutor_lemma
    )


def is_ombuds_person(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in ombuds_person_lemma
        or first_token.nbor(-2).lemma_ in ombuds_person_lemma
        or first_token.nbor(-3).lemma_ in ombuds_person_lemma
    )


def is_accused(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in accused_lemma
        or first_token.nbor(-2).lemma_ in accused_lemma
        or first_token.nbor(-3).lemma_ in accused_lemma
    )


def is_advisor(ent):
    first_token = ent[0]
    return ent.label_ in ["PER", "LOC"] and (
        first_token.nbor(-1).lemma_ in advisor_lemma
        or first_token.nbor(-2).lemma_ in advisor_lemma
        or first_token.nbor(-3).lemma_ in advisor_lemma
    )


def is_ip_address(ent):
    octet_rx = r"(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    pattern = re.compile(r"^{0}(?:\.{0}){{3}}$".format(octet_rx))
    is_ip = pattern.match(str(ent))
    return ent.label_ in ["NUM", "NUM_IP"] and is_ip


def is_phone(ent):
    first_token = ent[0]
    return ent.label_ == "NUM" and (
        first_token.nbor(-1).lemma_ in phone_lemma
        or first_token.nbor(-2).lemma_ in phone_lemma
        or first_token.nbor(-3).lemma_ in phone_lemma
        or first_token.nbor(-1).text in phone_text
        or first_token.nbor(-2).text in phone_text
        or (
            first_token.nbor(-1).text == "("
            and first_token.nbor(1).text == ")"
        )
    )


# TODO this function could be used in many methods, check it!
def is_token_in_x_left_pos(token, pos, nbors):
    try:
        return token.nbor(-pos).lower_ in nbors
    except Exception:
        return False


def is_address(ent):
    first_token = ent[0]
    last_token = ent[-1]
    address_1_tokens_to_left = is_token_in_x_left_pos(
        first_token, 1, address_first_left_nbors
    )
    address_2_tokens_to_left_first_nbors = is_token_in_x_left_pos(
        first_token, 2, address_first_left_nbors
    )
    address_2_tokens_to_left_second_nbors = is_token_in_x_left_pos(
        first_token, 2, address_second_left_nbors
    )
    address_3_tokens_to_left_first_nbors = is_token_in_x_left_pos(
        first_token, 3, address_first_left_nbors
    )
    address_3_tokens_to_left_second_nbors = is_token_in_x_left_pos(
        first_token, 3, address_second_left_nbors
    )
    address_4_tokens_to_left_first_nbors = is_token_in_x_left_pos(
        first_token, 4, address_first_left_nbors
    )
    address_4_tokens_to_left_second_nbors = is_token_in_x_left_pos(
        first_token, 4, address_second_left_nbors
    )

    is_address_from_PER = ent.label_ in ["PER"] and (
        address_1_tokens_to_left
        or address_2_tokens_to_left_second_nbors
        or last_token.like_num
        or last_token.nbor().like_num
    )

    is_address_from_NUM = ent.label_ in ["NUM"] and (
        address_1_tokens_to_left
        or address_2_tokens_to_left_first_nbors
        or address_2_tokens_to_left_second_nbors
        or address_3_tokens_to_left_first_nbors
        or address_3_tokens_to_left_second_nbors
        or address_4_tokens_to_left_first_nbors
        or address_4_tokens_to_left_second_nbors
    )

    return is_address_from_PER or is_address_from_NUM


def get_aditional_left_tokens_for_address(ent):
    if ent.label_ in ["PER"] and ent[-1].nbor().like_num:
        return 1
    if ent.label_ in ["NUM"]:
        token = ent[0]
        if token.nbor(-1).lower_ in address_first_left_nbors:
            return 1
        if (
            token.nbor(-2).lower_ in address_first_left_nbors
            or token.nbor(-2).lower_ in address_second_left_nbors
        ):
            return 2
        if token.nbor(-3).lower_ in address_first_left_nbors:
            return 3
        if token.nbor(-3).lower_ in address_second_left_nbors:
            return 2 - 1 if token.nbor(-2).lower_ == address_connector else 0
        if token.nbor(-4).lower_ in address_first_left_nbors:
            return 4
        if token.nbor(-4).lower_ in address_second_left_nbors:
            return 3 - 1 if token.nbor(-3).lower_ == address_connector else 0
    return 0


def get_entity_to_remove_if_contained_by(ent_start, ent_end, list_entities):
    for i, ent_from_list in enumerate(list_entities):
        if (
            ent_start >= ent_from_list.start
            and ent_start <= ent_from_list.end
            or ent_end >= ent_from_list.start
            and ent_end <= ent_from_list.end
        ):
            return ent_from_list
    return None


def generate_address_span(ent, new_ents, doc):
    address_token = get_aditional_left_tokens_for_address(ent)
    ent_start = ent.start - address_token
    ent_to_remove = get_entity_to_remove_if_contained_by(
        ent_start, ent.end, new_ents
    )
    if ent_to_remove:
        if (ent.end - ent_start) > (ent_to_remove.end - ent_to_remove.start):
            new_ents = remove_wrong_labeled_entity_span(
                new_ents, ent_to_remove
            )
            return Span(doc, ent_start, ent.end, label="DIRECCIÓN")

    return Span(doc, ent_start, ent.end, label="DIRECCIÓN")


def could_be_an_article(ent):
    token = ent[0]
    first_left_token = token.nbor(-1).lower_
    second_left_token = token.nbor(-2).lower_
    third_left_token = token.nbor(-3).lower_
    dont_consider = "bis"

    return (
        ent.label_ == "PATENTE_DOMINIO"
        and token.lower_.find(dont_consider) != -1
        and first_left_token not in license_plate_left_nbor
        and second_left_token not in license_plate_left_nbor
        and third_left_token not in license_plate_left_nbor
    )


def is_license_plate(ent):
    token = ent[0]
    first_left_token = token.nbor(-1).lower_
    second_left_token = token.nbor(-2).lower_
    third_left_token = token.nbor(-3).lower_

    return token.like_num and (
        first_left_token in license_plate_left_nbor
        or second_left_token in license_plate_left_nbor
        or third_left_token in license_plate_left_nbor
    )


def is_accused_or_advisor(ent):
    return is_accused(ent) or is_advisor(ent)


def get_start_end_license_plate(ent):
    token = ent[0]
    first_left_token = token.nbor(-1).lower_
    first_right_token = token.nbor(1).lower_
    if (
        len(ent.text) != 3
    ):  # this means it is not an "incomplete" license plate
        return ent.start, ent.end
    if len(first_left_token) == 3 and isinstance(first_left_token, str):
        # 3 letras - 3 núm
        return ent.start - 1, ent.end
    if (
        len(first_left_token) == 2
        and len(first_right_token) == 2
        and isinstance(first_left_token, str)
        and isinstance(first_right_token, str)
    ):
        # 2 letras - 3 núm - 2 letras
        return ent.start - 1, ent.end + 1
    if len(first_right_token) == 3 and isinstance(first_right_token, str):
        # 3 núm - 3 letras
        return ent.start, ent.end + 1


def remove_wrong_labeled_entity_span(ent_list, ent_to_remove):
    return [
        ent
        for ent in ent_list
        if not (
            ent_to_remove.start == ent.start and ent_to_remove.end == ent.end
        )
    ]


def process_fns(acc, data):
    # from 3.9 We can use functools.cache on some functions
    fn1, fn2, fn3 = data
    if not fn1() and fn2():
        acc.append(fn3())
    return acc


@Language.factory("EntityCustom")
class EntityCustom(object):
    name = "entity_custom"

    def __init__(
        self, nlp: Language, name: str = "entity_custom", tag="todas"
    ):
        self.nlp = nlp
        self.tag = tag
        self.tagged_fns_token = [
            self.tag_fn(self.num_causa, ["judicial", "argentina"]),
            self.tag_fn(self.edad, ["español"]),
            self.tag_fn(self.num_cuij, ["judicial", "argentina"]),
            self.tag_fn(self.num_actuacion, ["judicial", "argentina"]),
            self.tag_fn(self.num_expediente, ["judicial", "argentina"]),
            self.tag_fn(self.loc, ["lugar"]),
        ]
        self.tagged_fns_ent = [
            self.tag_fn(self.fecha_resolucion, ["judicial"]),
            self.tag_fn(self.ley, ["judicial", "argentina"]),
            self.tag_fn(self.periodo, ["español"]),
            self.tag_fn(self.juezx, ["judicial", "argentina"]),
            self.tag_fn(self.secretarix, ["judicial", "argentina"]),
            self.tag_fn(self.fiscal, ["judicial", "argentina"]),
            self.tag_fn(self.defensorx, ["judicial", "argentina"]),
            self.tag_fn(self.num_ip, ["internet"]),
            self.tag_fn(self.num_telefono, ["argentina"]),
            self.tag_fn(self.per, ["persona"]),
            self.tag_fn(self.direccion, ["español"]),
            self.tag_fn(self.patente_dominio, ["argentina"]),
        ]

    @staticmethod
    def tag_fn(fn, tags):
        return dict(fn=fn, tags=tags)

    @staticmethod
    def fetch_fn_by_tag(tagged_fns, tag):
        fns = []
        for tagged_fn in tagged_fns:
            if tag == "todas" or tag in tagged_fn["tags"]:
                fns.append(tagged_fn["fn"])
        return fns

    def num_causa(self, token):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, token.i),
                partial(is_caseNumber, token),
                partial(
                    Span, self.doc, token.i + 0, token.i + 1, label="NUM_CAUSA"
                ),
            ),
        )

    def edad(self, token):
        return process_fns(
            [],
            (
                partial(is_last, self.doc, token.i),
                partial(is_age, token),
                partial(
                    Span, self.doc, token.i + 0, token.i + 1, label="EDAD"
                ),
            ),
        )

    def num_cuij(self, token):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, token.i),
                partial(is_cuijNumber, token),
                partial(
                    Span, self.doc, token.i + 0, token.i + 1, label="NUM_CUIJ"
                ),
            ),
        )

    def num_actuacion(self, token):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, token.i),
                partial(is_actuacionNumber, token),
                partial(
                    Span,
                    self.doc,
                    token.i + 0,
                    token.i + 1,
                    label="NUM_ACTUACIÓN",
                ),
            ),
        )

    def num_expediente(self, token):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, token.i),
                partial(is_expedienteNumber, token),
                partial(
                    Span,
                    self.doc,
                    token.i + 0,
                    token.i + 1,
                    label="NUM_EXPEDIENTE",
                ),
            ),
        )

    def loc(self, token):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, token.i),
                partial(is_place_token, token),
                partial(Span, self.doc, token.i - 1, token.i + 1, label="LOC"),
            ),
        )

    def ley(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_law, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 0, label="LEY"
                ),
            ),
        )

    def periodo(self, ent):
        return process_fns(
            [],
            (
                partial(partial(is_last, self.doc, ent.start)),
                partial(is_period, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 1, label="PERIODO"
                ),
            ),
        )

    def juezx(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_judge, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 0, label="JUEZX"
                ),
            ),
        )

    def secretarix(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_secretary, ent),
                partial(
                    Span,
                    self.doc,
                    ent.start + 0,
                    ent.end + 0,
                    label="SECRETARIX",
                ),
            ),
        )

    def fiscal(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_prosecutor, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 0, label="FISCAL"
                ),
            ),
        )

    def defensorx(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_ombuds_person, ent),
                partial(
                    Span,
                    self.doc,
                    ent.start + 0,
                    ent.end + 0,
                    label="DEFENSORX",
                ),
            ),
        )

    def num_ip(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_ip_address, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 0, label="NUM_IP"
                ),
            ),
        )

    def num_telefono(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_phone, ent),
                partial(
                    Span,
                    self.doc,
                    ent.start + 0,
                    ent.end + 0,
                    label="NUM_TELÉFONO",
                ),
            ),
        )

    def per(self, ent):
        return process_fns(
            [],
            (
                partial(is_from_first_tokens, ent.start),
                partial(is_accused_or_advisor, ent),
                partial(
                    Span, self.doc, ent.start + 0, ent.end + 0, label="PER"
                ),
            ),
        )

    def direccion(self, ent):
        if not is_from_first_tokens(ent.start) and is_address(ent):
            self.new_ents.append(
                generate_address_span(ent, self.new_ents, self.doc)
            )
        return []

    def patente_dominio(self, ent):
        new_ents = []
        if (
            not is_from_first_tokens(ent.start)
            and could_be_an_article(ent)
            and ent.label_ == "PATENTE_DOMINIO"
        ):
            self.doc.ents = remove_wrong_labeled_entity_span(
                self.doc.ents, ent
            )

        if not is_from_first_tokens(ent.start) and is_license_plate(ent):
            start, end = get_start_end_license_plate(ent)
            new_ents.append(
                Span(self.doc, start, end, label="PATENTE_DOMINIO")
            )
        return new_ents

    def fecha_resolucion(self, ent):
        new_ents = []
        # Modifica FECHA a FECHA_RESOLUCION: solo la primera vez, si esta el token entre 3 y 100
        if (
            not self.find_fecha_resolucion
            and ent.label_ in ["FECHA"]
            and is_between_tokens(ent.start, 3, 100)
        ):
            self.find_fecha_resolucion = True
            new_ents.append(
                Span(self.doc, ent.start, ent.end, label="FECHA_RESOLUCION")
            )
        return new_ents

    def new_ents_by_ents(self):
        self.find_fecha_resolucion = False
        for i, ent in enumerate(self.doc.ents):
            for fn in self.fetch_fn_by_tag(self.tagged_fns_ent, self.tag):
                self.new_ents.extend(fn(ent))

    def new_ents_by_token(self):
        for token in self.doc:
            for fn in self.fetch_fn_by_tag(self.tagged_fns_token, self.tag):
                self.new_ents.extend(fn(token))

    def __call__(self, doc):
        self.new_ents = []
        self.doc = doc
        self.new_ents_by_token()
        self.new_ents_by_ents()
        if self.new_ents:
            # We'd always want the new entities to be appended first because
            # filter_spans prioritizes the first occurrences on overlapping
            self.doc.ents = filter_spans(self.new_ents + list(self.doc.ents))

        return self.doc
