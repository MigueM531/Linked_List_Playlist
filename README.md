# 📀 Práctica: Implementación de una Lista de Reproducción de Música con Listas Enlazadas 🎵

## Objetivo

El objetivo de esta práctica es desarrollar una aplicación en consola que simule una lista de reproducción de música, utilizando estructuras de datos enlazadas. Los estudiantes deberán analizar y justificar qué tipo de estructura es la más adecuada para implementar cada funcionalidad.

Se espera que el programa permita agregar canciones, avanzar y retroceder entre ellas, eliminarlas, reproducir en modo aleatorio, adelantar la reproducción y generar subplaylists.

> **Nota:** Se otorgarán puntos adicionales a los estudiantes que usen buenas prácticas de programación y diseño y que implementen una interfaz más amigable y organizada.

## 📌 Requisitos de la Implementación

### 📂 1. Estructura de la Lista de Reproducción

Implementar una estructura de datos enlazada para gestionar la lista de canciones.

Cada canción debe tener:

- **Título**
- **Artista**
- **Duración** (entre 10 y 15 segundos)

El estudiante debe analizar qué tipo de estructura es la más adecuada:

- Lista enlazada simple
- Lista doblemente enlazada
- Lista enlazada circular
- Pila implementada con listas enlazadas
- Cola implementada con listas enlazadas

### 🎶 2. Funcionalidades Obligatorias

- ✅ **Agregar una canción a la playlist**
- ✅ **Avanzar a la siguiente canción**
- ✅ **Retroceder a la canción anterior**
- ✅ **Eliminar una canción**
- ✅ **Mostrar la canción en reproducción**
- ✅ **Mostrar toda la playlist**
- ✅ **Reproducir en orden aleatorio (shuffle mode)**
- ✅ **Adelantar la canción un % específico**
- ✅ **Simulación del tiempo de reproducción**
- ✅ **Generar una subplaylist**

## 📌 Evaluación y Bonificación Extra

| **Criterio**                                      | **Puntaje**  |
|---------------------------------------------------|--------------|
| Implementación funcional de todas las características | 40%          |
| Sustentación                                      | 60%          |
| Buenas prácticas de programación                  | +10%         |
| Estética e interactividad de la consola           | +10%         |

### 🟢 Bonificación Extra (20 pts)

- Menús bien estructurados con opciones numeradas.
- Mensajes claros y visualmente diferenciados (colores o símbolos ASCII 🎵).
- Animaciones sencillas (barra de progreso, por ejemplo).
- Indicadores visuales de la canción actual.

## 📌 Ejemplo de Ejecución Esperada

### 📝 Menú Principal

🎵 Bienvenido a tu Playlist Interactiva 🎵

1️⃣ Agregar canción
2️⃣ Avanzar a la siguiente canción
3️⃣ Retroceder a la canción anterior
4️⃣ Eliminar una canción
5️⃣ Mostrar canción en reproducción
6️⃣ Mostrar toda la playlist
7️⃣ Activar modo aleatorio
8️⃣ Adelantar una canción
9️⃣ Generar una subplaylist
🔟 Salir

Seleccione una opción: _

### ➕ Agregar una Canción

Ingrese el título: Bohemian Rhapsody
Ingrese el artista: Queen
Ingrese la duración (10-15 seg): 12
✅ Canción agregada exitosamente.

### ▶️ Mostrar la Canción en Reproducción

🎵 Ahora reproduciendo:
🎧 Bohemian Rhapsody - Queen (12s)


### ⏩ Adelantar un 50% de la Canción

Ingrese el porcentaje de adelanto: 50
⌛ Adelantando 6s...


### 🔀 Activar Modo Aleatorio

🔀 Modo aleatorio activado.
🎵 Nueva reproducción: Hotel California - Eagles (11s)


### 📑 Generar una Subplaylist

Ingrese los títulos de las canciones a incluir en la subplaylist (separados por comas):

Bohemian Rhapsody, Hotel California

✅ Subplaylist creada con 2 canciones.

1️⃣ Quiere reproducir esta nueva subplaylist? ___


### ❌ Eliminar una Canción

Ingrese el título de la canción a eliminar: Bohemian Rhapsody
✅ Canción eliminada exitosamente.


### ⏳ Simulación de Tiempo de Reproducción

▶️ Reproduciendo: Smells Like Teen Spirit - Nirvana (14s)

⏳ 1s... 2s... 3s... (progresivamente hasta 14s) / Barra de progreso

🔄 Pasando a la siguiente canción...


## 📌 Entrega y Sustentación

- **Grupo 61:** 24 de abril
- **Grupo 62:** 25 de abril
- **Grupo 63:** 24 de abril
- **Grupo 64:** 25 de abril
