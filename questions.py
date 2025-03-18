import random
import sys
 # Preguntas para el juego
questions = [
 "¿Qué función se usa para obtener la longitud de una cadena en Python?",
 "¿Cuál de las siguientes opciones es un número entero en Python?",
 "¿Cómo se solicita entrada del usuario en Python?",
 "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
 "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
 ]
 # Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
 ("size()", "len()", "length()", "count()"),
 ("3.14", "'42'", "10", "True"),
 ("input()", "scan()", "read()", "ask()"),
 (
 "// Esto es un comentario",
 "/* Esto es un comentario */",
 "-- Esto es un comentario",
 "# Esto es un comentario",
 ),
 ("=", "==", "!=", "==="),
 ]
 # variable para calcular el puntaje
puntaje = 0
 # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# Hago una lista con todos los datos de questions,answers y el index de correct answers
questions_to_ask = random.choices(list(zip(questions,answers,correct_answers_index)), k=3)
# El usuario deberá contestar 3 preguntas
for question,answer,correct_answer in questions_to_ask:
 # Se selecciona una pregunta aleatoria
 # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer):
        print(f"{i + 1}. {answer}")
 # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        aux = input("Respuesta: ")
        if aux.isnumeric() == False:
            print ("Respuesta no válida")
            sys.exit()
        else:
            aux = int(aux)-1
            if aux >= 4 or aux <= -1:
                print ("Respuesta no válida")
                sys.exit()
            else:
                user_answer = aux
 # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            print("¡Correcto!")
            puntaje += 1
            break
        else:
 # Si el usuario no responde correctamente después de 2 intentos,
 # se muestra la respuesta correcta
            print("Incorrecto. La respuesta correcta es:")
            puntaje -= 0.50
            print (answer)
 # Se imprime un blanco al final de la pregunta
    print()
 # imprimo el puntaje obtenido 
print(puntaje)
