# 🛒 Amazon Product Scraper

A clean, modular web scraper for Amazon product listings and details, built with Python and structured using a clean architecture approach.

This scraper allows you to extract key product data (like titles, prices, ratings, and more) and explore it via a user-friendly Streamlit interface.

---

## 🚀 Features

- 🔍 Search for any product on Amazon by keyword  
- 🌍 Supports location-based scraping (e.g. `us`, `uk`, `fr`)  
- 🧠 Clean and maintainable architecture (controllers, models, enums, helpers)  
- 🧵 Multi-threaded for improved performance  
- 🖥️ Streamlit UI for interactive use  
- 📦 Organized codebase ready for extensions (LLM integration, analysis, etc.)

---

## 🌿 Branch Structure

This project is organized into four development branches, each representing a major step in the project’s lifecycle:

- `scraper_001`: sets up the environment and clean folder architecture (no scraper code yet)
- `scraper_002`: implements the scraping pipeline and controller logic
- `scraper_003`: adds the Streamlit user interface for interacting with the scraper
- `scraper_004`: prepares the branch for optional LLM integration to enhance functionality

Switching between branches lets you explore the project step by step and understand its evolution.

### 📁 Project Structure

amazon_scraper/
├── controllers/
│ └── scraper_controller.py # Handles scraping logic (listing + product page)
├── enums/
│ └── constant_urls.py # Enum for Amazon base URLs per location
├── helpers/
│ └── scraper_utils.py # Utility functions (like fetch, parse)
├── models/
│ └── product_data.py # Dataclasses for structured product data
├── llm/
│ └── openai_client.py # (Optional) For future LLM integration
├── ui/
│ └── app.py # Streamlit interface
├── main.py # Entrypoint for CLI use
├── requirements.txt # Python dependencies
└── README.md # Project overview

#### 💡 How It Works

1. **Product Listing Scrape**  
   Using `scraper_controller.py`, the script navigates to Amazon search results and collects product blocks.

2. **Product Page Scrape**  
   For each product, the scraper fetches its detailed page and extracts structured data.

3. **Streamlit UI**  
   Run the app and search interactively from your browser!

---

##### 🧪 Quickstart

### 1. Clone the repo

git clone https://github.com/Aminedalhy/Scraper
---

### 2. Create virtual environment
conda create --name Scraper
conda activate Scraper

### 3. Install Dependencies

pip install --break-system-packages -r requirements.txt

### 4. Install Dependencies

streamlit run app.py


🧰 Tech Stack
Python

BeautifulSoup4 – HTML parsing

Requests – HTTP client

Streamlit – UI

Dataclasses – Typed models

Enum – URL handling

Threading – Faster scraping

📌 Notes
This project is for educational purposes. Scraping Amazon may violate their Terms of Service.

Use responsibly, and consider adding proxies or delays if scaling.

🧑‍💻 Author
Made with ❤️ by AminDALY
👉 GitHub: @AmineDALHY
👉 YouTube: @withaminedaly




