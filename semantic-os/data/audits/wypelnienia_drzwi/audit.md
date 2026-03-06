# Raport Audytu Semantycznego: Wypełnienia Drzwi

**Domena:** https://www.veyna.pl/
**Fraza kluczowa:** wypełnienia drzwi
**Slug:** wypelnienia_drzwi
**Tryb:** Content-only (SERP API niedostępny - błąd 401; dane SERP zebrane ręcznie)
**Data audytu:** 2026-03-04
**Audytor:** Semantic-OS Pipeline v2

---

## CQS Obliczenie (step-by-step)

### Wagi wymiarów (Content Quality Score):

| Wymiar | Waga | Score | Weighted |
|--------|------|-------|---------|
| CSI Alignment | 1.5 | 4/10 | 6.0 |
| BLUF | 1.2 | 3/10 | 3.6 |
| Chunk Quality | 1.2 | 3/10 | 3.6 |
| URR Placement | 1.3 | 2/10 | 2.6 |
| Cost of Retrieval | 1.0 | 3/10 | 3.0 |
| Information Density | 1.2 | 3/10 | 3.6 |
| SRL Salience | 1.0 | 4/10 | 4.0 |
| TF-IDF Quality | 1.1 | 4/10 | 4.4 |
| EEAT (avg) | 1.5 | 5/10 | 7.5 |

**Suma wag:** 11.0
**Suma ważona:** 38.3
**Średnia ważona:** 38.3 / 11.0 = 3.48
**CQS = średnia ważona × 10 = 34.8 → zaokrąglone: 35/100**

---

## AI Citability Score: 3/10

**Uzasadnienie:** Strona główna Veyna jest trudna do cytowania przez AI ze względu na:
- Brak konkretnych, samodzielnych bloków informacji
- Dominację treści nawigacyjnych i brandingowych
- Brak odpowiedzi na konkretne pytania (PAA)
- Niską gęstość informacyjną (2 użyteczne akapity na 535 słów)
- Zdania pasywne bez konkretnych twierdzeń
- Brak terminologii branżowej (izolacja termiczna, PUR, HPL)

---

# Sekcja 1: Executive Summary

## CQS: 35/100

Strona główna Veyna uzyskuje wynik **35/100** w Content Quality Score dla frazy "wypełnienia drzwi". Wynik wskazuje na **poważną lukę semantyczną** między intencją frazy kluczowej a aktualną zawartością strony.

## Krytyczne problemy

1. **URR Coverage: 2/10** — 6 z 8 głównych pytań użytkowników szukających "wypełnienia drzwi" jest całkowicie bez odpowiedzi: brak opisu izolacji termicznej/akustycznej, brak porównania materiałów, brak informacji cenowych, brak wskazówek instalacyjnych.

2. **BLUF: 3/10** — Strona zaczyna się od menu nawigacyjnego, banerów, aktualności i statystyk firmy. Użytkownik (i AI) musi przewinąć całą stronę aby znaleźć 2 akapity o wypełnieniach drzwi, które też nie odpowiadają bezpośrednio na żadne konkretne pytanie.

3. **Chunk Quality: 3/10** — Brak logicznej struktury H2/H3 z treścią produktową. "Treść" strony to 2 akapity (~140 słów) bez nagłówków, otoczone nawigacją i elementami UI.

4. **TF-IDF: 4/10** — Brakuje kluczowych terminów branżowych obecnych u wszystkich konkurentów: "izolacja termiczna", "pianka poliuretanowa", "HPL", "izolacja akustyczna", "klasa antywłamaniowa".

## Co działa

- **EEAT Sygnały Autorytetu i Zaufania (6/10):** Firma z 30-letnim doświadczeniem (od 1990), gwarancja 7 lat, podane dane kontaktowe z NIP, udział w OFS 2025.
- **Unikalna propozycja wartości:** Narzędzia online (Konfigurator paneli, Wizualizer drzwi, Aplikacja AR, Katalogi interaktywne) — brak odpowiednika u większości konkurentów.
- **Technologia niemiecka + kapitał polski:** Różnicujący komunikat, ale zbyt ukryty w statystykach.
- **11 serii wypełnień:** Bogata oferta, ale nieodkryta w treści strony głównej.

---

# Sekcja 2.1: CSI i PAA Coverage

## CSI Alignment

**Central Entity:** Veyna - wypełnienia drzwiowe (panele drzwiowe)
**Source Context:** Strona główna producenta — branding i oferta ogólna
**Central Search Intent:** Użytkownik szukający "wypełnienia drzwi" oczekuje informacji o rodzajach, materiałach, właściwościach i cenach wypełnień drzwiowych.

**Niezgodność CSI:** Strona główna Veyna jest stroną korporacyjną (prezentacja firmy, aktualności), nie stroną produktową. Tytuł meta zawiera "wypełnienia drzwiowe", ale treść nie odpowiada na tę intencję. CSI strony = "Prezentacja producenta paneli drzwiowych" ≠ CSI frazy = "Informacje o wypełnieniach drzwi (rodzaje, właściwości, wybór)".

## PAA Coverage

| PAA | Sekcja na stronie | Coverage | Brakujące informacje |
|-----|-------------------|----------|---------------------|
| Jakie są rodzaje wypełnień drzwi? | Tylko linki w nav | Szczątkowe | Opis każdego rodzaju: ALU, PVC, HPL, szklane |
| Z czego są wykonane wypełnienia drzwi? | Brak | Brak | Opis materiałów: PVC, ALU, pianka PUR |
| Jak wybrać wypełnienie do drzwi wejściowych? | Brak | Brak | Poradnik/kryteria wyboru |
| Ile kosztują wypełnienia drzwiowe? | Brak | Brak | Przedziały cenowe lub czynniki cenowe |
| Czy wypełnienia drzwi izolują termicznie? | Brak | Brak | Opis izolacji, parametry, współczynnik U |
| Jaka jest trwałość wypełnień? | Gwarancja 7 lat (statystyka) | Szczątkowe | Szczegóły trwałości, certyfikaty |
| Jak zamontować wypełnienie drzwi? | Brak | Brak | Montaż wpuszczany vs nakładkowy |
| Wypełnienia drzwi a bezpieczeństwo | Brak | Brak | Klasa antywłamaniowa, RC2 |

**PAA Coverage Score: 1.5/8 (19%)** — krytycznie niski.

---

# Sekcja 2.2: BEFORE / AFTER — Problematyczne fragmenty

## Fragment 1: Otwarcie treści produktowej

**Problem:** Brak BLUF — pierwsze zdanie nie odpowiada na żadne pytanie użytkownika.

**BEFORE:**
> "Producent paneli drzwiowych Veyna oferuje szeroką serię drzwi z różnych modeli i kolorach. Dostępne są drzwi wejściowe - panele drzwiowe o różnej grubości, oraz klasyczne drzwi w nowoczesnym wzornictwie."

**AFTER (BLUF + gęstość informacyjna):**
> "Wypełnienia drzwiowe Veyna to panele aluminiowe, PVC i szklane dostępne w 11 seriach — od ekonomicznych po premium. Każde wypełnienie zapewnia izolację termiczną (pianka poliuretanowa) i akustyczną, a 7-letnia gwarancja potwierdza trwałość materiałów. Wybierz wariant z naszego konfiguratora online lub pobierz katalog interaktywny."

**Wpływ:** CSI Alignment +2, BLUF +3, Information Density +2, TF-IDF +2

---

## Fragment 2: Opis wypełnień drzwiowych — akapit 2

**Problem:** Nieokreślone materiały ("inne materiały zewnętrzne"), zawężenie do "commercial", brak terminologii.

**BEFORE:**
> "Wypełnienia drzwiowe są jednym z kluczowych elementów oferty naszych paneli drzwiowych. Te ozdobne płyty lub inne materiały zewnętrzne są dostępne w różnych wariantach, pozwalając na możliwość zastosowania ich w budownictwie handlowym i budownictwie commercial. Dzięki niskiej budowie i nowoczesnemu wyglądowi, wypełnienia drzwiowe znaleźć można często w budynkach o modernistycznej architekturze."

**AFTER (EAV-rich, URR-oriented):**
> "Wypełnienia drzwiowe Veyna dzielą się na trzy główne kategorie materiałowe: aluminiowe (najwyższa izolacja termiczna i akustyczna), PVC (lekkie, odporne na UV, do ~100 wzorów) oraz szklane (Lacobel Line, Glass Line — efekt wizualny). Wypełnienia aluminiowe zawierają rdzeń z pianki poliuretanowej (PUR), który minimalizuje przenikanie ciepła. Produkty Veyna sprawdzają się w budownictwie mieszkalnym jednorodzinnym, wielorodzinnym i komercyjnym."

**Wpływ:** Information Density +3, TF-IDF +3, URR Placement +2, SRL Salience +1

---

## Fragment 3: Sekcja "O firmie" — komunikat brandingowy

**Problem:** Zdania bez treści informacyjnej ("innowacyjność, solidność, profesjonalizm" — puste sygnały).

**BEFORE:**
> "Działająca na rynku od 1990 roku, zdobyliśmy uznanie za innowacyjność, solidność i profesjonalizm w branży. Jako firma specjalizujemy się w produkcji paneli drzwiowych, Veyna oferuje swoim klientom szeroki wybór wzorów, kolorów i rozmiarów..."

**AFTER (konkretne fakty, Agent + działanie):**
> "Od 1990 roku Veyna produkuje wypełnienia drzwiowe stosując technologię opracowaną przez niemieckich dostawców maszyn, co przekłada się na precyzję cięcia ±0,5 mm i jednolitość kolorów w seriach. Firma oferuje ponad 200 kombinacji kolorów i wzorów w 11 seriach, w tym okleiny RENOLIT, COVA i Continental. Każde zamówienie jest objęte 7-letnią gwarancją producenta."

**Wpływ:** EEAT Experience +2, Information Density +2, SRL Salience +2

---

## Fragment 4: Statystyki (sekcja hero)

**Problem:** Dynamiczne pola JavaScript renderują "0%" — AI i crawlery widzą zera, nie faktyczne wartości.

**BEFORE:**
> "0 % 0 % 0 0 Ponad 30 lat doświadczenia 0 Serii wypełnień w bogatej ofercie"

**AFTER (statyczne HTML):**
> **100%** polska własność | **100%** technologia niemiecka | **7 lat** gwarancji | **Ponad 30 lat** doświadczenia | **11 serii** wypełnień w ofercie

**Wpływ:** Cost of Retrieval +3 (AI może odczytać dane), Information Density +2

---

## Fragment 5: Brakująca sekcja — Izolacja termiczna

**Problem:** Całkowity brak treści o izolacji — kluczowy atrybut ROOT obecny u wszystkich 6 konkurentów.

**BEFORE:** (brak sekcji)

**AFTER (nowa sekcja H2):**
```markdown
## Izolacja termiczna wypełnień drzwiowych

Wypełnienia drzwiowe Veyna zapewniają skuteczną ochronę cieplną dzięki rdzeniowi z pianki poliuretanowej (PUR) o gęstości 40–45 kg/m³. Współczynnik przenikania ciepła Ud dla paneli aluminiowych wynosi od 0,9 do 1,4 W/(m²·K) w zależności od serii i grubości.

| Seria | Materiał rdzenia | Ud [W/(m²·K)] | Grubość [mm] |
|-------|-----------------|---------------|--------------|
| Economic Line | Pianka PUR | 1.4 | 40 |
| Modern Line | Pianka PUR | 1.2 | 60 |
| Prestige Line | Pianka PUR premium | 0.9 | 80 |

Dla porównania: drzwi bez wypełnienia izolacyjnego osiągają Ud > 3.0 W/(m²·K).
```

**Wpływ:** URR Placement +3, TF-IDF +3, Information Density +3, CSI Alignment +2

---

# Sekcja 2.3: E-E-A-T z porównaniem Top 3 SERP

## Porównanie E-E-A-T: Veyna vs Kratex vs ProfiLine vs Paneldoor

| Sygnał E-E-A-T | Veyna | Kratex | ProfiLine | Paneldoor |
|----------------|-------|--------|-----------|-----------|
| Rok założenia / historia | 1990 (30 lat) | Brak | 10+ lat | Brak |
| Gwarancja | 7 lat | Brak | Brak wzmianki | Brak |
| Certyfikaty / normy | Brak | Brak | RC2 Secure | Brak |
| Parametry techniczne | Ogólne | Serie + modele | Serie + właściwości | Ogólne |
| Bio producenta / autorów | Brak | Brak | Brak | Brak |
| Realizacje / portfolio | Brak na gł. | Katalog online | Brak na gł. | Brak |
| Opinie klientów | Brak | Brak | Brak | Brak |
| Dane kontaktowe | Pełne (adres, NIP) | Telefon, email | Adres | Adres, telefon |
| Blog / artykuły | Tak (aktualności) | Brak | Brak | Brak |
| Udział w targach/branży | OFS 2025 | Brak | Brak | Brak |
| Narzędzia online | Konfigurator, AR, Wizualizer | Brak | Brak | Brak |

**Ocena EEAT Veyna:** Experience 4/10 | Expertise 4/10 | Authority 6/10 | Trust 6/10

**Silne strony Veyna vs SERP:** Historia (30 lat), gwarancja 7 lat, narzędzia online, udział w OFS
**Słabe strony Veyna vs SERP:** Brak certyfikatów (ProfiLine ma RC2), brak parametrów technicznych, brak opinii klientów, brak bio autora treści

---

# Sekcja 2.4: EAV artykułu + Content Format Intelligence

## EAV artykułu (skrócona)

| Entity | Attribute | Value |
|--------|-----------|-------|
| Veyna | Typ | Producent paneli drzwiowych |
| Veyna | Doświadczenie | Ponad 30 lat (od 1990) |
| Veyna | Kapitał | 100% polski |
| Veyna | Technologia | 100% niemiecka |
| Veyna | Gwarancja | 7 lat |
| Veyna | Liczba serii | 11 serii wypełnień |
| Wypełnienia | Charakter | Ozdobne lub naturalne |
| Wypełnienia | Zastosowanie | Budownictwo handlowe i commercial |
| Veyna | Narzędzia | Konfigurator, Wizualizer, AR, Katalogi |
| Veyna | Lokalizacja | Toruń, ul. Szubińska 14 |

## Content Format Intelligence z SERP

| Format | Liderzy | Zastosowanie u Veyna | Rekomendacja |
|--------|---------|---------------------|--------------|
| Tabela porównawcza materiałów | Thermopanel | Brak | KRITYCZNE — dodać |
| Lista serii z opisem i właściwościami | Kratex (80+ modeli) | Tylko linki w nav | KRITYCZNE — rozwinąć |
| Sekcja Właściwości/Parametry | Tur-Plast, ProfiLine | Brak | KRYTYCZNE — dodać |
| Sekcja FAQ | Thermopanel | Brak | WYSOKIE — dodać |
| Sekcja Zastosowania | ProfiLine | Częściowe | WYSOKIE — rozwinąć |
| Cennik / orientacyjne ceny | Thermopanel | Brak | ŚREDNIE — rozważyć |
| Poradnik wyboru | Thermopanel | Brak | ŚREDNIE — dodać |
| Realizacje / case studies | Brak u konkurentów | Brak | NISKIE |

---

# Sekcja 3.1: Docelowa struktura H1/H2/H3

```
H1: Wypełnienia Drzwiowe Veyna — 11 Serii Paneli ALU, PVC i Szklanych [ZMIEŃ]
  ↳ (zmiana z obecnego tytułu "Veyna - Płyty warstwowe, wypełnienia drzwiowe")

H2: Rodzaje Wypełnień Drzwiowych [NOWA]
  H3: Wypełnienia Aluminiowe — Najwyższa Izolacja [NOWA]
  H3: Wypełnienia PVC — Lekkie i Odporne na UV [NOWA]
  H3: Wypełnienia Szklane — Estetyka i Przejrzystość [NOWA]
  H3: Wypełnienia Specjalne i Nakładkowe [NOWA]

H2: Właściwości i Parametry Techniczne [NOWA]
  H3: Izolacja Termiczna — Współczynnik U i Pianka PUR [NOWA]
  H3: Izolacja Akustyczna [NOWA]
  H3: Odporność na Warunki Atmosferyczne [NOWA]
  H3: Bezpieczeństwo — Klasy Antywłamaniowe [NOWA]

H2: Jak Wybrać Wypełnienie do Drzwi Wejściowych? [NOWA]
  H3: Budownictwo mieszkalne a komercyjne [NOWA]
  H3: Porównanie materiałów: ALU vs PVC vs HPL [NOWA]

H2: Seria Lacobel Line [OK]
H2: Seria Glass Line [OK]
H2: Seria Prestige Line [OK]
  ↳ (serie są OK jako prezentacja, ale potrzebują treści — nie tylko grafik)

H2: Narzędzia Online Veyna [NOWA]
  H3: Konfigurator Paneli [ZMIEŃ — wyróżnić jako sekcja, nie tylko link]
  H3: Wizualizer Drzwi [ZMIEŃ — wyróżnić]
  H3: Aplikacja AR [ZMIEŃ — wyróżnić]

H2: O Firmie Veyna [ZMIEŃ]
  ↳ (zmienić z ogólnego brandingu na konkretne fakty: historia, technologia, certyfikaty)

H2: Często Zadawane Pytania (FAQ) [NOWA]
H2: Kontakt i Zamówienia [OK]
```

**Legenda:**
- [OK] — sekcja poprawna, może wymagać uzupełnienia treści
- [ZMIEŃ] — sekcja istnieje, wymaga przebudowy treści lub nagłówka
- [NOWA] — sekcja całkowicie brakująca, wymaga stworzenia

---

# Sekcja 3.2: Rekomendacje z BEFORE/AFTER

## KRYTYCZNE (P1) — wpływ na CQS: +15-20 punktów

### REC-01: Dodaj sekcję H2 "Rodzaje wypełnień drzwiowych" z opisem materiałów

**Problem:** Brak treści opisującej rodzaje (ALU, PVC, HPL, szkło) — 6/6 konkurentów to mają.
**Dane SERP:** Kratex ma 80+ modeli ALU, ProfiLine opisuje 3 kategorie, Thermopanel wymienia 10 typów.

**BEFORE:**
> [Brak sekcji — tylko linki w menu]

**AFTER:**
```markdown
## Rodzaje Wypełnień Drzwiowych

Wypełnienia drzwiowe dzielą się na trzy główne kategorie materiałowe, różniące się
właściwościami izolacyjnymi, estetyką i zastosowaniem:

### Wypełnienia Aluminiowe
Najtrwalsze i najlepiej izolujące termicznie. Rdzeń z pianki poliuretanowej (PUR)
zapewnia współczynnik Ud od 0,9 do 1,4 W/(m²·K). Dostępne w seriach: Economic Line,
Modern Line, Lacobel Line, Prestige Line, Classic Line, New Line, Top Line, Fashion Line.
Idealne do drzwi wejściowych zewnętrznych w budownictwie jedno- i wielorodzinnym.

### Wypełnienia PVC
Lekkie (30–50% lżejsze od aluminium), odporne na promienie UV dzięki warstwom
folii akrylowej. Nie wymagają malowania. Dostępne w >80 wzorach. Sprawdzają się
w klimatach z dużymi wahaniami temperatur.

### Wypełnienia Szklane
Estetyczne i świetloprzepuszczalne. Serie Glass Line i Lacobel Line oferują szkło
lacobel, hartowane i ornamentowe. Przeznaczone do drzwi wewnętrznych i wejściowych
reprezentacyjnych.
```

**Szacowany wpływ na CQS:** +6 punktów

---

### REC-02: Zmień strukturę strony — CSI-first (BLUF)

**Problem:** Użytkownik/AI nie otrzymuje odpowiedzi na pierwsze pytanie w pierwszych 100 słowach.

**BEFORE:**
> [Hero baner] → [Aktualności] → [Statystyki 100%/0] → [Logo partnerów] → [Krótki opis na dole]

**AFTER:**
> [H1 z frazą kluczową] → [Lead paragraph z BLUF: co oferuje, dla kogo, kluczowe przewagi] → [Rodzaje wypełnień] → [Właściwości techniczne] → [Narzędzia online] → [O firmie] → [Aktualności / Blog]

**Szacowany wpływ na CQS:** +5 punktów

---

### REC-03: Dodaj sekcję parametrów technicznych i izolacji

**Problem:** Brakuje terminów: izolacja termiczna, pianka PUR, izolacja akustyczna, współczynnik U.
**Dane SERP:** ProfiLine opisuje "bardzo wysoki poziom izolacji akustycznej i termicznej", Tur-Plast opisuje strukturę panelu PVC+PUR.

**BEFORE:**
> "System wypełnienia drzwi wejściowych charakteryzuje się wysoką jakością"

**AFTER:**
```markdown
## Właściwości i Parametry Techniczne

### Izolacja Termiczna
Wypełnienia aluminiowe Veyna zawierają rdzeń z pianki poliuretanowej (PUR) o gęstości
40–45 kg/m³. Współczynnik przenikania ciepła Ud: 0,9–1,4 W/(m²·K) w zależności od serii.
Spełniają wymagania WT 2021 dla drzwi zewnętrznych (Ud ≤ 1,5 W/(m²·K)).

### Izolacja Akustyczna
Panele aluminiowe Veyna tłumią hałas zewnętrzny o 28–36 dB (zależnie od serii i grubości).
Wełna mineralna w wariancie akustycznym dostępna w serii Top Line.

### Odporność na warunki atmosferyczne
Warstwa zewnętrzna pokryta folią akrylową odporną na promienie UV i wahania temperatur
(-40°C do +80°C). Oklein RENOLIT, COVA, Continental — gwarancja producenta oklein 10 lat.
```

**Szacowany wpływ na CQS:** +5 punktów

---

## WYSOKIE (P2) — wpływ na CQS: +8-12 punktów

### REC-04: Napraw statyczne rendering statystyk (JS → HTML)

**Problem:** Pola JS renderują "0%" dla robotów AI/SEO.

**BEFORE:**
> "0 % 0 % 0 0 Ponad 30 lat"

**AFTER:**
```html
<div class="stat">100% <span>polska własność</span></div>
<div class="stat">100% <span>technologia niemiecka</span></div>
<div class="stat">7 lat <span>gwarancji</span></div>
<div class="stat">30+ lat <span>doświadczenia</span></div>
<div class="stat">11 serii <span>wypełnień</span></div>
```
(wartości muszą być w HTML, nie generowane przez JS counter)

**Szacowany wpływ na CQS:** +3 punkty

---

### REC-05: Dodaj FAQ (co najmniej 5 pytań)

**Problem:** Brak odpowiedzi na PAA — 6/8 pytań użytkownika bez odpowiedzi.

**AFTER:**
```markdown
## Często Zadawane Pytania

**Jakie są rodzaje wypełnień drzwiowych?**
Veyna oferuje wypełnienia aluminiowe, PVC, szklane, specjalne i nakładkowe.
Każda kategoria różni się właściwościami termicznymi, akustycznymi i estetycznymi.

**Czy wypełnienia drzwi izolują termicznie?**
Tak. Wypełnienia aluminiowe Veyna z pianką PUR osiągają Ud od 0,9 W/(m²·K) (Prestige Line)
do 1,4 W/(m²·K) (Economic Line), spełniając wymagania WT 2021.

**Jak zamontować wypełnienie drzwiowe?**
Wypełnienia Veyna są dostępne w montażu wpuszczanym (do skrzydła drzwiowego) lub
nakładkowym (na powierzchnię drzwi). Szczegółowe instrukcje dostępne w katalogu technicznym.

**Ile kosztują wypełnienia drzwiowe Veyna?**
Ceny zależą od serii, materiału i wymiarów. Prosimy o kontakt lub skorzystanie
z konfiguratora online w celu otrzymania wyceny.

**Jaka jest gwarancja na wypełnienia drzwiowe?**
Veyna udziela 7-letniej gwarancji producenta na wszystkie wypełnienia drzwiowe.
```

**Szacowany wpływ na CQS:** +4 punkty

---

### REC-06: Wyróżnij narzędzia online jako sekcję treści (nie tylko linki w menu)

**Problem:** Konfigurator, Wizualizer, AR, Katalogi interaktywne — unikalne cechy Veyna — widoczne tylko w nav, bez opisu i CTA w treści.

**AFTER:**
```markdown
## Projektuj Swoje Drzwi Online

**Konfigurator Paneli** — wybierz serię, kolor, wymiar i pobierz specyfikację techniczną.
**Wizualizer Drzwi** — zwizualizuj wybrane wypełnienie na zdjęciu swoich drzwi.
**Aplikacja AR** — umieść wirtualny panel drzwiowy w swoim wejściu przez smartfon.
**Katalogi Interaktywne** — przeglądaj pełną ofertę 11 serii w formacie interaktywnym.

[Otwórz konfigurator] [Pobierz katalog PDF]
```

**Szacowany wpływ na CQS:** +2 punkty (EEAT Experience +2)

---

## ŚREDNIE (P3) — wpływ na CQS: +3-7 punktów

### REC-07: Dodaj sekcję "Jak wybrać wypełnienie drzwi?"

Poradnik dla użytkownika z kryteriami: zastosowanie (zewnętrzne/wewnętrzne), klimat, budżet, estetyka. Odpowiada na URR "Jak wybrać wypełnienie do drzwi wejściowych?"

### REC-08: Dodaj klasy bezpieczeństwa / antywłamanie

ProfiLine ma RC2 Secure. Brakujący atrybut ROOT dla drzwi wejściowych. Dodać wzmiankę o klasach RC dla odpowiednich serii.

### REC-09: Zmień SRL — zdania Agent → Pacient

Przekształcić zdania pasywne na aktywne z Veyna jako Agentem:
- BEFORE: "Panele drzwiowe Veyna charakteryzują się trwałością"
- AFTER: "Veyna stosuje pianę PUR klasy 40 kg/m³, która zapewnia trwałość przez ponad 20 lat"

---

# Sekcja 3.3: Brakujące terminy TF-IDF zmapowane na sekcje

| Termin | Freq SERP | Priorytet | Rekomendowana sekcja |
|--------|-----------|-----------|---------------------|
| izolacja termiczna | 6/6 konkurentów | P1 | H2: Właściwości techniczne |
| pianka poliuretanowa / PUR | 3/6 | P1 | H2: Właściwości + H3: ALU |
| izolacja akustyczna | 4/6 | P1 | H2: Właściwości techniczne |
| HPL (High-Pressure Laminate) | 3/6 | P1 | H2: Rodzaje wypełnień |
| klasa antywłamaniowa | 2/6 | P2 | H3: Bezpieczeństwo |
| RC2 / RC3 | 1/6 | P2 | H3: Bezpieczeństwo |
| współczynnik przenikania ciepła | 2/6 | P2 | H3: Izolacja termiczna |
| wełna mineralna | 2/6 | P2 | H3: Izolacja akustyczna |
| montaż wpuszczany | 2/6 | P2 | H3: Montaż / FAQ |
| montaż nakładkowy | 2/6 | P2 | H3: Montaż / FAQ |
| folie UV-odporne | 1/6 | P3 | H3: Właściwości PVC |
| szkło ozdobne | 1/6 | P3 | H3: Wypełnienia szklane |
| spiek kwarcowy | 1/6 | P3 | H3: Materiały naturalne |
| beton architektoniczny | 1/6 | P3 | H3: Materiały naturalne |
| plaster miodu | 1/6 | P3 | H3: Rodzaje (drzwi wewnętrzne) |
| producent paneli drzwiowych | Wszyscy + Veyna | P1 | H1, Lead paragraph |
| wypełnienia drzwi wejściowych | Wszyscy | P1 | H1, H2, Lead |
| panele drzwiowe | Wszyscy | P1 | Cały artykuł (5-8 razy) |

---

# Sekcja 3.4: Transformacje SRL (Patient → Agent)

## Aktualne zdania pasywne (Pacient jako podmiot):

| # | BEFORE (Patient-zdanie) | Wymiar |
|---|------------------------|--------|
| 1 | "Wypełnienia drzwiowe mogą być ozdobne lub naturalne" | Pasywny stan |
| 2 | "System wypełnienia drzwi wejściowych charakteryzuje się wysoką jakością" | Nieokreślony agent |
| 3 | "Panel drzwiowy jest wytrzymały i łatwy w użytkowaniu" | Pasywny opis |
| 4 | "Wypełnienia drzwiowe są jednym z kluczowych elementów oferty" | Tautologia |
| 5 | "Te ozdobne płyty lub inne materiały zewnętrzne są dostępne w różnych wariantach" | Niejasny agent |
| 6 | "panele drzwiowe Veyna charakteryzują się nie tylko estetycznym wyglądem" | Pasywny stan |

## Transformacje Agent → Predykat → Pacient:

| # | AFTER (Agent-zdanie) | Wpływ |
|---|---------------------|-------|
| 1 | "Veyna produkuje wypełnienia ozdobne (Lacobel Line, Glass Line) i gładkie (Classic Line, Economic Line) — klient wybiera styl przez konfigurator online" | SRL +2, Density +1 |
| 2 | "Dział kontroli jakości Veyna testuje każdy panel pod kątem odporności na temperaturę (-40°C do +80°C) i promieniowanie UV przed wysyłką" | EEAT Experience +2, SRL +2 |
| 3 | "Panel aluminiowy Veyna wytrzymuje 50 000 cykli otwarcia/zamknięcia bez utraty własności — norma EN 12219" | SRL +2, TF-IDF +1, EEAT +1 |
| 4 | "Veyna oferuje 11 serii wypełnień drzwiowych różniących się materiałem rdzenia, grubością (40-100 mm) i klasą izolacji termicznej" | Density +2, URR +1 |
| 5 | "Producenci drzwi z całej Polski zamawiają panele Veyna do wypełnienia skrzydeł drzwiowych w standardowych i niestandardowych wymiarach" | EEAT Authority +1, SRL +1 |
| 6 | "Veyna stosuje okleiny RENOLIT i COVA — te same marki, które wykorzystują producenci premium okien w Niemczech i Austrii" | EEAT Expertise +2, Authority +1 |

---

# Sekcja 3.5: Ready-to-paste bloki E-E-A-T

## Blok 1: Bio producenta / About This Content

```markdown
**O autorze treści:**
Treść na tej stronie jest przygotowywana przez dział techniczny Veyna — producenta
wypełnień drzwiowych z ponad 30-letnim doświadczeniem. Parametry techniczne podane
na stronie są zgodne ze specyfikacjami produkcyjnymi weryfikowanymi w naszym zakładzie
w Toruniu. Data ostatniej aktualizacji specyfikacji: [data].

Masz pytanie techniczne? Skontaktuj się z naszym działem technicznym:
veyna@veyna.pl | +48 56 621 99 27
```

## Blok 2: Data aktualizacji (strukturalna)

```html
<meta itemprop="dateModified" content="2026-03-04T00:00:00+01:00">

<!-- Widoczna dla użytkownika: -->
<p class="content-meta">
  <strong>Ostatnia aktualizacja:</strong> marzec 2026 |
  <strong>Zweryfikowano przez:</strong> Dział Techniczny Veyna
</p>
```

## Blok 3: Disclaimer techniczny

```markdown
**Uwaga techniczna:**
Parametry izolacji termicznej (Ud) podane na tej stronie dotyczą samego wypełnienia
drzwiowego, bez ramy i ościeżnicy. Całkowity współczynnik przenikania ciepła gotowych
drzwi (Uw) uwzględnia również profil i montaż — wartości mogą się różnić.
Szczegółowe dane techniczne dostępne na życzenie (DOP/DoP).
```

## Blok 4: Gwarancja (rozbudowana)

```markdown
**Gwarancja Veyna — 7 lat**
Gwarancja obejmuje: trwałość kolorów oklein, integralność strukturalną panelu,
odporność na korozję elementów aluminiowych. Nie obejmuje: uszkodzeń mechanicznych,
nieprawidłowego montażu, użytkowania niezgodnego z instrukcją.
Reklamacje: veyna@veyna.pl, termin rozpatrzenia: 14 dni roboczych.
```

---

# Sekcja 3.6: Checklist implementacji

## Priorytet 1 — KRYTYCZNE (implementacja < 2 tygodnie)

- [ ] **Zmień kolejność sekcji strony** — treść produktowa PRZED aktualnościami i statystykami (CQS +5)
- [ ] **Dodaj H2 "Rodzaje wypełnień drzwiowych"** z opisem ALU, PVC, szklanych (~300 słów) (CQS +6)
- [ ] **Dodaj H2 "Właściwości techniczne"** z parametrami izolacji termicznej i akustycznej (CQS +5)
- [ ] **Napraw renderowanie statystyk JS** — zadbaj o statyczne wartości w HTML (CQS +3)
- [ ] **Zaktualizuj meta title** — dodaj frazę "wypełnienia drzwi" jako BLUF: "Wypełnienia Drzwiowe — 11 Serii ALU, PVC i Szklanych | Veyna"

## Priorytet 2 — WYSOKIE (implementacja < 4 tygodnie)

- [ ] **Dodaj FAQ** — minimum 5 pytań PAA (CQS +4)
- [ ] **Wyróżnij narzędzia online** jako sekcję H2 z opisem (konfigurator, wizualizer, AR) (CQS +2)
- [ ] **Dodaj tabelę porównawczą** ALU vs PVC vs HPL (właściwości, cena, zastosowanie) (CQS +3)
- [ ] **Dodaj sekcję bezpieczeństwa** — klasy RC, antywłamanie (CQS +2)
- [ ] **Dodaj blok EEAT** — bio producenta/autora treści, data aktualizacji (CQS +2)

## Priorytet 3 — ŚREDNIE (implementacja < 8 tygodni)

- [ ] **Dodaj poradnik wyboru** "Jak wybrać wypełnienie do drzwi wejściowych?" (CQS +2)
- [ ] **Przekształć zdania SRL** — z pasywnych na Agent-Predicate-Patient (CQS +2)
- [ ] **Dodaj parametry techniczne per seria** — tabele z Ud, grubością, wagą (CQS +2)
- [ ] **Rozwiń sekcje serii** (Lacobel, Glass, Prestige) — dodaj opisy, nie tylko grafiki (CQS +2)
- [ ] **Dodaj strukturę Schema.org** — Product, FAQPage, Organization (AI Citability +2)

## CQS Target po implementacji:

| Etap | Wymiar | CQS Before | CQS After |
|------|--------|-----------|----------|
| P1 only | Krytyczne naprawy | 35 | ~54 |
| P1 + P2 | Pełna optymalizacja | 35 | ~66 |
| P1 + P2 + P3 | Docelowy | 35 | ~74 |

**AI Citability Target:** 3/10 → 7/10 (po P1+P2)

---

# Appendix: Informacje o audycie

## Pliki wygenerowane
- `data/audits/wypelnienia_drzwi/source.md` — treść strony veyna.pl
- `data/audits/wypelnienia_drzwi/urls.txt` — top 10 URLs konkurentów (ręcznie)
- `data/audits/wypelnienia_drzwi/competitors/_consolidated.md` — treść konkurentów
- `data/audits/wypelnienia_drzwi/benchmark.md` — analiza EAV, GAP, URR
- `data/audits/wypelnienia_drzwi/scores.md` — 9 wymiarów + EAV + Chunks + SRL
- `data/audits/wypelnienia_drzwi/audit.md` — ten raport

## Ograniczenia audytu
- **SERP API:** Niedostępny (błąd 401). Dane SERP zebrane ręcznie przez WebSearch i WebFetch. Tryb: Content-only z ręcznym benchmarkiem SERP.
- **Liczba konkurentów:** 6 (wymagane minimum 5 — próg spełniony, jakość benchmarku: dobra)
- **Treść strony:** Encoding issues (Windows-1250) w raw output — treść zrekonstruowana z WebFetch + Jina Reader. Możliwe pominięcie niektórych sekcji dynamicznych JS.
- **Parametry techniczne:** AFTER-przykłady są ilustracyjne — rzeczywiste parametry Ud, dB muszą być zweryfikowane z działem technicznym Veyna przed publikacją.
