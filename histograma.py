from random import seed, random
# Gera n números aleatórios no intervalo [a, b)
def GeraAmostra(a, b, n):
    # Use o seu NUSP como semente
    NUSP = 1234567
    seed(NUSP)
    amostra = n * [0]
    for k in range(n):
        amostra[k] = a + (b - a)*random()
    return amostra

def GeraIntervalos(a, b, m):
    res = m * [[0,0]]
    t = (b-a)/m
    for i in range(m):
        res[i] = [a + t*i, a + t*(i+1)]
    return res

def GeraFrequencias(amostra, intervalos):
    n = len(amostra)
    m = len(intervalos)
    frequencias = m * [0]
    i = 0
    while i<n:
        j = 0
        while j<m and i<n:
            if amostra[i]<intervalos[j][1]:
                frequencias[j]+=1
                i+=1
                j=0
            else:
                j+=1
    return frequencias

def histograma(intervalos, frequencias):
    print("Gráfico")

    h = max(frequencias)
    n = len(intervalos)
    for i in range(h-1,-1,-1):
        for j in range(n):
            if i < frequencias[j]:
                print("%5s"%("\u2588"),end=" ")
            else:
                print(" "*5, end=" ")
        print("\n")
    for k in range(n):
        print("%5.2f" %(intervalos[k][0]),end=" ")
    print('\n')
    for k in range(n):
        print("%5.2f" %(intervalos[k][1]),end=" ")
    print('\n')
    for k in range(n):
        print("%5.03d" %(frequencias[k]),end=" ")
    print('\n')

def main():
    print("="*20)
    novo = input("Novo gráfico? s/n: ")
    if novo == "s":
        dados()
    else:
        print("Fim do Programa")

def dados():
    print("Limites [a, b) com a < b e a >= 0")
    a = float(input("Entre com a: "))
    if a>=0:
        b = float(input("Entre com b: "))
        if b>a and b<100:
            n = int(input("Tamanho da amostra: "))
        
            amostra = GeraAmostra(a, b, n)
            print("Amostra: ")
            for i in amostra:
                print("%.2f" %(i), end=" ")
            print('\n')
            
            n_intervalos = int(input("\nNúmero de Intervalos: "))
            if (b-a)/n_intervalos >=0.01:
                intervalos = GeraIntervalos(a,b,n_intervalos)
                frequencias = GeraFrequencias(amostra, intervalos)

                print("%s %12s" %("Intervalo","Frequencia"))
                for i in range(len(intervalos)):
                    print("%.2f A %.2f" %(intervalos[i][0], intervalos[i][1]),end="")
                    print("%10.03d" %(frequencias[i]))
                print('\n')
                histograma(intervalos, frequencias)
                main()
            else:
                print("Muitos intervalos desejados para o intervalo dado. Insira os dados novamente.")
                main()
        else:
            print("b tem que ser maior que a e menor de 100. Insira os dados novamente.")
            main()
    else:
        print("a tem que ser maior que 0. Insira os dados novamente.")
        main()
    
main()

    
    
    
    
