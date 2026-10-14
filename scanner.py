import json
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import time

def fetch_finviz_catalyst(ticker):
    """
    Attempts to scrape Finviz for a headline. 
    Returns a fallback string if the stock has no recent news.
    """
    url = f"https://finviz.com{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=4) as response:
            soup = BeautifulSoup(response.read().decode('utf-8', errors='ignore'), "html.parser")
            news_table = soup.find("table", id="news-table")
            if news_table:
                first_row = news_table.find("tr")
                if first_row:
                    links = first_row.find_all("a")
                    for link in links:
                        headline_text = link.text.strip()
                        if headline_text:
                            return headline_text
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
                
                # Verify we have enough columns to safely extract the complete layout array
                if len(cols) >= 6:
                    text_cells = [c.text.strip() for c in cols]
                    
                    # If the first cell is an index number row (1, 2, 3), drop it to align columns
                    if text_cells[0].isdigit():
                        text_cells = text_cells[1:]
                    
                    # FIXED EXTRACTOR DICTIONARY: Maps distinct, explicit indexes 
                    ticker = text_cells[0]
                    name = text_cells[1]
                    change_text = text_cells[2].replace("%", "").replace("+", "").replace(",", "").strip()
                    price_text = text_cells[3].replace("$", "").replace(",", "").strip()
                    
                    # Safely handle the market cap column index variant if it shifts slightly
                    market_cap_text = text_cells[5].upper().strip() if len(text_cells) >= 6 else "N/A"
                    
                    try:
                        change = float(change_text)
                        price = float(price_text)
                        
                        # Only skip absolute flat tickers
                        if change == 0:
                            continue
                            
                        move_type = "gainer" if change > 0 else "loser"
                        
                        # FETCH NEWS (Decoupled completely so failures won't drop the stock)
                        print(f"🔍 Fetching catalyst headline for {ticker}...")
                        try:
                            catalyst = fetch_finviz_catalyst(ticker)
                            time.sleep(0.2) # Friendly spacing delay to remain unblocked
                        except Exception:
                            catalyst = "Catalyst database offline."
                            
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

    # Sort absolute top percentage runners first
    payload.sort(key=lambda x: abs(x["change"]), reverse=True)

    with open("data.js", "w", encoding="utf-8") as file:
        file.write(f"const fullMarketData = {json.dumps(payload, indent=2)};")
        
    print(f"✅ Processing complete! Safely extracted {len(payload)} unfiltered tickers into data.js.")

if __name__ == "__main__":
    run_unfiltered_scan()
