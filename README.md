# AI-Driven Data Extraction Workflow

Ten projekt to w pełni działający schemat automatyzacji (Blueprint dla platformy [Make.com](https://make.com)), którego celem jest inteligentne i zautomatyzowane wyciąganie ustrukturyzowanych danych finansowych z nieustrukturyzowanego tekstu (np. e-maili, komunikatów czy notatek) przy pomocy narzędzi sztucznej inteligencji od OpenAI.

## 🔴 Problem, który rozwiązujemy
W wielu firmach działy finansowe, administracji czy księgowości tracą setki godzin miesięcznie na manualne odczytywanie i wpisywanie danych z dokumentów i wiadomości. 
Proces polegający na **ręcznym przepisywaniu (data entry)**:
- Jest **niezwykle czasochłonny** i powtarzalny.
- Prowadzi do **ludzkich błędów**, literówek w kwotach i pomyłek w kategoryzacji.
- Utrudnia skalowanie biznesu w miarę wzrostu obrotów i liczby dokumentów.

## 🟢 Rozwiązanie: Automatyzacja wspierana przez AI
Ten Blueprint tworzy rzetelny potok (pipeline), w którym:
1. **Odbiór Danych:** Webhook lub inna integracja płynnie wyłapuje przychodzące, nieustrukturyzowane dane tekstowe.
2. **AI-Driven Parsing:** Zapytanie jest formatowane do modeli **OpenAI (GPT / o1 models)** z wykorzystaniem specjalnie przygotowanego inżynierii promptów (Prompt Engineeringu). Sztuczna inteligencja skutecznie rozpoznaje kluczowe dane, takie jak data, kwoty, kontrahenci, opisy kosztów czy kategorie finansowe, z zamiarem wygenerowania czystego, twardego formatu (np. JSON).
3. **Zapis ustrukturyzowany:** Gotowe informacje trafiają w pełni bezobsługowo w odpowiednie struktury baz danych (w tym przykładzie: systemów Core Banking lub odpowiedniego Arkusza Google).

## 📈 Benefity Biznesowe
- **Redukcja Kosztów i Czasu pracy (ROI):** Zmniejszenie o 90%+ czasu potrzebnego do administracji danych. Zespół może skupić się w tym czasie na weryfikacji strategicznej, kontrolingu i analizie.
- **Odporność na błędy (Consistency):** Zastąpienie zasobnego w błędy wklepywania poprzez zestandaryzowane wyciąganie JSON-ów przez LLM, które jest dużo powtarzalniejsze.
- **Natychmiastowy Dostęp do Informacji:** Bieżące, nieprzerwane operacje (Real-time financial tracking), bez czekania na zbiorcze manualne księgowania pracownika.
- **Bezpieczeństwo i Anonimowość Konfiguracji:** Szablon w tym repozytorium ma zanonimizowane wrażliwe wejścia (takie jak maile, połączenia z systemami), pozwalając na darmowe udostępnianie procesów z ochroną danych. 

## ⚙️ Uruchomienie projektu (Korzystanie z szablonu)
Prywatne dane takie jak Twój adres e-mail, identyfikator połączeń z OpenAI / Google Sheets, czy też ID Arkuszy trzymaj w specjalnym pliku `.json`, unikając ujawniania ich w repozytorium GitHub!

1. Utwórz u siebie na dysku plik o nazwie `variables.json` (znajduje się w pliku `.gitignore`, więc na pewno nie wpadnie przez pomyłkę do sieci):
```json
{
  "YOUR_EMAIL": "twoj_adres_email@example.com",
  "YOUR_SPREADSHEET_ID": "id-twojego-arkusza",
  "OPENAI_CONNECTION_ID": 1111111,
  "GOOGLE_CONNECTION_ID": 2222222
}
```

2. Uruchom skrypt w Pythonie z poziomu konsoli:
```bash
python3 apply_variables.py
```

Skrypt odczyta plik `AI_Financial_Extraction.blueprint.json`, przypisze do niego Twoje bezpieczne zmienne tekstowe i utworzy gotowy plik pod nazwą `AI_Financial_Extraction_Ready.json`. 

3. Ten ostatni wygenerowany plik importujesz na żywo w interfejsie platformy Make. gotowe!
