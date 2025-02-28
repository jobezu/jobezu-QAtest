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
    *   allure
    *   allure pytest
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

1.  **Instalar Eclipse Temurin JDK:**
    *   Descargar Eclipse Temurin JDK anteriormente AdoptOpenJDK) desde [https://adoptium.net/]
    *   Asegúrese de seleccionar la opción de añadir Eclipse Temurin JDK a su PATH durante la instalación.


3.  **Configurar el entorno:**
    ```
    pip install -r requisitos.txt
    ```
*   Instalar Scoop, Scoop es un instalador de línea de comandos para Windows:

    Abra PowerShell como administrador.

    Ejecute el siguiente comando en PowerShell:

    ```
    Set-ExecutionPolicy RemoteSigned -scope CurrentUser
    iex "& { $(irm get.scoop.sh) } -RunAsAdmin"
    ```
*   Instalar Allure:

    Ejecute el siguiente comando en PowerShell:
    ```
    scoop install allure
    ```
    Esto agregará automáticamente Allure a tu PATH.



## Ejecución de las pruebas

1.  **Pruebas Selenium:**

    * Navegue hasta el directorio raíz y ubique el archivo `run_tests.bat` y ejecútelo haciendo doble clic en el archivo o ejecutándolo desde la línea de comandos:
        ```
        Este archivo ejecutará el siguiente script:
        @echo off
        pytest --alluredir=QA-tests-results
        allure serve QA-tests-results

        Lo que simplifica el proceso de ejecución de las pruebas y la generación del informe de Allure.

        ```

2.  **Pruebas de estrés de Locust:**
    * Navegue hasta el directorio que contiene el archivo `locustfile.py`.
    * Existen dos maneras de ejecutar Locust 
    
        1. Usando el siguiente comando:
        ```

        locust -f locustfile.py -u 200 -r 10 --headless --html=./locust_report.html --host=https://the-internet.herokuapp.com
        ```
        2. utilizando el siguiente comando:

        ```

        locust -f locustfile.py -u 200 -r 10 --headless --html=./locust_report.html --host=https://the-internet.herokuapp.com
        ```
        en ingresando a la web UI: [http://localhost:8089/]

        *   `-u 200`: Simula 200 usuarios simultáneos.
        *   `-r 10`: Crea 10 usuarios por segundo.
        *   `--headless`: Ejecuta Locust en modo headless (no web UI).
        *   `--html=locust_report.html`: Genera un informe HTML denominado `locust_report.html`.
        *   `--host=https://the-internet.herokuapp.com`: Especifica el host de destino.

3.  **Analizar los resultados:**
    * Para las pruebas Selenium, revise el reporte generado por allure que aparece al finalizar la ejecución del archivo `run_tests.bat`  
    * Para las pruebas Locust, abra el archivo `locust_report.html` en su navegador para analizar los resultados, incluyendo:
        * Tiempos de respuesta
        * Tasas de éxito/fracaso
        * Peticiones por segundo

## Enlace de video Ejecución de las pruebas
        
        [https://youtu.be/_369Z8ETYoU]
