---
<p align="center">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/telegram-bot-green?logo=telegram" alt="Telegram">
  <img src="https://img.shields.io/badge/github-actions-lightgrey?logo=github" alt="GitHub Actions">
</p>



<h1 align="center">📚 Audiobook Checker </h1>

<p align="center">Automated system for tracking new audiobook releases on audioboo.org.
Sends Telegram notifications when new books are detected.</p>
---
## ✨ Features

- 🔍 **Automatic daily checks** for updates
- 📱 **Telegram notifications** for new books
- ➕ **Easy series management** through menu
- 🗑️ **Add/remove series** easily
- ☁️ **GitHub synchronization** for reliable storage
- ⚡ **Auto-update** of data when changes detected

## 🛠️ Installation

### Requirements
- Python 3.8+
- Telegram bot (get token from @BotFather)
- GitHub account (for automated checks)

### Local Setup
1. Clone the repository:
```bash
git clone https://github.com/ekolodenets/audiobook-checker.git
cd audiobook-checker
```
2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```
3. Install dependencies
```bash
pip install requests beautifulsoup4 python-dotenv
```
4. Configure environment:
```bash
# Create .env file with your Telegram credentials
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

🤖 Automated GitHub Actions
The system automatically runs daily at 08:00 UTC (11:00 Moscow time):
Checks all series for updates
Sends Telegram notifications
Commits changes to series.json
Stores logs in GitHub Actions


🤝 Contributing
1. Fork the project
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a pull request

📮 Support
If you have any questions or issues:

1. Check existing GitHub Issues
2. Create new Issue with detailed description
3. Provide error logs and steps to reproduce

⭐ Star this repo if you find it useful!


