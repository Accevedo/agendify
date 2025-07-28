# 📒 Contact Manager - Proyecto CRUD en Python

Este es un proyecto de consola desarrollado en Python que permite **gestionar contactos** personales a través de un archivo CSV. Incluye funcionalidades completas de **Crear, Leer, Actualizar y Eliminar (CRUD)** contactos, manteniendo los datos organizados con un `ID` autoincremental y validados correctamente.

## 🛠️ Tecnologías utilizadas
- Python 3
- Módulos estándar: `csv`, `os`, `re`
- Librería externa: `tabulate` (para mostrar tablas de forma elegante)

## 📁 Estructura del proyecto

📦 proyecto_contactos
├── csv/
│ └── data.csv # Archivo donde se almacenan los contactos
├── core/
│ └── writer.py # Función para registrar nuevos contactos (con ID incremental)
├── main.py # Archivo principal con las funciones del CRUD
├── README.md # Este archivo

markdown
Copy
Edit

## ✅ Funcionalidades

- **📥 Agregar contacto:** Solicita nombre, teléfono y email, los valida y guarda en CSV con un ID.
- **🔍 Buscar contacto:** Busca por ID exacto y muestra los datos del contacto.
- **📋 Mostrar todos:** Lista todos los contactos en una tabla ordenada.
- **✏️ Editar contacto:** Permite modificar campos individuales del contacto seleccionado por ID.
- **🗑️ Eliminar contacto:** Borra un contacto por ID manteniendo los demás intactos.

## 🧪 Validaciones implementadas

- Nombre no puede estar vacío.
- Teléfono debe tener el formato `XXX-XXX-XXXX`.
- Email debe tener un formato válido.
- No se permite duplicación de ID gracias al sistema de autoincremento.

## ▶️ Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Instala la librería tabulate:
   ```bash
   pip install tabulate
Ejecuta el archivo principal:

bash
Copy
Edit
python main.py
📌 Notas adicionales
El archivo data.csv se crea automáticamente si no existe.

El ID se maneja automáticamente, no es necesario pedirlo al usuario al momento de agregar un nuevo contacto.

Este proyecto es una excelente base para integraciones futuras como: interfaz gráfica, base de datos, o exportación a PDF.

🧠 Aprendizajes clave
Manipulación de archivos CSV en Python.

Validación de datos con expresiones regulares.

Uso de DictReader y DictWriter.

Estructuración de un proyecto limpio y modular.

Buenas prácticas con funciones, comentarios y documentación.

🚀 Autor
Desarrollado por [Edward Terrero] 🧑‍💻
Con dedicación, refactorización constante y enfoque en la mejora progresiva.
