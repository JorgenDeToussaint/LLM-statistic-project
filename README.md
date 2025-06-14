# Steam GPU LLM Capability Analysis

## Opis projektu

Projekt analizuje dane ze Steam Hardware Survey (kwiecień 2025), w celu oceny zdolności przeciętnych użytkowników do lokalnego uruchamiania dużych modeli językowych (LLM).

W tym celu:
- przetworzono dane o popularności GPU graczy Steam,
- zestawiono je z danymi technicznymi z bazy TechPowerUp (VRAM, typ pamięci, CUDA),
- przypisano klasy możliwości ML/LLM do modeli kart,
- przygotowano środowisko scrapujące i analizujące dane.

## Instalacja

Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```
## Środowisko i wymagania

Projekt uruchamiany lokalnie z wykorzystaniem:

- Python 3.10+
- Jupyter Notebook
- Biblioteki: pandas, matplotlib, seaborn, openpyxl, requests, beautifulsoup4

Pliki danych wejściowych znajdują się w folderze `/data`.

> Uwaga: Wersje kart graficznych i ich parametry VRAM/CUDA zostały przypisane ręcznie na podstawie TechPowerUp i stron producentów.

## Cel projektu

Celem projektu jest analiza możliwości lokalnego uruchamiania modeli językowych (LLM) na podstawie najpopularniejszych GPU według ankiety Steam. Projekt klasyfikuje sprzęt na cztery klasy ML/LLM, uwzględniając m.in. VRAM, wsparcie CUDA/ROCm oraz architekturę.
