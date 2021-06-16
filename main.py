# Autor: Lucas Leal Vale 
# Disciplina logica da computacao 23/fev/21

import sys
import re
from abc import ABC, abstractmethod

# ===============================================================================================

class Token:
  def __init__(self, tipo, valor):
    self.tipo = tipo
    self.valor = valor
    
# ===============================================================================================

class Tokenizer:
  def __init__(self, origin):
    self.origin = origin
    self.position = 0
    self.actual = Token("",None)

  def selectNext(self):
    
    
    if(self.position == len(self.origin)):
        nextToken = Token("EOF", None)
        self.actual = nextToken

    elif (self.origin[self.position] == "+"):
        nextToken = Token("+", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "-"):
        nextToken = Token("-", None)
        self.position+=1
        self.actual = nextToken
    
    elif(self.origin[self.position] == "*"):
        nextToken = Token("*", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "/"):
        nextToken = Token("/", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "("):
        nextToken = Token("(", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == ")"):
        nextToken = Token(")", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == " "):
        self.position+=1
        self.selectNext()

    elif(self.origin[self.position] == "	"):
        self.position+=1
        self.selectNext()
        
    elif(self.origin[self.position] == ";"):
        nextToken = Token(";", None)
        self.position+=1
        self.actual = nextToken
    
    elif(self.origin[self.position] == ","):
        nextToken = Token(",", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "=" and self.origin[self.position + 1] == "=" ): 
        nextToken = Token("==", None)
        self.position+=2
        self.actual = nextToken
    
    elif(self.origin[self.position] == "="):
        nextToken = Token("=", None)
        self.position+=1
        self.actual = nextToken
    
    elif(self.origin[self.position] == ">"):
        nextToken = Token(">", None)
        self.position+=1
        self.actual = nextToken
    
    elif(self.origin[self.position] == "<"):
        nextToken = Token("<", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "{"):
        nextToken = Token("{", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "}"):
        nextToken = Token("}", None)
        self.position+=1
        self.actual = nextToken

    elif(self.origin[self.position] == "|" and self.origin[self.position + 1] == "|" ):
        nextToken = Token("||", None)
        self.position+=2
        self.actual = nextToken
        
    
    elif(self.origin[self.position] == "&" and self.origin[self.position + 1] == "&" ): 
        nextToken = Token("&&", None)
        self.position+=2
        self.actual = nextToken
    
    elif(self.origin[self.position] == '"'): 
        self.position+=1
        string=''    
        
        while(self.origin[self.position] != '"'):
            
            string += self.origin[self.position]
    
            self.position+=1
        self.position+=1

        nextToken = Token("STRINGV", string)
        self.actual = nextToken

    elif(self.origin[self.position].isalpha()): 
        variavel=""    
        while(self.position < (len(self.origin)) and (self.origin[self.position].isalpha() or self.origin[self.position].isnumeric() or self.origin[self.position] == "_")):
            
            variavel += self.origin[self.position]
    
            self.position+=1
        
        if variavel == "listen":
            nextToken = Token("READ", None)
            self.actual = nextToken

        elif variavel == "wow":
            nextToken = Token("PRINT", None)
            self.actual = nextToken
        
        elif variavel == "dont":
            nextToken = Token("!", None)
            self.actual = nextToken
    
        elif variavel == "return":
            nextToken = Token("RETURN", None)
            self.actual = nextToken
        
        elif variavel == "rool":
            nextToken = Token("WHILE", None)
            self.actual = nextToken

        elif variavel == "veryIf":
            nextToken = Token("IF", None)
            self.actual = nextToken

        elif variavel == "suchElse":
            nextToken = Token("ELSE", None)
            self.actual = nextToken

        elif variavel == "int":
            nextToken = Token("INTV", None) # ESSE
            self.actual = nextToken

        elif variavel == "string":
            nextToken = Token("STRING", "string") # ESSE
            self.actual = nextToken

        elif variavel == "bool":
            nextToken = Token("BOOL", "bool") #ESSE
            self.actual = nextToken

        elif variavel == "VERYTRUE":
            nextToken = Token("BOOLV", "true")
            self.actual = nextToken
        
        elif variavel == "SUCHFALSE":
            nextToken = Token("BOOLV", "false")
            self.actual = nextToken

        else:
            nextToken = Token("ID", variavel)
            self.actual = nextToken

        variavel=""

    elif(self.origin[self.position].isnumeric()):
        
        nextInt=""    
        while(self.position < (len(self.origin)) and (self.origin[self.position].isnumeric())):
            
            nextInt += self.origin[self.position]
            nextToken = Token("INT",int(nextInt))
            self.position+=1
            self.actual = nextToken
            
        nextInt=""

        if((self.origin[self.position]).isalpha()):
            
            raise ValueError


    else:
        print("a",self.origin[self.position])
        raise ValueError
    return    
# ===============================================================================================

class symbolTable:
    # https://www.tutorialspoint.com/python/dictionary_get.htm
    def __init__(self):
        self.symbols = dict()       

    def getValue(self, variavel):
        # print("variavel:",variavel,"table:",self.symbols)
        return (self.symbols[variavel][0],self.symbols[variavel][1],self.symbols[variavel][2],)

    def getFunc(self, funcName):
        # print("getFunc",funcName,"////",TableFuncs.symbols)
        
        if funcName in TableFuncs.symbols:
            return TableFuncs.symbols[funcName]
        else:
            raise ValueError("getFunc",funcName,"////",TableFuncs.symbols)

    def setValue(self, variable, newVariableValue):
        # print("setvalue",variable,newVariableValue)
        if(self.symbols[variable][0]=="bool" and newVariableValue[0] == "int"):
            if newVariableValue[1] > 0:
                self.symbols[variable][1] = 1
            elif newVariableValue[1]<=0:
                self.symbols[variable][1] = 0
        else:

            self.symbols[variable][1] = newVariableValue[1]
        
    def setType(self,  newVariableType, newVariable, conteudo = None):
        # print( newVariableType, newVariable)
        if(newVariable != "return"):
            if(newVariable in self.symbols):
                print(self.symbols)
                print("variavel ja adicionada, tentativa de instanciacao reptida")
                raise ValueError
        self.symbols[newVariable] = [newVariableType, None, conteudo]
# ===============================================================================================

class Parser:
    def __init__(self):
        pass

#---------------------------------------------------------------------------------
    
    def Block(self):
        nodeResult = treeNode()
        
        if self.OBJETO.actual.tipo == "{":
            self.OBJETO.selectNext()
            
            while(self.OBJETO.actual.tipo != "}"):
                node = self.command()
                nodeResult.children.append(node)      

            if self.OBJETO.actual.tipo == "}":
                self.OBJETO.selectNext()

            elif(self.OBJETO.actual.tipo == "EOF"):
                    
                nodeResult.children.append(node)
            
            return nodeResult

                     
#---------------------------------------------------------------------------------
    def FuncDefBlock(self):
        code = treeNode()
        while(self.OBJETO.actual.tipo == "INTV" or self.OBJETO.actual.tipo == "STRING" or self.OBJETO.actual.tipo == "BOOL"):
        
            funcType = self.OBJETO.actual.tipo
            self.OBJETO.selectNext()
            if self.OBJETO.actual.tipo == "ID":
                funcName = self.OBJETO.actual.valor
             
                newFunc = funcDec(funcType,funcName)
                args = treeNode()
              
                self.OBJETO.selectNext()
                if self.OBJETO.actual.tipo == "(":
                    self.OBJETO.selectNext()
                  
                    while( self.OBJETO.actual.tipo != ")"):
                        if (self.OBJETO.actual.tipo == "INTV" or self.OBJETO.actual.tipo == "STRING" or self.OBJETO.actual.tipo == "BOOL"):
                            variavelTipo = self.OBJETO.actual.tipo
                            self.OBJETO.selectNext()
                            if self.OBJETO.actual.tipo == "ID":
                                variavelValor = self.OBJETO.actual.valor
                         
                                if variavelTipo == "INTV":
                                    nodeAssign = UnOp("INTV")
                                    
                                elif variavelTipo == "BOOL":
                                    nodeAssign = UnOp("BOOL")
                                
                                elif variavelTipo == "STRING":
                                    nodeAssign = UnOp("STRING")
                                else: 
                                    raise ValueError 

                                nodeAssign.children[0] = variavelValor  

                                args.children.append(nodeAssign) 

                                self.OBJETO.selectNext()
                                if self.OBJETO.actual.tipo == ",":
                                    self.OBJETO.selectNext()
                                   
                                    if (self.OBJETO.actual.tipo != "INTV" and self.OBJETO.actual.tipo != "STRING" and self.OBJETO.actual.tipo != "BOOL"):
                                        raise ValueError
                        else:
                            raise ValueError
                    if self.OBJETO.actual.tipo == ")":
                        self.OBJETO.selectNext()
                        newFunc.children[0] = args
                        nodeLoop = self.command() 
                        newFunc.children[1] = nodeLoop
                       
                    code.children.append(newFunc)
   
        code.children.append(funcCall("main"))
        self.OBJETO.selectNext()
        if self.OBJETO.actual.tipo != "EOF":
            raise ValueError

        return code
#---------------------------------------------------------------------------------

    def command(self):
        
        if self.OBJETO.actual.tipo == "PRINT":
            
            self.OBJETO.selectNext()
            
            if self.OBJETO.actual.tipo == "(":
                
                nodeCommand = self.orExpression()
                # print("command print")
                prin = println()
                
                prin.children[0] = nodeCommand
               
                if self.OBJETO.actual.tipo == ";":
                    self.OBJETO.selectNext()
                    # print("command print2")
                    return prin
                else:
                    print("DEBUGCommandPrintError: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
                    raise ValueError
            else:
                print("DEBUGCommandPrintError: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
                raise ValueError
        
        # VAR DECLARATION
        elif self.OBJETO.actual.tipo == "BOOL" or self.OBJETO.actual.tipo == "INTV" or self.OBJETO.actual.tipo == "STRING":
     
            tipo = self.OBJETO.actual.tipo

            if tipo == "INTV":
                nodeAssign = UnOp("INTV")
                tipo = "INT"

            elif tipo == "BOOL":
                nodeAssign = UnOp("BOOL")
                tipo = "BOOLV"
            
            elif tipo == "STRING":
                nodeAssign = UnOp("STRING")
                tipo = "STRINGV"
                
            else: 
                raise ValueError 

           
            self.OBJETO.selectNext()
            

            if self.OBJETO.actual.tipo == "ID":
                
                variavel = self.OBJETO.actual.valor
                nodeAssign.children[0] = variavel
                self.OBJETO.selectNext()
                
                if self.OBJETO.actual.tipo == ";" :
                    self.OBJETO.selectNext()
                    
                    return nodeAssign
                else:
                    raise ValueError
            else:
                raise ValueError 
            
            if self.OBJETO.actual.tipo == ";" :
                self.OBJETO.selectNext()
                
                return nodeAssign

        elif self.OBJETO.actual.tipo == "RETURN":
          
            self.OBJETO.selectNext()
            nodeReturn= self.orExpression()
            if self.OBJETO.actual.tipo == ";" :
                self.OBJETO.selectNext()
                node = returnOp(nodeReturn)
                
                return node
            else:
                print("ERRO RETURN")
                raise ValueError 

        elif self.OBJETO.actual.tipo == "ID":
            # print("DEBUG: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
            variavel = self.OBJETO.actual.valor
            self.OBJETO.selectNext()
           
            if self.OBJETO.actual.tipo == "=":
                self.OBJETO.selectNext()

                nodeCommand = self.orExpression()
                nodeAssign = BinOp("=")
                nodeAssign.children[0] = variavel
                nodeAssign.children[1] = nodeCommand
                
                
                if self.OBJETO.actual.tipo == ";" :
                    self.OBJETO.selectNext()
                    
                    return nodeAssign
                
                    
            # FUNCTION CALL
            
            elif self.OBJETO.actual.tipo == "(":
                self.OBJETO.selectNext()
                
                nodeFunctionCall = funcCall(variavel)
             
                while( self.OBJETO.actual.tipo != ")"):
         
                    funcArg = self.orExpression()
               
                    nodeFunctionCall.children.append(funcArg)
                   
                    if self.OBJETO.actual.tipo == ",":
                        self.OBJETO.selectNext()

                if self.OBJETO.actual.tipo == ")":
                    self.OBJETO.selectNext()
                    if self.OBJETO.actual.tipo == ";" :
                        self.OBJETO.selectNext()
                        return nodeFunctionCall
                else:
                    raise ValueError


        elif self.OBJETO.actual.tipo == "WHILE":
            self.OBJETO.selectNext()
            if self.OBJETO.actual.tipo == "(":
                self.OBJETO.selectNext()
                nodeCommand = self.orExpression()
                
                
                if self.OBJETO.actual.tipo == ")":
                    self.OBJETO.selectNext()

                    whileCond = whileCondition()
                    # print("criando no while")
                    whileCond.children[0] = nodeCommand
                
                    nodeLoop = self.command()
                    
                    whileCond.children[1] = nodeLoop
                    
                    return whileCond

                else:
                    raise ValueError 

        elif self.OBJETO.actual.tipo == "IF":
            self.OBJETO.selectNext()
            
            if self.OBJETO.actual.tipo == "(":
                
                self.OBJETO.selectNext()
                
                nodeCommand = self.orExpression()
                
                if self.OBJETO.actual.tipo == ")":
                    
                    self.OBJETO.selectNext()
                    
                    ifCond = ifCondition()
                    ifCond.children[0] = nodeCommand
                
                    nodeIf = self.command()
                    
                    ifCond.children[1] = nodeIf


                    if(self.OBJETO.actual.tipo == "ELSE"):
                        
                        self.OBJETO.selectNext()
                        nodeElse = self.command()
                        ifCond.children[2] = nodeElse

                    return ifCond

                else:
                    
                    print("no closing bracket")
                    raise ValueError
            else:
                print("no opening bracket")
                raise ValueError        
        elif self.OBJETO.actual.tipo == ";":
            self.OBJETO.selectNext()
            nodeNull = NoOp()
            return nodeNull

        elif(self.OBJETO.actual.tipo == "ELSE"):
            print("DEBUGIF: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
            raise ValueError
        else:
            node = self.Block()
            return node
#---------------------------------------------------------------------------------   

    def factor(self):
        # print("factor: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
        if self.OBJETO.actual.tipo == "(":
            self.OBJETO.selectNext()

            nodeFactor = self.orExpression()
            
            if self.OBJETO.actual.tipo == ")":
                
                self.OBJETO.selectNext()
                
                return nodeFactor

            else:
                print("Parentesis Error: ",self.OBJETO.actual.tipo,self.OBJETO.actual.valor)
                raise ValueError

        elif(self.OBJETO.actual.tipo == "READ"):
            self.OBJETO.selectNext()
            
            if self.OBJETO.actual.tipo == "(":
                self.OBJETO.selectNext()

                if self.OBJETO.actual.tipo == ")":
                    nodeFactor = inputEval(self.OBJETO.actual.valor)
                    self.OBJETO.selectNext()
                else:
                    print("erro read1")
                    raise ValueError
            else:
                print("erro read2")
                raise ValueError
                    
        elif (self.OBJETO.actual.tipo == "-"):
            self.OBJETO.selectNext()
            
            nodeFactor = UnOp("-")
            nodeFactor.children[0] = self.factor()

        elif(self.OBJETO.actual.tipo == "+"):
        
            self.OBJETO.selectNext()

            nodeFactor = UnOp("+")
            nodeFactor.children[0] = self.factor()
            
        elif(self.OBJETO.actual.tipo == "!"):
        
            self.OBJETO.selectNext() 

            nodeFactor = UnOp("!")
            nodeFactor.children[0] = self.factor()

        elif self.OBJETO.actual.tipo =="INT":  
            nodeFactor = IntVal(self.OBJETO.actual.valor)
            self.OBJETO.selectNext()
        
        elif self.OBJETO.actual.tipo =="BOOLV":  
            nodeFactor = BoolVal(self.OBJETO.actual.valor)
            self.OBJETO.selectNext()

        elif self.OBJETO.actual.tipo =="STRINGV":  
            nodeFactor = StringVal(self.OBJETO.actual.valor)
            self.OBJETO.selectNext()
            
        elif self.OBJETO.actual.tipo =="ID":  
            variavel2 = self.OBJETO.actual.valor
  
            nodeFactor = variableVal(self.OBJETO.actual.valor)
            nameFunc = nodeFactor
            self.OBJETO.selectNext()

            if self.OBJETO.actual.tipo == "(":
                
                self.OBJETO.selectNext()
                nodeFactor = funcCall(variavel2)
               
                while( self.OBJETO.actual.tipo != ")"):
                  
                    funcArg = self.orExpression()
                    nodeFactor.children.append(funcArg)
                    
                    if self.OBJETO.actual.tipo == ",":
                        self.OBJETO.selectNext()
                
                if self.OBJETO.actual.tipo == ")":
                    self.OBJETO.selectNext()
                    
                                            
                else:
                    print("factor parentesis error")
                    raise ValueError
        
        return nodeFactor
    
#---------------------------------------------------------------------------------   

    def term(self):
        
        nodeTerm = self.factor()
        if self.OBJETO.actual.tipo =="INT":  
            raise ValueError
        
        while(self.OBJETO.actual.tipo == "*" or self.OBJETO.actual.tipo == "/" ):
            
            if(self.OBJETO.actual.tipo == "*"):
                
                self.OBJETO.selectNext()
                
                x = self.factor()
                
                nodeTermCopy = BinOp("*")
                nodeTermCopy.children[0] = nodeTerm
                nodeTermCopy.children[1] = x
                
            elif(self.OBJETO.actual.tipo == "/"):

                self.OBJETO.selectNext()
                x = self.factor()

                nodeTermCopy = BinOp("/")
                nodeTermCopy.children[0] = nodeTerm 
                nodeTermCopy.children[1] = x

            nodeTerm = nodeTermCopy
            
            
        return nodeTerm

#---------------------------------------------------------------------------------

    def RelExpression(self):
        
        returnRel = self.parserExpression()
        
        while(self.OBJETO.actual.tipo == ">" or self.OBJETO.actual.tipo == "<" ):
            if(self.OBJETO.actual.tipo ==">"):
                self.OBJETO.selectNext()
                returnRelEx = self.EqExpression()
                nodeRel = BinOp(">")
                nodeRel.children[0] = returnRel
                nodeRel.children[1] = returnRelEx
            
            elif(self.OBJETO.actual.tipo =="<"):
                self.OBJETO.selectNext()
                returnRelEx = self.EqExpression()
                nodeRel = BinOp("<")
                nodeRel.children[0] = returnRel
                nodeRel.children[1] = returnRelEx
            
            returnRel = nodeRel

        return returnRel

#---------------------------------------------------------------------------------

    def EqExpression(self):
        
        returnEq = self.RelExpression()
        
        while(self.OBJETO.actual.tipo =="=="):
            
            self.OBJETO.selectNext()
            returnEqRel = self.RelExpression()
            nodeEq = BinOp("==")
            nodeEq.children[0] = returnEq
            nodeEq.children[1] = returnEqRel
        
            returnEq = nodeEq

        return returnEq
        
#---------------------------------------------------------------------------------

    def andExpression(self):
        
        returnAnd = self.EqExpression()
        
        while(self.OBJETO.actual.tipo =="&&"):
            self.OBJETO.selectNext()
            returnAndEx = self.EqExpression()
            nodeAnd = BinOp("&&")
            nodeAnd.children[0] = returnAnd
            nodeAnd.children[1] = returnAndEx
        
            returnAnd = nodeAnd

        return returnAnd

#---------------------------------------------------------------------------------

    def orExpression(self):
        
        returnOr = self.andExpression()

        while(self.OBJETO.actual.tipo =="||"):
            self.OBJETO.selectNext()
            returnAndOr = self.andExpression()
            nodeOr = BinOp("||")
            nodeOr.children[0] = returnOr
            nodeOr.children[1] = returnAndOr
        
            returnOr = nodeOr

        return returnOr
        
#---------------------------------------------------------------------------------  
    def parserExpression(self):
        
        nodeParser = self.term()
        
        while(self.OBJETO.actual.tipo == "-" or self.OBJETO.actual.tipo == "+"):
            
            if(self.OBJETO.actual.tipo =="+"):

                self.OBJETO.selectNext()
                proximo = self.term()

                nodeCopy = BinOp("+")
                nodeCopy.children[0] = nodeParser
                nodeCopy.children[1] = proximo
                
            elif(self.OBJETO.actual.tipo =="-"):

                self.OBJETO.selectNext()
                proximo = self.term()

                nodeCopy = BinOp("-")
                nodeCopy.children[0] = nodeParser
                nodeCopy.children[1] = proximo
            
            nodeParser = nodeCopy
        
        return nodeParser
        
#---------------------------------------------------------------------------------  

    def run(self,code):
        
        preproObj = PrePro()
        code = preproObj.filter(code)
        self.OBJETO = Tokenizer(code)
        self.OBJETO.selectNext()
        
        outFuncDefBlock = self.FuncDefBlock()
  
        output = outFuncDefBlock.Evaluate(TableFuncs)
        

            
# ===============================================================================================
# Referencias:
# https://stackoverflow.com/questions/2736255/abstract-attributes-in-python
# https://stackoverflow.com/questions/31457855/cant-instantiate-abstract-class-with-abstract-methods

class node(ABC):
   
    def __init__(self, value):
        super().__init__(value)

    @abstractmethod
    def Evaluate(self,table):
        pass     

# ===============================================================================================
# Referencias:
# https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size

class BinOp(node):
    def __init__(self, value):
        self.value = value
      
        self.children = [None] * 2 
        
    def Evaluate(self,table):

        if self.value =="=":     
            
            return  table.setValue(self.children[0],self.children[1].Evaluate(table))

        
        x = self.children[0].Evaluate(table)
        y = self.children[1].Evaluate(table)
        

        if self.value == "+":
            return  ("int",x[1]+y[1])   

        elif self.value =="-":
            return ("int",x[1]-y[1])

        elif self.value =="/":
            return ("int",int(x[1]/y[1]))
            
        elif self.value =="*":
            return ("int",x[1]*y[1])

        #  Booleanos
        # --------------------------
        elif self.value =="||":
         
            if x[0]=="string" and y[0]=="string":
                raise ValueError
            elif(x[0]=="int") or y[0]=="int":
                if (x[1]>0 or y[1]>0):
                   return ("bool",1)
                else:
                    return ("bool",0)
            
            return ("bool", x[1] or y[1])
        
        elif self.value =="&&":
           
            if x[0]=="string" or y[0]=="string":
                raise ValueError

            elif x[1]==y[1]:
                return ("bool",1)

            else:
                return ("bool",0)

            return ("bool",x[1] and y[1])

        elif self.value =="==":
            if x[0]=="string" and y[0]=="string":
                if x[1]==y[1]:
                    return ("bool",1)
                else:
                    return ("bool",0)

            if x[1]==y[1]:
                   return ("bool",1)
            else:
                return ("bool",0)
            return ("bool",x[1] == y[1])

        elif self.value ==">":
            if x[1]>y[1]:
                   return ("bool",1)
            else:
                return ("bool",0)
            return ("bool",x[1] > y[1])

        elif self.value =="<":
            if x[1]<y[1]:
                   return ("bool",1)
            else:
                return ("bool",0)
            return ("bool",x[1] < y[1])
        
        
# ===============================================================================================
class treeNode():
    def __init__(self):
        
        self.children = [] 
        
    def Evaluate(self,table):
    
        for i in self.children:
            # print("treeNode pre return", i)
            a=i.Evaluate(table)
            
            if (type(i)==returnOp) and type(i) !=funcCall:
                
                return a
         
# ===============================================================================================

class returnOp():
    def __init__(self,children):
        self.children = children
        
    def Evaluate(self,table):
       
        resultado = self.children.Evaluate(table)
        TableFuncs.setType(resultado[0],"return")
        TableFuncs.setValue("return", resultado)
     

# ===============================================================================================

class funcCall():
    def __init__(self,name):
        self.name = name
      
        self.children = []
        
    def Evaluate(self,table):
        
        funcTable = symbolTable()
       
        func = table.getFunc(self.name)
        
        func[2].children[0].Evaluate(funcTable)
       
        if(len(self.children) != len(func[2].children[0].children)):
            raise ValueError

        for i in range(len(self.children)):
   
            tipoVar = funcTable.getValue(func[2].children[0].children[i].children[0])[0]
            tipoFuncVar=self.children[i].Evaluate(table)[0]
            if (tipoVar != tipoFuncVar):
                raise ValueError
            
            funcTable.setValue(func[2].children[0].children[i].children[0], self.children[i].Evaluate(table))
        
        a =func[2].children[1].Evaluate(funcTable)

        if self.name != "main": 
            retornoFunc = TableFuncs.getValue("return")
            
            if retornoFunc[0] != func[0]:
                        
                if retornoFunc[0] == "int" and  func[0] == "INTV":
                    return retornoFunc
                if retornoFunc[0] == "bool" and  func[0] == "BOOL":
                    return retornoFunc
                if retornoFunc[0] == "bool" and  func[0] == "INTV":
                    return retornoFunc  
                raise ValueError("error",retornoFunc[0],func[0])
            
            return retornoFunc
# ===============================================================================================

class funcDec():
    def __init__(self,tipo,nome):
        self.children = [None] * 2  
        self.tipo = tipo
        self.nome = nome
        
    def Evaluate(self,table):
        # print("funcdec",self.children[1].children)
        table.setType(self.tipo,self.nome, self)
# ===============================================================================================
class UnOp(node):
    def __init__(self, value):
        self.value = value
        self.children = [None]

    def Evaluate(self,table):
        if self.value == "BOOL" or self.value == "INTV" or self.value == "STRING":
            # print("debug Set: ",self.children[0],self.children[1]) 
            if(self.value =="BOOL"):
                valor = "bool"
            elif(self.value =="STRING"):
                valor = "string"
            else:
                valor = "int"

            return  table.setType(valor,self.children[0])

        x = self.children[0].Evaluate(table)

        if self.value == "+":
            return  ("int",+x[1])

        elif self.value =="-":

            return  ("int",-x[1])
        
        elif self.value =="!":
            
            return  ("int",not x[1])
        
        
# ===============================================================================================

class println(node):
    def __init__(self):
        
        self.children = [None]

    def Evaluate(self,table):
        
        x = self.children[0].Evaluate(table)
        
        if(type(x[1])==tuple):
            print(x[1][1])
        else:
            print(x[1])

# ===============================================================================================

class ifCondition(node):
    def __init__(self):
        
        self.children = [None] * 3 
        
    def Evaluate(self,table):
        
        
        condition = self.children[0].Evaluate(table)[1]
        
        if type(condition)==str:
            raise ValueError

        if type(condition)==int and condition > 0:
            condition = True

        if  condition == True:
            x = self.children[1].Evaluate(table)
            # print("ifcondition",self.children[0].Evaluate(table)[0],x)
            return (self.children[0].Evaluate(table)[0],x)

        elif self.children[2] != None:
            x = self.children[2].Evaluate(table)
            # print("ifcondition",self.children[0].Evaluate(table)[0],x)
            return (self.children[0].Evaluate(table)[0],x)

            
# ===============================================================================================

class whileCondition(node):
    def __init__(self):
        
        self.children = [None] * 2
        
    def Evaluate(self,table):
       
        while (self.children[0].Evaluate(table)[1] == True):

            x = self.children[1].Evaluate(table)
            # print("x", x)
        return (self.children[0].Evaluate(table)[0],x)    

# ===============================================================================================

class IntVal(node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,table):
        
        return   ("int", self.value)
# ===============================================================================================

class StringVal(node):
    def __init__(self, value):
        self.value = value

    def Evaluate(self,table):
        
        return   ("string", self.value)

# ===============================================================================================

class BoolVal(node):
    def __init__(self, value):
        self.value = value
        
    def Evaluate(self,table):
   
        if self.value == "true":
            return  ("bool",1)

        elif self.value == "false":
            return ("bool",0)

        else:
            raise ValueError 

# ===============================================================================================

class variableVal(node):
    def __init__(self, value):
        self.value = value
        
    def Evaluate(self,table):
        
        return table.getValue(self.value)

# ===============================================================================================

class inputEval(node):
    def __init__(self, value):
        self.value = value
        
    def Evaluate(self,table):

        valor = input()
        
        if valor.isnumeric(): 
            return   ("int",int(valor))
        else:
            print(valor)
            raise ValueError


# ===============================================================================================

class NoOp(node):
    def __init__(self):
        pass
    def Evaluate(self,table):
        return 

# ===============================================================================================

class PrePro:

    def __init__(self):
        pass
        
    def filter(self,codeBruto):
        # codigos de regex disponiveis em: https://stackoverflow.com/questions/241327/remove-c-and-c-comments-using-python , esta funcao ja filtra quase todos comentarios
        codeBruto = re.sub("\n","",codeBruto)
        return re.sub('//.*?\n|/\*.*?\*/', '', codeBruto, flags=re.M)     

# ===============================================================================================

if __name__ == '__main__':
    
    TableFuncs = symbolTable()
    conta = Parser()
    with open(sys.argv[1], 'r') as leitura:
        test = leitura.read()
    conta.run(test)