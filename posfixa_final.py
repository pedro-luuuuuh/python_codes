import re

global sinais
sinais = ['+','-','*','/','//','%','**','<','>']
global exp0
exp0 = '-(15+2*3**5/7)-3**5'

class Pilha:
    def __init__(self, cont = []):
        self.cont = cont
    def append(self, el):
        t = [el]
        for i in self.cont:
            t.append(i)
        self.cont = t
    def pop(self):
        if len(self.cont) >= 1:
            a = self.cont[0]
        else:
            a = None
        if len(self.cont)>1:
            self.cont = self.cont[1:]
        else:
            self.cont = []
        return a
    def __getitem__(self,k):
        return self.cont[k]
    def __len__(self):
        return len(self.cont)
    def __str__(self):
        t = '{'
        for i in list(reversed(self.cont)):
            t+=str(i)
            t+=', '
        t+='}'
        return t
    def getContent(self):
        return self.cont


def main():
    exp = input('>>> ')
    if exp == 'fim':
        return None
    else:
        nexp = re.findall(r"(\b\d*[\.]?\d+\b|[\(\)\+\*\-\/\%])",exp)
        print(CalculaPosFixa(TraduzPosFixa(sub_dup_op(nexp))))
        main()

#substituir operadores duplos
def sub_dup_op(nexp):
    nnexp = []
    i = 0
    while i<len(nexp):
        el = nexp[i]
        if el not in sinais:
            try:
                nnexp.append(float(el))
            except:
                nnexp.append(el)
        else:
            if i<len(nexp)-1 and el == '*' and nexp[i+1] == '*':
                nnexp.append('**')
                i+=1
            elif i<len(nexp)-1 and el == '/' and nexp[i+1] == '/':
                nnexp.append('//')
                i+=1
            elif i == 0 and el in sinais or i>0 and nexp[i-1] in sinais:
                if el == '+':
                    nnexp.append('>')
                elif el == '-':
                    nnexp.append('<')
            else:
                nnexp.append(el)
        i+=1
    return nnexp

def isDigit(el):
    return type(el) is float or type(el) is int

def isOp(el):
    return el in sinais or el == '('

def prioridade(el):
    if el in sinais:
        return sinais.index(el)
    else:
        return -1

def TraduzPosFixa(nexp):
    op = Pilha()
    res = Pilha()
    for id, k in enumerate(nexp):
        if isDigit(k):
            res.append(k)
            #processa operadores
            while len(op)>0 and op[0]!='(':
                res.append(op.pop())
        elif isOp(k):
            if len(res)>0:
                while isOp(res[0]) and prioridade(k)>prioridade(res[0]):
                    op.append(res.pop())
            op.append(k)
        elif k == ')':
            op.pop()
            while len(op)>0 and op[0]!='(':
                res.append(op.pop())
    
    return res.getContent()

def CalculaPosFixa(nexp):
    temp = Pilha()
    while len(nexp)>0:
        el = nexp.pop()
        if isOp(el):
            if el == '<':
                el = (-1*temp[0])
                temp.pop()
            else:
                t1 = str(temp[0])
                temp.pop()
                t0 = str(temp[0])
                temp.pop()
                el = eval(t0+el+t1)
        temp.append(el)
    return temp[0]


main()