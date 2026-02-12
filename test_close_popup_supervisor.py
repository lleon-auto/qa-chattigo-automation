from playwright.sync_api import sync_playwright, TimeoutError

URL = "https://qa-pantera.chattigo.com/login/pages/login"
USER = "supervisor_auto_07_pantera@chattigo.com"
PASSWORD = "Super2024@12"

def test_close_popup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel="chrome", slow_mo=500)
        page = browser.new_page()

        try:
            # 1. Login
            page.goto(URL)
            page.fill('input[formcontrolname="user"]', USER)
            page.fill('input[formcontrolname="password"]', PASSWORD)
            page.click('#loginButton')

            # Esperar a que termine la navegación después del login
            #page.wait_for_load_state('networkidle', timeout=10000)

            # 2. Detectar y cerrar pop-up
            popup = page.locator(".widget-generic-modal")

            try:

                # Hacer clic en el primer botón de cerrar VISIBLE
                page.locator("button.ch-ui-modal__close:visible").first.click()
                print("✅ Pop-up cerrado con botón X")


            except TimeoutError:
                print("ℹ️ No apareció el pop-up")

            # 3. Validar carga del dashboard
            page.locator('.c-sidebar-menu__label')
            print("✅ Vista de Supervisor cargada")

            #page.wait_for_timeout(10000)
                       
        finally:
            browser.close()

test_close_popup()