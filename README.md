**Proyecto de Web Scraping con CI/CD**

Este proyecto está diseñado para realizar scraping de datos desde fuentes específicas y automatizar el proceso utilizando GitHub Actions para la integración continua. Desarrollado en Python, permite la ejecución programada y la validación del código en cada cambio.


**Características**

Scraping automatizado: Extracción de datos desde páginas web seleccionadas.

Integración continua: Validación de código y ejecución de pruebas con cada cambio.

Ejecución programada: Automatización del scraping en intervalos definidos.

Exportación de datos: Almacenamiento de los datos extraídos en formatos como JSON o CSV.


**Tecnologías utilizadas**

Python 3.x

Librerías: requests, beautifulsoup4, pandas, openpyxl

GitHub Actions: Para la automatización de flujos de trabajo.


**Estructura del proyecto**

.
├── .github/
│   └── workflows/
│       └── docker.yml
├── docs/
├── src/
│   └── edu_pad/
├── .gitignore
├── README.md
├── dockerfile
├── integracionyml_old.txt
├── mainpy_old.txt
├── mainyml_old.txt
├── pruebadocker.py
├── setup.py
└── requirements.txt


**Flujo de trabajo CI (GitHub Actions)**

Cada vez que se realiza un push o pull request a la rama main, se ejecuta un flujo de trabajo automatizado que:

Instala las dependencias necesarias.

Ejecuta linea a linea para asegurar la calidad del código.

Ejecuta pruebas automatizadas.

Realiza el scraping y almacena los datos extraídos.


**Paso a Paso del flujo de trabajo**

1. Checkout del repositorio: Usa la acción actions/checkout@v4 para obtener el código fuente en la máquina virtual del runner.
2. Autenticación en DockerHub: Usa docker/login-action@v2 con credenciales almacenadas en secrets.DOCKER_USERNAME y secrets.DOCKER_TOKEN para hacer login en DockerHub.
3. Construcción de la imagen Docker: Se construye la imagen usando el Dockerfile del proyecto con el nombre contenedor.
4. Ejecución del extractor de datos: Se lanza un contenedor desde la imagen contenedor, montando volúmenes para que los datos procesados (CSV y base de datos) queden almacenados localmente en el repositorio (static/csv y static/db). El script ejecutado es edu_pad.main_extractor.
5. Ejecución del módulo de ingesta: De forma similar al paso anterior, se ejecuta el módulo edu_pad.main_ingesta en otro contenedor, usando los mismos volúmenes montados.


**Cómo ejecutar localmente**

git clone https://github.com/1J3G/pad_2025_1_2JG.git
cd pad_2025_1_2JG
pip install -r requirements.txt
python src/edu_pad/main.py

**Licencia**
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
