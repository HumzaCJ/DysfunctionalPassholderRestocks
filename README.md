# Dysfunctional Passholder Restock Monitor
A lightweight restock monitoring tool that notifies you via Discord webhook when a restock of the popular Pokenots Bundle restocks on the Dysfunctional Passholder site.

## Features
- Real-time stock monitoring with easily configurable intervals
- Discord webhook integration with quick links
- TLS fingerprint spoofing to avoid detection

## Requirements
```
tls_client
requests
```

## Configuration

1. Replace `WEBHOOK_URL` with your Discord webhook URL
2. Update the embed details in `send_webhook()` to match your branding style
3. Run ``python main.py`` and leave the code running


## Future Additions

1. Proxy rotation to prevent IP bans from Squarespace's systems. This script was made to be run at the times of a drop once the item went out of stock, not for long term scraping.

2. Cache Solving. Methods such as randomising header rotations, random queries on the request URL, dynamic cooldowns and more.

3. Automated Ccheckout. Once the item restocks, complete the entire checkout using requests/headless browser to automate the entire process.


## Disclaimer
This tool is for **educational purposes** only. Automated monitoring may violate the website's Terms of Service. Use responsibly.
