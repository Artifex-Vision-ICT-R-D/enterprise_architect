# 🔐 SABSA Overview

## Was ist SABSA?

**SABSA** = **Sherwood Applied Business Security Architecture**

SABSA ist ein **Framework** für **Security Architecture**, das Security als **geschäftsgetriebenen Prozess** betrachtet.

> **SABSA beantwortet:** "Wie entwickle ich Security-Architektur, die dem Business dient?"

### SABSA vs. TOGAF
| Aspekt | TOGAF | SABSA |
|--------|-------|-------|
| **Fokus** | Enterprise Architecture (generell) | Security Architecture (speziell) |
| **Treiber** | Business-IT-Alignment | Risk & Business Value |
| **Methode** | ADM (Architecture Development Method) | SABSA Lifecycle (ähnlich ADM) |
| **Kompatibilität** | SABSA kann **in** TOGAF integriert werden | Ergänzt TOGAF für Security |

**Fazit:** TOGAF = Framework für EA, SABSA = Framework für Security innerhalb EA

---

## 🎯 SABSA Kernelemente

### 1. **SABSA Matrix (6x6)**
Das **Herzstück von SABSA** ist die **Matrix**, die Security-Architektur strukturiert:

#### **6 Fragen (Was-Achse):**
1. **What** (Assets): Was schützen wir?
2. **Why** (Motivation): Warum schützen wir es?
3. **How** (Process): Wie schützen wir es?
4. **Who** (People): Wer ist verantwortlich?
5. **Where** (Location): Wo schützen wir es?
6. **When** (Time): Wann schützen wir es?

#### **6 Schichten (Wie-Achse):**
1. **Contextual** (Business View): Business-Treiber, Risiken
2. **Conceptual** (Architect's View): Security-Konzepte, Prinzipien
3. **Logical** (Designer's View): Security-Services, Policies
4. **Physical** (Builder's View): Security-Mechanismen, Produkte
5. **Component** (Tradesman's View): Tools, Technologien
6. **Operational** (Facility Manager's View): Monitoring, Betrieb

**Matrix-Beispiel:**

| Schicht | What (Assets) | Why (Motivation) | How (Process) | Who (People) | Where (Location) | When (Time) |
|---------|---------------|------------------|---------------|--------------|------------------|-------------|
| **Contextual** | Business Data | Risk Appetite | Risk Management | Business Owner | Global Operations | Business Hours |
| **Conceptual** | Information | Risk-based Strategy | Defense in Depth | Security Architect | Trust Zones | Lifecycle Phases |
| **Logical** | Data Classes | Security Policy | Access Control | Security Admin | Network Segments | Session Timeouts |
| **Physical** | Databases | Compliance | Encryption | Security Engineer | Data Centers | Real-time |
| **Component** | PostgreSQL | Audit Logs | TLS 1.3 | DBA | AWS eu-central-1 | 24/7 |
| **Operational** | DB Instances | Monitoring | SIEM | SOC Analyst | Frankfurt DC | Incident Response |

---

### 2. **Business Attributes**
SABSA ist **business-driven**, nicht technik-zentriert. Statt "Wir brauchen Firewall" fragt SABSA:

**Was sind die Business-Anforderungen an Security?**

**Beispiel Business Attributes:**
- **Confidentiality:** Nur autorisierte Personen sehen Daten
- **Integrity:** Daten dürfen nicht unbemerkt verändert werden
- **Availability:** System muss 99,9% verfügbar sein
- **Accountability:** Aktionen müssen nachvollziehbar sein
- **Auditability:** Compliance-Nachweis

**Mapping:**
```
Business Attribute       → Security Service           → Technology
Confidentiality          → Access Control             → IAM, Encryption
Integrity                → Data Validation            → Checksums, Signatures
Availability             → Redundancy                 → Load Balancer, Failover
Accountability           → Logging & Monitoring       → SIEM, Audit Logs
```

---

### 3. **SABSA Lifecycle**
SABSA hat einen **iterativen Lebenszyklus** ähnlich TOGAF ADM:

```
Strategy & Planning
       ↓
   Design
       ↓
Implementation
       ↓
  Operations
       ↓
(zurück zu Strategy)
```

#### **Phase 1: Strategy & Planning**
- Risk Assessment
- Business Attributes definieren
- Security-Strategie entwickeln

#### **Phase 2: Design**
- Conceptual Security Architecture
- Logical Security Services
- Physical Security Mechanisms

#### **Phase 3: Implementation**
- Build Security Controls
- Integration & Testing
- Deployment

#### **Phase 4: Operations**
- Monitoring & Incident Response
- Continuous Improvement
- Lessons Learned

---

### 4. **Risk Management (zentral)**
SABSA ist **risiko-basiert**. Alles dreht sich um:

**Risk = Threat × Vulnerability × Impact**

**Prozess:**
1. **Risk Identification:** Welche Risiken gibt es?
2. **Risk Assessment:** Wie wahrscheinlich? Wie hoch der Impact?
3. **Risk Treatment:**
   - **Avoid** (vermeiden)
   - **Mitigate** (reduzieren)
   - **Transfer** (Versicherung)
   - **Accept** (akzeptieren)
4. **Risk Monitoring:** Risiken kontinuierlich überwachen

**Beispiel:**
- **Threat:** Ransomware-Angriff
- **Vulnerability:** Keine Backups
- **Impact:** 1 Mio CHF Schaden
- **Risk:** Hoch
- **Treatment:** Mitigate (Backups implementieren)

---

## 🧩 SABSA Layered Architecture Model

### **6 Schichten (Top → Bottom):**

#### 1. **Contextual (Business View)**
**Wer:** Management, Business Owner  
**Was:** Business-Treiber, Risk Appetite  
**Output:** Business Security Requirements

**Beispiel:**
- "Wir müssen GDPR-compliant sein"
- "Customer Data darf nicht leaken"

---

#### 2. **Conceptual (Architect's View)**
**Wer:** Security Architect  
**Was:** Security-Konzepte, Prinzipien  
**Output:** Conceptual Security Architecture

**Beispiel:**
- Prinzip: "Zero Trust Architecture"
- Konzept: "Defense in Depth"

---

#### 3. **Logical (Designer's View)**
**Wer:** Security Designer  
**Was:** Security-Services, Policies  
**Output:** Logical Security Architecture

**Beispiel:**
- Service: "Multi-Factor Authentication (MFA)"
- Policy: "Passwords müssen 12+ Zeichen haben"

---

#### 4. **Physical (Builder's View)**
**Wer:** Security Engineer  
**Was:** Security-Mechanismen, Produkte  
**Output:** Physical Security Architecture

**Beispiel:**
- Mechanismus: "TLS 1.3 für Datenübertragung"
- Produkt: "Keycloak für IAM"

---

#### 5. **Component (Tradesman's View)**
**Wer:** System Admin, DevOps  
**Was:** Tools, Technologien  
**Output:** Security-Komponenten

**Beispiel:**
- Tool: "Vault für Secrets Management"
- Config: "TLS Certificate Rotation"

---

#### 6. **Operational (Facility Manager's View)**
**Wer:** SOC Analyst, Ops Team  
**Was:** Monitoring, Incident Response  
**Output:** Operational Security

**Beispiel:**
- Monitoring: "SIEM (Splunk, ELK)"
- Incident Response: "Playbook für Ransomware"

---

## 🎯 SABSA Prinzipien

### 1. **Business-Driven**
Security muss **Business Value** liefern, nicht nur "sicher machen".

**Beispiel:**
- ❌ Falsch: "Wir brauchen Firewall, weil Security"
- ✅ Richtig: "Wir brauchen Firewall, um Datenverlust zu verhindern (GDPR-Compliance, 10 Mio € Strafe vermeiden)"

---

### 2. **Risk-Based**
Priorisierung nach **Risiko**, nicht nach "Best Practice".

**Beispiel:**
- Risiko Hoch: Customer Data Breach → **Priorität 1**
- Risiko Niedrig: Internes Wiki gehackt → **Priorität 3**

---

### 3. **Holistic (Ganzheitlich)**
Security ist nicht nur Technologie, sondern auch:
- **People:** Schulung, Awareness
- **Process:** Policies, Governance
- **Technology:** Firewalls, Encryption

---

### 4. **Continuous**
Security ist kein Projekt, sondern ein **kontinuierlicher Prozess**.

**Lifecycle:**
- Design → Implement → Operate → Improve → Repeat

---

## 📊 SABSA in der Praxis

### Wann SABSA nutzen?
- ✅ Security-kritische Umgebungen (Finance, Healthcare, Gov)
- ✅ Regulierte Industrien (GDPR, PCI-DSS, HIPAA)
- ✅ Große Organisationen (100+ Mitarbeiter)
- ✅ Komplexe Bedrohungsszenarien

### Wann SABSA **nicht** nutzen?
- ❌ Kleine Startups (Overhead zu groß)
- ❌ Non-Security-fokussierte Projekte (TOGAF reicht)
- ❌ Keine regulatorischen Anforderungen

---

## 🔗 SABSA + TOGAF Integration

SABSA kann **innerhalb** von TOGAF verwendet werden:

### **TOGAF ADM + SABSA:**
- **Phase A (Vision):** SABSA Contextual (Business Security Requirements)
- **Phase B (Business):** SABSA Conceptual (Security Principles)
- **Phase C (Information):** SABSA Logical (Data Security Policies)
- **Phase D (Technology):** SABSA Physical (Security Mechanisms)
- **Phase G (Governance):** SABSA Operational (Security Monitoring)

**Beispiel:**
- TOGAF Phase D: "Wir migrieren in die Cloud"
- SABSA: "Shared Responsibility Model, Zero Trust, Encryption at Rest/Transit"

---

## 🧠 SABSA Mindset

### Was SABSA **ist**
- ✅ Business-driven Security
- ✅ Risk-basiert
- ✅ Ganzheitlich (People, Process, Technology)
- ✅ Lifecycle-orientiert

### Was SABSA **nicht ist**
- ❌ Nicht nur Technologie
- ❌ Nicht "Security Checklist"
- ❌ Nicht statisch (kontinuierlich)

---

## 🛡️ SABSA vs. andere Security Frameworks

| Framework | Fokus | Zielgruppe |
|-----------|-------|------------|
| **SABSA** | Security Architecture (business-driven) | Security Architects, Enterprise Architects |
| **NIST CSF** | Security Governance & Risk Management | CISOs, Risk Managers |
| **ISO 27001** | Information Security Management System (ISMS) | Compliance, Auditors |
| **NIST SP 800-207** | Zero Trust Architecture (speziell) | Network Architects, Security Engineers |
| **COBIT** | IT Governance (allgemein) | IT Management |

**Empfehlung:**
- **SABSA** für Security-Architektur
- **NIST CSF** für Risk Management
- **ISO 27001** für Compliance
- **NIST SP 800-207** für Zero Trust

---

## 📖 Weiterführende Ressourcen

### Kostenlos
- **SABSA Executive Summary:** https://sabsa.org/sabsa-executive-summary/
- **SABSA White Papers:** https://sabsa.org/knowledge-base/
- **NIST SP 800-207 (Zero Trust):** https://csrc.nist.gov/publications/detail/sp/800-207/final

### Bezahlt
- **SABSA Foundation Training:** ~600 CHF (online)
- **SABSA Practitioner Training:** ~800 CHF
- **SABSA White Papers Bundle:** ~100 CHF

---

## 🚀 Nächster Schritt

1. **SABSA Matrix auswendig lernen:** 6 Fragen × 6 Schichten
2. **Business Attributes definieren:** Für ein fiktives Projekt
3. **Risk Assessment:** 1 Threat Modeling Übung
4. **Mapping:** Business Attribute → Security Service → Technology

> **Tipp:** SABSA ist **business-driven**, nicht technik-zentriert. Immer vom Business aus denken!

---

*Letzte Aktualisierung: Februar 2026*
