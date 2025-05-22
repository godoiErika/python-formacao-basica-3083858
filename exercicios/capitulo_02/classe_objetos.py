class Estudante:
    def __init__(self, nome='Não Informado', faculdade='Não Informado'):
        self.nome = nome
        self.faculdade = faculdade
        self.campus = 'São José dos Campos'

    def exibir_faculdade(self):
        print(self.nome + ' estuda na ' + self.faculdade + ' em ' + self.campus)


aluno1 = Estudante('João', 'Univap')
aluno2 = Estudante('Maria', 'Unip')
aluno3 = Estudante('Erika', 'Instituto Federal de São Paulo')

aluno1.exibir_faculdade()
aluno2.exibir_faculdade()
aluno3.exibir_faculdade()