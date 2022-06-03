class Pessoa:
    def __init__(self,*filhos, nome='João', idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    joao = Pessoa(nome='João')
    claudio = Pessoa(joao, nome='Claudio')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    for filho in claudio.filhos:
        print(claudio.filhos)
    claudio.sobrenome = 'Flavio'
    del claudio.filhos
    print(claudio.__dict__)
    print(joao.__dict__)
