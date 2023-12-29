
import vosk
import pyaudio
import pyttsx3
import random
import time
import pygame
from io import BytesIO

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


# Cargar el modelo una vez fuera de la función
model_path = "C:/Users/Cris/Desktop/recoDeVoz/final/vosk-model-es-0.42"
loaded_model = vosk.Model(model_path)

def recognize_microphone(model):
    rec = vosk.KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

    print("Habla ahora...")

    start_time = time.time()
    recognized_text = ""

    while time.time() - start_time < 5:  # Bucle durante 5 segundos
        data = stream.read(8000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result_dict = eval(result)
            recognized_text += result_dict.get('text', '')

    print("Fin de la grabación.")
    result = rec.FinalResult()
    result_dict = eval(result)
    recognized_text += result_dict.get('text', '')

    return recognized_text.strip()

def precios():
    return random.randint(10,25) 
    
def regateo(cantidad):
    aleatorio = random.randint(10, cantidad)
    return "te llevo por "+str(aleatorio)+" ese es el precio final"
    

def decidir():
    aleatorio = random.random()
    print(aleatorio)
    if aleatorio < 0.8:
        return True
    else:
        return False
        

        
def viajando(partida, destino):
    
    if partida == 1 and destino == 1:  # cine a colón
       hablar("¡En camino!")

    # Definir las coordenadas como una lista de tuplas
       coordenadas = [(195, 177), (200, 360),(350, 360)]

    # Mover a cada posición por separado
       for target_position in coordenadas:
        mover(target_position, 12)

    elif partida == 1 and destino == 2:#cine a estadio

        hablar("¡En camino!")
        coordenadas = [(170, 180),(170, 165)]
    
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 1 and destino == 3:#cine a teleferico
        hablar("¡En camino!")
        coordenadas = [(530, 150),(560, 130),(590, 130),(600, 120),(650, 120),(700, 120),(750, 120),(800, 400)]

        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 2 and destino == 1:#facultad a colon
        hablar("¡En camino!")
        coordenadas = [(700, 430),(630, 430),(600, 455),(500, 455),(400, 455),(350,360)]

        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 2 and destino == 2:#facultad a estadio
        hablar("¡En camino!")
        coordenadas = [(700, 430),(630, 430),(600, 455),(500, 465),(400, 480),(300,480),(255, 480),(240, 360),(230, 300),(230, 250),(190,165)]
        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 2 and destino == 3:#facultad a teleferico
        hablar("¡En camino!")
        coordenadas = [(700, 430),(750, 430),(800, 400)]

        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 3 and destino == 1:#septiembre a colon
        hablar("¡En camino!")
        coordenadas = [(245, 360),(350, 360)]

        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 3 and destino == 2:#septiembre a estadio
        hablar("¡En camino!")
        coordenadas = [(245, 360),(240, 360),(230, 300),(230, 250),(190,165)]

        
        for target_position in coordenadas:
         mover(target_position, 12)
    elif partida == 3 and destino == 3:#septiembre a teleferico
        hablar("¡En camino!")
        coordenadas = [(400, 460),(600, 430),(700, 430),(750, 430),(800, 400)]
        for target_position in coordenadas:
         mover(target_position, 12)
    
    hablar("Ya llegamos")
    min_text = recognize_microphone(loaded_model)
    print("Texto reconocido:", min_text)
                
    if "adiós" in min_text or "chao" in min_text or "hasta luego" in min_text:
        hablar("Págueme por favor")
        min_text = recognize_microphone(loaded_model)
        print("Texto reconocido:", min_text)
                    
        if "cóbrese" in min_text or "se cobra" in min_text:
            hablar("gracias, hasta luego")
    elif "cóbrese" in min_text or "se cobra" in min_text:
        hablar("gracias, hasta luego")
        

def mover(target_position, animation_speed):
    global moving_to_target

    moving_to_target = True

    # Animar el movimiento hacia el objetivo
    while moving_to_target:
        diff_x = target_position[0] - point_rect.x
        diff_y = target_position[1] - point_rect.y

        if abs(diff_x) > animation_speed:
            point_rect.move_ip(animation_speed if diff_x > 0 else -animation_speed, 0)
        elif abs(diff_y) > animation_speed:
            point_rect.move_ip(0, animation_speed if diff_y > 0 else -animation_speed)
        else:
            point_rect.topleft = target_position
            moving_to_target = False

        # Dibujar la imagen y el punto en la pantalla
        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, point_color, point_rect)
        pygame.display.flip()

        # Pequeño retraso para ralentizar el movimiento
        time.sleep(0.15)  # ajusta según sea necesario




if __name__ == "__main__":
    
    # Inicializar Pygame
    pygame.init()
    window_size = (1000, 800)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Moviendo Punto")

    # Cargar la imagen y configurar el punto
    background_image = pygame.image.load("C:/Users/Cris/Desktop/recoDeVoz/final/img/mapa1.jpg")
    point_rect = pygame.Rect(10, 400, 20, 20)
    point_color = (255, 0, 0)  # Rojo
    
    # Parámetros de animación hacia el objetivo
    global target_position, moving_to_target
    target_position = (0, 0)
    moving_to_target = False
    animation_speed = 95  # Ajusta la velocidad de la animación (mayor valor para moverse más rápido)
    
    mover(target_position, animation_speed)#graficando por primera vez
        
    correcto = False
    
    while correcto == False:
        
        hablar("Desde qué punto desea iniciar?")
        texto_reconocido = recognize_microphone(loaded_model)
        print("Texto reconocido:", texto_reconocido)
    
        if "center  " in texto_reconocido or "cine" in texto_reconocido:
            incio = 1 #Quizá les sirva para los gráficos
            correcto = True
            hablar("Punto de incio establecido, cine center")
            target_position = (500, 170)
            mover(target_position, animation_speed)
        elif "facultad" in texto_reconocido or "tecnología" in texto_reconocido or "ciencias" in texto_reconocido:
            incio = 2
            correcto = True
            hablar("Punto de incio establecido, facultad de ciencias y tecnología, universidad mayor de san simón")
            target_position = (700, 510)
            mover(target_position, animation_speed)
        elif "septiembre" in texto_reconocido or "catorce" in texto_reconocido:
            incio = 3
            correcto = True
            hablar("Punto de incio establecido, plaza 14 de septiembre")
            target_position = (310, 500)
            mover(target_position, animation_speed)
        else:
            hablar("Por favor elija uno de los 3 puntos de inicio establecidos")
    
    
    hablar("Iniciando servicio de asistencia")
    texto_reconocido = recognize_microphone(loaded_model)
    print("Texto reconocido:", texto_reconocido)
    

    
    if "disponible" in texto_reconocido or "libre" in texto_reconocido or "en servicio" in texto_reconocido:
        if decidir() == True:
            hablar("buen día,  sí")
            correcto = False
    
            while correcto == False:
                
                hablar("a dónde quiere ir?")
                texto_reconocido = recognize_microphone(loaded_model)
                print("Texto reconocido:", texto_reconocido)
                    
                if "colón" in texto_reconocido:
                    destino = 1 #puede que tambien les sirva
                    correcto = True
                    precio = precios()
                    hablar("Son "+str(precio)+" bolivianos")
                    texto_reconocido = recognize_microphone(loaded_model)
                    print("Texto reconocido:", texto_reconocido)
                elif "estadio" in texto_reconocido or "capriles" in texto_reconocido:
                    destino = 2
                    correcto = True
                    precio = precios()
                    hablar("Son "+str(precio)+" bolivianos")
                    texto_reconocido = recognize_microphone(loaded_model)
                    print("Texto reconocido:", texto_reconocido)
                elif "teleférico" in texto_reconocido:
                    destino = 3
                    correcto = True
                    precio = precios()
                    hablar("Son "+str(precio)+" bolivianos")
                    texto_reconocido = recognize_microphone(loaded_model)
                    print("Texto reconocido:", texto_reconocido)
                else:
                    hablar("Ese no es un destino definido")
            

            if "rebájame" in texto_reconocido or "nada menos" in texto_reconocido or "descuento" in texto_reconocido:
                
                if decidir() == True:
                    hablar(regateo(precio))
                    texto_reconocido = recognize_microphone(loaded_model)
                    print("Texto reconocido:", texto_reconocido)

                    if "llévame" in texto_reconocido or "ya" in texto_reconocido or "vamos" in texto_reconocido:
                        viajando(incio, destino)#Revisar funcion
                    else:
                        hablar("Lo siento, hasta luego. tenga buen día")
                else:
                    hablar("No te puedo rebajar, ese es el precio")
                    texto_reconocido = recognize_microphone(loaded_model)
                    print("Texto reconocido:", texto_reconocido)
                    
                    if "llévame" in texto_reconocido or "ya" in texto_reconocido or "vamos" in texto_reconocido:
                        viajando(incio, destino)
                    else:
                        hablar("Lo siento, hasta luego. tenga buen día")
            
            elif "llévame" in texto_reconocido or "ya" in texto_reconocido or "vamos" in texto_reconocido:
                viajando(incio, destino)
            else:
                hablar("Lo siento, hasta luego. tenga buen día")
            
        else:
            hablar("no estoy en servicio, lo siento")