from playwright.sync_api import Page, expect

def test_borrar_canal_bot(page: Page):

    page.get_by_role("textbox", name='Buscar Bot...' ).fill('webchat_bot_auto Copia')
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Gestionar campañas").click()
    page.locator(".icon-trash.c-association__campaign-header-icon").click()
    page.get_by_role("button", name= "Eliminar").click()
    page.get_by_role("button", name= "Salir").click()

    expect(page.get_by_text('Se ha desasociado')).to_be_visible()

    #Conecta nuevamente los canales
    page.get_by_role("textbox", name='Buscar Bot...' ).fill('webchat_bot_auto Copia')
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Gestionar campañas").click()
    page.get_by_role("button", name= "Asociar nueva campaña").click()
    page.get_by_role("button", name="Seleccionar").click()
    page.get_by_text("PruebasQA Parent").click()
    page.get_by_title("pruebasqaparent3607-9707-webchat@wc").click()
    page.get_by_title("pruebasqaparent3607-9733-webchat@wc").click()
    page.get_by_role("button", name="Guardar").click()
    page.get_by_role("button", name="Salir").click()
