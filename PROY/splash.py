from Clases.classBanco import Banco
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage

ventana_principal = None
bancoPrincipal = None

if __name__ == "__main__":
    # Funcion para abrir la pantalla principal
    def abrir_pantalla_principal():
        ventana_bienvenida.destroy()  # Cierra la pantalla de bienvenida
        pantalla_principal()  # Abre la pantalla principal

    def Entrada():
        ventana_principal.destroy()
        mainBanco()

    def mainBanco():
        #Funcion que se ejecuta cuando se presione el boton
        def crear_objeto():
            global bancoPrincipal
            nombre = entry_nombre.get()
            numero = entry_numero.get()
            codigo_internacional = entry_codigo.get()
            monto = entry_monto.get()
            if not nombre or not numero or not codigo_internacional or not monto:
                messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
                return
            else:
                bancoPrincipal=Banco(nombre,numero,codigo_internacional,monto)

        def cancelar():
            entry_nombre.delete(0, tk.END)
            entry_numero.delete(0, tk.END)
            entry_codigo.delete(0, tk.END)
            entry_monto.delete(0, tk.END)
            
        def mostrar_informacion():
            if bancoPrincipal is not None:
                info= f"No.: {bancoPrincipal.getnumero()}\nNombre del Banco Principal: {bancoPrincipal.getnombreBanco()}\nCodigo Internacional: {bancoPrincipal.getcodigoInternacional()}\nMonto: {bancoPrincipal.getmontoPrincipal()}"
                messagebox.showinfo("Informacion", info)
            else:
                messagebox.showinfo("Informacion", "El Banco no ha sido Creado aun")

        #Crear la  Ventana Pricipal
        ventana = tk.Tk()
        ventana.title("Datos de Identifiacion")

        #Etiquetas y Campos de Entrada
        tk.Label(ventana, text="Nombre del Banco Principal:").grid(row=0, column=0, padx=10, pady=5)
        entry_nombre = tk.Entry(ventana)
        entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(ventana, text="Numero del Banco:").grid(row=1, column=0, padx=10, pady=5)
        entry_numero = tk.Entry(ventana)
        entry_numero.grid(row=1, column=1, padx=10, pady=5)       

        tk.Label(ventana, text="Codigo Internacional:").grid(row=2, column=0, padx=10, pady=5)
        entry_codigo = tk.Entry(ventana)
        entry_codigo.grid(row=2, column=1, padx=10, pady=5)       

        tk.Label(ventana, text="Monto Principal:").grid(row=3, column=0, padx=10, pady=5)
        entry_monto = tk.Entry(ventana)
        entry_monto.grid(row=3, column=1, padx=10, pady=5)

        #Botones
        btn_guardar = tk.Button(ventana, text="Guardar", command=crear_objeto)
        btn_guardar.grid(row=4, column=0, padx=10, pady=10)

        btn_guardar = tk.Button(ventana, text="Cancelar", command=cancelar)
        btn_guardar.grid(row=4, column=1, padx=10, pady=10)  

        btn_guardar = tk.Button(ventana, text="Mostrar Informacion", command=mostrar_informacion)
        btn_guardar.grid(row=5, column=0, columnspan=10, pady=10)

        #Ejecutar la Ventana
        ventana.mainloop() 

    # Funcion para mostrar la pantalla principal
    def pantalla_principal():
        global ventana_principal
        ventana_principal = tk.Tk()
        ventana_principal.title("Pantalla principal")
        ventana_principal.geometry("600x400")
        label_principal = tk.Label(ventana_principal, text="Bienvenida a la pantalla principal", font=("Arial", 18))
        label_principal.pack(pady=20)
        btn_Saludar = tk.Button(ventana_principal, text="Presione para Continuar", command=Entrada)
        btn_Saludar.pack(pady=10)
        ventana_principal.mainloop() 

    # Configuración de la pantalla de bienvenida
    ventana_bienvenida = tk.Tk()
    ventana_bienvenida.title("Pantalla de Bienvenida")
    ventana_bienvenida.geometry("600x400")

    # Título del sistema
    label_titulo = tk.Label(ventana_bienvenida, text="Iniciando Pagina del Banco", font=("Arial", 24, "bold"))
    label_titulo.pack(pady=10)

    # Logo (Asegúrate de tener el archivo 'PROYECT.png' en el path especificado)
    try:
        logo = PhotoImage(file="src/IMG/PROYECT.png")
        logo = logo.subsample(5)
        label_logo = tk.Label(ventana_bienvenida, image=logo)
        label_logo.pack(pady=20)
    except Exception as e:
        print("No se encontró el archivo del logo:", e)

    # Mensaje de espera
    label_mensaje = tk.Label(ventana_bienvenida, text="Cargando, por favor espere...", font=("Arial", 14))
    label_mensaje.pack(pady=10)

    # Configurar el temporizador para 5 segundos
    ventana_bienvenida.after(5000, abrir_pantalla_principal)

    # Iniciar el loop de la ventana
    ventana_bienvenida.mainloop()