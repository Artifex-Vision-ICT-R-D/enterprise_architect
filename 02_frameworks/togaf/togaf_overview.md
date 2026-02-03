# 🏛️ TOGAF Overview

## Was ist TOGAF?

**TOGAF** = **The Open Group Architecture Framework**

TOGAF ist ein **Framework** und **Werkzeugkasten** für Enterprise Architecture. Es ist **kein Prozess**, den man stupide befolgt, sondern eine **strukturierte Methode**, um:
- Business-IT-Alignment zu erreichen
- Architekturentscheidungen zu dokumentieren
- Langfristige IT-Steuerung zu ermöglichen
- Mit Management und Business zu kommunizieren

> TOGAF beantwortet: **"Wie entwickle ich Architektur systematisch?"**

---

## 🎯 TOGAF Kernelemente

### 1. **Architecture Development Method (ADM)**
Der ADM ist das **Herzstück von TOGAF**. Es ist ein **iterativer Zyklus** mit 9 Phasen:

```
        Preliminary
             |
         Phase A (Vision)
             |
     +-------+-------+
     |       |       |
  Phase B  Phase C  Phase D
  (Business) (Information) (Technology)
     |       |       |
     +-------+-------+
             |
         Phase E (Opportunities & Solutions)
             |
         Phase F (Migration Planning)
             |
         Phase G (Implementation Governance)
             |
         Phase H (Architecture Change Management)
             |
    Requirements Management (zentral)
```

**Jede Phase hat:**
- **Inputs** (Was brauche ich?)
- **Steps** (Was tue ich?)
- **Outputs** (Was produziere ich?)

---

### 2. **Enterprise Continuum**
Das Enterprise Continuum ist ein **Repository-Konzept**, das Architektur-Assets klassifiziert:

```
Foundation Architectures → Common System Architectures → Industry Architectures → Organization-Specific Architectures
(Generisch)                                                                    (Spezifisch)
```

**Beispiel:**
- **Foundation:** TOGAF selbst, ISO-Standards
- **Common Systems:** AWS Well-Architected, Microservices-Pattern
- **Industry:** Banking-Referenzarchitekturen
- **Organization-Specific:** Deine Firma (Ist/Soll)

---

### 3. **Architecture Content Framework**
Definiert **was** dokumentiert wird:

| Ebene | Beschreibung | Beispiel |
|-------|--------------|----------|
| **Deliverables** | Was dem Stakeholder übergeben wird | Architecture Vision Document |
| **Artifacts** | Detaillierte Dokumentation | Business Process Model, Network Diagram |
| **Building Blocks** | Wiederverwendbare Komponenten | Identity Provider, API Gateway |

---

### 4. **Architecture Capability Framework**
Beschreibt, **wie** du EA-Fähigkeiten in der Organisation aufbaust:
- Rollen (Lead Architect, Domain Architects)
- Skills (Architekturdenken, Kommunikation)
- Governance (Architecture Board, Compliance)

---

## 🔄 TOGAF ADM im Detail

### **Preliminary Phase: Framework & Principles**
**Ziel:** TOGAF an die Organisation anpassen

**Aktivitäten:**
- Architekturprinzipien definieren
- Framework tailoring (TOGAF ist anpassbar!)
- Stakeholder identifizieren
- Tools auswählen (z. B. Archi, Enterprise Architect)

**Output:**
- Architecture Principles
- Tailored Architecture Framework
- Request for Architecture Work

---

### **Phase A: Architecture Vision**
**Ziel:** Business-Problem verstehen, Zielarchitektur skizzieren

**Aktivitäten:**
- Stakeholder Concerns erfassen
- Business Scenarios (Warum brauchen wir das?)
- High-level Zielarchitektur (Ist → Soll)
- Statement of Architecture Work

**Output:**
- Architecture Vision Document
- Stakeholder Map
- Architecture Principles (Bestätigung)

**Beispiel:**
- **Problem:** Legacy-System kostet zu viel, nicht skalierbar
- **Vision:** Cloud-basierte Microservices-Architektur
- **Stakeholder:** CTO (Kosten), Dev-Teams (Velocity)

---

### **Phase B: Business Architecture**
**Ziel:** Business-Prozesse und Capabilities modellieren

**Aktivitäten:**
- Business Capability Mapping
- Value Streams
- Business Process Modeling

**Output:**
- Business Architecture Document
- Capability Map
- Business Process Diagrams

**Beispiel:**
- **Capability:** "Kundenidentifikation"
- **Prozess:** Onboarding → KYC → Identity Verification

---

### **Phase C: Information Systems Architecture**
**Ziel:** Daten- und Applikationsarchitektur entwickeln

**C1: Data Architecture**
- Datenmodelle (Logical, Physical)
- Data Flow Diagrams
- Data Governance

**C2: Application Architecture**
- Applikationslandschaft (Ist/Soll)
- Application Portfolio Management
- Integration Patterns

**Output:**
- Data Architecture Document
- Application Architecture Document
- Interface Catalog

---

### **Phase D: Technology Architecture**
**Ziel:** IT-Infrastruktur und Plattformen definieren

**Aktivitäten:**
- Hardware & Network Architecture
- Cloud vs. On-Premise
- Security Architecture

**Output:**
- Technology Architecture Document
- Technology Standards Catalog
- Network Diagrams

**Beispiel:**
- **Ist:** On-Premise Data Center, monolithische App
- **Soll:** AWS (EC2, S3, RDS), Kubernetes, API Gateway

---

### **Phase E: Opportunities & Solutions**
**Ziel:** Migrationsprojekte identifizieren, Work Packages definieren

**Aktivitäten:**
- Gap Analysis (Ist vs. Soll)
- Transition Architectures (Zwischenschritte)
- Konsolidierung von Work Packages

**Output:**
- Implementation & Migration Plan
- Transition Architectures (v1, v2, v3)

**Beispiel:**
- **Gap:** Keine Microservices, keine Cloud
- **Transition 1:** Lift & Shift (VM → Cloud)
- **Transition 2:** Refactor (Monolith → Microservices)
- **Ziel:** Cloud-native Architecture

---

### **Phase F: Migration Planning**
**Ziel:** Detaillierte Implementierungs-Roadmap

**Aktivitäten:**
- Priorisierung (Business Value vs. Risk)
- Abhängigkeiten (Reihenfolge der Projekte)
- Kosten/Nutzen-Analyse

**Output:**
- Implementation & Migration Plan (finalisiert)
- Architecture Roadmap
- Architecture Definition Document (finalisiert)

---

### **Phase G: Implementation Governance**
**Ziel:** Sicherstellen, dass die Implementierung der Architektur folgt

**Aktivitäten:**
- Architecture Compliance Reviews
- Änderungsanträge bewerten
- Zusammenarbeit mit Projektmanagement

**Output:**
- Architecture Contracts
- Compliance Assessments

**Beispiel:**
- Dev-Team will MySQL statt PostgreSQL → Architecture Board prüft
- Entscheidung: PostgreSQL (Standardisierung + Support)

---

### **Phase H: Architecture Change Management**
**Ziel:** Architektur kontinuierlich weiterentwickeln

**Aktivitäten:**
- Monitoring von Technologien
- Change Requests bewerten
- Lessons Learned

**Output:**
- Architecture Updates
- Change Requests (akzeptiert/abgelehnt)

---

### **Requirements Management (zentral)**
**Ziel:** Anforderungen während aller Phasen managen

**Aktivitäten:**
- Requirements aufnehmen
- Priorisieren
- Traceability (Anforderung → Architektur-Element)

**Output:**
- Requirements Repository

---

## 🧩 Architecture Building Blocks (ABBs)

### **ABB** = Architecture Building Block
**Definition:** Logische, wiederverwendbare Komponente

**Beispiel:**
- Identity Provider (ABB)
- API Gateway (ABB)
- Message Queue (ABB)

### **SBB** = Solution Building Block
**Definition:** Konkrete Implementierung eines ABB

**Beispiel:**
- Identity Provider (ABB) → **Keycloak** (SBB)
- API Gateway (ABB) → **Kong** (SBB)
- Message Queue (ABB) → **RabbitMQ** (SBB)

**Mapping:**
```
ABB (Was?)         → SBB (Womit?)
Identity Provider  → Keycloak, Auth0, Okta
API Gateway        → Kong, Apigee, AWS API Gateway
```

---

## 📜 Architecture Governance

**Ziel:** Sicherstellen, dass Architektur eingehalten wird

### Architecture Board
- Entscheidungsgremium (CTO, Lead Architects, etc.)
- Prüft Architecture Compliance
- Genehmigt Change Requests

### Architecture Contracts
- Vereinbarung zwischen Projekt & Architecture Board
- "Du darfst abweichen, wenn..."
- Beispiel: "PostgreSQL Standard, aber MongoDB erlaubt für Analytics-Use-Case"

### Compliance Reviews
- Review während Projektverlauf
- Prüfpunkte: Design Review, Code Review, Deployment Review

---

## 🎯 TOGAF Prinzipien

### Beispiele für Architecture Principles
1. **Business-driven:** IT folgt Business, nicht umgekehrt
2. **Simplicity:** Einfachheit über Komplexität
3. **Interoperability:** Systeme müssen miteinander kommunizieren
4. **Reusability:** Wiederverwendung von Komponenten
5. **Security by Design:** Security von Anfang an

**Format eines Prinzips:**
- **Name:** Simplicity
- **Statement:** "Keep it simple"
- **Rationale:** Komplexität erhöht Fehleranfälligkeit & Kosten
- **Implications:** Neue Features nur wenn nötig, Tech Debt reduzieren

---

## 🧠 TOGAF Mindset

### Was TOGAF **ist**
- ✅ Framework (Werkzeugkasten)
- ✅ Strukturierte Methode
- ✅ Kommunikations-Tool (Business ↔ IT)
- ✅ Iterativ & anpassbar

### Was TOGAF **nicht ist**
- ❌ Kein starrer Prozess (nicht Wasserfall)
- ❌ Keine Silver Bullet (denken erforderlich)
- ❌ Nicht für kleine Projekte (Overkill)
- ❌ Kein Tool (TOGAF ist Framework, nicht Software)

---

## 💡 TOGAF in der Praxis

### Wann TOGAF nutzen?
- ✅ Enterprise-Level (100+ Mitarbeiter)
- ✅ Komplexe IT-Landschaften
- ✅ Langfristige Architektur (3-5 Jahre)
- ✅ Regulierte Industrien (Banking, Healthcare)

### Wann TOGAF **nicht** nutzen?
- ❌ Startup (zu viel Overhead)
- ❌ Single-Application (kein Enterprise-Kontext)
- ❌ Agile-only (TOGAF passt nicht zu pure Agile)

---

## 📖 Weiterführende Ressourcen

### Kostenlos
- **TOGAF Standard 10:** https://www.opengroup.org/togaf
- **ADM Quick Reference:** https://www.opengroup.org/library/togaf
- **YouTube:** "TOGAF in 100 seconds"

### Bezahlt
- **Coursera TOGAF 10 Foundation** (~50 CHF)
- **Udemy TOGAF 10 Exam Prep** (~20 CHF)
- **TOGAF 10 Foundation Study Guide** (~50 CHF)

---

## 🚀 Nächster Schritt

1. **ADM-Zyklus visualisieren:** Eigenes Diagramm zeichnen
2. **1 Phase detailliert:** Phase A (Architecture Vision) durcharbeiten
3. **Beispiel anwenden:** Eigenes (fiktives) Projekt durch ADM laufen lassen

> **Tipp:** TOGAF nicht auswendig lernen, sondern **verstehen** und **anwenden**.

---

*Letzte Aktualisierung: Februar 2026*
