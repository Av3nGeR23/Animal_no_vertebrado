from Cienpies import *
from Estrella import *



class Animal_No_Vertebrado(Estrella, Cienpies):
    columna_vertebral = ''

    def __init__(self, columna_vertebral, patas, veneno, color, tamano):
        super().__init__(patas, veneno)
        super().__init__(color, tamano)
        self.patas = patas
        self.veneno = veneno
        self.color = color
        self.tamano = tamano
        self.columna_vertebral = columna_vertebral

    def __str__(self):
        return '''
        Este es un animal no Vertebrado   ...
        '''.format(self.columna_vertebral, self.patas, self.veneno, self.color, self.tamano)





