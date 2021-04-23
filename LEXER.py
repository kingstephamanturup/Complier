from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        
        self.lexer.add('PRINT', r'print')
        
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        self.lexer.add('OPEN_BRAC', r'\{')
        self.lexer.add('CLOSE_BRAC', r'\}')
       
        self.lexer.add('SEMI_COLON', r'\;')
        
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')

        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')

        self.lexer.add('IF', r'\if(statement)')
        self.lexer.add('IF...ELSE', r'\if(statement)..else(statement)')
        self.lexer.add('TRY...CATCH', r'\try(statement)....catch(statement)')
       
        self.lexer.add('NUMBER', r'\d+')
        
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
