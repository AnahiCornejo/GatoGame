from tkinter import *
from tkinter import ttk, messagebox

class JuegoDelGato:
    def __init__(self, root):
        # Inicio: Se crea la ventana principal
        self.root = root
        self.root.title("Juego del Gato")
        self.root.configure(bg="#ffeef8")  # Color de fondo suave rosa

        # Inicialización: Se inicializan las variables del juego
        self.tablero = [""] * 9  # Representa el tablero
        self.clicks = 0  # Contador de clics

        # Creación de Botones: Se crean los botones que representan las casillas del tablero
        self.mainframe = ttk.Frame(root, padding="12 12 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.botones = []
        for i in range(3):
            fila = []
            for j in range(3):
                boton = ttk.Button(self.mainframe, text="", command=lambda idx=len(fila) + 3 * i: self.jugar(idx),
                                   style="TButton")
                boton.grid(column=j + 1, row=i + 2, sticky=W, ipadx=20, ipady=20)
                fila.append(boton)
            self.botones.append(fila)

        # Estilo para los botones
        estilo = ttk.Style()
        estilo.configure("TButton", background="#f48fb1", foreground="#880e4f", font=("Helvetica", 16, "bold"))
        estilo.map("TButton", background=[("active", "#f06292")])

        # Botón de reinicio
        self.reinicio_boton = ttk.Button(self.mainframe, text="Reiniciar", command=self.reiniciar, style="TButton")
        self.reinicio_boton.grid(column=1, row=5, columnspan=3, sticky=(E, W))

        # Mostrar Ventana: La ventana del juego se muestra en la pantalla
        self.root.mainloop()

    def jugar(self, indice):
        # Función jugar(indice):
        if self.tablero[indice] == "":
            self.tablero[indice] = "O" if self.clicks % 2 == 0 else "X"  # Asigna "X" o "O"
            self.botones[indice // 3][indice % 3].config(text=self.tablero[indice])
            self.clicks += 1  # Incrementa el contador
            self.verificar_ganador()  # Verificación de Ganador

    def verificar_ganador(self):
        combinaciones_ganadoras = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
            (0, 4, 8), (2, 4, 6)              # Diagonales
        ]

        for a, b, c in combinaciones_ganadoras:
            if self.tablero[a] == self.tablero[b] == self.tablero[c] != "":
                self.mostrar_mensaje(f"Ganador: {self.tablero[a]}")
                self.reiniciar()
                return

        if self.clicks == 9:  # Empate
            self.mostrar_mensaje("Empate!")
            self.reiniciar()

    def mostrar_mensaje(self, resultado):
        messagebox.showinfo("¡Juego Terminado!", resultado)

    def reiniciar(self):
        # Reinicio:
        self.tablero = [""] * 9  # Limpia el tablero
        self.clicks = 0  # Restablece el contador
        
        for fila in self.botones:
            for boton in fila:
                boton.config(text="")  # Actualiza los botones

if __name__ == "__main__":
    root = Tk()
    juego = JuegoDelGato(root)