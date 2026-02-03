# 🤖 TOGAF EA Learning Agent (Lernagent für TOGAF EA)

Ein interaktiver, Python-basierter Learning Agent für **TOGAF (The Open Group Architecture Framework)**, optimiert für **AuDHD-Lernstile**.

## 🎯 Zweck

Dieser Learning Agent hilft dir, TOGAF systematisch zu lernen durch:
- **Strukturierte Lernsessions** für alle TOGAF ADM Phasen
- **Timeboxing** mit Pomodoro-Technik
- **Active Recall** durch interaktive Quizzes
- **Output-fokussiertes Lernen** (jede Session = 1 Deliverable)
- **Automatisches Progress Tracking**
- **Visuelle Darstellung** des Lernfortschritts

## ✨ Features

### 1. **TOGAF ADM Phases lernen**
- Alle 10 ADM-Phasen (Preliminary bis Phase H + Requirements Management)
- Strukturierte Lernschritte: Input → Verarbeitung → Active Recall
- Deliverable-Templates für jede Phase
- Zeitschätzungen pro Phase

### 2. **Active Recall Quizzes**
- Interaktive Quiz-Fragen zu jeder Phase
- Sofortiges Feedback mit Erklärungen
- Score-Tracking und History
- Empfehlungen basierend auf Quiz-Ergebnissen

### 3. **Progress Tracking**
- Automatisches Speichern des Lernfortschritts
- Übersicht über abgeschlossene Phasen
- Deliverable-Tracking
- Quiz-Score-History
- Visuelle Progress Bar

### 4. **Intelligente Lernempfehlungen**
- Nächste empfohlene Phase
- Wiederholungsempfehlungen bei niedrigen Scores
- Personalisierte Tipps

### 5. **TOGAF Prinzipien & Building Blocks**
- Übersicht über Architecture Principles
- ABB (Architecture Building Blocks) vs. SBB (Solution Building Blocks)
- Enterprise Continuum

## 📋 Voraussetzungen

- Python 3.6 oder höher
- Keine externen Dependencies (nur Python Standard Library)

## 🚀 Installation & Start

### 1. Repository klonen (falls noch nicht geschehen)
```bash
git clone <repository-url>
cd enterprise_architect
```

### 2. Learning Agent ausführen
```bash
cd 09_tools_and_methods
python togaf_learning_agent.py
```

oder direkt als ausführbare Datei:
```bash
chmod +x togaf_learning_agent.py
./togaf_learning_agent.py
```

## 🎮 Nutzung

### Hauptmenü
Nach dem Start siehst du folgende Optionen:

```
1. 📚 TOGAF ADM Phases lernen    - Lerne eine spezifische ADM Phase
2. 🧠 Active Recall Quiz         - Teste dein Wissen
3. 📊 Fortschritt anzeigen       - Zeige deinen Lernfortschritt
4. 🎯 Lernempfehlung erhalten    - Erhalte personalisierte Empfehlungen
5. 📖 TOGAF Prinzipien           - Zeige Prinzipien & Building Blocks
6. ❓ Hilfe                      - Zeige Hilfe-Informationen
7. 🚪 Beenden                    - Programm beenden
```

### Typischer Workflow

1. **Starte mit Preliminary Phase**
   - Wähle Option 1 (TOGAF ADM Phases lernen)
   - Wähle Phase 1 (Preliminary Phase)
   - Folge den Lernschritten

2. **Erstelle dein Deliverable**
   - Input: Lies TOGAF-Dokumentation (20-30 Min)
   - Verarbeitung: Erstelle Diagramm/Dokument (30-40 Min)
   - Active Recall: Quiz machen (10-15 Min)

3. **Mache das Quiz**
   - Teste dein Wissen direkt nach der Lernsession
   - Wiederhole bei Score < 70%

4. **Prüfe deinen Fortschritt**
   - Option 3: Fortschritt anzeigen
   - Siehe abgeschlossene Phasen und Scores

5. **Hole dir Empfehlungen**
   - Option 4: Lernempfehlung
   - Erhalte personalisierte nächste Schritte

## 📊 Progress Tracking

Der Learning Agent speichert deinen Fortschritt automatisch in:
```
togaf_learning_progress.json
```

Diese Datei enthält:
- Anzahl abgeschlossener Sessions
- Gelernte Phasen
- Erstellte Deliverables
- Quiz-Scores
- Letzte Session

**⚠️ Tipp:** Committe diese Datei nicht ins Repository (zu persönlich). Füge sie zur `.gitignore` hinzu.

## 🧠 AuDHD-Optimierte Features

### Für ADHD
- ✅ **Zeitboxing:** Klare Zeitlimits pro Phase (60-120 Min)
- ✅ **Dopamin:** Sofortiges Feedback durch Quiz und Progress
- ✅ **Task-Initiation:** Kleine, klare Schritte
- ✅ **Hyperfokus-Management:** Zeitschätzungen verhindern "Verlust"

### Für Autismus
- ✅ **Struktur:** Klare, konsistente Abläufe
- ✅ **Checklisten:** Visuelle Bestätigung durch ✅
- ✅ **Vorhersagbarkeit:** Gleicher Ablauf jeder Session
- ✅ **Detailliert:** Alle Konzepte klar erklärt

### Für AuDHD
- ✅ **Flexible Struktur:** Strukturiert, aber nicht starr
- ✅ **Output-fokussiert:** Jede Session produziert etwas
- ✅ **Visual:** Farben, Symbole, Progress Bar
- ✅ **Active Recall:** Nicht passiv konsumieren

## 📚 TOGAF ADM Phases im Agent

| Phase | Name | Zeitschätzung | Deliverable |
|-------|------|---------------|-------------|
| Preliminary | Framework & Principles | 60 Min | Architecture Principles Document |
| Phase A | Architecture Vision | 90 Min | Architecture Vision Document |
| Phase B | Business Architecture | 90 Min | Business Capability Map |
| Phase C | Information Systems | 120 Min | Application & Data Architecture Doc |
| Phase D | Technology Architecture | 90 Min | Technology Architecture Document |
| Phase E | Opportunities & Solutions | 60 Min | Implementation & Migration Plan |
| Phase F | Migration Planning | 60 Min | Architecture Roadmap |
| Phase G | Implementation Governance | 60 Min | Architecture Contract Template |
| Phase H | Change Management | 60 Min | Change Management Process Doc |
| Requirements | Requirements Management | 60 Min | Requirements Traceability Matrix |

**Gesamt:** Ca. 12-15 Stunden reine Lernzeit (verteilt über 2-4 Wochen)

## 🎯 Lernempfehlungen

### Woche 1: ADM Grundlagen
- Tag 1: Preliminary Phase (60 Min)
- Tag 2: Phase A - Architecture Vision (90 Min)
- Tag 3: Phase B - Business Architecture (90 Min)
- Tag 4: Quiz-Wiederholung & Deliverables
- Tag 5: Pause/Reflexion

### Woche 2: Information & Technology
- Tag 1: Phase C - Information Systems (120 Min)
- Tag 2: Phase D - Technology Architecture (90 Min)
- Tag 3: Quiz-Wiederholung
- Tag 4-5: Deliverables erstellen & committen

### Woche 3: Implementation
- Tag 1: Phase E - Opportunities & Solutions (60 Min)
- Tag 2: Phase F - Migration Planning (60 Min)
- Tag 3: Phase G - Implementation Governance (60 Min)
- Tag 4: Phase H - Change Management (60 Min)
- Tag 5: Requirements Management (60 Min)

### Woche 4: Konsolidierung
- Tag 1-2: Alle Quizzes wiederholen
- Tag 3-4: Beispiel-Projekt durch ADM durchspielen
- Tag 5: Portfolio aufräumen & committen

## 💡 Best Practices

### 1. **Konsequenz > Perfektion**
```bash
# Jeden Tag zur gleichen Zeit:
python togaf_learning_agent.py
```

### 2. **Deliverables commiten**
```bash
# Nach jeder Session:
git add deliverables/
git commit -m "Phase A: Architecture Vision Document"
```

### 3. **Spacing nutzen**
- Tag 1: Neue Phase lernen
- Tag 3: Quiz wiederholen (Active Recall)
- Tag 7: Quiz nochmal
- Tag 14: Quiz nochmal

### 4. **Portfolio aufbauen**
Erstelle für jedes Deliverable:
```
deliverables/
├── preliminary/
│   └── architecture_principles.md
├── phase_a/
│   └── architecture_vision.drawio
├── phase_b/
│   └── capability_map.drawio
...
```

## 🛠️ Erweiterung & Anpassung

### Eigene Quiz-Fragen hinzufügen
Editiere die Methode `get_quiz_questions()` in `togaf_learning_agent.py`:

```python
"phase_a": [
    {
        "question": "Deine Frage hier?",
        "options": [
            "Option 1",
            "Option 2",
            "Option 3",
            "Option 4"
        ],
        "correct": 2,  # Nummer der richtigen Option (1-4)
        "explanation": "Erklärung hier"
    }
]
```

### Weitere Phasen hinzufügen
Füge neue Phasen in `get_togaf_phases()` hinzu:

```python
{
    "id": "neue_phase",
    "name": "Neue Phase",
    "description": "Beschreibung",
    "key_concepts": [...],
    "deliverable": "Deliverable Name",
    "time_estimate": "60 Min"
}
```

## 📖 Weiterführende Ressourcen

### Im Repository
- [TOGAF Overview](../02_frameworks/togaf/togaf_overview.md)
- [Learning Methods](../00_roadmap/learning_methods.md)
- [TOGAF Certification Guide](../00_roadmap/certifications.md)

### Extern
- [TOGAF Standard 10 (offiziell)](https://www.opengroup.org/togaf)
- [TOGAF 10 Foundation Study Guide](https://www.opengroup.org/library/togaf)
- [Coursera TOGAF 10 Foundation](https://www.coursera.org)
- [ArchiMate for TOGAF](https://pubs.opengroup.org/architecture/archimate32-doc/)

## 🤝 Feedback & Verbesserungen

Wenn du Ideen hast, wie dieser Learning Agent verbessert werden kann:
- Öffne ein GitHub Issue
- Erstelle einen Pull Request
- Füge weitere Quiz-Fragen hinzu

## 📄 Lizenz

MIT License - Frei nutzbar für Lern- und Ausbildungszwecke.

---

## 🎓 Erfolgsformel

```
TOGAF-Expertise = Konsistenz × Deliverables × Active Recall

Konsistenz:    5 Tage/Woche, 60-90 Min/Tag
Deliverables:  1 pro Phase (10 total)
Active Recall: Quiz nach jeder Phase + Spacing
```

---

**Viel Erfolg beim Lernen! 🚀**

*Erstellt im Rahmen des Enterprise Architect Roadmap Projekts*  
*Letzte Aktualisierung: Februar 2026*
