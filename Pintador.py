from Color import Color

#desplazamiento x e y en los colores que aparecen a la izquierda
desplazamiento_x_colores=-123.0
desplazamiento_y_colores=109

#desplazamiento x e y para las pistas de las derecha
desplazamiento_x_pista_left=115.0
desplazamiento_x_pista_right=131.0

desplazamiento_y_pista_up=222.0
desplazamiento_y_pista_down=205.0


#desplazamiento x e y para los colores que vamos a utilizar como respuesta
desplazamiento_x_uno=-48.0
desplazamiento_x_dos=-3.0
desplazamiento_x_tres=38.0
desplazamiento_x_cuatro=79.0

desplazamiento_y = 213.0
ancho = 42

class Pintador():
    '''Clase con la que pintaremos todo aquello que vemos en pantalla
        y nos permitirá mover colores donde corresponde'''
    def __init__(self):
        
        self.colores=['red','yellow','green','blue','orange','purple']
        self.colores_elegir=[Color(desplazamiento_x_colores,desplazamiento_y_colores-41*fila,self.colores[fila])
                             for fila in range(0,6)]
        
        self.colores_respuesta=[[Color(desplazamiento_x_uno,desplazamiento_y-ancho*y),
                                 Color(desplazamiento_x_dos,desplazamiento_y-ancho*y),
                                 Color(desplazamiento_x_tres,desplazamiento_y-ancho*y),
                                 Color(desplazamiento_x_cuatro,desplazamiento_y-ancho*y)]
                                for y in range(0,10)]
        self.color_elegido=None
        self.activo=0
        self.escritor=Color(-122.0,-53.0)
        self.escritor.hideturtle()
        self.seleccionado=Color(-170.0,185.0)
        self.colores_pista=[[Color(desplazamiento_x_pista_left,desplazamiento_y_pista_up-ancho*y),
                             Color(desplazamiento_x_pista_right,desplazamiento_y_pista_up-ancho*y),
                            Color(desplazamiento_x_pista_left,desplazamiento_y_pista_down-ancho*y),
                             Color(desplazamiento_x_pista_right,desplazamiento_y_pista_down-ancho*y)]
                            for y in range(0,10)]

    def pinta_colores_elegir(self):
        '''Recorremos la lista de colores a elegir(colores de la izquierda) y los pintamos'''
        self.seleccionado.pinta_seleccionado()
        for color in self.colores_elegir:
            color.pinta_pos()

    def pinta_colores_respuesta(self):
        '''Recorremos las listas de colores respuesta(colores grises donde ponemos las respuesta)
            y los pinta'''
        for lista in self.colores_respuesta:
            for color in lista:
                color.pinta_pos()

    def pinta_colores_pista(self):
        '''Recorremos las listas de colores pista(puntitos pequeños de la derecha) y los pintamos'''
        for lista in self.colores_pista:
            for color in lista:
                color.pinta_pos_s()
            
    def coge_color_origen(self,a,b):
        '''Teniendo en cuenta el centro de cada color a elegir,definimos el color seleccionado
            y lo guardamos en colore_elegido'''
        color_elegido=''
        
        for color in self.colores_elegir:
            if color.distance(a,b) < 20:
                color_elegido=color.color
                    
        return color_elegido
            
    
    def coge_color_destino(self,a,b,color_elegido):
        '''Teniendo en cuenta el centro de los colores de la respuesta, seleccionamos
            la tortuga que va a cambiar su color al seleccionado'''
        
        for lista in self.colores_respuesta:
            for color in lista:
                if color.distance(a,b) < 20:
                    color.color=color_elegido
                    color.pinta_pos()
                    
    def pinta_pistas(self,posicionados,acertados):
        '''Pinta de color negro y de color blanco en funcion del número de
        posicionados(negro,esta y esta en su posición)
        y de aciertos(blanco, esta el color pero no en la posición)'''
        for pos in range(posicionados):
            if self.colores_pista[self.activo-1][pos].color=='gray':
                self.colores_pista[self.activo-1][pos].color='black'
                self.colores_pista[self.activo-1][pos].pinta_pos_s()
            
        for ace in range(acertados):
            if self.colores_pista[self.activo-1][posicionados+ace].color=='gray':
                self.colores_pista[self.activo-1][posicionados+ace].color='white'
                self.colores_pista[self.activo-1][posicionados+ace].pinta_pos_s()

    def selecciona_coordenadas(self,x,y):
        '''Selecciona la coordenada,en funcion de si es color respuesta o color a elegir
        determina un comportamiento:
            color a elegir: selecciona color
            color respuesta: selecciona la respuesta y cambia al color seleccionado
            con anterioridad(si no se ha seleccionado el color tratamos el error
            para que simplemente no lleve acabo ninguna acción ya que debemos
            seleccionar un color con anterioridad)'''
        print(x,y)
        if -143.0 < x < -103.0:
            self.color_elegido=self.coge_color_origen(x,y)
            print(x,y,self.color_elegido)
            self.seleccionado.color=self.color_elegido
            self.seleccionado.pinta_seleccionado()
        else:
            try:
                for elemento in self.colores_respuesta[self.activo]:
                    if elemento.distance(x,y) < 20:
                        self.coge_color_destino(x,y,self.color_elegido)
                        print(x,y,self.color_elegido)
            except IndexError:
                        print('')
                    
    def registra_respuesta(self):
        '''Registramos la respuesta para que así podamos pintar en la siguiente fila'''
        respuesta=[]
        cont=0
        for elemento in self.colores_respuesta[self.activo]:
            if elemento.color != 'gray':
                cont += 1
        
        if cont==4:
            
            for elemento in self.colores_respuesta[self.activo]:
                respuesta.append(elemento.color)
                
            self.activo += 1
            return respuesta
        


