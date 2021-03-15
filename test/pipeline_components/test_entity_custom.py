from pipeline_components.entity_custom import (
    EntityCustom,
    law_left_nbors,
    period_rules,
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


if __name__ == "__main__":
    unittest.main()
