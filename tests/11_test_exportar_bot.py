from playwright.sync_api import Page, expect

def test_exportar_bot(page: Page):
    page.get_by_role("button").nth(2).click()

    with page.expect_download():
        page.get_by_role("paragraph").filter(has_text="Exportar proyecto").click()
    
    expect(page.get_by_text("El proyecto se ha exportado")).to_be_visible()