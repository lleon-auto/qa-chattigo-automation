from playwright.sync_api import Page, expect

def test_filtrar_por_canal(page: Page):
    page.locator(".b-filters__icon > .ch-icon").first.click()
    page.get_by_role("button", name="Seleccionar...").first.click()
    page.get_by_role("button", name="PruebasQA Parent").click()
    
    page.get_by_text('WEBCHAT', exact="true").click()

    page.get_by_role("button", name="Aplicar filtros").click()
    alerta_exito = page.get_by_text("Filtros aplicados con éxito")
    expect(alerta_exito).to_be_visible()