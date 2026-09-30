#classe
class Pessoa:

    def __init__(self, nome, idade, salario=0):
        self.set_nome(nome)
        self.set_idade(idade)
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

    # getter e setter do salário
    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        # Verifica se o salário é negativo
        if salario < 0:
            raise ValueError("Salário não pode ser negativo.")
        self._salario = salario

class Paciente(Pessoa):
    def __init__(self, nome, idade,salario,posicao):
        super().__init__(nome, idade,salario)
        self._posicao_fila = posicao 
        
    @property
    def funcao(self):
        return self._posicao_fila 
            

class Medico(Pessoa):
    def __init__(self, nome, idade,salario):
        super().__init__(nome, idade,salario)
        self._qtd_pacientes = Paciente
        
    @property
    def num_pacientes(self):
        return self._qtd_pacientes
    
class Calcula:
    
    def __init__(self):
        self._qtd = 0
    #calcula media dos salarios            
    def _media_sal(self,p1,p4):
        self._total1 = (p1.get_salario() + p4.get_salario()) / 2
        return self._total1
    
    #calcula media das idades   
    def _num_total_pacientes(self):
        self._qtd += 1
        for Pacientes in Pessoa:
            
            return self._qtd
    
    def _num_fila(self):
        for Pacientes in Paciente:

        return self._total =      
              

#main                
if __name__ == "__main__":
    pacientes = [Paciente("Ana",23,3000),
                 Paciente("Bia",18,2000),
                 Paciente("José",27,5000)]
    #p1 = Paciente("Ana", 23,3000,calcular._num_fila) # primeira pessoa criada
    #p2 = Paciente("Bia", 18,2000) 
    #p3 = Paciente("José", 27,4000)
    
    medico = Medico("Joâo", 33,10000) 

    #imprime as informações da primeira pessoa
    print("Pessoa 1:")
    print("Nome:", p1.get_nome())
    print("Idade:", p1.get_idade())
    print("Salário:", p1.get_salario())

    #imprime as informações da segunda pessoa
    print("\nPessoa 2:")
    print("Nome:", p2.get_nome())
    print("Idade:", p2.get_idade())
    print("Salário:", p2.get_salario())
    
    print("\nPessoa 2:")
    print("Nome:", p3.get_nome())
    print("Idade:", p3.get_idade())
    print("Salário:", p3.get_salario())
        
    print("\nPessoa 4:")
    print("Nome:", medico.get_nome())
    print("Idade:", medico.get_idade())
    print("Salário:", medico.get_salario())
    
    


    #atribui a classe Calcula
    Calcular = Calcula()

    i = 0
    while i < 3: 
        print("Média dos salários paciente {i}: ",  Calcular._media_sal(Paciente[i], medico))
          

    #teste de exceção para idade negativa
    try:
        p3 = Pessoa("Carlos", -5, , 3000)
    except ValueError as erro:
        print("Criação recusada:", erro)  


