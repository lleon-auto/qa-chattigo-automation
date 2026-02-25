from playwright.sync_api import Page, expect

def test_crear_bot_gpt(page: Page):

    #Crear bot
    page.get_by_role("button", name="Crear Bot").click()
    page.get_by_role("textbox", name="Escriba el nombre del bot aquí").fill("QA auto GPT-Laura")
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_role("button", name="ChattiGPT").click()
    page.get_by_role("textbox", name="Ejemplo: Usted es un experto [rol o profesión que asumirá GPT]. Crea [tema o tarea]. El objetivo es [contexto]. El contenido es para [a quién dirige la respuesta]. Tus directrices para escribir son [restricciones]").fill("Eres un chatbot especializado en atención al cliente para Chattigo")
    page.get_by_text("Configuración Avanzada").click()
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_role("button", name="gpt-4o", exact=True).click()
    page.get_by_role("button", name="Comenzar").click()

    #Cerrar Pop Ups del editor de bot
    page.locator("app-gpt-services").get_by_role("button", name="Entendido").click()
    page.locator("app-modal-gpt").get_by_role("button", name="Entendido").click()
    
    expect(page.get_by_role("button", name="Iniciar edición")).to_be_visible()
    