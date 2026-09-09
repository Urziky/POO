#classe
class Pessoa:

    def __init__(self, nome,idade,profissao,salario):
        
        self._nome = nome
        self._idade = idade
        self._profissao = profissao
        self._salario = salario
        
class Calcula:
    
    def __init__(self):
        self._qtd = 0
    #calcula media dos salarios            
    def _media_sal(self,a,b):
        self._qtd += 1
        self._total1 = (a+b)/2
        return self._total1
    
    #calcula media das idades   
    def _media_idade(self,a,b):
        self._qtd += 1      
        self._total2 = (a + b)/2
        return self._total2

#main                
if __name__ == "__main__":
    
    p1 = Pessoa("Ana", 23,"Advogada",4000) # primeira pessoa criada

    p2 = Pessoa("Joâo", 33,"Médico",10000) # segunda pessoa criada

    #atribui a classe Calcula
    Calcular = Calcula()

    #exibe a média dos salários e das idades das duas pessoas
    print("Média dos salários: ",  Calcular._media_sal(4000,10000))
    print("Média das idades: ",  Calcular._media_idade(23,33))        
   
    print("Número de vezes que a classe foi usada: ", Calcular._qtd) 