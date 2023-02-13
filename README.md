# IA² | Línea de comandos

<p align="center">
  <a target="_blank" rel="noopener noreferrer">
    <img width="220px" src="public/images/ia2-logo.png" alt="IA²" />
  </a>
</p>
<br/>
<h4 align="center">Línea de comandos del proyecto IA²</h4>

## Stack Tecnológico

- Python, versión 3.10
- [Fire](https://github.com/google/python-fire)
- [Spacy](https://spacy.io/) , versión 3.4.4

## Instalación

**Build**
```bash
make jupyter-build
```
**Build and run(GPU)**
```bash
make jupyter-run
```
**Build & run (CPU)**
```bash
make jupyter-run-cpu
```

## Consideraciones

El proyecto no cuenta con datasets iniciales. Para construir nuestros dataset de entrenamiento y validación iniciales se utilizó la herramienta de etiquetado [Dataturks](http://dataturks.com/).

La línea de comandos contiene herramientas para transformar el etiquetado Dataturks a datasets soportados por Spacy. Para más información consulte el comando de ayuda de la línea de comandos.

## Circuito básico de prueba

El siguiente circuito de prueba contempla los siguientes procesos:

+ Adaptación del dataset. Creación de Docbin (Spacy V3).
+ Descargar un modelo de spacy para utilizar como modelo base.
+ Creación de un modelo base.
+ Agregar entidades al pipeline de reconocimiento de nombre de entidades del modelo base.
+ Ejecutar el entrenamiento.

### Notebooks Train

Dentro de la carpeta 01_train, se encuentran las notebooks:
+ 01_create_data : A partir de esta notebook se transforman los datasets etiquetados provenientes de  [Dataturks](http://dataturks.com/) a [Dockbin](https://spacy.io/api/docbin).

+ 02_train: A partir de esta notebook se realiza el entrenamiento del modelo basado en `es_core_news_lg`

+ 03_create_custom_pipeline: A partir de esta notebook se agregan nuevas reglas y realiza el deploy del modelo.
Pipelines que se incluyen:

- **EntityRuler**: `entity_ruler.py`
- **EntityMatcher**: `entity_matcher.py`
- **EntityCustom**: `entoty_custom.py`
## Tests

Algunos tests utilizan un modelo de spacy para realizar pruebas sobre texto plano. Por esta razón es necesario generar un archivo *`.env`*, utilizando *`.env.example`* como base. La variable `TEST_MODEL_PATH` del achivo `.env` debe contener la ruta hacia un modelo. Luego puede utilizar el siguiente comando para correr las pruebas:

```bash
make test
```

## Licencia

[**GNU General Public License version 3**](LICENSE)

## Contribuciones

Por favor, asegúrese de leer los [lineamientos de contribución](CONTRIBUTING.md) antes de realizar Pull Requests.
