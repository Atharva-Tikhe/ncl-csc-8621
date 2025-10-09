import csv
import os
from collections import defaultdict

from question import Question


class QuestionManager:
    """TODO : Add decorator or utility method for input type validation"""

    def __init__(self, questions=None):
        if questions is None:
            self.__questions = []
        elif type(questions) == list:
            element_types = [isinstance(obj, Question) for obj in questions]
            if False in element_types:
                # write test, true and false assert
                raise TypeError(
                    f"Input list contains atleast one non-Question object: Got {questions}"
                )
            else:
                # IMPORTANT (Duplication removal) : using fromkeys keeps the order of questions but removes the duplicates.
                # TODO : Ask mr. omid or dr. warrender about input duplication validation
                self.__questions = list(dict.fromkeys(questions))
        else:
            raise TypeError(
                f"`questions` should be a list of questions. Got: {type(questions)}"
            )

    """
    @property
    def questions(self):
        return self.__questions
    """

    def get_questions(self):
        """return questions list"""
        return self.__questions

    def __str__(self):
        return f"QuestionManager({self.__get_questions})"

    def __repr__(self):
        return f"QuestionManager(questions = {self.__questions})"

    def add_question(self, question):
        """Appends the question to the list"""
        if isinstance(question, Question):
            searched_questions = [
                True if _question == question else False
                for _question in self.__questions
            ]
            if True in searched_questions:
                raise ValueError(
                    f"Duplicate question! question already in the system: {searched_questions}"
                )
            else:
                self.__questions.append(question)
        else:
            raise TypeError(f"Expected `Question` object. Got: {type(question)}")

    def remove_question(self, question):
        """

        Note: questions.remove() doesn't work because __eq__ references self
        """
        if isinstance(question, Question):
            for index, _question in enumerate(self.__questions):
                if _question == question:
                    self.__questions.pop(index)
        else:
            raise TypeError(
                f"Unexpected object instead of Question. Got: {type(question)}"
            )

    def edit_question(self, old_question, new_question):
        if (
            isinstance(old_question, Question)
            and isinstance(new_question, Question)
            and old_question != new_question
        ):
            self.__questions = [
                new_question if old_question == question else question
                for question in self.__questions
            ]
            return self.get_questions()
        else:
            raise TypeError(
                f"Input questions to edit are of wrong type. Got: old_question: {type(old_question)} \n new_question: {type(new_question)}"
            )

    def search_by_text(self, text):
        results_list = []
        if isinstance(text, str):
            for question in self.__questions:
                if text.strip().upper() == question.get_text().strip().upper():
                    results_list.append(question)
            return results_list
        else:
            raise TypeError(f"Unexpected text type. Expected 'str'. Got: {type(text)}")

    def search_by_total_marks(self, total_marks):
        results_list = []
        if isinstance(total_marks, int):
            for question in self.__questions:
                if total_marks == question.get_total_marks():
                    results_list.append(question)
            return results_list
        else:
            raise TypeError(
                f"Unexpected total_marks type. Expected 'int'. Got: {type(total_marks)}"
            )

    def get_questions_by_topic_and_last_attempt(self, topic, last_attempt):
        results_list = []
        if isinstance(topic, str) and isinstance(last_attempt, bool):
            for question in self.__questions:
                if (
                    topic == question.get_topic()
                    and last_attempt == question.get_last_attempt()
                ):
                    results_list.append(question)
            return results_list
        else:
            raise TypeError(
                f"Unexpected types. Expected 'str,bool'. Got: {type(topic)},{type(last_attempt)}"
            )

    def get_category_count_per_topic(self):
        result_dict = defaultdict(int)
        for question in self.__questions:
            result_dict[question.topic] += 1
        return dict(result_dict)

    def load_from_file(self, file_name):
        questions_to_add = []
        with open(os.path.abspath(file_name), "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if len(row) == 9:
                    questions_to_add.append(row)
                else:
                    print("Unexpected columns", len(row), row)

        for question in questions_to_add[1:]:
            temp_options = dict.fromkeys(["a", "b", "c", "d"])
            (
                temp_options["a"],
                temp_options["b"],
                temp_options["c"],
                temp_options["d"],
            ) = (question[1], question[2], question[3], question[4])

            temp_answers = set(question[5])

            marks_per_question = int(question[6])

            # 8th index is last attempt column, cant pass it directly, convert to string and then pass boolean.
            if question[8].lower().capitalize() == "True":
                last_attempt = True
            else:
                last_attempt = False

            self.add_question(
                Question(
                    question[0],  # text
                    temp_options,
                    temp_answers,
                    marks_per_question,
                    question[7],  # topic
                    last_attempt,
                )
            )

    def save_to_file(self, file_name):
        print(self.__questions[0].to_dict())
        try:
            with open(os.path.abspath(file_name), "w") as f:
                writer = csv.writer(f)
                field_names = [
                    "text",
                    "option_a",
                    "option_b",
                    "option_c",
                    "option_d",
                    "answers",
                    "marks_per_answer",
                    "topic",
                    "last_attempt",
                ]
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(
                    [question.to_dict() for question in self.get_questions()]
                )

        except Exception as e:
            print(f"Error writing file: {e}")


if __name__ == "__main__":
    q1 = Question(
        "q1 : What is 1+1?",
        {"a": "11", "b": "2", "c": "1", "d": "10"},
        {"b"},
        1,
        "maths",
        True,
    )

    q2 = Question(
        "q2 : What is 1+1?",
        {"a": "2", "b": "11", "c": "1", "d": "10"},
        {"b"},
        1,
        "algebra",
        False,
    )
    q3 = Question(
        "q3 : What is nothing?",
        {"a": "11", "b": "2", "c": "1", "d": "10"},
        {"b"},
        1,
        "maths",
        True,
    )

    q = QuestionManager([q1, q2])
    q.add_question(q3)
    """
    print(q.get_questions_by_topic_and_last_attempt("maths", True))
    print(q.get_questions())
    print(q.get_category_count_per_topic())
    print(q.get_questions())
    """
    print(q.load_from_file("../sample_data.csv"))
    q.save_to_file("test2.csv")
