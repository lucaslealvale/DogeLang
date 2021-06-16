# DOGELANG
Atividade Prática Supervisionada da matéria Lógica da Computação
![diagrama](/diagrams/dogeLogo.jpg=250x250)  
Motivação

EBNF para este projeto:  
FUNCDEFBLOCK = ( λ | {TYPEFunc});  
TYPEFunc = ("BOOL" | "INTV" | "STRING"), "IDENTIFIER", "(" ,{"TYPE", "IDENTIFIER", { "," }, } ,")", "COMMAND" ;  
BLOCK = { "{", COMMAND, "}" } ;  
COMMAND = ( λ | ASSIGNMENT | PRINT | TYPE | RETURN | IDENTIFIER_FUNC | BLOCK | WHILE | IF), ";" ;  
ASSIGNMENT = IDENTIFIER, "=", OREXPRESSION ;  
PRINT = "wow", "(", OREXPRESSION, ")" ;  
TYPE = ("BOOL" | "INTV" | "STRING"), IDENTIFIER;  
RETURN = "RETURN", "OREXPRESSION";  
IDENTIFIER_FUNC = "(", OREXPRESSION, { "," } ")" ;  
WHILE = "rool", "(" , "OREXPRESSION", ")", COMMAND ;  
IF = ("veryIf", "(" , "OREXPRESSION", ")", COMMAND), {ELSE, COMMAND};  
ELSE = "suchElse", COMMAND;   
OREXPRESSION = ANDEXPRESSION, { ("||"), ANDEXPRESSION } ;  
ANDEXPRESSION = EQEXPRESSION, { ("&&"), EQEXPRESSION } ;  
EQEXPRESSION = RELEXPRESSION, { ("=="), RELEXPRESSION } ;  
RELEXPRESSION = EXPRESSION, { (">" | "<"), EXPRESSION } ;  
EXPRESSION = TERM, { ("+" | "-"), TERM } ;  
TERM = FACTOR, { ("*" | "/"), FACTOR } ;  
FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | "(", OREXPRESSION, ")" | IDENTIFIER_FUNC | READLN, "(", ")" ;  
READLN = "listen";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
NOT =  "dont", "(", OREXPRESSION, ")" ;  
BOOL = (SUCHFALSE | VERYTRUE) ;  
STRING = " "" LETTER, { LETTER | DIGIT }," "" ;  
 

 para rodar com determinado arquivo de testes:  

<ol>
<li>$ python3 main.py testes.c</li>
</ol>  
  
Diagrama Sintático:  
  
![diagrama](/diagrams/block.PNG)  
![diagrama](/diagrams/command.PNG)  
![diagrama](/diagrams/factor.PNG)  
![diagrama](/diagrams/binOP.PNG)  
