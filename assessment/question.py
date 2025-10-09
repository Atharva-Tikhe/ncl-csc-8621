class Question:
    def __init__(self, text, options, answers, marks_per_answer, topic, last_attempt):
        """Initialize with basic validation"""
        if type(text) is str:
            self.text = text
        else:
            raise TypeError(f"`text` should be a string. Got: {type(text)}")

        if type(options) is dict:
            key_types = [isinstance(obj, str) for obj in options.keys()]
            value_types = [isinstance(obj, str) for obj in options.values()]
            if False in key_types or False in value_types:
                raise ValueError(
                    f"dictionary keys and values are supposed to be string. Got: keys: {options.keys()}\t values: {options.values()}"
                )
            else:
                self.options = options
        else:
            raise TypeError(f"`options` should be a dictionary. Got: {type(options)}")

        if type(answers) is set:
            self.answers = answers
        else:
            raise TypeError(f"`answers` should be a set. Got: {type(answers)}")

        if type(marks_per_answer) is int:
            if marks_per_answer >= 1:
                self.marks_per_answer = marks_per_answer
            else:
                raise ValueError(
                    f"`marks_per_answer` should be greater than or equal to 1. Got: {marks_per_answer}"
                )
        else:
            raise TypeError(
                f"`marks_per_answer` should be an integer. Got: {marks_per_answer}"
            )

        if type(topic) is str:
            self.topic = topic
        else:
            raise TypeError(f"`topic` should be a string. Got: {type(topic)}")

        if type(last_attempt) is bool:
            self.last_attempt = last_attempt
        else:
            raise TypeError(
                f"`last_attempt` should be a boolean. Got: {type(last_attempt)}"
            )

    def get_text(self):
        return self.text

    def get_options(self):
        return self.options

    def get_answers(self):
        return self.answers

    def get_marks_per_answer(self):
        return self.marks_per_answer

    def get_topic(self):
        return self.topic

    def get_last_attempt(self):
        return self.last_attempt

    def __str__(self):
        """Returns string representation of object for general users"""
        return f"Question({self.text}, {self.options}, {self.answers}, {self.marks_per_answer}, {self.topic}, {self.last_attempt})"

    def __repr__(self):
        """Returns representation of the object for debugging and development"""
        return (
            f"Question(text={self.text!r}, options={self.options!r}, "
            f"answers={self.answers!r}, marks_per_answer={self.marks_per_answer!r}, "
            f"topic={self.topic!r}, last_attempt={self.last_attempt!r})"
        )

    def __eq__(self, other):
        """Check equality between given question object `other` and instance

        Note: strings are stripped and converted to upper case to match question content and not case or \n \r etc
        """

        if (
            other.text.strip().upper() == self.text.strip().upper()
            and other.options == self.options
            and other.answers == self.answers
            and other.topic.strip().upper() == self.topic.strip().upper()
            and other.marks_per_answer == self.marks_per_answer
            and other.last_attempt == self.last_attempt
        ):
            return True
        else:
            return False

    def __hash__(self):
        return hash(
            (
                self.text,
                self.topic,
                self.marks_per_answer,
                self.last_attempt,
            )
        )

    def get_total_marks(self):
        if len(self.answers) > 1:
            return self.marks_per_answer * len(self.answers)
        else:
            return self.marks_per_answer

    def to_dict(self):
        """UTILITY FUNCTION : to convert list of questions to a dictionary, unpacks options and answers"""
        option_a, option_b, option_c, option_d = list(self.get_options().values())
        answers = list(self.get_answers())[0]
        temp_dict = dict.fromkeys(
            [
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
        )
        temp_dict["text"] = self.get_text()
        temp_dict["option_a"] = option_a
        temp_dict["option_b"] = option_b
        temp_dict["option_c"] = option_c
        temp_dict["option_d"] = option_d
        temp_dict["answers"] = answers
        temp_dict["marks_per_answer"] = self.get_marks_per_answer()
        temp_dict["topic"] = self.get_topic()
        temp_dict["last_attempt"] = self.get_last_attempt()

        return temp_dict


if __name__ == "__main__":
    q = Question(
        "What is 1+1?",
        {"a": "11", "b": "2", "c": "1", "d": "10"},
        {"b"},
        1,
        "maths",
        False,
    )
    q1 = Question(
        "What is 1+1?",
        {"a": "11", "b": "2", "c": "1", "d": "10"},
        {"b"},
        1,
        "maths",
        False,
    )

    # test eq and hash
    print(True) if q == q1 else print(False)
    print(q.__hash__())
    print(q1.__hash__())

    # test str and repr
    print(q.__str__())
    print(q.__repr__())

    # test getters
    print(q.get_marks_per_answer())

    q2 = Question(
        "What is 1+1?",
        {"a": 11, "b": "2", "c": "1", "d": "10"},
        {"b"},
        1,
        "maths",
        False,
    )

    print(q2.get_total_marks())
