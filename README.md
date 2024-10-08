<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>File Scraper & Telegram Bot</title>
  <style>
    body { font-family: Arial, sans-serif; color: #333; line-height: 1.6; }
    h1 { color: #3498db; text-align: center; }
    h2 { color: #2c3e50; }
    p, li { font-size: 1.1em; }
    code { background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 4px; }
    pre { background: #f4f4f4; padding: 1em; border-radius: 4px; overflow-x: auto; }
    ul { list-style-type: square; padding-left: 20px; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .button { display: inline-block; padding: 10px 15px; font-size: 1em; color: #fff; background-color: #3498db; border-radius: 5px; text-decoration: none; }
    .button:hover { background-color: #2980b9; }
  </style>
</head>
<body>
  <div class="container">
    <h1>📄 File Scraper & Telegram Bot 🤖</h1>
    <p>This Python script allows you to extract text and data from various file formats and send it directly to a Telegram bot. It’s an all-in-one tool for automated file scraping and messaging.</p>

    <h2>✨ Features</h2>
    <ul>
      <li><strong>File Scraping</strong>: Extracts data from PDF, DOCX, CSV, TXT, and XLSX files.</li>
      <li><strong>Telegram Bot Integration</strong>: Automatically sends scraped data to any Telegram chat.</li>
      <li><strong>Customizable</strong>: Easily modify the script to add new file types or adjust processing.</li>
    </ul>

    <h2>⚙️ Requirements</h2>
    <p>Before running the script, make sure you have the following:</p>
    <ul>
      <li>Python 3.x installed</li>
      <li>A Telegram Bot Token (available from the <a href="https://core.telegram.org/bots#botfather" target="_blank">Telegram BotFather</a>)</li>
    </ul>
    <p>Install the required Python packages using:</p>
    <pre><code>pip install requests pandas python-telegram-bot PyPDF2 python-docx openpyxl</code></pre>

    <h2>🚀 Usage</h2>
    <ol>
      <li>Clone the repository and navigate to the project directory.</li>
      <li>Update the script with your <code>TELEGRAM_BOT_TOKEN</code>.</li>
      <li>Run the script with the path to the file you want to scrape.</li>
    </ol>
    <p>The extracted data will be automatically sent to your Telegram bot.</p>

    <h2>📚 Example</h2>
    <p>To scrape a file and send its content to your bot, use:</p>
    <pre><code>python file_scraper.py /path/to/your/file.txt</code></pre>

    <h2>🛠️ Potential Use Cases</h2>
    <ul>
      <li>Automate data extraction and notifications.</li>
      <li>Set up alerts for specific content in files.</li>
      <li>Use in a business to share data quickly over Telegram.</li>
    </ul>

    <p><a href="https://github.com/your-repo-link" class="button">🌐 View on GitHub</a></p>
  </div>
</body>
</html>
