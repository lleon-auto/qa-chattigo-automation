from playwright.sync_api import Page, expect

def test_crear_bot_ivr (page: Page):
    page.get_by_role("button", name="Crear Bot").click()
    page.get_by_role("textbox", name="Escriba el nombre del bot aquí...").fill("QA auto IVR-Laura")
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_role("button", name="IVR").click()
    page.get_by_role("button", name="Comenzar").click()

    expect(page.get_by_role("button", name="Iniciar edición")).to_be_visible()

