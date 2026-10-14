# CanaryCraft — Dynamic Honey-Token & Canary Document Generator

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Active Defense](https://img.shields.io/badge/SOC-Active%20Defense%20%26%20Deception-red)
![Detection Engineering](https://img.shields.io/badge/Domain-Threat%20Traps%20%26%20Telemetry-navy)

**CanaryCraft** is an active defense and deception engineering CLI tool designed for SOC Analysts, Incident Responders, and Threat Hunters. It transforms passive log monitoring into active trap detection by generating weaponized canary documents, decoy environment configurations, and fake cloud API credentials that instantly alert your security team when accessed by an unauthorized entity or threat actor.

---

## 🛠️ Technical Architecture & Under-the-Hood Mechanics

CanaryCraft is modularly engineered to simulate believable enterprise assets while embedding zero-day-style tracking triggers:

1. **Canary Document Generator (`src/document_generator.py`):**
   - Programmatically builds Microsoft Word (`.docx`) documents containing executive-level placeholder text.
   - Unpacks the `.docx` archive (ZIP format) and directly manipulates `word/document.xml`.
   - Injects a remote web bug field (`INCLUDEPICTURE`) pointing back to the Canary listener URL. When an attacker or automated scraper opens the document, Microsoft Word automatically fires an outbound HTTP GET request, compromising their anonymity and capturing their metadata.

2. **Decoy Credential Generator (`src/credential_generator.py`):**
   - Creates realistic AWS credential profiles (`~/.aws/credentials`) and `.env` configuration files.
   - Populates them with synthetic, high-privilege-looking access keys, database passwords, and callback tracking parameters designed to trap credential scrapers, insider threats, and lateral movement scripts.

3. **Real-Time Webhook Listener (`src/web_listener.py`):**
   - A lightweight Flask-based alert receiver running asynchronously to catch inbound phone-home triggers.
   - Instantly extracts and prints high-priority SOC alert blocks detailing the Timestamp, Token ID, Source IP address, and User-Agent string.

---

## 📥 Installation & Setup

```bash
# Clone the repository
git clone [https://github.com/har1kr1sh/canary-craft.git](https://github.com/har1kr1sh/canary-craft.git)
cd canary-craft

# Install required Python dependencies
pip install -r requirements.txt

# Set up local configuration
cp config/config.example.txt config/config.txt
```

🚀 Usage & Execution Guide
1. Launch the Alert Listener Server
Start the telemetry receiver to monitor for incoming canary trips:

```bash
python3 main.py --listener
```

2. Generate Deception Assets (CLI Flags)
You can target specific honey-tokens using command-line arguments:

```bash
# Generate a canary Word document pointing to your listener
python3 main.py --doc --server-url "http://your-listener-ip:8080"

# Generate decoy AWS credentials
python3 main.py --aws

# Generate a decoy environment variables file
python3 main.py --env
```

3. Interactive Menu Mode
Running python3 main.py without arguments launches an interactive prompt allowing you to select your desired asset generation or start the listener on demand.

👨‍💻 Author
Hari Krishnan

GitHub: @har1kr1sh
Role: SOC L2 Analyst | Detection Engineering & Threat Hunting
