import pytest
from playwright.sync_api import Page

URL = "https://qa-pantera.chattigo.com/login/pages/login"
USUARIO = "BOT Prueba Publicador"
CONTRASEÑA = "Admin1234"

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
    page.locator("ch-ui-widget-generic-modal").get_by_role("button", name="Entendido").click()
    page.locator("app-modal-alert").get_by_text("Entendido").click()
    page.get_by_role("button", name="Entendido").click()

    yield