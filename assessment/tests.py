import unittest

from question import Question


class TestQuestion(unittest.TestCase):
    def setUp(self):
        """Create a base valid Question object for reuse."""
        self.q = Question(
            "What is 1+1?",
            {"a": "11", "b": "2", "c": "1", "d": "10"},
            {"b"},
            1,
            "maths",
            False,
        )

    def test_valid_initialization(self):
        self.assertEqual(self.q.text, "What is 1+1?")
        self.assertIsInstance(self.q.options, dict)
        self.assertIsInstance(self.q.answers, set)
        self.assertEqual(self.q.marks_per_answer, 1)
        self.assertEqual(self.q.topic, "maths")
        self.assertFalse(self.q.last_attempt)

    def test_invalid_text_type_raises(self):
        with self.assertRaises(TypeError):
            Question(123, {}, set(), 1, "maths", False)

    def test_invalid_options_type_raises(self):
        with self.assertRaises(TypeError):
            Question("Q", ["a", "b"], set(), 1, "maths", False)

    def test_invalid_answers_type_raises(self):
        with self.assertRaises(TypeError):
            Question("Q", {}, ["a"], 1, "maths", False)

    def test_invalid_marks_type_raises(self):
        with self.assertRaises(TypeError):
            Question("Q", {}, set(), "1", "maths", False)

    def test_invalid_marks_value_raises(self):
        with self.assertRaises(ValueError):
            Question("Q", {}, set(), 0, "maths", False)

    def test_invalid_topic_type_raises(self):
        with self.assertRaises(TypeError):
            Question("Q", {}, set(), 1, 123, False)

    def test_invalid_last_attempt_type_raises(self):
        with self.assertRaises(TypeError):
            Question("Q", {}, set(), 1, "maths", "False")

    # --- Getter Tests ---
    def test_getters(self):
        self.assertEqual(self.q.get_text(), "What is 1+1?")
        self.assertEqual(
            self.q.get_options(), {"a": "11", "b": "2", "c": "1", "d": "10"}
        )
        self.assertEqual(self.q.get_answers(), {"b"})
        self.assertEqual(self.q.get_marks_per_answer(), 1)
        self.assertEqual(self.q.get_topic(), "maths")
        self.assertFalse(self.q.get_last_attempt())

    # --- String and Repr ---
    def test_str_contains_key_fields(self):
        result = str(self.q)
        self.assertIn("Question(", result)
        self.assertIn("maths", result)
        self.assertIn("1+1", result)

    def test_repr_contains_debug_format(self):
        result = repr(self.q)
        self.assertIn("Question(text=", result)
        self.assertIn("last_attempt", result)

    # --- Equality and Hash ---
    def test_equality_same_content(self):
        q2 = Question(
            " What is 1+1? ",
            {"a": "11", "b": "2", "c": "1", "d": "10"},
            {"b"},
            1,
            " Maths ",
            False,
        )
        self.assertTrue(self.q == q2)
        self.assertFalse(hash(self.q) == hash(q2))

    def test_inequality_different_marks(self):
        q2 = Question(
            "What is 1+1?",
            {"a": "11", "b": "2", "c": "1", "d": "10"},
            {"b"},
            2,
            "maths",
            False,
        )
        self.assertFalse(self.q == q2)

    def test_total_marks_single_answer(self):
        self.assertEqual(self.q.get_total_marks(), 1)

    def test_total_marks_multiple_answers(self):
        q2 = Question(
            "Select prime numbers",
            {"a": "2", "b": "3", "c": "4", "d": "5"},
            {"a", "b", "d"},
            2,
            "maths",
            False,
        )
        self.assertEqual(q2.get_total_marks(), 6)


if __name__ == "__main__":
    unittest.main()
