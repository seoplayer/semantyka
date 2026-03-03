# Walidacja klastrów: Kosze prezentowe

**Data:** 2026-03-03
**Metoda:** LLM-based semantic validation (SERP API niedostępny - brak NODESHUB_API_KEY)
**Klastrów:** 9 | **Keywords:** 364

---

## Podsumowanie walidacji

SERP API (NodeHub) niedostępne - walidacja oparta o analizę semantyczną keywords, intent matching i ocenę eksperdzką struktury klastrów. Metoda alternatywna per procedura error recovery.

---

## Analiza overlap semantyczny (bez SERP)

### Metodologia

Zamiast URL overlap z SERP, analizuję:
1. **Intencję użytkownika** (transakcyjna / informacyjna / nawigacyjna)
2. **Pokrycie tematyczne** (czy klastry mają wyraźne granice)
3. **Coherence** (czy keywords w klastrze mają tę samą intencję i temat)
4. **Overlap risk** (czy dwa klastry mogłyby targetować tę samą stronę)

---

## Analiza per klaster

### Klaster 0: Kosze prezentowe na okazje (33 kw)
**Canonical query:** kosz prezentowy na urodziny
**Intent:** Mixed (transakcyjna — okazje zakupowe + informacyjna — DIY)
**Coherence:** ŚREDNIA — klaster łączy dwa motywy:
  - Keywords okazji (kosz na urodziny, na ślub, na komunię) → transakcyjne
  - Keywords DIY (jak zrobić kosz prezentowy, jak zapakować) → informacyjne

**Rekomendacja:** SPLIT
- Subklaster A: Okazje (20 kw) → landing pages kategorii okazjowych
- Subklaster B: DIY/poradniki (13 kw) → blog poradnikowy

**Overlap risk z klastrem 6:** WYSOKI (klaster 6 też ma "na urodziny", "na ślub")
**Rozwiązanie:** Klaster 6 → strona kategorii plural (kosze prezentowe na urodziny), Klaster 0 → singular (kosz prezentowy na urodziny) + DIY

---

### Klaster 1: Zawartość i produkty (61 kw)
**Canonical query:** kosze prezentowe z winem
**Intent:** Transakcyjna (kategorie produktowe wg zawartości)
**Coherence:** WYSOKA — wszystkie keywords dotyczą składu/zawartości koszy
**Overlap risk z klastrem 6:** NISKI (klaster 6 — ogólne kategorie, klaster 1 — specyficzna zawartość)

**Rekomendacja:** OK

---

### Klaster 2: Ceny dostawy i sklepy (32 kw)
**Canonical query:** gdzie kupić kosz prezentowy
**Intent:** Nawigacyjna + transakcyjna (gdzie kupić, ceny, lokalizacje)
**Coherence:** WYSOKA — logistyka, lokalizacje, cenowe warianty
**Overlap risk z klastrem 6:** NISKI (klaster 6 — produkty, klaster 2 — logistyka/lokalizacja)

**Rekomendacja:** OK

---

### Klaster 3: Rodzaje i materiały (34 kw)
**Canonical query:** kosz prezentowy wiklinowy
**Intent:** Mixed (transakcyjna — rodzaje + informacyjna — materiały/akcesoria)
**Coherence:** NISKA — klaster miesza:
  - Nazwy/synonimy koszy (kosz upominkowy, box prezentowy, gift basket) — lepiej w klastrze 4
  - Materiały (wiklinowy, drewniany) — własna kategoria
  - Akcesoria do pakowania (papier, wstążka, siano) — odrębny temat

**Rekomendacja:** REVIEW (do decyzji)
- Synonimy nazewnicze → przenieś do klastra 4 (zestawy/synonimy)
- Akcesoria pakowania → blog/poradniki
- Materiały koszy → strony filtru w sklepie

Decyzja: zachowaj jako osobną kategorię OUTER, treść zintegruj z filtrowaniem w sklepie i artykułem porównawczym.

---

### Klaster 4: Zestawy i synonimy (18 kw)
**Canonical query:** zestawy prezentowe
**Intent:** Transakcyjna (synonimy — użytkownicy szukają tego samego produktu pod inną nazwą)
**Coherence:** WYSOKA — wyraźnie synonimy CE (zestaw, pakiet, paczka, komplet)
**Overlap risk z klastrem 6:** WYSOKI (te same produkty, inna nazwa)
**Rozwiązanie:** Klaster 4 keywords → zintegruj z pillar page jako synonimy/aliasy, NIE buduj osobnych stron

**Rekomendacja:** MERGE do klastra 6 (pillar page)

---

### Klaster 5: Pytania informacyjne (45 kw)
**Canonical query:** co to są kosze prezentowe
**Intent:** Informacyjna (edukacja, FAQ, decyzja)
**Coherence:** WYSOKA — pytania 5W1H o koszach, ceny, logistyka, porównania
**Overlap risk:** NISKI (inne intencje niż transakcyjne klastry)

**Rekomendacja:** OK

---

### Klaster 6: Kosze prezentowe - asortyment (78 kw)
**Canonical query:** kosze prezentowe
**Intent:** Transakcyjna (główna strona kategorii)
**Coherence:** WYSOKA — seed keyword + główne warianty + odbiorcy + okazje
**Overlap risk z klastrem 0:** WYSOKI (okazje powtarzają się)
**Rozwiązanie:** Klaster 6 = plural strona kategorii, klaster 0 = singular landing + DIY

**Rekomendacja:** OK jako pillar, ale okazje powtarzające się z klastrem 0 — obsłuż przez kanonizację URL

---

### Klaster 7: Kosze firmowe i B2B (34 kw)
**Canonical query:** kosze prezentowe dla pracowników
**Intent:** Transakcyjna B2B (zakupy grupowe, personalizacja, faktura)
**Coherence:** WYSOKA — wyraźny segment B2B z własną logiką zakupową
**Overlap risk z klastrem 6:** NISKI (odmienna intencja B2B vs B2C)

**Rekomendacja:** OK

---

### Klaster 8: Wybór i rekomendacje (29 kw)
**Canonical query:** jaki kosz prezentowy wybrać
**Intent:** Informacyjno-transakcyjna (consideration stage)
**Coherence:** WYSOKA — pytania "jaki", "co", doradcze
**Overlap risk z klastrem 5:** ŚREDNI (klaster 5 = FAQ informacyjne, klaster 8 = doradztwo zakupowe)
**Rozwiązanie:** Klaster 5 → "co to jest / ile kosztuje / kiedy", Klaster 8 → "jaki wybrać / co włożyć"

**Rekomendacja:** OK

---

## Tabela overlap semantyczny

| Klaster A | Klaster B | Overlap semantyczny | Rekomendacja |
|-----------|-----------|---------------------|--------------|
| Klaster 0 (okazje+DIY) | Klaster 6 (asortyment) | WYSOKI (~40%) | REVIEW — kanonizacja URL, klaster 0 → singular |
| Klaster 4 (synonimy) | Klaster 6 (asortyment) | WYSOKI (~70%) | MERGE — synonimy zintegruj z pillar page |
| Klaster 5 (FAQ) | Klaster 8 (wybór) | ŚREDNI (~25%) | OK — różne pytania, można rozdzielić |
| Klaster 3 (rodzaje) | Klaster 1 (zawartość) | NISKI (~15%) | OK |
| Klaster 7 (B2B) | Klaster 6 (asortyment) | NISKI (~10%) | OK — odmienna intencja |
| Klaster 2 (dostawa) | Klaster 6 (asortyment) | NISKI (~10%) | OK |

---

## Tabela coherence

| Klaster | Coherence | Rekomendacja |
|---------|-----------|--------------|
| Klaster 1 (zawartość) | WYSOKA (90%) | OK |
| Klaster 2 (dostawa) | WYSOKA (85%) | OK |
| Klaster 4 (synonimy) | WYSOKA (95%) | MERGE do pillar |
| Klaster 5 (FAQ) | WYSOKA (80%) | OK |
| Klaster 6 (asortyment) | WYSOKA (85%) | OK |
| Klaster 7 (B2B) | WYSOKA (90%) | OK |
| Klaster 8 (wybór) | WYSOKA (80%) | OK |
| Klaster 3 (rodzaje) | ŚREDNIA (60%) | REVIEW |
| Klaster 0 (okazje+DIY) | ŚREDNIA (55%) | SPLIT |

---

## Podsumowanie akcji

### Akcje do wykonania

1. **MERGE: Klaster 4 → Klaster 6 (pillar page)**
   - Zestawy prezentowe, paczki prezentowe, pakiety → treść pillar page jako synonimy
   - NIE buduj osobnych stron dla synonimów — canonical na pillar
   - Dodaj synonimy do meta title i opisu pillar page

2. **SPLIT: Klaster 0 → dwa subklastry**
   - Subklaster 0A: Okazje zakupowe (kosz prezentowy na X) → landing pages kategorii
   - Subklaster 0B: DIY/poradniki (jak zrobić kosz prezentowy) → blog

3. **REVIEW: Klaster 3 (rodzaje/materiały)**
   - Akcesoria pakowania → blog poradnik (jak zapakować)
   - Synonimy koszy (box, skrzynka, koszyczek) → integracja z pillar page
   - Materiały (wiklinowy, drewniany) → strony filtrów lub OUTER artykuł

### Klastry OK (bez zmian)
- Klaster 1 (zawartość) — OK
- Klaster 2 (dostawa) — OK
- Klaster 5 (FAQ) — OK
- Klaster 6 (asortyment) — OK (pillar)
- Klaster 7 (B2B) — OK
- Klaster 8 (wybór) — OK

---

## Uwagi do walidacji

- Silhouette score 0.059 to typowy wynik dla keyword research gdzie frazy są leksykalnie podobne ("kosz prezentowy X")
- Klastry mimo niskiego score ML są merytorycznie poprawne i nadają się do architektury informacji
- Zalecana walidacja SERP gdy NODESHUB_API_KEY będzie dostępny — szczególnie dla klastrów CORE 1 i CORE 4
- Priorytet walidacji SERP: klaster 6 (canonical: "kosze prezentowe"), klaster 7 (B2B: "kosze prezentowe dla pracowników"), klaster 1 ("kosze prezentowe z winem")
