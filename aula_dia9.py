#classe
class Pessoa:

    def __init__(self, nome, idade, profissao="não informado", salario=0):
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_profissao(profissao)
        self.set_salario(salario)

    # getter e setter do nome
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    # getter e setter da idade
    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        # Verifica se a idade é menor ou igual a zero
        if idade <= 0:
            raise ValueError("Idade deve ser maior que zero.")
        self._idade = idade

    # getter e setter da profissão
    def get_profissao(self):
        return self._profissao

    def set_profissao(self, profissao):
        self._profissao = profissao

    # getter e setter do salário
    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        # Verifica se o salário é negativo
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        self._salario = salario

class Calcula:
    
    def __init__(self):
        self._qtd = 0
    #calcula media dos salarios            
    def _media_sal(self,p1,p2):
        self._qtd += 1
        self._total1 = (p1.get_salario() + p2.get_salario()) / 2
        return self._total1
    
    #calcula media das idades   
    def _media_idade(self,p1,p2):
        self._qtd += 1      
        self._total2 = (p1.get_idade() + p2.get_idade()) / 2
        return self._total2

#main                
if __name__ == "__main__":
    
    p1 = Pessoa("Ana", 23,"Advogada",4000) # primeira pessoa criada

    p2 = Pessoa("Joâo", 33) # segunda pessoa criada

    #imprime as informações da primeira pessoa
    print("Pessoa 1:")
    print("Nome:", p1.get_nome())
    print("Idade:", p1.get_idade())
    print("Profissão:", p1.get_profissao())
    print("Salário:", p1.get_salario())

    #imprime as informações da segunda pessoa
    print("\nPessoa 2:")
    print("Nome:", p2.get_nome())
    print("Idade:", p2.get_idade())
    print("Profissão:", p2.get_profissao())
    print("Salário:", p2.get_salario())


    #atribui a classe Calcula
    Calcular = Calcula()

    #exibe a média dos salários e das idades das duas pessoas utilizando o objetos da classe Pessoa
    print("Média dos salários: ",  Calcular._media_sal(p1, p2))
    print("Média das idades: ",  Calcular._media_idade(p1, p2))      

    #teste de exceção para idade negativa
    try:
        p3 = Pessoa("Carlos", -5, "Professor", 3000)
    except ValueError as erro:
        print("Criação recusada:", erro)  
