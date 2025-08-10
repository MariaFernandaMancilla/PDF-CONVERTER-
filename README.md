# PDF to Word Converter

**PDF to Word Converter** es una aplicación de escritorio desarrollada en **Python** con **Tkinter** que permite convertir uno o varios archivos con extensión `.pdf` a documentos `.docx` de forma rápida, sencilla y con una interfaz intuitiva.  

La herramienta mantiene, en la medida de lo posible, el formato original del archivo PDF, y ofrece retroalimentación visual mediante una barra de progreso durante la conversión.

---

## Características

- **Conversión múltiple**: selecciona uno o más archivos PDF y conviértelos a Word en un solo proceso.
- **Interfaz gráfica moderna**: desarrollada con Tkinter, con botones, imágenes y diseño adaptado.
- **Barra de progreso**: muestra el avance de cada conversión.
- **Protección contra procesos simultáneos**: evita que se ejecuten múltiples conversiones al mismo tiempo.
- **Ventana de splash**: pantalla de presentación antes de iniciar la aplicación.
- **Mensajes informativos y de error**: mediante cuadros de diálogo.

---

## Tecnologías utilizadas

- **Python 3**
- **Tkinter** (interfaz gráfica)
- **Pillow (PIL)** (manejo de imágenes)
- **pdf2docx** (librería para convertir PDF a DOCX)
- **threading** (manejo de hilos para no congelar la interfaz)
- **os** y **time** (gestión de archivos y tiempos de espera)

---

## Estructura del proyecto

- gui.py # Interfaz principal con botones, imágenes y lógica visual
- hilos.py # Manejo de hilos para ejecutar la conversión en segundo plano
- logica.py # Lógica de conversión de PDF a DOCX con barra de progreso
- splash.py # Pantalla de presentación inicial
- assets/ # Carpeta con imágenes y recursos visuales

  
## ▶️ Ejecución

1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPO.git
   cd TU_REPO

2. **Instalar dependencias** 

- pip install -r requirements.txt

  **(en caso de no tener el archvivo requirements , instalar manualmente)**
  
- pip install pillow pdf2docx

3. **Ejecutar aplicacion**
- python splash.py

## Licencia
Este proyecto se distribuye bajo la licencia MIT.
Eres libre de usarlo, modificarlo y distribuirlo, siempre que mantengas el crédito correspondiente.



