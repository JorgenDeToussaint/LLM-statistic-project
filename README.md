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
