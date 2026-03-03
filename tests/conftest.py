import pytest
from playwright.sync_api import Page

URL = "https://qa-pantera.chattigo.com/login/pages/login"
USUARIO = "auto-bot@pantera.com"
CONTRASEÑA = "auto-bot@pantera.com"

@pytest.fixture(autouse=True)
def setup(page: Page):
    # Configuración que se ejecuta antes de cada test
    page.set_viewport_size({"width": 1440, "height": 900})
    page.set_default_timeout(30000)
    page.goto(URL)
    
    # Login
    page.get_by_role("textbox", name="Usuario").fill(USUARIO)
    page.get_by_role("textbox", name="Contraseña").fill(CONTRASEÑA)
    page.get_by_role("button", name="Ingresar").click()
    
    #Cerrar Pop Ups iniciales
    try:
        page.locator("ch-ui-widget-generic-modal").get_by_role("button", name="Entendido").click(timeout=3000)
    except:
        pass
    try:
        page.locator("app-modal-alert").get_by_text("Entendido").click(timeout=3000)
    except:
        pass
    try:
        page.get_by_role("button", name="Entendido").click(timeout=3000)
    except:
        pass

    print ("Inicio exitoso")

    yield