# Architecture Principles Template

**Projekt/Organisation:** [Name]  
**Datum:** YYYY-MM-DD  
**Version:** 1.0  
**Erstellt mit:** TOGAF Learning Agent (Preliminary Phase)

---

## Prinzip 1: [Name]

### Statement
[Kurze, prägnante Aussage - max. 1 Satz]

### Rationale
[Warum ist dieses Prinzip wichtig? Was sind die Business-Gründe?]

### Implications
[Was bedeutet dieses Prinzip für:
- Projektentscheidungen
- Architekturentscheidungen
- Operationen
- Kosten/Budget]

---

## Prinzip 2: Business-driven

### Statement
IT folgt Business, nicht umgekehrt

### Rationale
- Business-Ziele bestimmen die IT-Strategie
- IT ist Enabler für Business-Value
- Investitionen müssen Business-Nutzen nachweisen
- Business-Prioritäten leiten IT-Prioritäten

### Implications
- Neue IT-Initiativen benötigen Business-Justification
- Business-Stakeholder müssen in Architektur-Entscheidungen eingebunden sein
- IT-Metriken müssen Business-KPIs unterstützen
- Technology-Entscheidungen müssen Business-Anforderungen erfüllen

---

## Prinzip 3: Simplicity

### Statement
Keep it simple - Einfachheit über Komplexität

### Rationale
- Komplexität erhöht Fehleranfälligkeit
- Einfache Systeme sind wartbarer
- Geringere Total Cost of Ownership (TCO)
- Schnellere Onboarding neuer Team-Mitglieder

### Implications
- Neue Features nur wenn echte Business-Notwendigkeit
- Technologie-Stack begrenzen
- Dokumentation einfach halten
- Legacy-Systeme ablösen, nicht umgehen

---

## Prinzip 4: Interoperability

### Statement
Systeme müssen miteinander kommunizieren können

### Rationale
- Daten-Silos verhindern Business-Agility
- Integration ist kritisch für End-to-End-Prozesse
- Vendor Lock-in vermeiden
- Flexibilität für zukünftige Änderungen

### Implications
- Standardisierte APIs (RESTful, GraphQL)
- Daten-Standards definieren (JSON, XML)
- API-First-Design
- Integration Patterns dokumentieren

---

## Prinzip 5: Reusability

### Statement
Wiederverwendung von Komponenten

### Rationale
- Reduziert Entwicklungszeit
- Konsistenz über Systeme
- Geringere Maintenance-Kosten
- Schnellere Time-to-Market

### Implications
- Komponenten modular entwickeln
- Shared Services aufbauen
- Architecture Building Blocks definieren
- Inner-Source-Kultur fördern

---

## Prinzip 6: Security by Design

### Statement
Security von Anfang an, nicht nachträglich

### Rationale
- Nachträgliche Security ist teuer
- Regulatorische Anforderungen (GDPR, etc.)
- Reputationsrisiko bei Breaches
- Prevention over Reaction

### Implications
- Security in jeder ADM-Phase
- Threat Modeling in Design-Phase
- Security-Reviews verpflichtend
- Zero-Trust-Architektur

---

## Prinzip 7: [Weiteres Prinzip]

### Statement
[...]

### Rationale
[...]

### Implications
[...]

---

## Governance & Enforcement

### Architecture Board
- Prüft Compliance mit Prinzipien
- Entscheidet über Ausnahmen
- Review vor Projekt-Start

### Ausnahmen
Ausnahmen von Prinzipien müssen:
1. Dokumentiert werden (ADR)
2. Vom Architecture Board genehmigt werden
3. Zeitlich befristet sein
4. Tech Debt dokumentieren

### Review-Prozess
- Preliminary: Prinzipien definieren
- Phase A-H: Compliance prüfen
- Phase G: Compliance-Review
- Phase H: Prinzipien aktualisieren

---

## Mapping zu TOGAF ADM

| Prinzip | Phase A | Phase B | Phase C | Phase D | Phase E | Phase F | Phase G | Phase H |
|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Business-driven | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Simplicity | ✅ | - | ✅ | ✅ | ✅ | ✅ | - | ✅ |
| Interoperability | - | - | ✅ | ✅ | ✅ | - | - | - |
| Reusability | - | ✅ | ✅ | ✅ | ✅ | - | - | - |
| Security by Design | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Nächste Schritte

- [ ] Prinzipien mit Stakeholdern reviewen
- [ ] Im Architecture Repository ablegen
- [ ] In Phase A (Architecture Vision) referenzieren
- [ ] Governance-Prozess etablieren

---

## Referenzen

- TOGAF Standard 10: https://www.opengroup.org/togaf
- [Architecture Principles Guide](https://pubs.opengroup.org/architecture/togaf9-doc/arch/chap20.html)
- [Enterprise Architecture Principles](https://en.wikipedia.org/wiki/Enterprise_architecture_principles)

---

*Template erstellt: Februar 2026*  
*Quelle: TOGAF Learning Agent (Preliminary Phase)*
