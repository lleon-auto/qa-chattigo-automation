from playwright.sync_api import Page, expect

def test_eliminar_bot(page: Page):
    page.get_by_role("textbox", name="Buscar Bot...").fill("QA Auto-General Laura")
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Eliminar proyecto").click()
    page.get_by_role("button", name="Aceptar").click()

    expect(page.get_by_text("Se ha eliminado el bot")).to_be_visible()