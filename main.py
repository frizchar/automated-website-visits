import requests

def visit_website(url):
    response = requests.get(url)
    print(f"Visited {url} - Status code: {response.status_code}")

if __name__ == "__main__":
    visit_website("https://castoma.streamlit.app/")
