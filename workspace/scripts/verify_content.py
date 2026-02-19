from playwright.sync_api import sync_playwright

def verify_content():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Secos e Molhados (Link removal)
        page.goto("http://localhost:4321/blog/secos-e-molhados")
        # Wait for the content to load
        page.wait_for_selector("article")

        # Check that "Barão de Cotegipe" is present but NOT a link
        # We can select the paragraph containing it.
        # It's in the section "O CAMINHÃOZINHO DE MUDANÇA"

        # Scroll to view
        element = page.locator("text=Barão de Cotegipe")
        element.scroll_into_view_if_needed()

        # Take screenshot of Secos e Molhados
        page.screenshot(path="verification_secos.png")
        print("Screenshot of Secos e Molhados taken.")

        # Verify Chiquita Banana (Text change)
        page.goto("http://localhost:4321/blog/a-sabedoria-da-chiquita-banana")
        page.wait_for_selector("article")

        # Check for "conselho de um velho alfarrabista"
        element = page.locator("text=conselho de um velho alfarrabista")
        element.scroll_into_view_if_needed()

        # Take screenshot of Chiquita Banana
        page.screenshot(path="verification_chiquita.png")
        print("Screenshot of Chiquita Banana taken.")

        browser.close()

if __name__ == "__main__":
    verify_content()
