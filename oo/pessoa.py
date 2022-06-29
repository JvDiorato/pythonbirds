class Pessoa:
    olhos = 2


    def __init__(self,*filhos, nome='João', idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_de_atributos_de_classe(cls):
        return f'{cls} - olhos  {cls.olhos}'




class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe =super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'



class Mutante(Pessoa):
    olhos = 4

if __name__ == '__main__':
    joao = Mutante(nome='João')
    claudio = Homem(joao, nome='Claudio')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    for filho in claudio.filhos:
        print(claudio.filhos)
    claudio.sobrenome = 'Flavio'
    del claudio.filhos
    claudio.olhos = 1
    del claudio.olhos
    print(claudio.__dict__)
    print(joao.__dict__)
    print(Pessoa.olhos)
    print(joao.olhos)
    print(claudio.olhos)
    print(isinstance(joao, Homem))
    print(isinstance(joao, Pessoa))
    print(joao.olhos)
    print(claudio.cumprimentar())