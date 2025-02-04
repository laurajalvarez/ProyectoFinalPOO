A continuación, se presenta un archivo README para el proyecto disponible en [https://github.com/laurajalvarez/ProyectoFinalPOO](https://github.com/laurajalvarez/ProyectoFinalPOO):

# Proyecto Final de Programación Orientada a Objetos

## Descripción

Este proyecto consiste en la implementación de diversas figuras geométricas utilizando los principios de la Programación Orientada a Objetos (POO) en Python. Cada figura se representa como una clase con atributos y métodos específicos que definen sus propiedades y comportamientos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- **Clases de Figuras**:
  - `Circulo.py`: Define la clase `Circulo` con atributos como radio y métodos para calcular el área y el perímetro.
  - `Estrella.py`: Contiene la clase `Estrella` que representa una estrella con propiedades específicas.
  - `EstrellaFugaz.py`: Extiende la clase `Estrella` para modelar una estrella fugaz con comportamientos adicionales.
  - `Figura.py`: Clase base abstracta para todas las figuras, proporcionando una interfaz común.
  - `Hexagono.py`: Implementa la clase `Hexagono` con métodos para calcular sus propiedades geométricas.
  - `Linea.py`: Define la clase `Linea` que representa una línea en un plano.
  - `Luna.py`: Modela la figura de una luna con atributos específicos.
  - `NaveEspacial.py`: Clase que representa una nave espacial, posiblemente combinando varias figuras.
  - `Ovalo.py`: Implementa la clase `Ovalo` con métodos para calcular área y perímetro.
  - `Punto.py`: Define la clase `Punto` para representar coordenadas en el espacio.
  - `Triangulo.py`: Contiene la clase `Triangulo` con métodos para calcular sus propiedades.

- **Pruebas**:
  - `PruebaPolimorfismo.py`: Script que demuestra el uso del polimorfismo entre las diferentes figuras.

- **Configuración del Proyecto**:
  - `.idea/`: Directorio que contiene los archivos de configuración del entorno de desarrollo.

## Requisitos

- Python 3.x

## Ejecución

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/laurajalvarez/ProyectoFinalPOO.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd ProyectoFinalPOO
   ```

3. Ejecuta el script de prueba para ver el polimorfismo en acción:

   ```bash
   python PruebaPolimorfismo.py
   ```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar o agregar nuevas funcionalidades, por favor, sigue estos pasos:

1. Realiza un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad:

   ```bash
   git checkout -b nueva-funcionalidad
   ```

3. Realiza tus cambios y haz commit de los mismos:

   ```bash
   git commit -m "Agrega nueva funcionalidad"
   ```

4. Envía tus cambios al repositorio remoto:

   ```bash
   git push origin nueva-funcionalidad
   ```

5. Abre una Pull Request en GitHub.

## Licencia

Este proyecto no especifica una licencia. Si deseas utilizar el código, por favor, contacta al autor para obtener más información.

Este README proporciona una visión general del proyecto y guía al usuario en su comprensión y uso. 
