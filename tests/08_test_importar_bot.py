from playwright.sync_api import Page, expect

def test_importar_bot_chattigo(page: Page):

    page.get_by_title('Importar proyecto').click()
    
    with page.expect_file_chooser() as fc_info:
        page.get_by_role('button', name='Cargar').click()
    
    file_chooser = fc_info.value
    file_chooser.set_files('webchatbotauto Copia(GENERAL).json')

    expect(page.get_by_text('El proyecto se importó con éxito')).to_be_visible()

    #Elimina bot importado
    page.get_by_role("textbox", name='Buscar Bot...' ).fill('webchat_bot_auto Copia')
    page.get_by_role("button").nth(1).click()
    page.get_by_role("paragraph").filter(has_text="Eliminar proyecto").click()
    page.get_by_role("button", name="Aceptar").click()

    

