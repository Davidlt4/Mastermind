import Pantalla
import Pintador
from Pantalla import p
from random import randint
from Pintador import Pintador

class Partida:
    
    '''Partida que tiene un codigo_secreto, número de intentos y objeto de la clase pintador
    PD: tarda un rato en salir los colores, perdón :)'''
    
    def __init__(self):
        self.colores={'red':1,'yellow':2,'green':3,'blue':4,'orange':5,'purple':6}
        self.colores_respuesta={'1':'red','2':'yellow','3':'green','4':'blue','5':'orange','6':'purple'}
        self.codigo_secreto=self.genera_num()
        self.respuesta=''
        self.intentos=10
        self.pintador=Pintador()
    
    def genera_num(self):
        '''Genera una secuencia de numeros aleatoria'''
        secuencia=''

        while len(secuencia)<4:

            num_ale=str(randint(1,6))
            secuencia+=num_ale

        return secuencia

    def dime_aciertos(self):
        '''calcula los aciertos y los posicionados y en función de estos
        realiza un comportamiento u otro: ganar,peder y mostrar pistas teniendo en cuenta
        el número de intentos'''
        colores_respuesta=self.pintador.registra_respuesta()
        res=''
        acertados=0
        posicionados=0
        
        for color in colores_respuesta:
            res += str(self.colores[color])
            print(res)
            
        print(self.codigo_secreto)
        
        respuesta_lista = list(res)
        codigo_lista = list(self.codigo_secreto)
        
        for i in range(len(respuesta_lista)):
            if res[i] == self.codigo_secreto[i]:
                posicionados += 1
                respuesta_lista[i] = 'X'
                codigo_lista[i] = 'X'
                
        for r in respuesta_lista:        
            if r != 'X' and r in codigo_lista:
                acertados += 1

        print(posicionados,acertados)
        self.pintador.pinta_pistas(posicionados,acertados)
        self.respuesta=res
        
        if self.respuesta==self.codigo_secreto:
            
            self.intentos -= 1
            
            for i in p.turtles():
                i.clear()
                i.hideturtle()
            p.bgpic('mastermind_ganado.gif')
            
            
            with open('records.txt','a') as f:
                nombre=p.textinput('Jugador','Nombre')
                f.write('Jugador: ' + nombre + '  Intentos: ' + str(10-self.intentos) + '  Has ganado' + '\n')
                
            self.intentos=0
            self.pintador.activo=10
            print('Has ganado')
            
            
        else:
            
            self.intentos -= 1
            
            if self.intentos==0:
                
                for i in p.turtles():
                    i.clear()
                    i.hideturtle()
                    
                p.bgpic('mastermind_perdido.gif')
                
                lista_colores=[]
                
                for i in self.codigo_secreto:
                    lista_colores.append(self.colores_respuesta[i])
                print(lista_colores)
                self.pintador.escritor.pinta_respuesta(lista_colores)
                
                with open('records.txt','a') as f:   
                    nombre=p.textinput('Jugador','Nombre')
                    f.write('Jugador: ' + nombre + '  Intentos: ' + str(10-self.intentos) + '  Has perdido :(' + '\n')
                
                print('Has perdido')


    def jugar(self):
        '''Metodo que te permite jugar'''
        ganado=False

        while self.intentos!=0:
            
            p.onclick(self.pintador.selecciona_coordenadas)
            p.onkeypress(self.dime_aciertos,'a')
            p.listen()
            p.update()


party=Partida()
p.tracer(n=100,delay=0)        
party.pintador.pinta_colores_elegir()
party.pintador.pinta_colores_respuesta()
party.pintador.pinta_colores_pista()
party.jugar()
p.mainloop()

