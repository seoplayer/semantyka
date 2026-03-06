# Struktura serwisu — rowery / primal.pl
**Data:** 2026-03-05
**Seed keyword:** rowery
**Klient:** primal.pl — sklep rowerowy online (Orbea, Marin, Superior)

---

## 1. Drzewo ASCII — pełna hierarchia z priorytetami P0–P3

```
primal.pl/
│
├── [P0] /rowery/                          ← PILLAR — Rowery sklep internetowy
│   │    Canonical: "rowery sklep internetowy"
│   │    CE: Rower | Schema: ItemList, BreadcrumbList
│   │
│   ├── [P0] /rowery/gorskie/              ← Rowery górskie — kategoria
│   │   │    Canonical: "rowery górskie"
│   │   │    CE: Rower górski | Schema: ItemList
│   │   │
│   │   ├── [P1] /rowery/gorskie/mtb/      ← MTB hardtail i full sus
│   │   │        Canonical: "rower MTB hardtail"
│   │   │        CE: Rower MTB
│   │   │
│   │   ├── [P1] /rowery/gorskie/enduro/   ← Enduro full suspension
│   │   │        Canonical: "rower enduro"
│   │   │        CE: Rower enduro
│   │   │
│   │   └── [P1] /rowery/gorskie/xc/       ← Cross-country (XC)
│   │            Canonical: "rower XC"
│   │            CE: Rower XC
│   │
│   ├── [P0] /rowery/szosowe/              ← Rowery szosowe — kategoria
│   │        Canonical: "rowery szosowe"
│   │        CE: Rower szosowy | Schema: ItemList
│   │
│   ├── [P0] /rowery/elektryczne/          ← Rowery elektryczne — kategoria
│   │        Canonical: "rowery elektryczne"
│   │        CE: Rower elektryczny | Schema: ItemList, FAQPage
│   │
│   ├── [P1] /rowery/gravel/               ← Rowery gravel — kategoria
│   │        Canonical: "rowery gravel"
│   │        CE: Rower gravel | Schema: ItemList, FAQPage
│   │
│   ├── [P1] /rowery/trekkingowe/          ← Rowery trekkingowe
│   │        Canonical: "rowery trekkingowe"
│   │        CE: Rower trekkingowy
│   │
│   ├── [P1] /rowery/miejskie/             ← Rowery miejskie
│   │        Canonical: "rowery miejskie"
│   │        CE: Rower miejski
│   │
│   ├── [P1] /rowery/orbea/                ← MARKA: Orbea — landing page
│   │   │    Canonical: "rowery Orbea"
│   │   │    CE: Orbea | Schema: Brand, ItemList, AggregateRating
│   │   │
│   │   ├── [P2] /rowery/orbea/orca/        ← Orbea Orca (szosowe)
│   │   ├── [P2] /rowery/orbea/oiz/         ← Orbea Oiz (XC full sus)
│   │   ├── [P2] /rowery/orbea/alma/        ← Orbea Alma (XC hardtail)
│   │   ├── [P2] /rowery/orbea/rise/        ← Orbea Rise (e-MTB)
│   │   ├── [P2] /rowery/orbea/terra/       ← Orbea Terra (gravel)
│   │   ├── [P2] /rowery/orbea/gain/        ← Orbea Gain (e-road)
│   │   ├── [P2] /rowery/orbea/rallon/      ← Orbea Rallon (enduro)
│   │   └── [P2] /rowery/orbea/occam/       ← Orbea Occam (trail)
│   │
│   ├── [P1] /rowery/marin/                ← MARKA: Marin — landing page
│   │   │    Canonical: "rowery Marin"
│   │   │    CE: Marin Bikes | Schema: Brand, ItemList
│   │   │
│   │   ├── [P2] /rowery/marin/san-quentin/ ← Marin San Quentin (trail MTB)
│   │   ├── [P2] /rowery/marin/dsx/         ← Marin DSX / DSX FS (gravel)
│   │   ├── [P2] /rowery/marin/four-corners/ ← Marin Four Corners (bikepacking)
│   │   ├── [P2] /rowery/marin/bobcat-trail/ ← Marin Bobcat Trail (XC)
│   │   ├── [P2] /rowery/marin/nicasio/     ← Marin Nicasio (szosowy)
│   │   └── [P2] /rowery/marin/larkspur/    ← Marin Larkspur (miejski)
│   │
│   └── [P1] /rowery/superior/             ← MARKA: Superior — landing page
│       │    Canonical: "rowery Superior"
│       │    CE: Superior | Schema: Brand, ItemList
│       │
│       ├── [P2] /rowery/superior/xc-819/   ← Superior XC 819
│       ├── [P2] /rowery/superior/xc-899/   ← Superior XC 899
│       └── [P2] /rowery/superior/era/      ← Superior ERA (e-MTB)
│
├── [P2] /sklep/                           ← O nas, sklep stacjonarny Łódź
│        Schema: LocalBusiness, BicycleStore, GeoCoordinates
│
├── [P2] /serwis/                          ← Serwis rowerowy
│        Canonical: "serwis rowerowy"
│        Schema: Service, LocalBusiness
│
└── [P2-P3] /blog/                         ← OUTER — edukacja i porównania
    │
    ├── [P2] /blog/jaki-rower-wybrac/
    ├── [P2] /blog/rower-elektryczny-czy-tradycyjny/
    ├── [P2] /blog/jak-dobrac-rozmiar-roweru/
    ├── [P3] /blog/rower-gravel-co-to/
    ├── [P3] /blog/rower-aluminium-vs-carbon/
    ├── [P3] /blog/rower-fatbike/
    ├── [P3] /blog/serwis-roweru-przeglad/
    └── [P3] /blog/rower-skladany-wady-zalety/
```

---

## 2. Mapowanie keywords → strony

### Tabela per klaster (po scaleniu — 11 klastrów finalnych)

| Klaster | Strona (URL) | Przykładowe keywords | Typ strony | Kw |
|---|---|---|---|---|
| A — Rowery górskie/szosowe | `/rowery/gorskie/`, `/rowery/szosowe/` | rowery górskie, rower górski dla początkującego, rower szosowy, rowery szosowe | Kategoria | 91 |
| B — Typy + serwis + akcesoria | `/serwis/`, `/blog/` | serwis rowerowy, naprawa roweru, rower składany, kask rowerowy, lampka rowerowa | Serwis + Blog | 77 |
| C — Rowery elektryczne | `/rowery/elektryczne/` | rowery elektryczne, rower elektryczny, e-bike, pedelec, rower elektryczny górski | Kategoria | 45 |
| D — Sklep + lokalizacja | `/sklep/`, `/rowery/` | sklep rowerowy online, rowery najtaniej, rowery raty 0%, sklep rowerowy łódź | Zakup + About | 39 |
| E — Orbea modele | `/rowery/orbea/` + podstrony modeli | orbea orca, orbea oiz, orbea rise, orbea terra, orbea rallon | Brand LP + Produktowe | 28 |
| F — Rowery gravel | `/rowery/gravel/` | rowery gravel, rower gravel, gravel bike, e-gravel, rower szosowy vs gravel | Kategoria | 26 |
| G — Marin modele | `/rowery/marin/` + podstrony | marin san quentin, marin dsx fs, marin four corners, marin nicasio | Brand LP + Produktowe | 25 |
| H — MTB spec. techniczna | `/rowery/gorskie/mtb/` | rower MTB hardtail, rower MTB 29, rower XC hardtail, rower enduro full sus | Podkategoria | 24 |
| I — Orbea marka/opinie | `/rowery/orbea/` | rowery orbea, orbea polska, orbea opinie, orbea rowery cena | Brand LP | 16 |
| J — Online/outlet/trendy | `/rowery/`, `/blog/` | rowery online, rowery outlet, rowery leasing, rowery raty | Kategoria + Blog | 16 |
| K — Superior modele | `/rowery/superior/` + podstrony | superior xc 819, superior xc 899, superior era, superior rowery cena | Brand LP + Produktowe | 14 |

---

## 3. Linkowanie wewnętrzne — diagram kluczowych połączeń

```
/rowery/ (Pillar)
  ↓ link do każdej podkategorii i strony marki
  ├──→ /rowery/gorskie/
  │      ├──→ /rowery/gorskie/mtb/
  │      ├──→ /rowery/gorskie/enduro/
  │      └──→ /rowery/gorskie/xc/
  ├──→ /rowery/szosowe/
  ├──→ /rowery/elektryczne/
  ├──→ /rowery/gravel/
  ├──→ /rowery/orbea/ ←──────────────────────┐
  │      ├──→ /rowery/orbea/orca/             │ cross-link marki
  │      ├──→ /rowery/orbea/rise/ ←──────────┤ (e-MTB → elektryczne)
  │      └──→ /rowery/orbea/terra/ ←─────────┤ (gravel → gravel kat.)
  ├──→ /rowery/marin/                         │
  │      ├──→ /rowery/marin/san-quentin/ ─────┘
  │      ├──→ /rowery/marin/dsx/ ──→ /rowery/gravel/
  │      └──→ /rowery/marin/four-corners/ ──→ /rowery/gravel/
  └──→ /rowery/superior/
         ├──→ /rowery/superior/xc-819/ ──→ /rowery/gorskie/xc/
         └──→ /rowery/superior/era/ ──→ /rowery/elektryczne/

/blog/ (OUTER — wychodzące do CORE)
  ├──→ /blog/jaki-rower-wybrac/ ──→ /rowery/ (pillar)
  ├──→ /blog/rower-elektryczny-czy-tradycyjny/ ──→ /rowery/elektryczne/
  ├──→ /blog/rower-gravel-co-to/ ──→ /rowery/gravel/
  └──→ /blog/jak-dobrac-rozmiar-roweru/ ──→ /rowery/gorskie/mtb/

Serwis ←→ Sklep
  /serwis/ ←──→ /sklep/ (wzajemne cross-linki jako powiązane usługi)
```

### Kluczowe reguły linkowania:
1. Każda strona modelu (np. `/rowery/orbea/rise/`) linkuje do:
   - Strony marki (`/rowery/orbea/`)
   - Odpowiedniej kategorii produktowej (`/rowery/elektryczne/` dla e-MTB)
2. Strony kategorii linkują do powiązanych marek (górskie → Orbea Alma, Marin San Quentin, Superior XC)
3. Blog linkuje wyłącznie do stron CORE (nigdy do zewnętrznych konkurentów)
4. Pillar `/rowery/` agreguje linki do wszystkich bezpośrednich podkategorii
5. Breadcrumbs na każdej stronie: Strona główna → Rowery → [Kategoria] → [Model]

---

## 4. Priorytety publikacji — tabela zbiorcza

| # | URL | Klaster | Priorytet | Typ | Akcja | Status |
|---|---|---|---|---|---|---|
| 1 | `/rowery/` | C-1 (D+J) | P0 | Kategoria pillar | Utwórz lub zoptymalizuj | Do zrobienia |
| 2 | `/rowery/elektryczne/` | C (elektryczne) | P0 | Kategoria | Utwórz lub zoptymalizuj | Do zrobienia |
| 3 | `/rowery/gorskie/` | A | P0 | Kategoria | Utwórz lub zoptymalizuj | Do zrobienia |
| 4 | `/rowery/szosowe/` | A | P0 | Kategoria | Utwórz lub zoptymalizuj | Do zrobienia |
| 5 | `/rowery/orbea/` | E+I | P1 | Brand LP | Utwórz | Do zrobienia |
| 6 | `/rowery/marin/` | G | P1 | Brand LP | Utwórz | Do zrobienia |
| 7 | `/rowery/gravel/` | F | P1 | Kategoria | Utwórz | Do zrobienia |
| 8 | `/rowery/superior/` | K | P1 | Brand LP | Utwórz | Do zrobienia |
| 9 | `/rowery/gorskie/mtb/` | H | P1 | Podkategoria | Utwórz | Do zrobienia |
| 10 | `/sklep/`, `/serwis/` | D | P2 | Lokalny | Zoptymalizuj | Do zrobienia |
| 11 | `/rowery/orbea/orca/` | E | P2 | Produkt/model | Utwórz | Po #5 |
| 12 | `/rowery/orbea/rise/` | E | P2 | Produkt/model | Utwórz | Po #5 |
| 13 | `/rowery/orbea/terra/` | E | P2 | Produkt/model | Utwórz | Po #5 |
| 14 | `/rowery/marin/san-quentin/` | G | P2 | Produkt/model | Utwórz | Po #6 |
| 15 | `/rowery/marin/dsx/` | G | P2 | Produkt/model | Utwórz | Po #6 |
| 16 | `/blog/jaki-rower-wybrac/` | B | P2 | Artykuł | Napisz | Po P0 |
| 17 | `/blog/rower-elektryczny-czy-tradycyjny/` | B | P2 | Artykuł | Napisz | Po #2 |
| 18 | `/rowery/trekkingowe/` | - | P2 | Kategoria | Rozbuduj | Do zrobienia |
| 19 | `/rowery/miejskie/` | - | P2 | Kategoria | Rozbuduj | Do zrobienia |
| 20 | `/blog/rower-gravel-co-to/` | F | P3 | Artykuł | Napisz | Po #7 |
| 21 | `/blog/rower-aluminium-vs-carbon/` | B | P3 | Artykuł | Napisz | Po P1 |
| 22 | `/rowery/gorskie/enduro/` | A | P3 | Podkategoria | Utwórz | Po #3 |
| 23 | `/rowery/gorskie/xc/` | A | P3 | Podkategoria | Utwórz | Po #3 |
| 24 | Pozostałe podstrony modeli | E,G,K | P3 | Produktowe | Utwórz | Po odpowiednich LP |

---

## 5. Rekomendacje formatów — typ strony → format → schema markup

| Typ strony | URL pattern | Format contentu | Schema markup | Długość |
|---|---|---|---|---|
| **Pillar kategorii** | `/rowery/` | H1 + intro 150-300 słów + siatka produktów (lazy load) + bloki podkategorii + FAQ 5-8 pytań | `ItemList`, `BreadcrumbList`, `Organization`, `FAQPage` | 500-800 słów tekstu |
| **Kategoria produktów** | `/rowery/gorskie/`, `/elektryczne/`, `/gravel/` | H1 + lead 200 słów + filtry (typ/rozmiar/cena) + siatka produktów + sekcja "Jak wybrać?" (300 słów) + FAQ | `ItemList`, `BreadcrumbList`, `FAQPage` | 600-1000 słów |
| **Landing page marki** | `/rowery/orbea/`, `/marin/`, `/superior/` | H1 "Rowery [Marka]" + historia marki 300 słów + tabelka modeli + filtr po typie + sekcja "Dlaczego [Marka]?" + recenzje | `Brand`, `ItemList`, `BreadcrumbList`, `AggregateRating` | 800-1200 słów |
| **Podstrona modelu** | `/rowery/orbea/orca/` | H1 "[Model] — dane tech." + specyfikacja (tabela EAV) + galeria + warianty/rozmiary + CTA kup/zapytaj + FAQ | `Product`, `Offer`, `AggregateRating`, `BreadcrumbList` | 400-600 słów + tabela |
| **Podkategoria typ** | `/rowery/gorskie/mtb/` | H1 + opis typu 200-300 słów + filtr (atrybuty: koła/zawieszenie) + produkty + porównanie z innymi typami | `ItemList`, `FAQPage`, `BreadcrumbList` | 400-600 słów |
| **Sklep/About** | `/sklep/` | H1 + opis 200 słów + mapa/adres + godziny + galeria + recenzje Google | `LocalBusiness`, `BicycleStore`, `GeoCoordinates`, `OpeningHoursSpecification` | 300-500 słów |
| **Serwis** | `/serwis/` | H1 + lista usług (cennik) + FAQ serwisowe + CTA umów wizytę | `Service`, `LocalBusiness`, `FAQPage`, `PriceSpecification` | 400-600 słów |
| **Artykuł blogowy - poradnik** | `/blog/jaki-rower-wybrac/` | H1 pytajne + BLUF (odpowiedź w 2 zdaniach) + H2 sekcje typów + tabele porównań + CTA do kategorii | `Article`, `FAQPage`, `BreadcrumbList` | 1500-2500 słów |
| **Artykuł blogowy - porównanie** | `/blog/rower-aluminium-vs-carbon/` | H1 "[A] vs [B]" + BLUF werdykt + tabela porównań + H2 sekcje pro/con + werdykt końcowy + CTA | `Article`, `FAQPage`, `Table` | 1200-2000 słów |

### Kluczowe elementy UX każdej strony kategorii/marki:
1. **Filtr produktów** po: cena, rozmiar, typ zawieszenia, marka, koło (dla kategorii górskich)
2. **Sortowanie:** popularność / cena rosnąco / cena malejąco / nowości
3. **Breadcrumb** widoczny nad H1
4. **FAQ** (minimum 4 pytania) na każdej stronie kategorii — Schema FAQPage
5. **CTA do serwisu** w stopce każdej strony produktowej
6. **Sekcja "Produkty powiązane"** (cross-sell między kategoriami)
7. **Oceny i recenzje** (jeśli dostępne) — AggregateRating

---

## Podsumowanie struktury

| Metryka | Wartość |
|---|---|
| Łączna liczba URL do stworzenia/zoptymalizowania | ~35+ |
| Strony P0 (pillar) | 4 |
| Strony P1 (kategorie + brand LP) | 8 |
| Strony P2 (podkategorie, serwis, blog top) | 10+ |
| Strony P3 (modele, blog artykuły) | 13+ |
| Liczba klastrów CORE | 9 |
| Liczba klastrów OUTER | 2 |
| Keywords CORE | ~295 |
| Keywords OUTER | ~100 |
