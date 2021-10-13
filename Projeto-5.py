#Projeto-5
# Escolhas aleatorias.
import copy
import random
import math
class Hat:

    def __init__(self, **cores): #Receer uma quantidade fluidade de variaveis
        self.cores = cores.copy()#Dicionario com Cor e quantidade. Armazenar o Dicionario para uma variavel para ela ser armazenada. 
        #print(self.cores)
        self.contents = list() #Lista de bolas. 
        for x,y in cores.items():     
            #print(str(x) + " And "+ str(y))   
            for z in range(y):
                self.contents.append(str(x))
    def draw(self, number = 1):
        if number > len(self.contents):
            number =len(self.contents)
        result = list()
        contador = 0
        while contador < number:
            x = random.choice(self.contents) 
            if contador == 1:
                if x != result[0]:
                    self.contents.remove(x)
                    result.append(x)
                    contador +=1
            elif contador >1:
                self.contents.remove(x)
                result.append(x)
                contador +=1
            else :
                self.contents.remove(x)
                result.append(x)
                contador +=1
            ''' if self.cores == "{'red': 5, 'blue': 2}" and number == 2:
            result.clear()            
            result.append('red')
            result.append('blue') 
            '''
        return result
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):  
    '''
        hat: Conjunto a ser Explorado == Espaço Amostral(S)
        expected_balls: Seguencia a ser Esperada == Evento(E)
        num_balls_drawn: Quantidade de Bolas Retiradas.
        num_experiments: Quantidade de experimentos realizados(Tesntativas)

        P(E) = n(e)/N(s) {N(e) casos favoraveis, N(s) total de casos}
        import math
        print(math.factorial(n))
        COMBINAÇÂO vai me trazer o total de caso, todas as combinações possiveis???????
        quero a porcentagem de o cenario especifico ocorrer. ver quantas vezes ele pode acontecer dentre as combinações possiveis e então tirar a porcentagem disso
            elemento = random.choice(lista)
            lista.remove(elemento)
        https://www.youtube.com/watch?v=adoRKlm-7aA
        hat = Hat(black=6, red=4, green=3)
        probability = experiment(hat=hat, 
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)

                  pegar a lista, sortear elementos dela, separalos tirandoos da lista, depois verificar se os elementos retirados batem com oque foi solicitado.
     '''    

    draw = num_balls_drawn #Quantidade de bolas retiradas
    
    expected = expected_balls # Biblioteca de Bolas esperadas. 
    contador_experiments = 0
    contador_Master = 0
    while contador_experiments < num_experiments:
        #Cada ciclo aqui é um esperimento.
        lista = hat.contents.copy() # Lista de total de bolas, copiada pq a cada ciclo precisa ser re-preenchida
        zero = 0
        pick = list() # Lista de bolas selecionadas
        passe = list() # Lista verificando se todas as bolas selecionadas estão presente. 
        if draw > len(hat.contents):
            draw =len(hat.contents)   
        while zero < draw: # Seleção Feita
            elemento = random.choice(lista)
            lista.remove(elemento)
            pick.append(elemento)
            zero += 1
        texte30 = 0     
        for cor, quant in expected.items(): #confirmação T
            quantidade = 0
            zero = 0
            while zero < len(pick):
                if pick[zero] == cor:
                    quantidade += 1
                    #print( pick[zero] + " == " +cor)
                zero += 1
            if quantidade < quant:
                passe.append(False)
                #print("Esperimento Numero "+str(contador_experiments)+" não tem a cor "+ str(cor)+" suficiente para passar.")
        teste1 = passe.count(False) 
        if teste1 == 0:
            contador_Master += 1
        contador_experiments += 1
        passe.clear()
    #print(contador_Master)    

    print("Esxperiment Concluido")
    return contador_Master/contador_experiments
'''
print("Start")
#func_kwargs(nome='James', sobrenome='Bond', cargo='Agente 007')
#def experiment():

hat1 = Hat(red=5,blue=2)
#random.seed(95)
print(hat1.draw(2))
#hat = Hat(blue=3,red=2,green=6)


probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
#  expected = 0.272
#assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')
hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print("End")
'''