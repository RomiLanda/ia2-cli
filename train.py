import fire
import warnings
import pickle
import logging
import json
import random
import os
import spacy
from spacy.util import minibatch, compounding, filter_spans
from os import listdir
from os.path import isfile, join

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def removeEntitiesNotInList(spacyfile, entityList):
    # Esta funcion remueve de una training_data preparada para spacy ,todas las entidades que estan en la lista
    file = spacyfile
    newTrainingData = []
    for hit in file:
        entities = []
        data = hit[1]["entities"]
        for ent in data:
            if ent[2] in entityList:
                entities.append(ent)
        newTrainingData.append((hit[0], {"entities": entities}))
    return newTrainingData


def convert_dataturks_to_spacy(dataturks_JSON_FilePath):
    try:
        training_data = []
        lines = []
        with open(dataturks_JSON_FilePath, "r") as f:
            lines = f.readlines()
            for line in lines:
                # line=lines[0]
                data = json.loads(line)
                text = data["content"]
                entities = []
                annotations = []
                for annotation in data["annotation"]:
                    point = annotation["points"][0]
                    label = annotation["label"]
                    annotations.append(
                        (
                            point["start"],
                            point["end"],
                            label,
                            point["end"] - point["start"],
                        )
                    )
                print(annotations[3])
                annotations = sorted(
                    annotations, key=lambda student: student[3], reverse=True
                )
                print(annotations)
                seen_tokens = set()
                count_common = 0
                count_overlaped = 0
                for annotation in annotations:

                    start = annotation[0]
                    end = annotation[1]
                    labels = annotation[2]
                    if start not in seen_tokens and end - 1 not in seen_tokens:
                        count_common = count_common + 1
                        seen_tokens.update(range(start, end))
                    else:
                        count_overlaped = count_overlaped + 1
                        print("{} {} {} esta overlapeada".format(start, end, labels))
                        if not isinstance(labels, list):
                            labels = [labels]

                        for label in labels:
                            # dataturks indices are both inclusive [start, end] but spacy is not [start, end)
                            entities.append((start, end + 1, label))
                training_data.append((text, {"entities": entities}))
        print(count_common)
        print(count_overlaped)
        return training_data
    except Exception as e:
        logging.exception(
            "Unable to process " + dataturks_JSON_FilePath + "\n" + "error = " + str(e)
        )
        return None


class SpacyConverterTrainer:
    """
    Convertidor de formato Dataturks a Spacy y eliminador de repetidos .

    Metodos disponibles:
    create_blank_model(path_save_model: str)--> Crea un modelo en blanco
    create_custom_spacy_model(spacy_model: str, path_save_model: str)--> crea un modelo partiendo de un modelo de  spacy
    add_new_entity_to_model(ents: list, model_path: str)--> Agrega nuevas entidades para entrenar al modelo
    train_model(
        path_data_training: str, n_iter: int, model_path: str, ents: list
    )--> Entrena un modelo n_iter veces con la data en formato dataturks pasada.
    """

    def create_blank_model(self, path_save_model: str):
        """
        Crea un modelo en blanco .
        :param path_save_model: path donde se guardar el modelo

        """
        nlp = spacy.blank("es")
        nlp.to_disk(path_save_model)
        logger.info("Modelo creado exitosamente {path_save_model}...")

    def create_custom_spacy_model(self, spacy_model: str, path_save_model: str):
        """
        Crea un modelo en base al modelo pasado por parametro .
        :param spacy_model: modelo de spacy a partir de base
        :param path_save_model: path donde se guardar el modelo

        """
        nlp = spacy.load(spacy_model)
        nlp.to_disk(path_save_model)
        logger.info("Modelo creado exitosamente {path_save_model}...")

    def add_new_entity_to_model(self, ents: list, model_path: str):
        """
        Agrega nuevas entidades al modelo para entrenar
        :param ents: lista de entidades a entrenar
        :param model_path: path del modelo a  utilizar

        """

        nlp = spacy.load(model_path)
        ner = nlp.pipe_names
        if not ner:
            component = nlp.create_pipe("ner")
            nlp.add_pipe(component)
        ner = nlp.get_pipe("ner")
        for ent in ents:
            ner.add_label(ent)

        nlp.to_disk(model_path)

        logger.info("Agregados exitosamente las entidades al {model_path}...")

    def convert_dataturks_to_spacy(self, convert_data_path: str, output_path: str):
        """
        Dado una data en formato dataturks, la transforma para formato spacy.
        :param convert_data_path: path del output de dataturks
        :param output_path: path del archivo resultante

        """
        logger.info(f"Loading convert data from {convert_data_path} ...")
        training_data = []
        log = convert_dataturks_to_spacy(convert_data_path)
        print(log)
        with open(output_path, "a+") as f:
            training_data.append(convert_dataturks_to_spacy(convert_data_path))
        with open(output_path, "wb") as output:
            pickle.dump(training_data, output, pickle.HIGHEST_PROTOCOL)
        logger.info("Informacion convertida exitosamente")

    def train_model(
        self, path_data_training: str, n_iter: int, model_path: str, ents: list
    ):
        """
        Dado una data en formato dataturks, la transforma para formato spacy.
        :param path_data_training: path de la info a entrenar
        :param n_iter: Numero de cantidad de veces que se va correr el scripts
        :param model_path: path del modelo a  utilizar
        :ents: lista de entidades a entrenar
        """

        training_data = removeEntitiesNotInList(
            convert_dataturks_to_spacy(path_data_training), ents
        )
        nlp = spacy.load(model_path)

        # get names of other pipes to disable them during training
        pipe_exceptions = ["ner"]
        other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]

        # only train NER
        with nlp.disable_pipes(*other_pipes), warnings.catch_warnings():
            # show warnings for misaligned entity spans once
            warnings.filterwarnings("once", category=UserWarning, module="spacy")
            nlp.begin_training()
            for itn in range(n_iter):
                random.shuffle(training_data)  # Se randomiza
                losses = {}
                # Crea mini paquetes
                batches = minibatch(training_data, size=compounding(4.0, 32.0, 1.001))
                #
                for batch in batches:
                    texts, annotations = zip(*batch)
                    nlp.update(
                        texts,  # batch of texts
                        annotations,  # batch of annotations
                        drop=0.5,  # dropout - make it harder to memorise data
                        losses=losses,
                    )
                print("Losses", losses)
        # save model to output directory
        nlp.to_disk(model_path)

    def get_entities(self, model_path: str, text: str):
        """
        Dado una data en formato dataturks, la transforma para formato spacy.
        :param model_path:ruta del modelo
        :param text: texto a traducir.
        """
        nlp = spacy.load(model_path, disable=["tagger", "parser"])
        doc = nlp(text)
        print(doc.ents)

    def all_files_in_folder(
        self, path_folder: str, n_iter: int, model_path: str, ents: list
    ):
        """
        Entrenar un modelo con todos los archivos en la carpeta actual.
        :n_iter:numero de iteraciones
        :param model_path:ruta del modelo
        :param ents: Lista de las entidades a anonimizar.
        """
        onlyfiles = [f for f in listdir(path_folder) if isfile(join(path_folder, f))]
        for file in onlyfiles:
            self.train_model(path_folder + file, n_iter, model_path, ents)


if __name__ == "__main__":
    fire.Fire(SpacyConverterTrainer)