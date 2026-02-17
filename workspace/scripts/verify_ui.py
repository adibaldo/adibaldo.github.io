from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            print("Navigating to blog post...")
            response = page.goto("http://localhost:4321/blog/building-funes")
            if response.status != 200:
                print(f"Failed to load page: {response.status}")
                return

            # Wait for content to load
            page.wait_for_selector("article")

            # Take a screenshot of the header and first part of content
            # We want to see the Drop Cap and the metadata
            print("Taking screenshot...")
            page.screenshot(path="/home/jules/verification/blog-post-ui.png", full_page=False)
            print("Screenshot saved to /home/jules/verification/blog-post-ui.png")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    run()
