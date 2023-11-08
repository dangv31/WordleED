import tkinter as tk

def limpiar_frame(frame):
    # Limpia el frame
    for item in frame.winfo_children():
        item.destroy()

    # Imprime el titulo
    titulo = tk.Label(frame, text="Wordle", bg="white", font=("Comic Sans MS", 30, "bold"))
    titulo.pack()

def tablero_inicial(num_letras,frame):
    def limitar_longitud(*args):
        texto = texto_wordle.get()
        if len(texto) > num_letras:
            texto_wordle.set(texto[:num_letras])
    limpiar_frame(frame)
    frame_entry = tk.Frame(frame, bg="white")
    frame_entry.pack(fill="both", expand=True, padx=10, pady=10)
    texto_wordle = tk.StringVar()
    texto_wordle.trace_add("write", limitar_longitud)
    entry_wordle = tk.Entry(frame_entry, textvariable=texto_wordle, font=("Comic Sans MS", 15))
    entry_wordle.pack(fill="both", expand=True, padx=10, pady=10)
    frame_tablero = tk.Frame(frame, bg="white")
    frame_tablero.pack(fill="both", expand=True, padx=10, pady=10)
    for i in range(6):
        for j in range(num_letras):
            label_vacio = tk.Label(frame_tablero, text="", font=("Comic Sans MS", 30, "bold"),width=2, height=1, relief="solid")
            label_vacio.grid(row=i, column=j, padx=5, pady=5, sticky = "snew")
    frame_marcadores = tk.Frame(frame, bg="white")
    frame_marcadores.pack()
    aciertos = "0"
    fallos = "0"
    label_aciertos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), bg="green", text="Aciertos:", fg="white")
    label_aciertos.grid(row=0, column=0, padx=5, pady=5)
    text_aciertos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), text=aciertos)
    text_aciertos.grid(row=0, column=1, padx=5, pady=5)
    label_fallos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), bg="red", text="Fallos:", fg="white")
    label_fallos.grid(row=1, column=0, padx=5, pady=5)
    text_fallos = tk.Label(frame_marcadores, font=("Comic Sans MS", 10), text=fallos)
    text_fallos.grid(row=1, column=1, padx=5, pady=5)

def menu_inicial():
    ventana = tk.Tk()
    ventana.title("Wordle")
    ventana.resizable(0,0)

    frame = tk.Frame(ventana, bg="white")
    frame.pack(fill="both", expand=True)

    label_text1 = tk.Label(frame, text="Elije el numero de letras para jugar", anchor="center",fg="black", font=("Comic Sans MS", 30, "bold"), bg= "white")
    label_text1.pack(pady=10)

    label_botones = tk.Label(frame)
    label_botones.pack(pady=10)
    boton_1 = tk.Button(label_botones, text="4 letras",font=("Comic Sans MS", 15), command= lambda: tablero_inicial(4, frame))
    boton_1.grid(row = 0, column = 0, padx = 10)
    boton_2 = tk.Button(label_botones, text="5 letras", font=("Comic Sans MS", 15), command= lambda: tablero_inicial(5, frame))
    boton_2.grid(row = 0, column = 1, padx = 10)
    boton_3 = tk.Button(label_botones, text="6 letras", font=("Comic Sans MS", 15), command= lambda: tablero_inicial(6, frame))
    boton_3.grid(row = 0, column = 2, padx = 10)
    boton_4 = tk.Button(label_botones, text="7 letras", font=("Comic Sans MS", 15), command= lambda: tablero_inicial(7, frame))
    boton_4.grid(row = 0, column = 3, padx = 10)
    boton_5 = tk.Button(label_botones, text="8 letras", font=("Comic Sans MS", 15), command= lambda: tablero_inicial(8, frame))
    boton_5.grid(row = 0, column = 4, padx = 10)


    ventana.mainloop()


menu_inicial()