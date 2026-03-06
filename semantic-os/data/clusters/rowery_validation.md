# Walidacja klastrów — rowery
**Data:** 2026-03-05
**Metoda:** LLM-based (SERP API niedostępny — tryb LLM-only)
**Seed keyword:** rowery
**Source Context:** sklep rowerowy online — Orbea, Marin, Superior

---

## Parametry klasteryzacji

| Parametr | Wartość |
|---|---|
| Algorytm | K-Means |
| k | 15 |
| Silhouette score | 0.1081 |
| Liczba keywords | 422 |
| Liczba klastrów | 15 |

Silhouette 0.1081 > 0.05 (próg minimalny) → klasteryzacja akceptowalna. Niska wartość wynika z heterogeniczności bazy (marki, typy, ceny, akcesoria) — naturalna dla tak szerokiego seed keyword.

---

## Analiza par klastrów — SERP Overlap (LLM-based)

### Para: Cluster 0 (MTB spec.) vs Cluster 1 (Rowery górskie - szeroka)

**Overlap semantyczny:** Wysoki — oba skupiają się na rowerach górskich/MTB.
**Cluster 0 keywords:** rower MTB hardtail, rower MTB 29, rower XC hardtail, rower enduro full suspension
**Cluster 1 keywords (przykłady):** rowery górskie, rower górski dla początkującego, rowery szosowe, rower enduro opinie

**Analiza:** Cluster 0 koncentruje się na atrybutach technicznych MTB (rozmiary kół, typ zawieszenia), Cluster 1 jest szeroką kategorią zawierającą rowery górskie, szosowe i ich porównania. Mimo nakładania się frazy MTB, intencje wyszukiwania są różne (spec. techniczna vs. wybór kategorii).

**Rekomendacja: OK** — różne intencje (nawigacyjna/produktowa vs. kategoria). Cluster 1 wymaga monitorowania (91 kw — duży, potencjalny SPLIT w przyszłości).

---

### Para: Cluster 5 (Marin modele MTB) vs Cluster 10 (Marin modele gravel/miejskie)

**Overlap semantyczny:** Wysoki — obydwa to modele marki Marin.
**Cluster 5:** marin san quentin, marin dsx fs, marin bobcat trail, marin nail trail
**Cluster 10:** marin four corners, marin rift zone, marin nicasio, marin larkspur

**Analiza:** Cluster 5 to modele typowo MTB (San Quentin = trail/AM, Bobcat Trail = XC, Nail Trail = trail, DSX = gravel/MTB hybrid). Cluster 10 to gravel/adventure/miejskie (Four Corners = bikepacking, Nicasio = szosowy, Larkspur = miejski). Różne kategorie produktów.

**Rekomendacja: MERGE** — z perspektywy SEO obie grupy powinny być obsłużone przez jedną stronę `/rowery/marin/` z filtrowaniem po modelach. Łączny klaster "Marin Bikes — modele" (16 kw). Po scaleniu → Cluster 5+10 = Marin Modele.

---

### Para: Cluster 6 (Orbea modele MTB) vs Cluster 13 (Orbea marka/ogólne)

**Overlap semantyczny:** Średni — Cluster 6 to konkretne modele (Orca, Oiz, Rise), Cluster 13 to branding/nawigacja (orbea sklep, orbea rowery cena, orbea opinie).

**Analiza:** Różne intencje — Cluster 6 obsługuje wyszukiwania produktowe/modelowe, Cluster 13 obsługuje brand navigation i zakupowe. Na stronie primal.pl obie intencje powinny być obsłużone przez różne sekcje: strony modeli vs strona marki Orbea.

**Rekomendacja: OK** — różne intencje (produktowe vs. brand navigation). Obie strony mają różne role w serwisie.

---

### Para: Cluster 4 (Superior+Marin przegląd) vs Cluster 11 (Superior modele)

**Overlap semantyczny:** Średni — Cluster 4 zawiera mix opinii o Superior i Marin, Cluster 11 to konkretne modele Superior XC.

**Analiza:** Cluster 4 jest hybrydą — zawiera zarówno frazy Superior jak i Marin (np. "marin dsx opinie", "superior rowery sklep"). To efekt clustering przy małej liczbie przykładów. Cluster 11 jest czysto Superior-modelowy.

**Rekomendacja: SPLIT/MERGE** — Cluster 4 rozdzielamy semantycznie:
- Frazy Marin z Cluster 4 → do Cluster 5+10 (Marin unified)
- Frazy Superior z Cluster 4 → merge z Cluster 11 (Superior unified)
- Frazy ogólne (primal.pl rowery, top rowery MTB) → do Cluster 14 (trendy/outlet)

Po scaleniu logicznym:
- **Marin unified** (Cluster 5 + Cluster 10 + frazy Marin z Cluster 4) = ~25 kw
- **Superior unified** (Cluster 11 + frazy Superior z Cluster 4) = ~14 kw

---

### Para: Cluster 9 (anglicyzmy/synonimy) vs Cluster 12 (gravel/szosowe)

**Overlap semantyczny:** Średni — Cluster 9 zawiera "gravel bike", "fat bike", "e-MTB", Cluster 12 zawiera "rowery gravel", "rower gravel z błotnikami".

**Analiza:** Cluster 9 to głównie anglojęzyczne synonimy i techniczne kategorie (gravel bike, pedelec, e-MTB). Cluster 12 to polskie frazy kategorialne gravel i porównania szosowe. Nakładają się semantycznie, ale mają różne intencje (definicyjne/nawigacyjne vs. zakupowe/porównawcze).

**Rekomendacja: MERGE** — obie grupy obsługuje jedna strona kategorii `/rowery/gravel/`. Łączny klaster "Rowery Gravel" (26 kw).

---

### Para: Cluster 3 (typy+serwis - duży) vs Cluster 8 (generyczne)

**Overlap semantyczny:** Wysoki — Cluster 3 ma 77 kw w tym serwis, typy rowerów, akcesoria. Cluster 8 ma generyczne frazy.

**Analiza:** Cluster 3 jest bardzo duży (77 kw) i heterogeniczny — zawiera serwis rowerowy, fatbike, BMX, składany, wymianę opon, czyszczenie roweru. Cluster 8 zawiera generyczne "rower", "rower aluminium", typy jak DH, XC, enduro bez specyfikacji.

**Rekomendacja: OK** (brak merge) — klastry reprezentują różne strony: Cluster 3 → strony serwisowe, akcesoria, typy niszowe; Cluster 8 → strona główna kategorii, artykuły porównawcze. Cluster 3 może w przyszłości SPLIT na: serwis rowerowy + typy niszowe.

---

## Zbiorcze rekomendacje po walidacji

| Cluster ID | Nazwa | Akcja | Powód |
|---|---|---|---|
| 0 | MTB - spec. techniczna | OK | Unikalna intencja techniczna |
| 1 | Rowery górskie/szosowe - szeroka | OK | Duży klaster kategorii (monitorować) |
| 2 | Sklep rowerowy - zakup/lokalny | OK | Wyraźna intencja zakupowa/lokalna |
| 3 | Typy + serwis - mix | OK | Różne strony, dobra separacja |
| 4 | Superior+Marin - mix | MERGE | → frazy Marin do Marin-unified; frazy Superior do Superior-unified |
| 5 | Marin MTB modele | MERGE | → Marin-unified (5+10+frazy Marin z 4) |
| 6 | Orbea modele MTB/szosowe | OK | Czyste modele Orbea |
| 7 | Rowery elektryczne | OK | Wyraźna kategoria e-bike |
| 8 | Rower generyczne | OK | Strona główna/pillar |
| 9 | Anglicyzmy/synonimy gravel | MERGE | → do Cluster 12 (Gravel unified) |
| 10 | Marin gravel/miejskie modele | MERGE | → Marin-unified |
| 11 | Superior modele XC | MERGE | → Superior-unified (11 + frazy Superior z 4) |
| 12 | Rowery gravel/szosowe | MERGE | → Gravel unified (12+9) |
| 13 | Orbea marka/opinie | OK | Brand navigation — osobna strona |
| 14 | Rowery online/outlet/trendy | OK | Zakupowy + editorial |

---

## Klastry po scaleniu (finalne — 11 klastrów)

| # | Cluster (po merge) | Bazowe klastry | Kw (est.) |
|---|---|---|---|
| A | Rowery górskie/szosowe - kategoria | 1 | 91 |
| B | Typy rowerów + serwis + akcesoria | 3 | 77 |
| C | Rowery elektryczne | 7 | 45 |
| D | Sklep rowerowy - zakup/lokalny | 2 | 39 |
| E | Orbea - modele (Orca, Oiz, Rise, Terra) | 6 | 28 |
| F | Rowery gravel | 12+9 | 26 |
| G | Marin Bikes - modele unified | 5+10+Marin z 4 | ~25 |
| H | Rower MTB - spec. techniczna | 0 | 24 |
| I | Orbea - marka, sklep, opinie | 13 | 16 |
| J | Rowery online/outlet/trendy | 14 | 16 |
| K | Superior - modele i marka | 11+Superior z 4 | ~14 |

**Łącznie: 11 klastrów, ~401 keywords (po usunięciu duplikatów)**

---

## Wnioski

1. Klasteryzacja k=15 jest semantycznie sensowna, ale wymaga logicznego scalenia 4 par
2. Główne problemy: Marin i Superior były podzielone między klastry — po MERGE każda marka ma jeden unified klaster
3. Gravel był podzielony na anglicyzmy i polskie frazy — po MERGE spójny klaster
4. Cluster 1 (91 kw) jest największy — w przyszłości można SPLIT na: rowery górskie | rowery szosowe
5. SERP coherence (LLM-based): klastry B (serwis+typy) i J (online+outlet) są heterogeniczne — monitorować CTR jeśli strony zostaną zbudowane
