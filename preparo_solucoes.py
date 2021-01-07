from curva_calibracao import Curva

class Solucoes(Curva):
    def __init__(self, vidraria_estoque, vidraria_padrao, pipeta):
        self.vidraria_estoque = vidraria_estoque
        self.vidraria_padrao = vidraria_padrao
        self.pipeta = pipeta
                
    def preparo_solucoes(self, curva):
        
            list = []            
            for i in range(curva.pontos):
                list.append(i)
            return list


glicose = Curva(10,1,10,"g/ml")
print(glicose)
print(glicose.curva_calib())

solucoes = Solucoes(1000,100,1)

print(solucoes.preparo_solucoes(glicose))