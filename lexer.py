from mytoken import MyToken, TokenType

class Lexer:
    def __init__(self, prog):
        self.prog = prog
        self.index = 0
        self.line = 1
        self.char_to_token_type = {
            '[': TokenType.LBRACKET,
            ']': TokenType.RBRACKET,
            '{': TokenType.LBRACE,
            '}': TokenType.RBRACE,
            ',': TokenType.COMMA,
            ':': TokenType.COLON
        }

    def current(self):
        return self.prog[self.index]

    def peek(self):
        return self.prog[self.index + 1]

    def advance(self):
        self.index += 1
        while self.index < len(self.prog) and self.prog[self.index] in ['\t', ' ']:
            self.index += 1

    def match_number(self):
        number_string = ''
        while self.index < len(self.prog) and (self.current().isnumeric() or self.current() == '.'):
            number_string += self.current()
            self.index += 1
        self.index -= 1
        value = float(number_string) if '.' in number_string else int(number_string)
        return MyToken(TokenType.NUMBER, number_string, value, self.line)

    def match_char(self):
        token_type = self.char_to_token_type[self.current()]
        token = MyToken(token_type, self.current(), None, self.line)
        return token

    def match_string(self):
        text = ''
        self.index += 1
        while self.index < len(self.prog) and self.current() != '\"':
            text += self.current()
            self.index += 1
        return MyToken(TokenType.STRING, text, text, self.line)

    def lex(self):
        tokens = []
        while self.index < len(self.prog):
            c = self.current()
            if c.isnumeric():
                tokens.append(self.match_number())
            elif c in self.char_to_token_type:
                tokens.append(self.match_char())
            elif c == '\"':
                tokens.append(self.match_string())
            elif c == '\n':
                self.line += 1
            self.advance()
        return tokens
