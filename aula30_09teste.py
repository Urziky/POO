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
    def __init__(self, nome, idade, salario, posicao_fila):
        super().__init__(nome, idade, salario)
        self.set_posicao_fila(posicao_fila)

    def set_posicao_fila(self, posicao_fila):
        if posicao_fila < 1:
            raise ValueError("A posição na fila deve ser maior que zero.")
        self._posicao_fila = posicao_fila

    @property
    def posicao_fila(self):
        return self._posicao_fila

class Medico(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade, salario)
        self._qtd_pacientes = 0

    def atualizar_total_pacientes(self, pacientes):
        self._qtd_pacientes = len(pacientes)
        
    @property
    def num_pacientes(self):
        return self._qtd_pacientes
    
class Calcula:
    @staticmethod
    def calcular_pagamento(medico, paciente):
        media_salarios = (medico.get_salario() + paciente.get_salario()) / 2
        return media_salarios * 0.10

    @staticmethod
    def contar_pacientes(pacientes):
        return len(pacientes)

    @staticmethod
    def numero_na_fila(paciente):
        return paciente.posicao_fila

class atende:
    def __init__(self, medico, paciente, pacientes):
        self.medico = medico
        self.paciente = paciente
        self.pacientes = pacientes

    def realizar_atendimento(self):
        if self.paciente not in self.pacientes:
            raise ValueError("Esse paciente não está na fila.")

        pagamento = Calcula.calcular_pagamento(self.medico, self.paciente)
        self.paciente.set_salario(self.paciente.get_salario() - pagamento)
        self.pacientes.remove(self.paciente)

        for posicao, paciente in enumerate(self.pacientes, start=1):
            paciente.set_posicao_fila(posicao)

        self.medico.atualizar_total_pacientes(self.pacientes)
        print(f"Atendimento realizado para {self.paciente.get_nome()}. Pagamento: R$ {pagamento:.2f}")
        
#main                
if __name__ == "__main__":
    pacientes = [
        Paciente("Ana", 23, 3000, 1),
        Paciente("Bia", 18, 2000, 2),
        Paciente("José", 27, 5000, 3),
    ]

    medico = Medico("João", 33, 10000)
    medico.atualizar_total_pacientes(pacientes)
    calcular = Calcula()

    print("Total de pacientes na fila:", calcular.contar_pacientes(pacientes))
    print("Total de pacientes do médico:", medico.num_pacientes)

    for paciente in pacientes:
        pagamento = calcular.calcular_pagamento(medico, paciente)
        print(f"Paciente: {paciente.get_nome()}")
        print(f"Posição na fila: {calcular.numero_na_fila(paciente)}")
        print(f"Pagamento final: R$ {pagamento:.2f}")

    atendimento = atende(medico, pacientes[0], pacientes)
    atendimento.realizar_atendimento()
    print("Pacientes restantes na fila:", calcular.contar_pacientes(pacientes))
    print("Total atualizado no médico:", medico.num_pacientes)
    for paciente in pacientes:
        print(f"{paciente.get_nome()} agora está na posição {paciente.posicao_fila}.")


    #teste de exceção para idade negativa
    try:
        Paciente("Carlos", -5, 3000, 1)
    except ValueError as erro:
        print("Criação recusada:", erro)  
