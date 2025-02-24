# Prueba desarrollador QA - Jonathan Betancourt

## Descripión

Este repositorio contiene la solución para la Prueba Técnica de QA, según las instrucciones proporcionadas en el documento «Prueba-Tecnica-para-QA.docx». Incluye pruebas automatizadas usando Selenium WebDriver y pruebas de estrés usando Locust para evaluar el rendimiento y la fiabilidad de «Internet (Herokuapp)».

## Requisitos

Para realizar estas pruebas, necesitará lo siguiente:

*   **Sistema operativo:** Windows
*   **Software:**
    *   Python
    *   Pip
    *   Pytest
    *   selenium
    *   locust
    *   requests
    *   beautifulsoup4
    *   webdriver-manager
    *   Navegador web
    *   WebDriver
    *   VS Code


## Instalación

1.  **Instalar Python:**
    *   Descargar Python desde [https://www.python.org/downloads/]
    *   Asegúrese de seleccionar la opción de añadir Python a su PATH durante la instalación.


2.  **Crear un entorno virtual (recomendado):**
    ```
    python -m venv venv
    source venv/bin/activate # En macOS/Linux
    venv\Scripts\activate.bat # En Windows
    ```

3.  **Instalar dependencias:**
    ```
    pip install -r requisitos.txt
*   Allure pytest Plugin Version: 2.13.5
*   crear Configuration File: `pytest.ini`

    ```

## Ejecución de las pruebas

1.  **Pruebas Selenium:**

    * Navegue hasta el directorio raíz y ubique el archivo `run_tests.bat` y ejecútelo haciendo doble clic en el archivo o ejecutándolo desde la línea de comandos:
        ```
        Este archivo ejecutará el siguiente script:
        @echo off
        pytest --alluredir=allure-results
        allure serve allure-results

        Lo que simplifica el proceso de ejecución de las pruebas y la generación del informe de Allure.

        ```

2.  **Pruebas de estrés de Locust:**
    * Navegue hasta el directorio que contiene el archivo `locustfile.py`.
    * Ejecuta Locust usando el siguiente comando:
        ```

        locust -f locustfile.py -u 200 -r 10 --headless --run-time 10m --html=locust_report.html --host=https://the-internet.herokuapp.com
        ```
        *   `-u 200`: Simula 200 usuarios simultáneos.
        *   `-r 10`: Crea 10 usuarios por segundo.
        *   `--headless`: Ejecuta Locust en modo headless (no web UI).
        *   `--run-time 10m`: Realiza la prueba durante 10 minutos.
        *   `--html=locust_report.html`: Genera un informe HTML denominado `locust_report.html`.
        *   `--host=https://the-internet.herokuapp.com`: Especifica el host de destino.

3.  **Analizar los resultados:**
    * Para las pruebas Selenium, revise la salida en la consola.
    * Para las pruebas Locust, abra el archivo `locust_report.html` en su navegador para analizar los resultados, incluyendo:
        * Tiempos de respuesta
        * Tasas de éxito/fracaso
        * Peticiones por segundo

## Informe

En el archivo `locust_report.html` se incluye un informe detallado de los resultados de la prueba (incluidos los tiempos de respuesta, las tasas de éxito/fracaso y el rendimiento general del sitio bajo carga).
