# 🧠 Lernmethoden für Enterprise Architecture

## 🎯 Lernstrategien für AuDHD (Autism & ADHD)

Dieses Dokument enthält **spezifische Lernstrategien**, die für neurodivergente Menschen (insbesondere AuDHD) optimiert sind.

---

## 🔑 Kernprinzipien

### 1. **Output > Input**
**Problem:** Passives Lesen führt zu wenig Retention  
**Lösung:** Jede Lernsession muss ein **konkretes Ergebnis** produzieren

**Beispiele:**
- ❌ "2 Stunden TOGAF lesen"
- ✅ "1 ADM-Diagramm zeichnen"
- ✅ "1 ADR schreiben"
- ✅ "5 Architekturprinzipien dokumentieren"

---

### 2. **Zeitboxing (Nicht Aufgaben-basiert)**
**Problem:** "Bis fertig" führt zu Hyperfokus oder Prokrastination  
**Lösung:** **Feste Zeitblöcke**, unabhängig vom Fortschritt

**Technik: Pomodoro (angepasst)**
- 25 Min Arbeit → 5 Min Pause (oder 50/10, je nach Fokus)
- Nach 4 Pomodoros: 15-30 Min Pause
- **Wichtig:** Timer verwenden (visuell + akustisch)

**Zeitblöcke-Empfehlung:**
- **Optimal:** 60 Min/Tag (1x 50 Min + 10 Min Pause)
- **Intensiv:** 90 Min/Tag (2x 40 Min + 10 Min Pause)
- **Maximum:** 120 Min/Tag (mehr führt zu Burnout)

---

### 3. **Single-Tasking (Nur EIN Thema gleichzeitig)**
**Problem:** Mehrere Themen parallel → nichts wird fertig  
**Lösung:** **Eine Woche = Ein Thema**

**Beispiel Woche 1:**
- ✅ Montag-Freitag: **Nur** C4 Model
- ❌ Nicht: C4 Model + TOGAF + AWS gleichzeitig

**Regel:** Neues Thema erst starten, wenn altes abgeschlossen (Deliverable erstellt)

---

### 4. **Visuelles Lernen (Diagramme > Text)**
**Problem:** Lange Texte überfordern schnell  
**Lösung:** Immer **visualisieren**

**Technik:**
1. Text lesen (20 Min)
2. Diagramm zeichnen (30 Min)
3. Diagramm erklären (10 Min, laut oder schriftlich)

**Tools:**
- Draw.io (kostenlos, einfach)
- Obsidian (für Mindmaps)
- Papier & Stift (low-tech, gut für schnelle Skizzen)

---

### 5. **Active Recall (Nicht Wiederlesen)**
**Problem:** Wiederlesen täuscht Verständnis vor  
**Lösung:** **Aktives Abrufen** aus dem Gedächtnis

**Technik: Feynman-Methode**
1. Thema lernen (Input)
2. Thema erklären (ohne Notizen) → laut oder schriftlich
3. Lücken identifizieren
4. Lücken schließen (gezielt nachlesen)
5. Wiederholen

**Beispiel:**
- Tag 1: TOGAF ADM lesen
- Tag 2: ADM-Zyklus aus dem Gedächtnis aufzeichnen (ohne Notizen)
- Tag 3: Lücken füllen

---

### 6. **Spacing (Verteiltes Lernen)**
**Problem:** Cramming funktioniert nicht langfristig  
**Lösung:** **Verteiltes Lernen** über mehrere Tage

**Spacing-Schedule:**
- Tag 1: Neues Thema lernen
- Tag 3: Wiederholen (Active Recall)
- Tag 7: Wiederholen (Active Recall)
- Tag 14: Wiederholen (Active Recall)
- Tag 30: Wiederholen (Active Recall)

**Tool:** Anki (Flashcard-App mit Spacing-Algorithmus)

---

## 🛠️ Konkrete Techniken

### Technik 1: Lernsession-Template

**Struktur (60 Min):**
1. **Input (20-30 Min):** Video, Artikel, Dokumentation
2. **Verarbeitung (20-30 Min):** Diagramm, Notiz, Code
3. **Zusammenfassung (10 Min):** 1-2 Kerngedanken notieren

**Vorlage (`session_YYYY-MM-DD.md`):**
```markdown
# Lernsession: [Thema]

**Datum:** YYYY-MM-DD  
**Dauer:** 60 Min  
**Ziel:** [z. B. "ADM-Zyklus verstehen"]

## Input (30 Min)
- [ ] Video: "TOGAF ADM Overview" (15 Min)
- [ ] TOGAF Standard: Kapitel 5 (15 Min)

## Verarbeitung (20 Min)
- [ ] ADM-Diagramm zeichnen (Draw.io)
- [ ] 9 Phasen beschriften

## Zusammenfassung (10 Min)
**Kerngedanken:**
1. ADM ist iterativ, nicht linear
2. Requirements Management ist zentral
3. Jede Phase hat Input/Output

**Deliverable:** `diagrams/adm_cycle.drawio`
```

---

### Technik 2: Wochenplan-Template

**Struktur:**
- **Montag:** Überblick & Einordnung (Big Picture)
- **Dienstag:** Kernkonzepte (Details)
- **Mittwoch:** Praktische Anwendung (Diagramm/Code)
- **Donnerstag:** Vertiefung (ADR/Notiz)
- **Freitag:** Konsolidierung & Review

**Regel:** Jeder Tag = 1 Deliverable (Datei, Diagramm, ADR)

---

### Technik 3: Portfolio-First Learning

**Prinzip:** Lernen ist **Mittel**, Portfolio ist **Ziel**

**Statt:**
- "Ich lerne TOGAF" (unklar)

**Besser:**
- "Ich erstelle 1 Enterprise-Zielarchitektur mit TOGAF" (konkret)

**Vorteil:** Jede Lernsession produziert Portfolio-Material

---

### Technik 4: Interleaving (Themen mischen)

**Problem:** Nur TOGAF lernen wird monoton  
**Lösung:** **Verwandte** Themen abwechseln (nicht parallel, sondern wochenweise)

**Beispiel (4 Wochen):**
- Woche 1: TOGAF ADM
- Woche 2: C4 Model (Diagramme)
- Woche 3: TOGAF Governance
- Woche 4: SABSA (Security)

**Vorteil:** Gehirn verknüpft Konzepte besser

---

### Technik 5: Accountability (Externe Verantwortung)

**Problem:** Selbstdisziplin schwierig  
**Lösung:** **Öffentlich committen**

**Methoden:**
- GitHub (Commits sichtbar)
- LinkedIn (Fortschritt posten)
- Learning-Buddy (weekly check-in)
- Community (Discord, Reddit)

**Beispiel:**
- Jeden Freitag: `week_X_summary.md` auf GitHub committen
- Jeden Monat: LinkedIn-Post mit Fortschritt

---

## 🧩 AuDHD-spezifische Strategien

### Für ADHD (Aufmerksamkeit & Impulsivität)

#### 1. **Hyperfokus nutzen**
- Wenn Hyperfokus einsetzt → ausnutzen (aber max. 2 Std)
- Timer setzen (verhindert "Verlust" von 6 Stunden)

#### 2. **Distraktionen eliminieren**
- Handy: Flight Mode oder in anderen Raum
- Browser: Focus-Mode (z. B. Cold Turkey, Freedom)
- Umgebung: Noise-Cancelling Kopfhörer, Lofi-Musik

#### 3. **Dopamin-Management**
- **Reward nach Deliverable** (nicht nach Zeit)
- Beispiel: "Nach ADR → 20 Min YouTube"

#### 4. **Task-Initiation leichter machen**
- **5-Minuten-Regel:** "Ich mache nur 5 Min" → meist macht man mehr
- **Tiniest Step:** "Ich öffne nur Draw.io" → führt zu Diagramm

---

### Für Autismus (Struktur & Routine)

#### 1. **Feste Lernfenster**
- **Gleiche Zeit, gleicher Ort** (z. B. täglich 18:00-19:00)
- Kalender-Erinnerungen setzen

#### 2. **Rituale**
- **Start-Ritual:** Tee machen, Musik starten, Timer setzen
- **End-Ritual:** Deliverable committen, Fortschritt notieren

#### 3. **Checklisten**
- Jede Session: Checkliste abhaken
- Visuelle Bestätigung (✅) gibt Dopamin

#### 4. **Special Interests nutzen**
- Wenn Security interessiert → SABSA zuerst
- Wenn Cloud interessiert → AWS zuerst
- **Motivation > Reihenfolge**

---

### Für AuDHD (Kombination)

#### 1. **Flexible Struktur**
- Struktur gibt Sicherheit (Autismus)
- Flexibilität verhindert Langeweile (ADHD)
- **Lösung:** Wochenplan (strukturiert), aber Tagesreihenfolge flexibel

#### 2. **Körperliches Lernen**
- Beim Gehen lernen (Spaziergang + Podcast)
- Stehen statt Sitzen (Standing Desk)
- Fidget Tools (während Video schauen)

#### 3. **Multimodales Lernen**
- Text + Video + Diagramm + Audio (parallel)
- Beispiel: Video schauen + Diagramm zeichnen

---

## 📊 Fortschritts-Tracking

### Technik: Habit-Tracking

**Tool:** Obsidian, Notion, oder Papier

**Vorlage:**
```
[ ] Montag: 60 Min TOGAF
[ ] Dienstag: 60 Min TOGAF
[ ] Mittwoch: 60 Min TOGAF
[ ] Donnerstag: 60 Min TOGAF
[ ] Freitag: 60 Min TOGAF
```

**Ziel:** Chain nicht brechen (Jerry Seinfeld-Methode)

---

### Technik: Progress Log

**Datei:** `progress_log.md`

**Struktur:**
```markdown
# Fortschritt

## Woche 1 (2026-02-03)
- ✅ C4 System Context Diagram
- ✅ C4 Container Diagram
- ✅ week_01_summary.md

## Woche 2 (2026-02-10)
- ✅ 10 Architekturprinzipien dokumentiert
- ✅ Coupling-Diagramm
- ✅ week_02_summary.md
```

---

## 🚫 Was NICHT funktioniert (aus Erfahrung)

### ❌ 1. "Ich lerne wenn ich Zeit habe"
**Problem:** Zeit kommt nie  
**Lösung:** Feste Zeitblöcke (Kalender)

### ❌ 2. "Ich lese das Buch komplett"
**Problem:** 800 Seiten überfordern  
**Lösung:** Selektiv lesen (Inhaltsverzeichnis → relevante Kapitel)

### ❌ 3. "Ich lerne mehrere Themen parallel"
**Problem:** Nichts wird fertig  
**Lösung:** Single-Tasking (1 Woche = 1 Thema)

### ❌ 4. "Ich schaue alle Videos"
**Problem:** Passives Lernen = low retention  
**Lösung:** Video → Pause → Diagramm → Weiter

### ❌ 5. "Ich lerne wenn ich motiviert bin"
**Problem:** Motivation ist inkonsistent  
**Lösung:** Disziplin > Motivation (feste Routine)

---

## 💡 Erfolgsformel

```
Erfolg = Konsistenz × Output × Zeit

Konsistenz: 5 Tage/Woche, 60 Min/Tag
Output: 1 Deliverable/Tag (Diagramm, ADR, Notiz)
Zeit: 24 Monate
```

**Nicht:**
```
Erfolg ≠ Perfektion × Lange Sessions × Motivation
```

---

## 🎯 Quick Start (Erste Woche)

### Tag 1: Setup
- [ ] Repository anlegen (GitHub)
- [ ] README.md schreiben
- [ ] Ordnerstruktur erstellen
- [ ] Draw.io installieren

### Tag 2: Erste Lernsession
- [ ] C4 Model Website lesen (30 Min)
- [ ] System Context Diagramm zeichnen (20 Min)
- [ ] Zusammenfassung schreiben (10 Min)

### Tag 3: Zweite Lernsession
- [ ] C4 Container Diagram lesen (20 Min)
- [ ] Container Diagramm zeichnen (30 Min)
- [ ] Committen (10 Min)

### Tag 4: Reflexion
- [ ] Was lief gut?
- [ ] Was war schwierig?
- [ ] Anpassungen für nächste Woche?

### Tag 5: Pause
- [ ] Keine Lernsession (Erholung)

---

## 📚 Empfohlene Tools

### Zeitmanagement
- **Pomodoro-Timer:** Focus To-Do, Forest, Pomofocus
- **Kalender:** Google Calendar, Apple Calendar

### Notizen
- **Obsidian:** Markdown, Local, Backlinks
- **Notion:** Strukturiert, Datenbanken

### Diagramme
- **Draw.io:** Kostenlos, einfach
- **Excalidraw:** Sketch-Style

### Flashcards
- **Anki:** Spacing-Algorithmus
- **Quizlet:** Einfach, online

### Distraction-Blocking
- **Cold Turkey:** Windows/Mac
- **Freedom:** Multi-Device
- **Forest:** Gamified

---

## 🚀 Nächster Schritt

1. **Template wählen:** Lernsession-Template oder Wochenplan
2. **Erste Session:** C4 Model (60 Min)
3. **Deliverable:** 1 Diagramm
4. **Committen:** GitHub

> **Wichtig:** Anfangen > Perfekt sein

---

*Letzte Aktualisierung: Februar 2026*
