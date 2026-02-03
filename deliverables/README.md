# Deliverables Ordner

Dieser Ordner ist für deine TOGAF-Lern-Deliverables.

## Struktur

Jede TOGAF ADM Phase hat einen eigenen Unterordner:

```
deliverables/
├── preliminary/              # Preliminary Phase
│   └── architecture_principles.md
├── phase_a/                  # Architecture Vision
│   └── architecture_vision.md
├── phase_b/                  # Business Architecture
│   └── capability_map.drawio
├── phase_c/                  # Information Systems Architecture
│   ├── data_architecture.md
│   └── application_architecture.drawio
├── phase_d/                  # Technology Architecture
│   └── technology_architecture.drawio
├── phase_e/                  # Opportunities & Solutions
│   └── implementation_plan.md
├── phase_f/                  # Migration Planning
│   └── architecture_roadmap.md
├── phase_g/                  # Implementation Governance
│   └── architecture_contract_template.md
├── phase_h/                  # Change Management
│   └── change_management_process.md
└── requirements_management/  # Requirements Management
    └── requirements_traceability_matrix.md
```

## Empfohlene Deliverables pro Phase

### Preliminary Phase
- `architecture_principles.md` - Liste von Architecture Principles

### Phase A: Architecture Vision
- `architecture_vision.md` - Vision Document
- `stakeholder_map.drawio` - Stakeholder-Übersicht
- `high_level_architecture.drawio` - High-level Ist/Soll

### Phase B: Business Architecture
- `capability_map.drawio` - Business Capability Map
- `value_streams.md` - Value Stream Dokumentation
- `business_processes.drawio` - Business Process Diagramme

### Phase C: Information Systems Architecture
- `data_architecture.md` - Data Model & Data Flow
- `application_architecture.drawio` - Application Landscape
- `integration_patterns.md` - Integration Patterns

### Phase D: Technology Architecture
- `technology_architecture.drawio` - Technology Stack Diagram
- `network_diagram.drawio` - Network Architecture
- `technology_standards.md` - Technology Standards Catalog

### Phase E: Opportunities & Solutions
- `implementation_plan.md` - Implementation & Migration Plan
- `gap_analysis.md` - Gap Analysis (Ist vs. Soll)
- `transition_architectures.drawio` - Transition Steps

### Phase F: Migration Planning
- `architecture_roadmap.md` - Detaillierte Roadmap
- `prioritization_matrix.md` - Priorisierung der Projekte

### Phase G: Implementation Governance
- `architecture_contract_template.md` - Contract Template
- `compliance_checklist.md` - Compliance Review Checklist

### Phase H: Architecture Change Management
- `change_management_process.md` - Change Management Prozess
- `lessons_learned.md` - Lessons Learned

### Requirements Management
- `requirements_traceability_matrix.md` - Traceability Matrix

---

## Tools für Deliverables

### Diagramme
- **Draw.io** (https://app.diagrams.net/) - Kostenlos, lokal oder online
- **Excalidraw** (https://excalidraw.com/) - Sketch-Style
- **PlantUML** - Textbasiert (für Versionskontrolle)

### Dokumente
- **Markdown** (.md) - Einfach, Git-freundlich
- **Obsidian** - Markdown mit Links
- **Notion** - Strukturiert (aber Cloud)

### Architecture Modeling
- **Archi** (https://www.archimatetool.com/) - ArchiMate Tool
- **C4 Model** (https://c4model.com/) - Einfache Diagramme

---

## Beispiel Session

```bash
# 1. Learning Agent starten
python 09_tools_and_methods/togaf_learning_agent.py

# 2. Phase wählen (z.B. Phase A)

# 3. Deliverable erstellen
# Erstelle: deliverables/phase_a/architecture_vision.md

# 4. Committen
git add deliverables/phase_a/
git commit -m "Phase A: Architecture Vision Document"
git push
```

---

## Tipps

- ✅ **Ein Deliverable pro Phase:** Fokus auf Qualität statt Quantität
- ✅ **Templates nutzen:** Siehe `09_tools_and_methods/learning_sessions_templates/`
- ✅ **Committen:** Jedes Deliverable ist ein Commit
- ✅ **Portfolio:** Diese Deliverables sind dein Portfolio

---

*Dieser Ordner sollte im `.gitignore` sein, wenn Deliverables persönlich sind,*  
*ODER committtet werden, wenn sie als Portfolio dienen sollen.*
