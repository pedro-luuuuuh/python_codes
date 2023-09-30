import copy
import time

# retorna a matriz lida ou [] se houver algum erro
def LeiaMatrizLocal(NomeArquivo):
    # abrir o arquivo para leitura
    try:
        arq = open(NomeArquivo, "r")
    except:
        return [] # retorna lista vazia se deu erro
    # inicia matriz Sudoku a ser lida: 9 linhas x 9 colunas
    mat = [9 * [0] for k in range(9)]
    # ler cada uma das linhas do arquivo
    j = 0
    for linha in arq:
        v = linha.split() # elementos separados por espaços
        # verifica se tem 9 elementos
        if len(v)==9:
        # transforma de string para int se achar conveniente
            for i in range(len(v)):
                try:
                    v[i] = int(v[i])
                    #e se são todos entre '1' e '9'
                    if v[i]<0 or v[i]>9:
                        return []
                except:
                    return []
            mat[j] = v
            j+=1
        else:
            return []
    #Testa se não tem repetição nas linhas, colunas ou quadrados
        #Lembrando que aqui o 0 pode repetir
    if TestaMatrizLida(mat) == False:
        return []
    # fechar arquivo e retorna a matriz lida e consistida
    arq.close()
    return mat

#Testa se a matriz não tem repetição nas linhas, colunas ou quadrados
def TestaMatrizLida(mat):
    if mat == []:
        return False
    #Testa linhas
    for linha in mat:
        for el in linha:
            if SemElementosRepetidos(linha) == False:
                return False
    
    #Testa colunas
    for c in range(9):
        coluna = Coluna(mat,c)
        if SemElementosRepetidos(coluna) == False:
            return False
    
    #Testa quadrados
    for ql in range(2):
        for qc in range(2):
            quad = Quadrado(mat,ql,qc)
            if SemElementosRepetidos(quad) == False:
                return False
    return True

#retorna a linha - função feita para mater o padrão estético do código na função DefineCandidatos
def Linha(mat,l):
    return mat[l]

#retorna uma matriz com elementos mat[i][c] com i variando no range(9)
def Coluna(mat,c):
    coluna = []
    for l in range(9):
        coluna.append(mat[l][c])
    return coluna

# retorna o quadrado ql, qc
# isto é, o quadrado com elementos que são mat[ql+i][qc+j]
# com i e j variando no range(3)
# com ql e qc variando no range(0,9,3)
def Quadrado(mat,ql,qc):
    quad = []
    for l in range(3):
        for c in range(3):
            quad.append(mat[ql*3+l][qc*3+c])
    return quad

#Verifica se uma matriz não tem elementos repetidos
def SemElementosRepetidos (vet):
    for i in vet:
        if vet.count(i)>1 and i!=0:
            return False
    return True

#Imprime a Matriz
def ImprimaMatriz (mat):
    if mat == []:
        return ''
    for linha in range(9):
        for coluna in range(9):
            if coluna!=8:
                print(mat[linha][coluna], end=' ')
            elif linha != 8:
                print(mat[linha][coluna], end='\n')
            else:
                print(mat[linha][coluna], end='\n\n')

#Testa se a matriz está preenchida corretamente e de acordo com as regras do Sudoku
def TestaMatrizPreenchida(mat):
    if mat == []:
        return False
    for linha in mat:
        if linha.count(0) != 0:
            return False
    if TestaMatrizLida(mat) == False:
        return False
    return True

#Define os candidatos a ocupar a posição mat[l][c]
def DefineCandidatos(mat, l, c):
    if mat == []:
        return []
    
    candidatos = [i for i in range(1,10)]

    #Testa para a linha
    linha = Linha(mat, l)
    EliminaCandidatos(candidatos, linha)
    
    #Testa para a coluna
    coluna = Coluna(mat, c)
    EliminaCandidatos(candidatos, coluna)

    #Testa para o quadrado
    if l in [0,1,2]:
        ql = 0
    elif l in [3,4,5]:
        ql = 1
    elif l in [6,7,8]:
        ql = 2
    
    if c in [0,1,2]:
        qc = 0
    elif c in [3,4,5]:
        qc = 1
    elif c in [6,7,8]:
        qc = 2
    
    quad = Quadrado(mat, ql, qc)
    EliminaCandidatos(candidatos, quad)

    return candidatos

#Se tiver um elemento na array (linha, coluna, quadrado) elimina esse dos candidatos
def EliminaCandidatos(candidatos, arr):
    for i in arr:
        try:
            id = candidatos.index(i)
            del candidatos[id]
        except:
            pass


def Sudoku(mat, l=0,c=0):
    if l == 0 and c == 0:
        global contador
        contador = 0
    if mat == []:
        return []
    else:
        if mat[l][c] !=0:
            if l == 8 and c == 8:
                contador+=1
                print('* * * Matriz Completa - Solução',contador,'* * *')
                ImprimaMatriz(mat)
                if TestaMatrizPreenchida(mat):
                    print('* * * Matriz Completa e Consistente')
                    print('\n')
            elif c<8:
                Sudoku(mat, l, c+1)
            elif l<8:
                Sudoku(mat, l+1, 0)
        else:
            candidatos = DefineCandidatos(mat, l, c)
            if candidatos != []:
                for el in candidatos:
                    novo_mat = copy.deepcopy(mat)
                    novo_mat[l][c] = el

                    Sudoku(novo_mat, l, c)

def Candidatos_Vazios(mat):
    res = {}
    for l in range(9):
        for c in range(9):
            cand = DefineCandidatos(mat, l, c)
            if cand == [] and mat[l][c] == 0:
                return res
            elif mat[l][c] == 0:
                res[f"[{l},{c}]"] = cand
    
def main():
    arquivo = input('Entre com o nome do arquivo: ')
    if arquivo == 'fim':
        return None
    mat = LeiaMatrizLocal('sudoku0.txt')
    print('* * * Matriz Inicial * * *')
    ImprimaMatriz(mat)

    tempo1 = time.time()
    Sudoku(mat)
    tempo2 = time.time()
    tempo_decorrido = tempo2-tempo1
    print(f"* * * - Tempo decorrido = {tempo_decorrido} segundos")
    main()

main()
