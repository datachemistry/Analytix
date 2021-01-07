class Curva:
        
    def __init__(self, pontos, lim_inf,lim_sup, unid):
        self.pontos = pontos
        self.lim_sup = lim_sup
        self.lim_inf = lim_inf
        self.unid = unid
        self.incremento = (self.lim_sup - self.lim_inf)/(self.pontos - 1)
          
    def __str__(self):
        return f'Sua curva de calibração vai de {self.lim_inf} {self.unid} até {self.lim_sup} {self.unid} e tem {self.pontos} pontos de calibração.'
    
    def curva_calib(self):
        list = []
        for i in range(self.pontos):
            list.append(self.lim_inf + (self.incremento * i))
        return list
   
nitrato_sodio = Curva(6,10,60,"ppm")

print(nitrato_sodio)
print(nitrato_sodio.curva_calib())


poliestireno = Curva(5,200,1000,"mol/l")
print(poliestireno)
print(poliestireno.curva_calib())





