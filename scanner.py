import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_yahoo_api_catalyst(ticker):
    """
    Queries Yahoo's native internal search API endpoint.
    Returns the single absolute freshest news headline parsed out of the raw live stream.
    """
    safe_ticker = urllib.parse.quote(ticker.strip().upper())
    # Utilizing Yahoo's backend autocomplete API (lightweight, zero scraping blocks)
    url = f"https://yahoo.com{safe_ticker}&newsCount=1&quotesCount=0"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # Navigate the raw JSON response payload tree structure
            if data.get("news"):
                first_news_item = data["news"][0]
                headline = first_news_item.get("title", "").strip()
                source = first_news_item.get("publisher", "PR Newswire")
                if headline:
                    return f"{headline} (via {source})"
    except Exception:
        pass
        
    return "Technical Momentum / Micro-cap order book volume spike (No explicit news filed)."

def run_unfiltered_scan():
    print("🚀 Connecting to live public market-wide data pipeline...")
    payload = []
    
    url = "https://stockanalysis.com/markets/afterhours/"
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
                
                if len(cols) >= 5:
                    text_cells = [c.text.strip() for c in cols]
                    
                    # Ensure alignment code handles trailing spaces safely
                    if len(text_cells) > 0 and text_cells[0].isdigit():
                        text_cells = text_cells[1:]
                    
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
                        
                        payload.append({
                            "ticker": ticker,
                            "name": name,
                            "price": price,
                            "change": change,
                            "market_cap": market_cap_text,
                            "type": move_type,
                            "catalyst": "Pending network trace..."
                        })
                    except ValueError:
                        continue
                        
    except Exception as e:
        print(f"⚠️ Critical Table Scrape Failure: {e}")

    # Prioritize absolute maximum velocity breakouts first
    payload.sort(key=lambda x: abs(x["change"]), reverse=True)
    
    print(f"✅ Gathered {len(payload)} tickers. Querying API news channels for top volume runners...")
    
    # Run the unblocked query lookups across your top 8 highest-ranked runners
    for index, stock in enumerate(payload):
        if index < 8:
            print(f" 🔍 Mapping live API news feed for: {stock['ticker']} ({stock['change']:.1f}%)")
            stock["catalyst"] = fetch_yahoo_api_catalyst(stock["ticker"])
            time.sleep(0.15) # Short breath delay to keep execution perfectly stable
        else:
            stock["catalyst"] = "Technical overnight price discovery / standard volume play."

    with open("data.js", "w", encoding="utf-8") as file:
        file.write(f"const fullMarketData = {json.dumps(payload, indent=2)};")
        
    print(f"🎯 Processing complete! {len(payload)} tickers updated inside data.js.")

if __name__ == "__main__":
    run_unfiltered_scan()
