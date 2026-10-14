import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_yahoo_proxy_catalyst(ticker):
    """
    Routes Yahoo Finance RSS inquiries via a public JSON API proxy
    to prevent server-side access restrictions and capture clear headlines.
    """
    # URL-encode the target to prevent special symbols (like hyphens or dots) from damaging the request
    safe_ticker = urllib.parse.quote(ticker.strip().upper())
    target_feed = f"https://feeds.finance.yahoo.com/rss/2.0/headline?s={safe_ticker}&region=US&lang=en-US"
    
    # Wrap target inside a clean, high-availability conversion endpoint
    proxy_url = f"https://rss2json.com{urllib.parse.quote(target_feed)}"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        req = urllib.request.Request(proxy_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # Verify the conversion tool successfully parsed the target payload articles
            if data.get("status") == "ok" and data.get("items"):
                first_article = data["items"][0]
                headline = first_article.get("title", "").strip()
                if headline:
                    return headline
    except Exception:
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

    url = "https://stockanalysis.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            soup = BeautifulSoup(response.read().decode('utf-8'), "html.parser")
            
            rows = soup.find_all("tr")
            for row in rows:
                cols = row.find_all("td")
                
                if len(cols) >= 6:
                    text_cells = [c.text.strip() for c in cols]
                    
                    if text_cells[0].isdigit():
                        text_cells = text_cells[1:]
                    
                    # Direct data field alignment map layout
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
                        
                        # EXECUTE TWO-PHASE CATALYST LOOKUP
                        print(f"🔍 Accessing proxy feed pipeline for {ticker}...")
                        catalyst = fetch_yahoo_proxy_catalyst(ticker)
                        
                        # Short throttle cadence to balance local execution loop
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

    # Prioritize absolute maximum percentage breakouts first
    payload.sort(key=lambda x: abs(x["change"]), reverse=True)

    with open("data.js", "w", encoding="utf-8") as file:
        file.write(f"const fullMarketData = {json.dumps(payload, indent=2)};")
        
    print(f"✅ Processing complete! Safely extracted {len(payload)} unfiltered tickers into data.js.")

if __name__ == "__main__":
    run_unfiltered_scan()
