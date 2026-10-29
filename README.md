# Proyecto_Inicial_Orientada_Objetos
Este proyecto son las bases de la aplicacion de las clases en un lenguaje para el inicio de la logia de programación para rama Orientada a Objetos

# 🏦 Sistema de Identificación Bancaria - GUI

![Python](https://shields.io)
![Tkinter](https://shields.io)
![Status](https://shields.io)

Una aplicación de escritorio intuitiva desarrollada en **Python** utilizando **Tkinter** para la gestión y registro de información de entidades bancarias. El sistema cuenta con un flujo de navegación que incluye una pantalla de bienvenida y un formulario de captura de datos con validaciones en tiempo real.

---

## ✨ Características

*   **Pantalla de Bienvenida:** Interfaz inicial interactiva para el ingreso al sistema.
*   **Formulario de Captura:** Registro estructurado de datos clave: Nombre, Número, Código Internacional y Monto.
*   **Validación de Campos:** Sistema de alertas (`messagebox`) que impide el registro si existen campos vacíos.
*   **Persistencia en Memoria:** Creación de instancias de objetos de la clase `Banco` para el manejo limpio de datos.
*   **Consulta de Información:** Ventana emergente que muestra de forma ordenada el resumen del banco creado.

---

## 📁 Estructura del Proyecto

Para el correcto funcionamiento del proyecto, la estructura de directorios debe ser la siguiente:

```text
├── Clases/
│   └── classBanco.py       # Clase que define el objeto Banco y sus métodos
├── main.py                 # Script principal y lógica de la GUI
└── README.md               # Documentación del repositorio
```

---

## 🛠️ Requisitos Previos

El proyecto utiliza únicamente librerías estándar de Python, por lo que no requiere instalaciones complejas:

*   **Python 3.8 o superior**
*   **Tkinter** (incluido por defecto en las instalaciones estándar de Python).
    *   *Nota para usuarios de Linux (Ubuntu/Debian):* Si no está instalado, ejecuta:
        ```bash
        sudo apt-get install python3-tk
        ```

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para poner a funcionar el proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com
    ```
2.  **Navegar al directorio del proyecto:**
    ```bash
    cd TU_REPO
