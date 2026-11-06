import requests
from datetime import datetime

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[0m"

try:
    doviz = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10).json()
    dolar = doviz["rates"]["TRY"]
    euro = dolar / doviz["rates"]["EUR"]
    
    ons = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
    ons_dolar = ons["price"]
    
    altin = requests.get("https://turkpidya.com/wp-json/turkpidya-data/v1/gold", timeout=10).json()
    
    zaman = datetime.now().strftime("%d.%m.%Y - %H:%M:%S")
    print("\n" + B + "="*40 + W)
    print(C + "Guncelleme: " + zaman + W)
    print(Y + "Dolar: " + G + str(round(dolar, 2)) + " TL" + W + " | " + Y + "Euro: " + G + str(round(euro, 2)) + " TL" + W)
    print(B + "="*40 + W)
    
    print("\n" + Y + "Ons Altin (Dolar):" + W)
    print("  " + G + "Fiyat: " + str(round(ons_dolar, 2)) + " $" + W)
    
    for u in altin["prices"]:
        if u["type"] in ["gram_24k", "gram_22k", "ceyrek"]:
            print("\n" + Y + u["name_tr"] + ":" + W)
            print("  " + R + "Alis:  " + str(round(u["buy"], 2)) + " TL" + W)
            print("  " + G + "Satis: " + str(round(u["sell"], 2)) + " TL" + W)
            if u["type"] == "gram_24k" and u["sell"] > 7000:
                print("  " + R + "!!! DIKKAT: 24 AYAR ALTIN 7000 TL YI ASTI !!!" + W)
                
except Exception as e:
    print("Baglanti Hatasi: " + str(e))
