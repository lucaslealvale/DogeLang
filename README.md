# DOGELANG
Atividade Prática Supervisionada da matéria Lógica da Computação  
![diagrama](/diagrams/dogeLogo.jpg)  

### História e motivação  
 Uma foto de um cão da raça Shiba Inu viralizou em meados de 2013, devido à expressão na qual o animal fora fotografado, com as patas ligeiramente cruzadas e o mais importante um semblânte de desconfiança em sua face.  
 Essa postura somada à uma porção de palavras escritas em fonte comic sans com gráfia duvidosa (escrita informal da língua Inglesa), foi a receita de sucesso para o nascimento do maior meme de cachorro da história.  
 A partir dessa imagem muitas variações e montagens foram criadas e hoje existem acervos enormes na internet do doge. O meme ficou tão grande que ele se expandiu e criaram uma criptomoeda só dele a Dogecoin, moeda que explodiu em crescimento em 2021. Devido à popularidade do mesmo na internet e à grandes personalidades a impulsionando tal como Elon Musk.  
 Então como forma de agradecimento e de passar a palavra de Doge este projeto tomou forma, para quem conhece as falas atribuidas ao cachorro nas charge, algumas delas viraram a sintaxe desta linguagem de programação simples.  

Abaixo segue a EBNF da linguagem a qual possui as falas.  

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
