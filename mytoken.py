from enum import Enum

TokenType = Enum('TokenType',
                 'STRING NUMBER LBRACE RBRACE LBRACKET RBRACKET COMMA COLON')

class MyToken:
    def __init__(self, token_type, text, value, line):
        self.token_type = token_type
        self.text = text
        self.value = value
        self.line = line

    def __eq__(self, other):
        if isinstance(other, MyToken):
            return self.text == other.text and self.token_type == other.token_type and self.value == other.value and self.line == other.line
        return False

    def __str__(self):
        if self.value is not None:
            return '{}({})'.format(self.token_type, self.value)
        return '{}'.format(self.token_type)

    def __repr__(self):
        return str(self)
