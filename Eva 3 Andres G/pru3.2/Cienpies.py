

class Cienpies():
    patas = ''
    veneno = ''
    def __init__(self,patas,veneno):
        self.patas = patas
        self.veneno = veneno
        
    
    def Picar(self):
        p  = input('Este Cienpies puede Picar? : ')
        if p == 'si':
            print('Este Cienpies SI puede picar')
        elif p == 'no':
            print('Este Cienpies NO puede picar')

    def __str__(self):
        return '''
        Se creo un Cienpies con {} Patas y {} es Venenoso..
        '''.format(self.patas,self.veneno)

'''c = Cienpies('1000', 'si')
print(c)'''
        