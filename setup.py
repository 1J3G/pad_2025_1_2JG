from setuptools import setup, find_packages

setup(    
    name="edu_pad",
    version="0.0.1",
    author="Juan Guillermo González",
    author_email="juan.gonzalez93@iudigital.edu.co",
    description="Proyecto educativo para la IUDIGITAL de Antioquia",
    py_modules=["actividad1","actividad2"],
    install_requires=["pandas","openpyxl","requests","beautifulsoup4"]
    )