from playwright.sync_api import Page, expect

def test_clonar_bot(page: Page):
    page.get_by_role("textbox", name="Buscar Bot...").fill("webchat_bot_auto Copia")
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Duplicar proyecto").click()
    
    mensaje = page.get_by_text("El bot se clonó con éxito.")
    
    expect(mensaje).to_be_visible()