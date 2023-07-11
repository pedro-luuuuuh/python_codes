a = 'Adran Kairon Roguephile Hiroshi Aurora Fenrir'
def main():
    personagens = a.split(' ')#list(input('Quais personagens? (Separados por espaço): ').split(' '))
    global pers
    pers = {}
    for i in personagens:
        pers.update({i.lower():0})
    #print(pers)
    processaInimigo(pers)

def processaInimigo(pers, historico={}):
    global hist
    tipo = input('Que tipo de monstro? ').lower()
    exp = int(input('Qual o nível de XP gerado? '))
    try:
        historico[tipo]
    except:
        historico.update({tipo:{'xp':exp}})
    res = ['0']*3
    
    print('Quando acabar digite enter\n')
    nome = 'algo'
    while nome!='':
        res = []*3
        nome = input('Nome do Personagem: ')
        if nome=='':
            break
        assist = input('Número de assistências: ')
        kill = input('Número de mortes: ')
        res = [nome.lower(), assist, kill]
        try:
            res[1] = int(res[1])
        except:
            if res!=[]:
                print('O número de assistências deve ser um inteiro')
        try:
            res[2] = int(res[2])
        except:
            if res!=[]:
                print('O número de abates deve ser um inteiro')
        try:
            pers[res[0]] += (exp//2)*res[1] + (exp)*res[2]
            try:
                historico[tipo][res[0]][0]+=res[1]
                historico[tipo][res[0]][1]+=res[2]
            except:
                historico[tipo].update({res[0]:[res[1],res[2]]})
        except:
            if res!=[]:
                
                print('O personagem deve estar presente na lista de personagens inserida no início')
    while res!='s':
        res = input('Deseja inserir um novo monstro?(s/n) ')
        hist = historico
        mostraXP(pers, historico)
        if res=='n':
            return None
    processaInimigo(pers, historico)

def mostraXP(pers, historico):
    for i in pers.keys():
        print('%10s ganhou %5d de XP'%(i.capitalize(),pers[i]))
    print('\n')
    print('O histórico é o seguinte: ')
    print('%12s | %12s | %5s | %8s' %('Nome','Assistências', 'Abates','XP ganho'))
    for i in historico.keys():
        print(f'{i.capitalize()} - {historico[i]["xp"]} XP: ')
        for j in historico[i].keys():
            try:
                print('%12s | %-12d | %-12d| + %-7d XP'%(j.capitalize(),historico[i][j][0],historico[i][j][1],(historico[i]['xp']//2)*historico[i][j][0]+(historico[i]['xp'])*historico[i][j][1]))
            except:
                pass
main()
