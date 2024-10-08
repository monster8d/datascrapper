
# 📄 File Scraper & Telegram Bot 🤖

This Python script allows you to scrape data from various file formats and send it directly to a Telegram bot. It’s an ideal tool for automating data extraction and messaging.

## ✨ Features
- **File Scraping**: Extracts data from PDFs, DOCX, CSV, TXT, and XLSX files.
- **Telegram Bot Integration**: Automatically sends scraped data to any Telegram chat.
- **Customizable**: Easily modify the script to add new file types or adjust processing.

## ⚙️ Requirements
Before running the script, make sure you have the following:
- Python 3.x installed
- A Telegram Bot Token (available from the [Telegram BotFather](https://core.telegram.org/bots#botfather))

Install the required Python packages:
```bash
pip install requests pandas python-telegram-bot PyPDF2 python-docx openpyxl
```

## 🚀 Usage
1. Clone the repository and navigate to the project directory.
2. Update the script with your `TELEGRAM_BOT_TOKEN`.
3. Run the script with the path to the file you want to scrape.

For example:
```bash
python file_scraper.py /path/to/your/file.pdf
```

The extracted data will be automatically sent to your Telegram bot.

## 📚 Example
To scrape a file and send its content to your bot, use the command:
```bash
python file_scraper.py /path/to/your/file.txt
```

## 🛠️ Potential Use Cases
- Automate data extraction and notifications.
- Set up alerts for specific content in files.
- Use in a business to share data quickly over Telegram.

---

<p align="center">
  <a href="https://github.com/monster8d">
    <img src="https://img.shields.io/badge/View_on-GitHub-3498db?style=for-the-badge" alt="View on GitHub">
  </a>
</p>



