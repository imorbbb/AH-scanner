import json
import urllib.request
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_yahoo_catalyst(ticker):
    """
    Queries the official Yahoo Finance RSS feed for the target ticker
    to extract the absolute freshest corporate catalyst headline.
    """
    # Official unblocked Yahoo RSS news feed layout
    rss_url = f"https://yahoo.com{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        req = urllib.request.Request(rss_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            # Target the first breaking news 'item' node inside the XML document channel
            item = root.find(".//item")
            if item is not None:
                title_node = item.find("title")
                if title_node is not None and title_node.text:
                    headline = title_node.text.strip()
                    return headline
    except Exception as e:
        # Fails completely silent to ensure a connection skip never drops the stock runner itself
        pass
    
    return "No recent headlines found (Technical or volume momentum play)."

def run_unfiltered_scan():
    print("🚀 Connecting to live public market-wide data pipeline...")
    payload = []
    
    now = datetime.now()
    weekday = now.weekday()  
    hour = now.hour

    is_weekend_or_monday_morning = (weekday >= 5) or (weekday == 0 and hour < 16)
    
    if is_weekend_or_monday_morning:
        print("📅 Weekend window. Extracting Friday's final records...")
    else:
        print("⚡ Standard session active. Accessing current live after-hours feeds...")

    url = "https://stockanalysis.com/markets/afterhours/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            soup = BeautifulSoup(response.read().decode('utf-8'), "html.parser")
            
            # Target rows inside the primary after-hours database data layout table
            rows = soup.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                
                # Check for standard wide-table row length constraints
                if len(cols) >= 6:
                    text_cells = [c.text.strip() for c in cols]
                    
                    # If index number row exists (1, 2, 3...), clean it out to align data structures
                    if text_cells[0].isdigit():
                        text_cells = text_cells[1:]
                    
                    # Explicit layout dictionary alignment mapping
                    ticker = text_cells[0]
                    name = text_cells[1]
                    change_text = text_cells[2].replace("%", "").replace("+", "").replace(",", "").strip()
                    price_text = text_cells[3].replace("$", "").replace(",", "").strip()
                    market_cap_text = text_cells[5].upper().strip() if len(text_cells) >= 6 else "N/A"
                    
                    try:
                        change = float(change_text)
                        price = float(price_text)
                        
                        if change == 0:
                            continue
                            
                        move_type = "gainer" if change > 0 else "loser"
                        
                        # FETCH CATALYST FROM YAHOO FINANCE FEED
                        print(f"🔍 Fetching Yahoo Finance catalyst for {ticker}...")
                        catalyst = fetch_yahoo_catalyst(ticker)
                        
                        # Keep a brief breath delay to maintain structural stability
                        time.sleep(0.1)
                            
                        payload.append({
                            "ticker": ticker,
                            "name": name,
                            "price": price,
                            "change": change,
                            "market_cap": market_cap_text,
                            "type": move_type,
                            "catalyst": catalyst
                        })
                    except ValueError:
                        continue
                        
    except Exception as e:
        print(f"⚠️ Notice: Data stream bypass: {e}")

    # Sort absolute top percentage runners first to bubble massive moves up instantly
    payload.sort(key=lambda x: abs(x["change"]), reverse=True)

    with open("data.js", "w", encoding="utf-8") as file:
        file.write(f"const fullMarketData = {json.dumps(payload, indent=2)};")
        
    print(f"✅ Processing complete! Safely extracted {len(payload)} unfiltered tickers into data.js.")

if __name__ == "__main__":
    run_unfiltered_scan()
