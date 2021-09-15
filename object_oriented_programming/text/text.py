import pymorphy2
from razdel import tokenize, sentenize


class Text:
    morph = pymorphy2.MorphAnalyzer()

    def __init__(self, text):
        self.text = text
        self.tokens = list(tokenize(text))

    def text_length(self):
        return len(self.text)

    def number_of_tokens(self):
        return len(self.tokens)

    def number_of_sentences(self):
        return len(list(sentenize(self.text)))

    def number_of_lemmatized_tokens(self):
        return len(set([self.morph.parse(token.text)[0].normal_form for token in self.tokens]))
