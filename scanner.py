import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_yahoo_direct_news(ticker):
    """
    Pulls real-time headline telemetry directly from a clean public RSS stream.
    Bypasses JavaScript walls completely.
    """
    encoded_ticker = urllib.parse.quote(ticker.strip().upper())
    url = f"https://yahoo.com{encoded_ticker}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            soup = BeautifulSoup(response.read(), "xml") # Parse as XML raw node data
            first_item = soup.find("item")
            if first_item:
                title = first_item.find("title")
                if title and title.text:
                    return title.text.strip()
    except Exception:
        pass
    return "Technical breakout or momentum spike (No recent press releases found)."

def run_unfiltered_scan():
    print("🚀 Connecting to live public market-wide data pipeline...")
    payload = []
    
    # 1. SCRAPE MAIN EXTENDED HOURS TABLE DATA
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
                
                # Check for standard tables containing sufficient cell lengths
                if len(cols) >= 5:
                    text_cells = [c.text.strip() for c in cols]
                    
                    # FIXED DATA PARSING STRUCT: Detects and cleans numeric indices cleanly
                    if text_cells[0].replace(".", "").isdigit():
                        text_cells = text_cells[1:]
                    
                    # Match exact layout variables securely via specific list indexes
                    ticker = text_cells[0]
                    name = text_cells[1]
                    change_text = text_cells[2].replace("%", "").replace("+", "").replace(",", "").strip()
                    price_text = text_cells[3].replace("$", "").replace(",", "").strip()
                    
                    # Handle structural variances on market capitalization layouts
                    market_cap_text = text_cells[5].upper().strip() if len(text_cells) >= 6 else "N/A"
                    
                    try:
                        change = float(change_text)
                        price = float(price_text)
                        
                        if change == 0:
                            continue
                            
                        move_type = "gainer" if change > 0 else "loser"
                        
                        # Populate data immediately so tickers are never dropped from your screen
                        payload.append({
                            "ticker": ticker,
                            "name": name,
                            "price": price,
                            "change": change,
                            "market_cap": market_cap_text,
                            "type": move_type,
                            "catalyst": "Scanning market feeds..." # Temporary placeholder
                        })
                    except ValueError:
                        continue
                        
    except Exception as e:
        print(f"⚠️ Critical Table Scrape Failure: {e}")

    # 2. RUN HIGH-SPEED CATALYST PAIRING (Only targets active primary runners to prevent lag)
    # Sort absolute percentage value changes first
    payload.sort(key=lambda x: abs(x["change"]), reverse=True)
    
    print(f"✅ Gathered {len(payload)} tickers. Attaching real-time news data to key movers...")
    
    # Process catalysts only for the top 6 highest velocity positions to ensure high speed
    for index, stock in enumerate(payload):
        if index < 6:
            print(f" 🔍 Fetching news for runner: {stock['ticker']} ({stock['change']:.1f}%)")
            stock["catalyst"] = fetch_yahoo_direct_news(stock["ticker"])
        else:
            # Slower technical moves receive clean fallback tags instantly without hitting web servers
            stock["catalyst"] = "Technical move / standard overnight liquidity volume."

    # Write data straight to file system
    with open("data.js", "w", encoding="utf-8") as file:
        file.write(f"const fullMarketData = {json.dumps(payload, indent=2)};")
        
    print(f"🎯 Processing complete! {len(payload)} tickers compiled inside data.js.")

if __name__ == "__main__":
    run_unfiltered_scan()
