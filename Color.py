import turtle

class Color(turtle.Turtle):
    
    '''Cada uno de los objetos colores que aparecen en el juego'''

    def __init__(self,x,y,color='gray'):
        super().__init__()
        self._i=-1
        self.speed(0)
        self.coordenadas=(x,y)
        self.color=color

    def pinta_pos(self):
        '''Ocultamos la tortuga y la mandamos a la posición correspondiente donde
        pintaremos un punto de su atributo color'''
        self.hideturtle()
        self.penup()
        self.setpos(self.coordenadas)
        self.dot(40,self.color)

    def pinta_pos_s(self):
        '''Pinta los colores de pista que son de menor tamaño '''
        self.hideturtle()
        self.penup()
        self.setpos(self.coordenadas)
        self.dot(15,self.color)
        
    def pinta_seleccionado(self):
        '''Nos permite mostrar el color seleccionado en todo momento'''
        self.hideturtle()
        self.penup()
        self.setpos(self.coordenadas)
        self.dot(25,self.color)
        
    def pinta_respuesta(self,lista_colores):
        '''Cuando pierdes, te muestra los colores secretos por pantalla'''
        print(lista_colores)
        self.hideturtle()
        self.penup()
        self.setpos(self.coordenadas)
        
        self.dot(40,lista_colores[0])
        self.setpos(self.coordenadas[0]+42,self.coordenadas[1])
        
        self.dot(40,lista_colores[1])
        self.setpos(self.coordenadas[0]+84,self.coordenadas[1])
        
        self.dot(40,lista_colores[2])
        self.setpos(self.coordenadas[0]+126,self.coordenadas[1])
        
        self.dot(40,lista_colores[3])
        self.setpos(self.coordenadas[0]+168,self.coordenadas[1])
        