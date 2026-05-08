# QA-LAB-01

## Nombre del proyecto

QA-LAB-01: Configuración del entorno de pruebas y repositorio

## Objetivo

Configurar un entorno básico de desarrollo y pruebas para el curso de Pruebas y Aseguramiento de Calidad de Software, utilizando herramientas de control de versiones y pruebas automatizadas. El proyecto permite organizar el código fuente, crear casos de prueba y verificar su funcionamiento mediante pytest.

## Herramientas utilizadas

- Git
- GitHub
- Visual Studio Code
- Python
- pytest
- PowerShell o terminal del sistema

## Estructura del proyecto

~~~text
QA-LAB-01/
│
├── src/
│   └── calculadora.py
│
├── tests/
│   └── test_calculadora.py
│
├── docs/
│
├── README.md
└── requirements.txt
~~~

## Instrucciones de ejecución

### 1. Clonar el repositorio

~~~bash
git clone https://github.com/Juanjo166/QA-LAB-01.git
~~~

### 2. Ingresar a la carpeta del proyecto

~~~bash
cd QA-LAB-01
~~~

### 3. Instalar las dependencias

~~~bash
pip install -r requirements.txt
~~~

### 4. Ejecutar las pruebas automatizadas

~~~bash
python -m pytest
~~~

### 5. Resultado esperado

~~~bash
4 passed
~~~

## Autor(es)

- Juan Josue Huaman Soto
- Universidad Nacional de San Cristóbal de Huamanga
- Curso: Pruebas y Aseguramiento de Calidad de Software
- Código del curso: IS-489


## Parte 7: Actualización del README

### Objetivo del ejercicio

Implementar funciones básicas de una calculadora y verificar su correcto funcionamiento mediante pruebas automatizadas utilizando pytest. Este ejercicio permite aplicar conceptos de aseguramiento de calidad de software, validando que cada función cumpla con el resultado esperado.

### Herramientas utilizadas

- Git
- GitHub
- Visual Studio Code
- Python
- pytest
- PowerShell o terminal del sistema

### Descripción de ejecución de pytest

Para ejecutar las pruebas automatizadas se utilizó el siguiente comando:

~~~bash
python -m pytest
~~~

El resultado obtenido fue exitoso, ya que las pruebas implementadas pasaron correctamente:

~~~bash
4 passed
~~~

Las pruebas realizadas verificaron las siguientes operaciones:

- Suma correcta
- Resta correcta
- Multiplicación correcta
- División correcta

### Importancia de las pruebas automatizadas

Las pruebas automatizadas son importantes porque permiten comprobar de manera rápida y repetible que el software funciona correctamente. Además, ayudan a detectar errores de forma temprana, facilitan el mantenimiento del código y aseguran que los cambios realizados no afecten funcionalidades ya implementadas.