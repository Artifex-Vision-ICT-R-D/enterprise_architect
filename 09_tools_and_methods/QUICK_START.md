# 🚀 Quick Start: TOGAF Learning Agent

## In 5 Minuten starten

### 1. Learning Agent starten
```bash
cd 09_tools_and_methods
python togaf_learning_agent.py
```

### 2. Erste Phase wählen
- Wähle Option `1` (TOGAF ADM Phases lernen)
- Wähle Phase `1` (Preliminary Phase)

### 3. Lernsession durchführen
Folge den 3 Schritten:

#### Schritt 1: Input (20-30 Min)
- Lies: `02_frameworks/togaf/togaf_overview.md` (Preliminary Phase)
- Oder: TOGAF Standard (Kapitel 5)

#### Schritt 2: Verarbeitung (30-40 Min)
- Erstelle dein Deliverable: **Architecture Principles Document**
- Nutze Template oder erstelle eigenes Dokument
- Beispiel:

```markdown
# Architecture Principles

## 1. Business-driven
**Statement:** IT folgt Business, nicht umgekehrt
**Rationale:** Business-Ziele bestimmen IT-Strategie
**Implications:** IT-Entscheidungen benötigen Business-Justification

## 2. Simplicity
**Statement:** Keep it simple
**Rationale:** Komplexität erhöht Fehleranfälligkeit
**Implications:** Neue Features nur wenn nötig

[... weitere Prinzipien ...]
```

#### Schritt 3: Active Recall (10-15 Min)
- Mache das Quiz im Learning Agent
- Versuche ohne Notizen zu antworten
- Ziel: >80% richtig

### 4. Fortschritt speichern
Der Agent speichert automatisch in:
```
togaf_learning_progress.json
```

### 5. Deliverable committen
```bash
# Deliverable-Ordner erstellen
mkdir -p deliverables/preliminary

# Dein Dokument speichern
# z.B. deliverables/preliminary/architecture_principles.md

# Committen
git add deliverables/
git commit -m "Preliminary Phase: Architecture Principles"
git push
```

---

## 📅 Beispiel: Erste Woche

### Tag 1 (60 Min): Preliminary Phase
```bash
python togaf_learning_agent.py
# Option 1 → Phase 1
```
**Deliverable:** Architecture Principles Document

### Tag 2 (90 Min): Phase A
```bash
python togaf_learning_agent.py
# Option 1 → Phase 2
```
**Deliverable:** Architecture Vision Document

### Tag 3 (90 Min): Phase B
```bash
python togaf_learning_agent.py
# Option 1 → Phase 3
```
**Deliverable:** Business Capability Map

### Tag 4: Quiz & Review
```bash
python togaf_learning_agent.py
# Option 2 → Quiz für alle Phasen
# Option 3 → Fortschritt anzeigen
```

### Tag 5: Pause/Reflexion
- Deliverables reviewen
- Portfolio aufräumen
- Nächste Woche planen

---

## 🎯 Tipps für maximalen Erfolg

### ✅ DO's
- **Zeitbox nutzen:** Timer setzen (Pomodoro)
- **Deliverable erstellen:** Jede Session = 1 Ergebnis
- **Quiz machen:** Active Recall ist wichtig
- **Committen:** Git-History = Lernhistory
- **Spacing:** Wiederholen nach 3, 7, 14 Tagen

### ❌ DON'Ts
- Nicht länger als 90 Min pro Session
- Nicht mehrere Phasen gleichzeitig
- Nicht nur lesen ohne Deliverable
- Nicht Quiz überspringen
- Nicht Fortschritt ignorieren

---

## 📊 Progress Tracking

### Nach jeder Session
```bash
python togaf_learning_agent.py
# Option 3: Fortschritt anzeigen
```

Du siehst:
- Anzahl Sessions
- Abgeschlossene Phasen
- Deliverables
- Quiz-Scores
- Progress Bar

### Beispiel Output:
```
📊 Statistiken:
  Sessions abgeschlossen: 3
  Phases gelernt: 3/10
  Deliverables erstellt: 3
  Letzte Session: 2026-02-03 15:30

✅ Abgeschlossene Phasen:
  ✅ Preliminary Phase
  ✅ Phase A: Architecture Vision
  ✅ Phase B: Business Architecture

📦 Erstellte Deliverables:
  📄 Architecture Principles Document (2026-02-03)
  📄 Architecture Vision Document (2026-02-03)
  📄 Business Capability Map (2026-02-03)

Gesamtfortschritt: 30.0%
[███████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 30.0%
```

---

## 🤝 Hilfe bekommen

### Im Learning Agent
```bash
python togaf_learning_agent.py
# Option 6: Hilfe
```

### Empfehlungen erhalten
```bash
python togaf_learning_agent.py
# Option 4: Lernempfehlung erhalten
```

### Dokumentation
- [TOGAF Learning Agent README](TOGAF_LEARNING_AGENT_README.md)
- [TOGAF Overview](../02_frameworks/togaf/togaf_overview.md)
- [Learning Methods](../00_roadmap/learning_methods.md)

---

## 🎓 Erfolgsformel

```
1 Phase pro Tag (oder 2 Tage) 
    ↓
10 Phasen
    ↓
2-3 Wochen
    ↓
TOGAF Foundation Ready
```

**Bereit? Los geht's! 🚀**

```bash
python togaf_learning_agent.py
```

---

*Viel Erfolg beim Lernen!*
