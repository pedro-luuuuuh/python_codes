class Personagem:
    def __init__(self, nome, raca, classe, xp, tendencia):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.xp = xp
        self.tendencia = tendencia
        self.calcNivel()
        self.calcBP()
        
    def calcNivel(self):
        niveis = {0:1, 
                  300:2, 
                  900:3,
                  2700:4,
                  6500:5,
                  14000:6,
                  23000:7,
                  34000:8,
                  48000:9,
                  64000:10,
                  85000:11,
                  100000:12,
                  120000:13,
                  140000:14,
                  165000:15,
                  195000:16,
                  225000:17,
                  265000:18,
                  305000:19,
                  355000:20}
        self.nivel = 0
        for i in range(len(niveis.keys())-1):
            if self.xp>=niveis.keys()[i] and self.xp<niveis.keys()[i+1]:
                self.nivel = niveis.keys()[i]
        if self.nivel == 0:
            self.nivel = 20
    def calcBP(self):
        BP = {0:2,
              5:3,
              11:4,
              17:6}
        self.BP = 0
        for i in range(len(BP.keys())-1):
            if self.xp>=BP.keys()[i] and self.xp<BP.keys()[i+1]:
                self.BP = BP.keys()[i]
        if self.BP == 0:
            self.BP = 20
    def show(self):
        print(f'Nome: {self.nome}')
        print(f'Nível(XP): {self.nivel}({self.xp})')
        print(f'Bônus de Proficiência: {self.BP}')

party = {}

def criacao():
    nome = input("Nome: ")
    raca = input("Raça (Disponíveis apenss Tiefling): ")
    classe = input("Classe (Disponíveis apenas Bruxo): ")
    xp = input("xp inicial: ")
    tendencia = input("Tendencia (ex.: 'BC' = 'Bom e caótico'): ")
    party[nome] = Personagem(nome, raca, classe, xp, tendencia)
    mostrarParty()

def mostrarParty():
    for i in party.keys():
        party[i].show()



criacao()