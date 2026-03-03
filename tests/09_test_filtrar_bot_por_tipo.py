from playwright.sync_api import Page, expect

def test_filtrar_por_tipo(page: Page):

    page.locator('.b-filters__icon').click()
    page.get_by_role('button', name= 'Seleccionar...' ).nth(1).click()
    page.locator('.bot-dropdown-selector__items').get_by_text('Activos', exact=False)

    page.get_by_role('button',name= 'Aplicar filtros' ).click()

    expect(page.get_by_text('Filtros aplicados con éxito')).to_be_visible()