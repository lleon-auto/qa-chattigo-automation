from playwright.sync_api import Page, expect

def test_crear_bot_general(page: Page):

    #Crear bot
    page.get_by_role("button", name="Crear Bot").click()
    page.get_by_role("textbox", name="Escriba el nombre del bot aquí").fill("QA Test Laura")
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_role("button", name="General").click()
    page.get_by_role("button", name="Siguiente").click()
    page.get_by_role("button", name="Iniciar").click()

    #Cerrar Pop Ups del editor de bot
    page.locator("chattigo-bots-configuration-component .modal-bot-optimization__action").click()
    page.locator("app-modal-capi").first.get_by_role("button", name="Entendido").click()
    
    expect(page.get_by_role("button", name="Iniciar edición")).to_be_visible()
    