

class Estrella():
    color = ''
    tamano = ''
    def __init__(self, color,tamano):
       
        self.color = color
        self.tamano = tamano

    def Moverse(self):
        p = input('Este Estrella puede Moverse? : ')
        if p == 'si':
            print('Este Estrella SI puede Moverse ')
        elif p == 'no':
            print('Este Estrella NO puede Moverse')

    def __str__(self):
        return '''
        Se creo un Estrella de color  {} de Tamano {}  ...
        '''.format(self.color,self.tamano)


