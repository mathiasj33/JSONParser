from mytoken import TokenType

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.token_type_to_parse_fn = {
            TokenType.LBRACE: self.parse_dict,
            TokenType.LBRACKET: self.parse_list,
            TokenType.STRING: self.parse_string,
            TokenType.NUMBER: self.parse_number
        }

    def peek(self):
        return self.tokens[self.index]

    def advance(self):
        token = self.tokens[self.index]
        self.index += 1
        return token

    def match(self, token_type):
        if self.tokens[self.index].token_type != token_type:
            raise ParseError(self.tokens[self.index].line, 'Expected {}.'.format(token_type))
        return self.advance()

    def matches(self, token_type):
        return self.tokens[self.index].token_type == token_type

    def parse(self):
        token_type = self.peek().token_type
        result = self.token_type_to_parse_fn[token_type]()
        return result

    def parse_dict(self):
        self.match(TokenType.LBRACE)
        result = {}
        while not self.matches(TokenType.RBRACE):
            key = self.parse_string()
            self.match(TokenType.COLON)
            value = self.parse()
            result[key] = value
            if not self.matches(TokenType.RBRACE):
                self.match(TokenType.COMMA)
        self.match(TokenType.RBRACE)
        return result

    def parse_list(self):
        self.match(TokenType.LBRACKET)
        result = []
        while not self.matches(TokenType.RBRACKET):
            value = self.parse()
            result.append(value)
            if not self.matches(TokenType.RBRACKET):
                self.match(TokenType.COMMA)
        self.match(TokenType.RBRACKET)
        return result

    def parse_string(self):
        token = self.match(TokenType.STRING)
        return token.value

    def parse_number(self):
        token = self.match(TokenType.NUMBER)
        return token.value


class ParseError(Exception):
    def __init__(self, line, msg):
        self.line = line
        self.msg = msg
