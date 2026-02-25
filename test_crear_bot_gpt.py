from playwright.sync_api import Page, expect

url = "https://qa-pantera.chattigo.com/login/pages/login"
usuario = "auto-bot-6@pantera.com"
contraseña = "auto-bot-6@pantera.com"

def test_crear_bot(page: Page):
    page.set_viewport_size({"width": 1440, "height": 900})
    page.set_default_timeout(30000)

    page.goto(url)

    #Login
    page.get_by_role("textbox", name="Usuario").fill(usuario)
    page.get_by_role("textbox", name="Contraseña").fill(contraseña)
    page.get_by_role("button", name="Ingresar").click()

    expect(page).to_have_url("https://qa-pantera.chattigo.com/login/pages/dashboard/bot/list")

    #Cerrar Pop Ups iniciales
    page.locator("ch-ui-widget-generic-modal").get_by_role("button", name="Entendido").click()
    page.locator("app-modal-alert").get_by_text("Entendido").click()
    page.get_by_role("button", name="Entendido").click()

    #Crear bot
    page.get_by_role("button", name="Crear Bot").click()
    page.get_by_role("textbox", name="Escriba el nombre del bot aquí").fill("QA Test Laura Bot GPT")
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
    