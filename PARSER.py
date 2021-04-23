from rply import ParserGenerator
from ast import Number, Sum, Sub, Print, Mul, Div, If, IF..Else, Try..Catch


class Parser():
    def __init__(self, module, builder, printf):
        self.pg = ParserGenerator(
            
            ['NUMBER', 'PRINT', 'OPEN_PAREN', 'CLOSE_PAREN', 'OPEN_BRAC', 'CLOSE_BRAC'
             'SEMI_COLON', 'SUM', 'SUB', 'MUL', 'DIV', 'IF', 'IF..ELSE', 'TRY...CATCH']
        )
        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])
        @self.pg.production('program : PRINT OPEN_BRAC expression CLOSE_BRAC')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : IF condition statement ELSE statement')
        @self.pg.production('expression : TRY condition statement CATCH Statement')
        
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(self.builder, self.module, left, right)

             if operator.gettokentype() == 'MUL':
                return Mul(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(self.builder, self.module, left, right)

             if operator.gettokentype() == 'IF':
                return If(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'ELSE':
                return Else(self.builder, self.module, left, right)

            if operator.gettokentype() == 'TRY':
                return Try(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'CATCH':
                return Catch(self.builder, self.module, left, right)

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()
