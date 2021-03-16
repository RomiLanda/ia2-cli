from pipeline_components.entity_custom import (
    EntityCustom,
    law_left_nbors,
    period_rules,
    license_plate_left_nbor,
)
from pipeline_components.entity_matcher import (
    EntityMatcher,
    matcher_patterns,
    first_left_nbors,
    second_left_nbors,
    first_right_nbors,
)
from pipeline_components.entity_ruler import ruler_patterns
from spacy.pipeline import EntityRuler
from spacy.tokens import Span
from test.support.env_case import ModelSetup

import itertools
import spacy
import unittest


class EntityCustomTest(unittest.TestCase):
    def setUp(self):
        # Loads a Spacy model
        pipeline = ["entity_ruler", "entity_matcher", "entity_custom"]
        self.nlp = ModelSetup(pipeline)

    def test_a_custom_entity_pipeline_detects_periods(self):
        base_test_senteces = [
            (
                "seis",
                11,
                12,
                "Si se tratare de un instrumento público y con prisión de seis {}, si se tratare de un instrumento privado",
            ),
            (
                "6",
                11,
                12,
                "Si se tratare de un instrumento público y con prisión de 6 {}, si se tratare de un instrumento privado",
            ),
            (
                "67985",
                11,
                12,
                "Si se tratare de un instrumento público y con prisión de 67985 {}, si se tratare de un instrumento privado",
            ),
            (
                "veintitrés mil quinientos",
                11,
                14,
                "Si se tratare de un instrumento público y con prisión de veintitrés mil quinientos {}, si se tratare de un instrumento privado",
            ),
            (
                "tres mil ochocientos noventa y nueve",
                11,
                17,
                "Si se tratare de un instrumento público y con prisión de tres mil ochocientos noventa y nueve {}, si se tratare de un instrumento privado",
            ),
        ]
        for target_span_text, target_span_start, target_span_end, base_test_sentece_text in base_test_senteces:
            for nbor_word in period_rules:
                test_sentence = base_test_sentece_text.format(nbor_word)
                doc = self.nlp(test_sentence)
                # Checks that the text is tokenized the way we expect, so that we
                # can correctly pick up a span with text "seis {nbor}"
                a_like_num_span = Span(doc, target_span_start, target_span_end + 1, label="PERIODO")
                expected_period = f"{target_span_text} {nbor_word}"
                self.assertEqual(a_like_num_span.text, expected_period)
                # Asserts a PERIODO span exists in the document entities
                self.assertIn(a_like_num_span, doc.ents)

    def test_a_custom_entity_pipeline_detects_law_entities(self):
        nums = ["5845", "5666", "6", "12"]
        base_test_senteces = [
            (
                10,
                11,
                "Ha sufrido una modificación relativamente reciente mediante la {law_nbor} número {law_num}, en función de la cual no cualquier persona puede ser autora de esta contravención",
            ),
            (
                24,
                25,
                "Schumacher, Michael s/art. 73 Violar clausura impuesta por autoridad judicial o administrativa (Art. 74 según TC {law_nbor} número {law_num} y modif.)",
            ),
            (
                41,
                42,
                "NO HACER LUGAR a la excepción por manifiesto defecto en la pretensión por atipicidad interpuesta por la defensa (arts. 195, inciso c) y 197 CPPCABA -de aplicación supletoria conforme el art. 6 de la {law_nbor} número {law_num}).",
            ),
        ]

        test_sentences = list(itertools.product(nums, base_test_senteces))

        for (law_num, (target_span_start, target_span_end, base_test_sentece_text)) in test_sentences:
            for left_nbor_word in law_left_nbors:
                test_sentence = base_test_sentece_text.format(law_nbor=left_nbor_word, law_num=law_num)
                doc = self.nlp(test_sentence)
                # Checks that the text is tokenized the way we expect, so that we
                # can correctly pick up a span with text "seis {nbor}"
                expected_span = Span(doc, target_span_start, target_span_end, label="LEY")
                self.assertEqual(expected_span.text, law_num)
                # Asserts a PERIODO span exists in the document entities
                self.assertIn(expected_span, doc.ents)

    def test_a_custom_entity_pipeline_detect_loc_entities(self):
        locs = ["YPF", "504"]
        base_test_senteces = [
            (
                4,
                6,
                "Existio un allanamiento en Barrio {loc_nbor} donde se encontraron estupefacientes ",
            ),
            (
                12,
                14,
                "Existe un procedimiento a llevarse a cabo dentro del radio de la villa {loc_nbor} de la periferia de la ciudad",
            ),
            (
                12,
                14,
                "Existe un procedimiento a llevarse a cabo dentro del radio de la localidad {loc_nbor} de la periferia de la ciudad",
            ),
            (
                23,
                25,
                "En la mañana Fierro, Martin s/art. 23 Inculpar a vecino por desacato judicial o administrativa en la actualidad en Paraje {loc_nbor}",
            ),
        ]

        test_sentences = list(itertools.product(locs, base_test_senteces))

        for (left_nbor_word, (target_span_start, target_span_end, base_test_sentece_text)) in test_sentences:

            test_sentence = base_test_sentece_text.format(loc_nbor=left_nbor_word)

            doc = self.nlp(test_sentence)

            expected_span = Span(doc, target_span_start, target_span_end, label="LOC")
            # Check if span detected in doc.ents
            self.assertIn(expected_span, doc.ents)

    def test_a_custom_entity_pipeline_detect_false_positive_loc_entities(self):
        # Primer test para chequear casos de falsos positivios en PER no esten incluidos en las ocurrencias detectadas
        locs = ["Moreno", "Fierro"]
        base_test_sentences = [
            (
                6,
                8,
                10,
                12,
                "En las personas de  Juan Antonio Barrio {loc_name} y mariela barrio {loc_name} se encontraron estupefacientes ",
            ),
            (6, 8, 10, 12, "Acompañada de otras personas como Roxana villa {loc_name}, Martín Villa {loc_name}  "),
        ]

        test_sentences = list(itertools.product(locs, base_test_sentences))
        for (
            right_loc_word,
            (
                target_span_start,
                target_span_end,
                another_target_span_start,
                another_target_span_end,
                base_test_sentece_text,
            ),
        ) in test_sentences:

            test_sentence = base_test_sentece_text.format(loc_name=right_loc_word)

            doc = self.nlp(test_sentence)

            expected_span = Span(doc, target_span_start, target_span_end, label="LOC")
            another_expected_span = Span(doc, another_target_span_start, another_target_span_end, label="LOC")
            # Filtrado solo entidades del tipo LOC
            # onlyLOCents = list(filter(lambda ent: ent.label_ == "LOC", doc.ents))
            self.assertNotIn(expected_span, doc.ents)
            self.assertNotIn(another_expected_span, doc.ents)

    def test_a_custom_entity_pipeline_detects_license_plates_entities(self):
        base_test_senteces = [
            (
                "AAA 410",
                23,
                25,
                "Tal situación tuvo lugar, en circunstancias en que ambos se encontraban en el interior del vehículo marca Renault Trafic, {license_plate_nbor} colocado {license_plate}.",
            ),
            (
                "AC 154 BC",
                4,
                7,
                "El vehículo {license_plate_nbor}: {license_plate} fue encontrado prendido fuego en la intersección de las Avenidas 1 y 2.",
            ),
            (
                "AC154BC",
                9,
                10,
                "Schumacher, Michael circulaba en el vehículo con {license_plate_nbor} {license_plate} a altas velocidades mientras tiraba objetos desde su vehículo.",
            ),
            (
                "110 ABC",
                3,
                5,
                "{license_plate_nbor} del vehículo {license_plate}, fue visto por última vez el 24 de mayo de 1996.",
            ),
        ]

        for target_span_text, target_span_start, target_span_end, base_test_sentece_text in base_test_senteces:
            for nbor_word in license_plate_left_nbor:
                test_sentence = base_test_sentece_text.format(
                    license_plate_nbor=nbor_word, license_plate=target_span_text
                )
                doc = self.nlp(test_sentence)
                # Checks that the text is tokenized the way we expect, so that we
                # can correctly pick up a span with text "{nbor} AAA 410"
                expected_span = Span(doc, target_span_start, target_span_end, label="PATENTE_DOMINIO")
                self.assertEqual(expected_span.text, target_span_text)
                # Asserts a PATENTE_DOMINIO span exists in the document entities
                self.assertIn(expected_span, doc.ents)

    def test_a_custom_entity_pipeline_removes_articles_marked_as_license_plates_entities(self):
        base_test_senteces = [
            (
                "174bis",
                27,
                28,
                "En lo demás, resolví estar a las medidas cautelares impuestas en sede Civil en los términos de la Ley 26485 en protección de la víctima ({article_marked_as_license_plate} CPP).",
            ),
        ]

        for target_span_text, target_span_start, target_span_end, base_test_sentece_text in base_test_senteces:
            test_sentence = base_test_sentece_text.format(article_marked_as_license_plate=target_span_text)
            doc = self.nlp(test_sentence)
            # Checks that the text is tokenized the way we expect, so that we
            # can correctly pick up a span with text "174bis"
            expected_span = Span(doc, target_span_start, target_span_end, label="ART")
            self.assertEqual(expected_span.text, target_span_text)
            # Asserts a ART span exists in the document entities
            self.assertNotIn(expected_span, doc.ents)


if __name__ == "__main__":
    unittest.main()
