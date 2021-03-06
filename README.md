# DOGELANG
Atividade Prática Supervisionada da matéria Lógica da Computação  
![diagrama](/diagrams/dogeLogo.jpg)  

### História e motivação  
 Uma foto de um cão da raça Shiba Inu viralizou em meados de 2013, devido à expressão na qual o animal fora fotografado, com as patas ligeiramente cruzadas e o mais importante um semblânte de desconfiança em sua face.  
 Essa postura somada à uma porção de palavras escritas em fonte comic sans com gráfia duvidosa (escrita informal da língua Inglesa), foi a receita de sucesso para o nascimento do maior meme de cachorro da história.  
 A partir dessa imagem muitas variações e montagens foram criadas e hoje existem acervos enormes na internet do doge.  
 O meme ficou tão grande que ele se expandiu e criaram uma criptomoeda só dele a Dogecoin, moeda que explodiu em crescimento em 2021. Devido à popularidade do mesmo na internet e à grandes personalidades a impulsionando tal como Elon Musk.  
 Então como forma de agradecimento e de passar a palavra de Doge este projeto tomou forma, para quem conhece as falas atribuídas ao cachorro nas charges, algumas delas viraram a sintaxe desta linguagem de programação simples.  
  
### Compilador  
 O compilador desta linguagem é feito em python, e ele funciona testadamente em linux por usar caracteristicas do Bash que variam entre sistemas operacionais. As bibliotecas do python útilizadas foram sys, re, ABC e abstractmethod. A primeira como mencionado para ter os recursos do bash para receber o programa a ser compilado, a re é o famoso regex, utilizado para filtrar o programa de entrada e remover comentários prévios à compilação.  
 Os dois últimos auxiliam a criação de classes, permitindo a criação de classes Abstratas assim como em linguagens inteiramente voltadas para programação à objetos.  
 Além disso vale ressaltar que ele é uma variação do projeto da matéria Lógica da computação, aonde fora feito o compilador do zero com base nas aulas e bibliográfia da matéria. Por tanto a propriedade intelectual de toda EBNF e do Diagrama Sintático é da matéria e de seus professores, este projeto é apenas a implementação desta lógica em python.  
 Os maiores desafios deste projeto com certeza fora a implementação de funções, sendo esta a maior e mais díficil sprint. Seguido pela funcionalidade de recursão entre as funções.  
 Para mais informações sobre versionamento e entregas, vide o Git original desta implementação em:  
 https://github.com/lucaslealvale/compilador  
   
### EBNF  
```
EBNF para este compilador:  
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
FACTOR = (("+" | "-" | "dont"), FACTOR) | NUMBER | "(", OREXPRESSION, ")" | IDENTIFIER_FUNC | READLN, "(", ")" ;  
READLN = "listen";  
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;  
NUMBER = DIGIT, { DIGIT } ;  
LETTER = ( a | ... | z | A | ... | Z ) ;  
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;  
NOT("!") =  "dont";  
BOOL = (SUCHFALSE | VERYTRUE) ;  
STRING = " "" LETTER, { LETTER | DIGIT }," "" ;  
```
### Usando DogeLang  
Para usar está linguagem é necessário executar o arquivo python do compilador (DOGELANG.py) junto com o programa que deseja rodar.  
 #### Para compilar e rodar um programa em DogeLang:  
```
$ python3 DOGELANG.py seuArquivo.c 
```

Este projeto possui um arquivo de exemplo que pode ser rodado com o seguinte commando no terminal, dado que este git fora clonado em algum diretório local:  
```
 $ python3 DOGELANG.py example.c
```  
Seguem outros exemplos possiveis (a extensão deve ser .c):  
```
/*code com loop e condicionais*/
int main()
{
    int a;
    int b;
    a = 0;
    b = 1;
    rool ((a < 99999) && (b ==1)){
        a = a +1;
        wow(a);
        veryIf(a == 5){
            b = 0;
            wow("long live DOGE");

        }suchElse veryIf(a==4)
        {
            wow("Obrigado por usar DogeLang");
        }
    }
    wow(a);
}
```
  
```
/*Funções aninhadas*/

int soma(int x, int y)
{
    int res;
    res = x + y;
    return res;    
}

bool comparaSoma()
{
    bool res;
    int x;
    x = 3;
    
    res = soma(x,2) == 8;
    
    return res;
}


int main()
{
    int x;
    bool z;
    
    z = comparaSoma();
    x = z;
    wow(x);
    
}

```
  
```
/*True e False*/
int main()
{
    bool x;
    x = VERYTRUE;
    bool y;
    y = SUCHFALSE;
    veryIf ( x || y){
        wow(1);
    }
    suchElse{
        wow(0);
    }
}
```  
```
/* Recursão*/

int serie(int x)
{
    veryIf (x == 1) {
        return x;
    }suchElse{
    	return x + serie(x-1);
    }
    
}

int main()
{
    int x;
    x = 5;
    wow(serie(x));
    
}

```  
### Diagrama Sintático:  
  
![diagrama](/diagrams/block.PNG)  
![diagrama](/diagrams/command.PNG)  
![diagrama](/diagrams/factor.PNG)  
![diagrama](/diagrams/binOP.PNG)  
