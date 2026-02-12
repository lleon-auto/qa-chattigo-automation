# Automatización de Pruebas - Chattigo
Este proyecto contiene la automatización de flujos de la plataforma Chattigo utilizando Python y Playwright.

# Flujos Automatizados
Módulo Supervisor: Inicio de sesión y cierre automático de anuncios/pop-ups iniciales.

Módulo Bots: Navegación al editor de bots y flujo de creación de nuevos agentes.

# Herramientas
Lenguaje: Python 3.13.6

Librerías: Playwright & Pytest

# Instalación y Uso
Clonar el proyecto: git clone https://github.com/LauraLeon/qa-chattigo-automation.git

Configurar el entorno e instalar dependencias: python -m venv .venv-1

En Windows: .venv-1\Scripts\activate

En Mac/Linux: source .venv-1\Scripts\activate

Una vez activado el entorno, instalar los paquetes necesarios: pip install playwright pytest-playwright playwright install

# Cómo ejecutar las pruebas
Para ejecutar todos los tests de la carpeta: pytest

Para ejecutar un test específico: pytest tests/test_crear_bot.py pytest tests/test_close_popup_supervisor.py
