from flask import Flask, request, jsonify
from colorama import Fore
from datetime import datetime
from src.utils import print_alert

app = Flask(__name__)

@app.route('/canary/<token>', methods=['GET', 'POST'])
def canary_trigger(token):
    src_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print_alert(token, src_ip, user_agent, timestamp)

    return jsonify({"status": "acknowledged", "timestamp": timestamp}), 200

def start_listener(port: int = 8080):
    print(f"{Fore.GREEN}[+] CanaryCraft Webhook Listener online on port {port}...{Style.RESET_ALL if 'Style' in globals() else ''}")
    app.run(host='0.0.0.0', port=port, debug=False)
