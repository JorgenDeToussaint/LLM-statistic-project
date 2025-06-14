"""
Prototyp scrapera GPU benchmarków – wersja niekompletna, pozostawiona jako dokumentacja podejścia.

Obecna forma nie działa niezawodnie – dane zostały pozyskane ręcznie.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Wczytanie danych (ręcznie przygotowany plik)
df = pd.read_excel("Tabela_GPU_Steam.xlsx")  # <-- plik z nazwami GPU
gpu_names = df["GPU"].dropna().unique()

# Nagłówki dla symulacji przeglądarki
headers = {"User-Agent": "Mozilla/5.0"}

# Wyniki końcowe
gpu_data = []

for gpu in gpu_names:
    print(f"[INFO] Szukam: {gpu}")
    search_url = f"https://www.techpowerup.com/gpu-specs/?ajaxsrch={gpu.replace(' ', '+')}"
    
    # Zapytanie do wyszukiwarki TechPowerUp
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Znajdź pierwszy pasujący wynik
    first_result = soup.select_one("a[href*='/gpu-specs/']")
    
    if first_result:
        gpu_url = "https://www.techpowerup.com" + first_result['href']
        print(f"→ Znalazłem stronę: {gpu_url}")
        
        time.sleep(1.5)  # zabezpieczenie skryptu w kontekście wykrywania procesu scrappowania
        
        # Wejdź na stronę GPU
        gpu_response = requests.get(gpu_url, headers=headers)
        gpu_soup = BeautifulSoup(gpu_response.text, 'html.parser')
        
        # Pobierz parametry
        vram = gpu_soup.find(text="Memory Size").find_next("td").text.strip()
        mem_type = gpu_soup.find(text="Memory Type").find_next("td").text.strip()
        cuda = "Yes" if gpu_soup.find(text="CUDA Cores") else "No"
        year = gpu_soup.find(text="Release Date").find_next("td").text.strip()
        
        gpu_data.append({
            "GPU": gpu,
            "VRAM": vram,
            "Memory Type": mem_type,
            "CUDA": cuda,
            "Release Year": year,
            "Link": gpu_url
        })
    else:
        print(f"× Nie znaleziono: {gpu}")
        gpu_data.append({
            "GPU": gpu,
            "VRAM": "Not found",
            "Memory Type": "Not found",
            "CUDA": "Not found",
            "Release Year": "Not found",
            "Link": "N/A"
        })

# Zapisz do pliku
df_out = pd.DataFrame(gpu_data)
df_out.to_excel("gpu_scraped_data.xlsx", index=False)
print("✅ Zapisano dane do gpu_scraped_data.xlsx")

print("Zakończono prototyp.")
