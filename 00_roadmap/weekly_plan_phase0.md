# 📅 Wochenplan Phase 0: Architektur-Grundlagen

**Dauer:** 4 Wochen  
**Zeitaufwand:** 60-90 Min/Tag, 5 Tage/Woche  
**Kosten:** 0 CHF  
**Ziel:** Architekturdenken verstehen, erste Diagramme erstellen

---

## 📋 Woche 1: Architekturdenken & C4 Model

### **Tag 1 (Montag): Was ist Architektur?**
**Zeitaufwand:** 60 Min

#### Input (30 Min)
- [ ] YouTube: "What do Software Architects do?" (10 Min)
- [ ] C4 Model Website lesen: https://c4model.com (20 Min)

#### Verarbeitung (30 Min)
- [ ] Notiz erstellen: `week_01_overview.md`
- [ ] 3 Kerngedanken notieren:
  1. Was ist Architektur? (Definition in eigenen Worten)
  2. Unterschied Engineer vs. Architect
  3. Warum C4 Model?

**Deliverable:** `week_01_overview.md`

---

### **Tag 2 (Dienstag): C4 Level 1 - System Context**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] C4 Model: System Context Diagram (Beispiele anschauen)

#### Verarbeitung (40 Min)
- [ ] Draw.io öffnen (https://app.diagrams.net/)
- [ ] 1 System Context Diagram erstellen für fiktives System:
  - **Beispiel:** E-Commerce-Plattform
  - **Akteure:** Customer, Admin, Payment Gateway, Email Service
- [ ] Diagramm speichern: `diagrams/week_01_system_context.drawio`

**Deliverable:** System Context Diagram

---

### **Tag 3 (Mittwoch): C4 Level 2 - Container**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] C4 Model: Container Diagram (Beispiele anschauen)

#### Verarbeitung (40 Min)
- [ ] Container Diagram erstellen für dein E-Commerce-System:
  - Web App (React)
  - API (Node.js)
  - Database (PostgreSQL)
  - Message Queue (RabbitMQ)
- [ ] Speichern: `diagrams/week_01_container.drawio`

**Deliverable:** Container Diagram

---

### **Tag 4 (Donnerstag): C4 Level 3 - Component**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] C4 Model: Component Diagram (Beispiele anschauen)

#### Verarbeitung (40 Min)
- [ ] Component Diagram für **eine** Container (z. B. API):
  - Auth Controller
  - Product Controller
  - Order Controller
  - Database Repository
- [ ] Speichern: `diagrams/week_01_component.drawio`

**Deliverable:** Component Diagram

---

### **Tag 5 (Freitag): Wochenabschluss & Review**
**Zeitaufwand:** 60 Min

#### Konsolidierung (45 Min)
- [ ] `week_01_summary.md` erstellen
- [ ] Antworten:
  1. Was habe ich gelernt? (C4 Model, 3 Ebenen)
  2. Was kann ich jetzt? (Diagramme erstellen)
  3. Was ist noch unklar? (Notizen für später)
- [ ] Alle 3 Diagramme in `assets/diagrams/` committen

#### Reflexion (15 Min)
- [ ] Was lief gut?
- [ ] Was war schwierig?
- [ ] Nächste Woche: Architekturprinzipien

**Deliverable:** `week_01_summary.md` + 3 Diagramme

---

## 📋 Woche 2: Architekturprinzipien

### **Tag 1 (Montag): Top 10 Architekturprinzipien**
**Zeitaufwand:** 60 Min

#### Input (30 Min)
- [ ] YouTube: "Software Architecture Principles" (15 Min)
- [ ] Microsoft Cloud Design Patterns lesen: https://learn.microsoft.com/en-us/azure/architecture/patterns/ (15 Min)

#### Verarbeitung (30 Min)
- [ ] `architecture_principles.md` erstellen
- [ ] 10 Prinzipien dokumentieren:
  1. Separation of Concerns
  2. Single Responsibility Principle
  3. DRY (Don't Repeat Yourself)
  4. KISS (Keep It Simple, Stupid)
  5. Loose Coupling
  6. High Cohesion
  7. YAGNI (You Ain't Gonna Need It)
  8. Fail Fast
  9. Defense in Depth
  10. Least Privilege

**Deliverable:** `architecture_principles.md`

---

### **Tag 2 (Dienstag): Prinzip Vertiefung - Loose Coupling**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "Loose Coupling & High Cohesion" Artikel lesen

#### Verarbeitung (40 Min)
- [ ] Beispiel dokumentieren:
  - **Tight Coupling:** Monolith, direkte DB-Calls
  - **Loose Coupling:** Microservices, API Gateway
- [ ] Diagramm: Tight vs. Loose Coupling
- [ ] Speichern: `diagrams/week_02_coupling.drawio`

**Deliverable:** Coupling-Diagramm + Notizen

---

### **Tag 3 (Mittwoch): Trade-offs verstehen**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "No Free Lunch in Software Architecture" lesen

#### Verarbeitung (40 Min)
- [ ] `trade_offs.md` erstellen
- [ ] 3 Trade-off-Beispiele dokumentieren:
  1. **Consistency vs. Availability** (CAP Theorem)
  2. **Performance vs. Security** (Caching vs. Fresh Data)
  3. **Simplicity vs. Flexibility** (Monolith vs. Microservices)

**Deliverable:** `trade_offs.md`

---

### **Tag 4 (Donnerstag): Technical Debt**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "Technical Debt Explained" YouTube (10 Min)
- [ ] Artikel: "Managing Technical Debt" (10 Min)

#### Verarbeitung (40 Min)
- [ ] `technical_debt.md` erstellen
- [ ] Antworten:
  1. Was ist Technical Debt?
  2. Wann ist Technical Debt akzeptabel?
  3. Wie vermeidet man Technical Debt?
  4. Beispiel: Schnelle MVP vs. Clean Architecture

**Deliverable:** `technical_debt.md`

---

### **Tag 5 (Freitag): Wochenabschluss**
**Zeitaufwand:** 60 Min

#### Konsolidierung (40 Min)
- [ ] `week_02_summary.md` erstellen
- [ ] Portfolio-Update: Neue Dateien committen

#### Prüfungsfragen (20 Min)
- [ ] 5 Fragen selbst beantworten:
  1. Was ist Separation of Concerns?
  2. Was ist Loose Coupling?
  3. Nenne 3 Architekturprinzipien
  4. Was ist ein Trade-off?
  5. Was ist Technical Debt?

**Deliverable:** `week_02_summary.md`

---

## 📋 Woche 3: Modularität & Patterns

### **Tag 1 (Montag): Architektur-Patterns Übersicht**
**Zeitaufwand:** 60 Min

#### Input (30 Min)
- [ ] "Top 5 Software Architecture Patterns" YouTube (15 Min)
- [ ] Microsoft Patterns lesen (15 Min)

#### Verarbeitung (30 Min)
- [ ] `architecture_patterns.md` erstellen
- [ ] 5 Patterns dokumentieren:
  1. Layered (N-Tier)
  2. Microservices
  3. Event-Driven
  4. Client-Server
  5. Pipeline

**Deliverable:** `architecture_patterns.md`

---

### **Tag 2 (Dienstag): Layered Architecture**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "Layered Architecture Pattern" lesen

#### Verarbeitung (40 Min)
- [ ] Diagramm: Layered Architecture (3-Tier)
  - Presentation Layer
  - Business Logic Layer
  - Data Access Layer
- [ ] Vor-/Nachteile dokumentieren

**Deliverable:** Layered Architecture Diagramm

---

### **Tag 3 (Mittwoch): Microservices Pattern**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "Microservices Architecture" YouTube (15 Min)

#### Verarbeitung (40 Min)
- [ ] Diagramm: Microservices Architecture
  - API Gateway
  - Service A, B, C
  - Message Queue
  - Databases (pro Service)
- [ ] Vor-/Nachteile dokumentieren

**Deliverable:** Microservices Diagramm

---

### **Tag 4 (Donnerstag): Monolith vs. Microservices**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "When to use Microservices" Artikel

#### Verarbeitung (40 Min)
- [ ] Vergleichstabelle erstellen:

| Aspekt | Monolith | Microservices |
|--------|----------|---------------|
| Deployment | Einfach | Komplex |
| Skalierung | Vertikal | Horizontal |
| Technologie | Einheitlich | Polyglot |
| Komplexität | Niedrig | Hoch |
| Team-Größe | Klein | Groß |

**Deliverable:** `monolith_vs_microservices.md`

---

### **Tag 5 (Freitag): Wochenabschluss**
**Zeitaufwand:** 60 Min

#### Konsolidierung (40 Min)
- [ ] `week_03_summary.md` erstellen
- [ ] Alle Diagramme & Notizen committen

#### Review (20 Min)
- [ ] Selbsttest: 5 Patterns aus dem Gedächtnis aufzählen
- [ ] Nächste Woche vorbereiten: Portfolio finalisieren

**Deliverable:** `week_03_summary.md`

---

## 📋 Woche 4: Portfolio Setup & ADR

### **Tag 1 (Montag): Repository-Struktur finalisieren**
**Zeitaufwand:** 60 Min

#### Aktivität (60 Min)
- [ ] README.md schreiben:
  - Wer bin ich?
  - Was ist dieses Repo?
  - Roadmap-Übersicht
- [ ] Ordnerstruktur prüfen:
  - `00_roadmap/`
  - `01_architecture_principles/`
  - `diagrams/`
- [ ] `.gitignore` erstellen (falls nötig)

**Deliverable:** README.md finalisiert

---

### **Tag 2 (Dienstag): ADR-Template erstellen**
**Zeitaufwand:** 60 Min

#### Input (20 Min)
- [ ] "Architecture Decision Records" lesen: https://adr.github.io/

#### Verarbeitung (40 Min)
- [ ] ADR-Template erstellen: `templates/adr_template.md`
- [ ] Struktur:
  1. Title
  2. Status (Proposed, Accepted, Rejected)
  3. Context
  4. Decision
  5. Consequences

**Deliverable:** ADR-Template

---

### **Tag 3 (Mittwoch): Erste ADR schreiben**
**Zeitaufwand:** 60 Min

#### Aktivität (60 Min)
- [ ] ADR-001 schreiben: "Use PostgreSQL for Database"
- [ ] Struktur ausfüllen:
  - **Context:** Need relational DB, ACID-compliant
  - **Decision:** PostgreSQL
  - **Alternatives:** MySQL, MongoDB
  - **Consequences:** Strong consistency, but not NoSQL

**Deliverable:** `07_architecture_decision_records/adr_001_database.md`

---

### **Tag 4 (Donnerstag): Portfolio polieren**
**Zeitaufwand:** 60 Min

#### Aktivität (60 Min)
- [ ] Alle Diagramme überprüfen (Konsistenz, Lesbarkeit)
- [ ] Alle Markdown-Dateien prüfen (Rechtschreibung, Formatierung)
- [ ] Links prüfen (funktionierende URLs)

**Deliverable:** Poliertes Portfolio

---

### **Tag 5 (Freitag): Phase 0 Abschluss**
**Zeitaufwand:** 60 Min

#### Konsolidierung (40 Min)
- [ ] `phase_0_summary.md` erstellen
- [ ] Checkliste abhaken:
  - [ ] 5+ Diagramme erstellt
  - [ ] 10+ Prinzipien dokumentiert
  - [ ] 1 ADR geschrieben
  - [ ] Portfolio öffentlich (GitHub)

#### Reflexion (20 Min)
- [ ] Was habe ich gelernt?
- [ ] Was kann ich jetzt besser?
- [ ] Bereit für Phase 1?

**Deliverable:** `phase_0_summary.md`

---

## ✅ Erfolgsmetriken Phase 0

Nach 4 Wochen solltest du haben:
- ✅ 5+ Architekturdiagramme (C4, Patterns)
- ✅ 10+ Architekturprinzipien dokumentiert
- ✅ 1+ ADR geschrieben
- ✅ Portfolio-Repository öffentlich (GitHub)
- ✅ Verständnis für Architekturdenken

---

## 🧠 AuDHD-Tipps

### Wenn es zu schnell geht:
- **Pause einlegen:** 1 Tag Pause pro Woche ok
- **Tempo reduzieren:** 4 Wochen → 6 Wochen
- **Fokus:** Lieber 3 gute Diagramme als 10 halbfertige

### Wenn es zu langsam geht:
- **Tempo erhöhen:** 90 Min → 120 Min/Tag
- **Parallel arbeiten:** 2 Themen gleichzeitig (nur wenn Energie da)

### Wenn Fokus schwer fällt:
- **Pomodoro:** 25 Min arbeiten, 5 Min Pause
- **Musik:** Lofi/Ambient (oder Stille, je nach Präferenz)
- **Umgebung:** Ruhiger Raum, Handy weg

---

## 🚀 Nächster Schritt

**Phase 1:** System- & Security-Architektur (Monat 2-6)  
**Fokus:** Netzwerk, IAM, Zero Trust, Security+

---

*Letzte Aktualisierung: Februar 2026*
