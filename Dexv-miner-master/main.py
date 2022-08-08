import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os

checked = 0

while True:
    os.system(f"title dexv miner // Checked Wallets: {checked} // by DEXV#6969")
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    wallets = soup.find_all("tr")
    for wallet in wallets:
        getwallet = str(wallet.getText()).strip()
        privkey = getwallet.split()[0].strip()
        uncompaddy = getwallet.split()[1].strip()
        compaddy = getwallet.split()[2].strip()
        balance = getwallet.split()[3].strip()
        if "Private Key" in getwallet:
            pass
        else:
            checked += 1
            if float(balance) > 0:              
                #requests.post("WEBHOOK_HERE", json={"content": f"{balance} BTC found\n\nAdress: {compaddy}\nPrivate Key: {privkey}"}) #put in your webhook here
                open('hits.txt', 'a+').write(f"{balance} BTC found in Adress: {compaddy} // Private Key: {privkey}")
            os.system("cls")
            os.system(f"title dexv miner // Checked Wallets: {checked} // by DEXV#6969")
            print(f""" 
Private Key: {privkey}
Uncompressed Address: {uncompaddy}
Compressed Address: {compaddy}
Balance: {balance}

""")
        time.sleep(0.5)

    
