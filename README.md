# APS-LinguagemComputacao
Atividade Pratica Supervisionada da matéria Linguagem de Programação

EBNF para este projeto:  
BLOCK = { "{", COMMAND, "}" } ;  
COMMAND = ( λ | ASSIGNMENT | PRINT | BLOCK | WHILE | IF), ";" ;  
ASSIGNMENT = IDENTIFIER, "=", OREXPRESSION ;  
PRINT = "println", "(", OREXPRESSION, ")" ;  
OREXPRESSION = ANDEXPRESSION, { ("||"), ANDEXPRESSION } ;  
ANDEXPRESSION = EQEXPRESSION, { ("&&"), EQEXPRESSION } ;  
EQEXPRESSION = RELEXPRESSION, { ("=="), RELEXPRESSION } ;  
RELEXPRESSION = EXPRESSION, { (">" | "<"), EXPRESSION } ;  
EXPRESSION = TERM, { ("+" | "-"), TERM } ;  
TERM = FACTOR, { ("*" | "/"), FACTOR } ;  
FACTOR = (("+" | "-" | "|"), FACTOR) | NUMBER | "(", OREXPRESSION, ")" | IDENTIFIER | READLN, "(", ")";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
