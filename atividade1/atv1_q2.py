class Gato:
    
    sexo = None
    fertil = None
    cio = None
    prenhe = None
    puerperio = None
    peso = None
    idade = None 
    

    
    def __init__(self, sexo, fertil, prenhe, puerperio, peso, idade):
        self.sexo = sexo
        self.fertil = fertil
        self.prenhe = prenhe
        self.puerperio = puerperio 
        self.peso = peso
        self.idade = idade 

    def engordar(self, peso_ganho):
        self.peso = self.peso + peso_ganho
        
    def envelhecer (self):
        self.idade += self.idade

    def entrar_no_cio(self):
        if (self.sexo == "fêmea" and self.idade >= 1):
            self.cio = True 
        else:
            ("Invalido")
    def sexos_opostos(self, outro_gato):
        return self.sexo != outro_gato.sexo

    def femea_no_cio(self, outro_gato):
        if (self.sexo == 'F' and self.cio):
            return self
        elif (outro_gato.sexo == 'F' and outro_gato.cio):
            return outro_gato
        return None

    def parir(self):
        if (self.sexo == 'F' and self.prenhe == True):
            self.prenhe = False
            self.puerperio = True
            print(self.nome + ' pariu um filho cujo pai é o ' +
                  self.filhos[-1].pai.nome + '. Ela está agora em estado puerperal.')
        else:
            print(self.nome + ' não pode parir')

    def cruzar(self, outro_gato, femea_Cio):
        femea_Cio = self.femea_no_cio(outro_gato)
        if (not self.sexos_opostos(outro_gato)):
            print('O sexo dos gatos devem ser opostos para o cruzamento.')
        elif (femea_Cio == None):
            print('A fêmea deve estar no cio.')
        else:
            femea_Cio.prenhe = True
            filho = Gato("Filho de "+self.nome+" e "+outro_gato.nome, False, False, False, False, 0.1, 0, 'M')
            filho.mae = femea_Cio
            filho.pai = self if self.sexo == 'M' else outro_gato
            self.filhos.append(filho)
            outro_gato.filhos.append(filho)
            print(self.nome + ' e ' + outro_gato.nome + ' cruzaram')

    def tem_filho_de(self, outro_gato):
        for filho in self.filhos:
            if (filho in outro_gato.filhos):
                print('Eu, ' + self.nome + ', tenho filho de ' +
                      outro_gato.nome + '. O nome dele é ' + filho.nome + '.')
                return True
        print('Eu, ' + self.nome + ', não tenho filho de ' + outro_gato.nome + '.')
        return False


if __name__ == "__main__":
    bambino = Gato("Bambino", False, True, False, False, 2.0, 3, 'M')
    bambina = Gato("Bambina", True, False, False, False, 2.0, 3, 'F')
    bambinao = Gato("Bambinao", True, True, False, False, 2.0, 3, 'M')

    # a) Bambino tenta cruzar com o Bambinao
    bambino.cruzar(bambinao)

    # b) Bambino cruza com a Bambina quando ela não está no cio
    bambino.cruzar(bambina)

    # c) Bambina entra no cio
    bambina.entrar_no_cio()

    # d) Bambino cruza com a Bambina quando ela está no cio
    bambino.cruzar(bambina)

    # e) Bambina fica preenhe de Bambino
    bambino.tem_filho_de(bambina)

    # f) Bambina pariu
    bambina.parir()

    # g) Bambino engorda 1 kg
    bambino.engordar(1.0)

    # h) Bambino envelhece 1 ano
    bambino.envelhecer()