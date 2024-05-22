#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = None  # Initial internal value
        self.value = value  # Use the property setter

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [s for s in self.value.split() if s.endswith(('.', '?', '!'))]
        return len(sentences)


