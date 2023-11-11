import tkinter as tk
from collections import deque
from tkinter import messagebox

def limpiar_frame(frame, texto):
    for item in frame.winfo_children():
        item.destroy()

    titulo = tk.Label(frame, text=texto, bg="white", font=("Comic Sans MS", 30, "bold"))
    titulo.pack()

def tablero_inicial(num_letras, frame):
    def mostrar_ventana_exito():
        global aciertos
        respuesta = messagebox.askyesno("¡Éxito!", "¡Has acertado la palabra! ¿Quieres jugar de nuevo?")
        if respuesta:
            texto_wordle.set("")
            aciertos = str(int(aciertos) + 1)
            print(aciertos)
            menu_inicial(frame)
        else:
            ventana.quit()

    def mostrar_ventana_fallo():
        global fallos
        respuesta = messagebox.askyesno("¡Se acabaron los intentos!", "¡No has acertado la palabra! ¿Quieres jugar de nuevo?")
        if respuesta:
            texto_wordle.set("")
            fallos = str(int(fallos) + 1)
            print(aciertos)
            menu_inicial(frame)
        else:
            ventana.quit()

    def elegir_palabra(num_letras):
        import random
        archivo_palabras = f"{num_letras}letras.txt"

        try:
            with open(archivo_palabras, "r", encoding="utf-8") as archivo:
                palabras = archivo.read().splitlines()
            
                if palabras:
                    palabra_elegida = random.choice(palabras)
                    return palabra_elegida
                else:
                    return None

        except FileNotFoundError:
            return None  
        
    palabra_aleatoria = elegir_palabra(num_letras)     

    def verificar_palabra(event):
        print(palabra_aleatoria)
        palabra_ingresada = texto_wordle.get()
        if len(palabra_ingresada) == num_letras:
            if len(palabras_ingresadas) <= 5:
                palabras_ingresadas.append(palabra_ingresada)
                fila = 0
                for palabra in palabras_ingresadas:
                    for i, letra in enumerate(palabra):
                        label_letra = tk.Label(frame_tablero, text=letra, font=("Comic Sans MS", 30, "bold"), width=2,
                                                   height=1, relief="solid")
                        label_letra.grid(row=fila, column=i, padx=5, pady=5, sticky="snew")
                    fila += 1
        if len(palabras_ingresadas) == 6 and palabra_ingresada != palabra_aleatoria:
            mostrar_ventana_fallo()
        if palabra_ingresada == palabra_aleatoria:
            mostrar_ventana_exito()
    def convertir_mayuscula(event):
        contenido = entry_wordle.get()
        entry_wordle.delete(0, tk.END)
        entry_wordle.insert(0, contenido.upper())
    def limitar_longitud(*args):
        texto = texto_wordle.get()
        if len(texto) > num_letras:
            texto_wordle.set(texto[:num_letras])

    limpiar_frame(frame, "Wordle")

    frame_entry = tk.Frame(frame, bg="white")
    frame_entry.pack(fill="both", expand=True, padx=10, pady=10)

    texto_wordle = tk.StringVar()
    texto_wordle.trace_add("write", limitar_longitud)

    entry_wordle = tk.Entry(frame_entry, textvariable=texto_wordle, font=("Comic Sans MS", 15), justify="center")
    entry_wordle.pack(fill="both", expand=True, padx=10, pady=10)
    palabras_ingresadas = deque()
    frame_tablero = tk.Frame(frame, bg="white")
    frame_tablero.pack(fill="both", expand=True, padx=10, pady=10)

    for i in range(6):
        for j in range(num_letras):
            label_vacio = tk.Label(frame_tablero, text="", font=("Comic Sans MS", 30, "bold"), width=2, height=1, relief="solid")
            label_vacio.grid(row=i, column=j, padx=5, pady=5, sticky="snew")

    frame_marcadores = tk.Frame(frame, bg="white")
    frame_marcadores.pack()


    label_aciertos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), bg="green", text="Aciertos:", fg="white")
    label_aciertos.grid(row=0, column=0, padx=5, pady=5)

    text_aciertos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), text=aciertos)
    text_aciertos.grid(row=0, column=1, padx=5, pady=5)

    label_fallos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), bg="red", text="Fallos:", fg="white")
    label_fallos.grid(row=1, column=0, padx=5, pady=5)

    text_fallos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), text=fallos)
    text_fallos.grid(row=1, column=1, padx=5, pady=5)
    entry_wordle.bind("<KeyRelease>", convertir_mayuscula)
    entry_wordle.bind("<Return>", verificar_palabra)

def menu_inicial(frame):
    limpiar_frame(frame, "Elije el número de letras para jugar")

    label_botones = tk.Label(frame)
    label_botones.pack(pady=10)

    boton_1 = tk.Button(label_botones, text="4 letras", font=("Comic Sans MS", 15), command=lambda: tablero_inicial(4, frame))
    boton_1.grid(row=0, column=0, padx=10)

    boton_2 = tk.Button(label_botones, text="5 letras", font=("Comic Sans MS", 15), command=lambda: tablero_inicial(5, frame))
    boton_2.grid(row=0, column=1, padx=10)

    boton_3 = tk.Button(label_botones, text="6 letras", font=("Comic Sans MS", 15), command=lambda: tablero_inicial(6, frame))
    boton_3.grid(row=0, column=2, padx=10)

    boton_4 = tk.Button(label_botones, text="7 letras", font=("Comic Sans MS", 15), command=lambda: tablero_inicial(7, frame))
    boton_4.grid(row=0, column=3, padx=10)

    boton_5 = tk.Button(label_botones, text="8 letras", font=("Comic Sans MS", 15), command=lambda: tablero_inicial(8, frame))
    boton_5.grid(row=0, column=4, padx=10)

ventana = tk.Tk()
ventana.title("Wordle")
ventana.resizable(0, 0)
frame = tk.Frame(ventana, bg="white")
frame.pack(fill="both", expand=True)
aciertos = "0"
fallos = "0"
menu_inicial(frame)
ventana.mainloop()

