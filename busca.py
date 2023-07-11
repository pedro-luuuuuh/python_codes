from random import seed, randrange

# locais
locais = ['Agudos', 'Alambari', 'Altinopolis', 'Aluminio', 'Barbosa'
 'Bariri', 'Barra Bonita', 'Barretos', 'Barrinha', 'Candido Rodrigues',
 'Dracena', 'Fartura', 'Fernandopolis', 'Hortolandia', 'Lavinia',
 'Lavrinhas', 'Nantes', 'Narandiba', 'Nhandeara', 'Nipoa',
 'Ouroeste', 'Queiroz', 'Queluz', 'Quintana', 'Rancharia',
 'Sumare', 'Tabapua', 'Tabatinga', 'Urupes', 'Valentim Gentil'
 ]
# profissões
profiss = ['Professor e.m.', 'Faxineiro', 'Mecanico', 'Motorista',
 'Pedreiro', 'Professor e.s.', 'Eletricista', 'Enfermeiro',
 'Analista rh', 'Mestre de Obras', 'Operador', 'Farmaceutico',
 'Soldador', 'Analista Suporte', 'Contador', 'Programador',
 'Gerente adm', 'Gerente com', 'Analista sistemas', 'Medico'
 ]
# nomes
n1 = ["Felicia", "Catulo", "Osmund", "Artmio", "Senizio", "Tilenio"]
n2 = ["Cartuxo", "Olambro", "Romulo", "Ambulo", "Atomon", "Virino"]
n3 = [" Sereno", " Soterno", " Moncoes", " Oscaran", " Topovi", " Talento", ""]
n4 = [" Lasmia", " Mantega", " Casas", " Lorentao", " Melkioz", " Motivio", ""]

def GeraRegistro():
    global n1, n2, n3, n4, locais, profiss

    nome = n1[randrange(6)] + ' ' + n2[randrange(6)] + n3[randrange(7)] + n4[randrange(7)]
    prof = profiss[randrange(len(profiss))]
    loc = locais[randrange(len(locais))]
    return nome + ',' + prof + ',' + loc

def GeraArquivo(aleatorio = 123456, nomearq = 'registros.txt', nreg = 100):
    seed(aleatorio)

    arq = open(nomearq, 'w')
    for k in range(nreg):
        reg = GeraRegistro()
        arq.write(reg+'\n')

        print(k+1,' - ',reg)
    arq.close()

def main():
    NomeArq = input("Entre com o nome do arquivo: ")
    if NomeArq == '':
        return None
    TAB = LeiaArq(NomeArq)
    busca(TAB)

def LeiaArq(NomeArq):

    mat = []

    #tenta abrir o arquivo
    try:
        arq = open(NomeArq, "r")
    #no caso do arquivo não existir, informar o erro
    except:
        print(f"Algo deu errado na abertura do arquivo {NomeArq}.txt")
        print("Certifique-se de colocar .txt no final")
        main()
    #lê cada linha do arquivo e armazena cada peça de informação <nome>, <profissão>, <local>, numa matriz mat
    for linha in arq:
        lin = linha[
            :len(linha)-1]
        v = lin.split(",")
        mat.append(v)
    arq.close()
    return mat

def busca(TAB):
    nome = TirarAcento(input("Entre com o nome ou parte: "))
    profissao = TirarAcento(input("Entre com a profissão ou parte: "))
    local = TirarAcento(input("Entre com o local ou parte: "))
    TAB_filtrado = TAB
    if nome !='':
        TAB_filtrado = list(filter(lambda i:nome in i[0].lower(), TAB_filtrado))
    if profissao !='':
        TAB_filtrado = list(filter(lambda i:profissao in i[1].lower(), TAB_filtrado))
    if local!='':
        TAB_filtrado = list(filter(lambda i:local in i[2].lower(), TAB_filtrado))
    MostrarRegistros(TAB_filtrado, TAB)

def MostrarRegistros(arr,TAB):
    for i in arr:
        print('{0:40} - {1:20} - {2:20}'.format(i[0],i[1],i[2]))
    print('\n'*3)
    busca(TAB)

def TirarAcento(palavra):
    
    conv= { "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u", "â": "a", "ê": "e", "î": "i", "ô": "o", "û": "u", "ã": "a", "õ": "o", "ñ": "n", "ç":"c", "û":"u", "ä":"a", "ë":"e", "ï":"i", "ö":"o", "ß":"ss", "å":"a", "ø":"o", "Ø":"O", "Þ":"?" , "æ":"ae"}
    a = list(palavra.lower())
    for i in range(len(a)):
        try:
            a[i] = conv[a[i]]
        except:
            pass
    b = ''
    
    for i in a:
        b+=i
    return b

main()
