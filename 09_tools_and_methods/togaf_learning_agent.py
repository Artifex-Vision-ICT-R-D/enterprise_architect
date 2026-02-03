#!/usr/bin/env python3
"""
TOGAF EA Learning Agent (Lernagent für TOGAF EA)

An interactive learning agent for TOGAF (The Open Group Architecture Framework)
optimized for AuDHD learning styles with:
- Timeboxing (Pomodoro technique)
- Active recall exercises
- Visual learning support
- Progress tracking
- Output-focused learning (deliverables per session)

Usage:
    python togaf_learning_agent.py
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# ANSI color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class TOGAFLearningAgent:
    """Interactive learning agent for TOGAF Enterprise Architecture"""
    
    def __init__(self):
        self.progress_file = Path("togaf_learning_progress.json")
        self.progress_data = self.load_progress()
        self.current_session = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time_started": datetime.now().strftime("%H:%M"),
            "phase": None,
            "deliverable": None
        }
        
    def load_progress(self) -> Dict:
        """Load learning progress from JSON file"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "sessions_completed": 0,
            "phases_learned": [],
            "deliverables": [],
            "last_session": None,
            "quiz_scores": {}
        }
    
    def save_progress(self):
        """Save learning progress to JSON file"""
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.progress_data, f, indent=2, ensure_ascii=False)
    
    def print_header(self, text: str):
        """Print formatted header"""
        print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{text.center(70)}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{'='*70}{Colors.ENDC}\n")
    
    def print_section(self, text: str):
        """Print formatted section header"""
        print(f"\n{Colors.BOLD}{Colors.CYAN}▶ {text}{Colors.ENDC}")
        print(f"{Colors.CYAN}{'-'*70}{Colors.ENDC}")
    
    def print_success(self, text: str):
        """Print success message"""
        print(f"{Colors.GREEN}✅ {text}{Colors.ENDC}")
    
    def print_info(self, text: str):
        """Print info message"""
        print(f"{Colors.BLUE}ℹ️  {text}{Colors.ENDC}")
    
    def print_warning(self, text: str):
        """Print warning message"""
        print(f"{Colors.YELLOW}⚠️  {text}{Colors.ENDC}")
    
    def get_togaf_phases(self) -> List[Dict]:
        """Get all TOGAF ADM phases with learning content"""
        return [
            {
                "id": "preliminary",
                "name": "Preliminary Phase",
                "description": "Framework & Principles - Anpassung von TOGAF an die Organisation",
                "key_concepts": [
                    "Architekturprinzipien definieren",
                    "Framework Tailoring",
                    "Stakeholder identifizieren",
                    "Tools auswählen"
                ],
                "deliverable": "Architecture Principles Document",
                "time_estimate": "60 Min"
            },
            {
                "id": "phase_a",
                "name": "Phase A: Architecture Vision",
                "description": "Business-Problem verstehen, Zielarchitektur skizzieren",
                "key_concepts": [
                    "Stakeholder Concerns erfassen",
                    "Business Scenarios erstellen",
                    "High-level Zielarchitektur (Ist → Soll)",
                    "Statement of Architecture Work"
                ],
                "deliverable": "Architecture Vision Document",
                "time_estimate": "90 Min"
            },
            {
                "id": "phase_b",
                "name": "Phase B: Business Architecture",
                "description": "Business-Prozesse und Capabilities modellieren",
                "key_concepts": [
                    "Business Capability Mapping",
                    "Value Streams",
                    "Business Process Modeling",
                    "Capability-based Planning"
                ],
                "deliverable": "Business Capability Map",
                "time_estimate": "90 Min"
            },
            {
                "id": "phase_c",
                "name": "Phase C: Information Systems Architecture",
                "description": "Daten- und Applikationsarchitektur entwickeln",
                "key_concepts": [
                    "Data Architecture (Logical & Physical Models)",
                    "Application Architecture",
                    "Integration Patterns",
                    "Data Flow Diagrams"
                ],
                "deliverable": "Application & Data Architecture Document",
                "time_estimate": "120 Min"
            },
            {
                "id": "phase_d",
                "name": "Phase D: Technology Architecture",
                "description": "IT-Infrastruktur und Plattformen definieren",
                "key_concepts": [
                    "Hardware & Network Architecture",
                    "Cloud vs. On-Premise",
                    "Security Architecture",
                    "Technology Standards"
                ],
                "deliverable": "Technology Architecture Document",
                "time_estimate": "90 Min"
            },
            {
                "id": "phase_e",
                "name": "Phase E: Opportunities & Solutions",
                "description": "Migrationsprojekte identifizieren, Work Packages definieren",
                "key_concepts": [
                    "Gap Analysis (Ist vs. Soll)",
                    "Transition Architectures",
                    "Work Packages konsolidieren",
                    "Implementation & Migration Strategy"
                ],
                "deliverable": "Implementation & Migration Plan",
                "time_estimate": "60 Min"
            },
            {
                "id": "phase_f",
                "name": "Phase F: Migration Planning",
                "description": "Detaillierte Implementierungs-Roadmap",
                "key_concepts": [
                    "Priorisierung (Business Value vs. Risk)",
                    "Abhängigkeiten analysieren",
                    "Kosten/Nutzen-Analyse",
                    "Architecture Roadmap"
                ],
                "deliverable": "Architecture Roadmap",
                "time_estimate": "60 Min"
            },
            {
                "id": "phase_g",
                "name": "Phase G: Implementation Governance",
                "description": "Sicherstellen, dass Implementierung der Architektur folgt",
                "key_concepts": [
                    "Architecture Compliance Reviews",
                    "Change Request Management",
                    "Architecture Contracts",
                    "Governance Framework"
                ],
                "deliverable": "Architecture Contract Template",
                "time_estimate": "60 Min"
            },
            {
                "id": "phase_h",
                "name": "Phase H: Architecture Change Management",
                "description": "Architektur kontinuierlich weiterentwickeln",
                "key_concepts": [
                    "Technology Monitoring",
                    "Change Request Evaluation",
                    "Lessons Learned",
                    "Continuous Improvement"
                ],
                "deliverable": "Change Management Process Document",
                "time_estimate": "60 Min"
            },
            {
                "id": "requirements",
                "name": "Requirements Management (zentral)",
                "description": "Anforderungen während aller Phasen managen",
                "key_concepts": [
                    "Requirements aufnehmen",
                    "Priorisierung",
                    "Traceability (Anforderung → Architektur)",
                    "Requirements Repository"
                ],
                "deliverable": "Requirements Traceability Matrix",
                "time_estimate": "60 Min"
            }
        ]
    
    def show_welcome(self):
        """Display welcome message and overview"""
        self.print_header("TOGAF EA Learning Agent")
        print(f"{Colors.BOLD}Willkommen zum TOGAF Learning Agent!{Colors.ENDC}")
        print("\nDieser interaktive Lernagent hilft dir, TOGAF (The Open Group Architecture Framework)")
        print("systematisch zu lernen - optimiert für AuDHD-Lernstile.")
        
        print(f"\n{Colors.BOLD}Lernprinzipien:{Colors.ENDC}")
        print("  ✅ Output > Input - Jede Session produziert ein Deliverable")
        print("  ✅ Zeitboxing - Feste Zeitblöcke (60-90 Min)")
        print("  ✅ Active Recall - Aktives Abrufen, nicht passives Wiederholen")
        print("  ✅ Visuell - Diagramme und strukturierte Darstellung")
        print("  ✅ Progress Tracking - Fortschritt wird gespeichert")
        
        if self.progress_data["sessions_completed"] > 0:
            self.print_info(f"Du hast bereits {self.progress_data['sessions_completed']} Session(s) abgeschlossen!")
            self.print_info(f"Letzte Session: {self.progress_data.get('last_session', 'N/A')}")
    
    def show_main_menu(self) -> str:
        """Display main menu and get user choice"""
        self.print_section("Hauptmenü")
        print("1. 📚 TOGAF ADM Phases lernen")
        print("2. 🧠 Active Recall Quiz")
        print("3. 📊 Fortschritt anzeigen")
        print("4. 🎯 Lernempfehlung erhalten")
        print("5. 📖 TOGAF Prinzipien & Building Blocks")
        print("6. ❓ Hilfe")
        print("7. 🚪 Beenden")
        
        choice = input(f"\n{Colors.BOLD}Wähle eine Option (1-7): {Colors.ENDC}").strip()
        return choice
    
    def show_phases_menu(self):
        """Display TOGAF phases and allow selection"""
        self.print_section("TOGAF ADM Phases")
        phases = self.get_togaf_phases()
        
        for i, phase in enumerate(phases, 1):
            status = "✅" if phase["id"] in self.progress_data["phases_learned"] else "⭕"
            print(f"{status} {i}. {phase['name']} ({phase['time_estimate']})")
            print(f"   {phase['description']}")
        
        print(f"\n0. Zurück zum Hauptmenü")
        
        choice = input(f"\n{Colors.BOLD}Wähle eine Phase (0-{len(phases)}): {Colors.ENDC}").strip()
        
        try:
            choice_num = int(choice)
            if choice_num == 0:
                return
            if 1 <= choice_num <= len(phases):
                self.learn_phase(phases[choice_num - 1])
            else:
                self.print_warning("Ungültige Auswahl!")
        except ValueError:
            self.print_warning("Bitte gib eine Zahl ein!")
    
    def learn_phase(self, phase: Dict):
        """Interactive learning session for a specific phase"""
        self.print_header(phase["name"])
        self.current_session["phase"] = phase["id"]
        
        print(f"{Colors.BOLD}Beschreibung:{Colors.ENDC}")
        print(f"  {phase['description']}")
        
        print(f"\n{Colors.BOLD}Zeitschätzung:{Colors.ENDC} {phase['time_estimate']}")
        print(f"{Colors.BOLD}Deliverable:{Colors.ENDC} {phase['deliverable']}")
        
        print(f"\n{Colors.BOLD}Key Concepts:{Colors.ENDC}")
        for i, concept in enumerate(phase["key_concepts"], 1):
            print(f"  {i}. {concept}")
        
        print(f"\n{Colors.YELLOW}💡 Tipp: Nutze Pomodoro-Technik (25 Min Arbeit, 5 Min Pause){Colors.ENDC}")
        
        input(f"\n{Colors.BOLD}Drücke Enter, um fortzufahren...{Colors.ENDC}")
        
        # Learning steps
        self.print_section("Lernschritte")
        print("Folge diesen Schritten für eine effektive Lernsession:")
        print()
        print("1️⃣  Input (20-30 Min)")
        print("    - Lies die TOGAF-Dokumentation zu dieser Phase")
        print("    - Schaue ein Tutorial-Video (falls verfügbar)")
        print("    - Notiere dir Unklarheiten")
        print()
        print("2️⃣  Verarbeitung (30-40 Min)")
        print(f"    - Erstelle dein Deliverable: {phase['deliverable']}")
        print("    - Zeichne ein Diagramm (Draw.io, Excalidraw)")
        print("    - Dokumentiere Key Concepts in eigenen Worten")
        print()
        print("3️⃣  Active Recall (10-15 Min)")
        print("    - Erkläre die Phase ohne Notizen")
        print("    - Beantworte Quiz-Fragen")
        print("    - Identifiziere Wissenslücken")
        
        input(f"\n{Colors.BOLD}Session abgeschlossen? Drücke Enter...{Colors.ENDC}")
        
        # Mark as completed
        if phase["id"] not in self.progress_data["phases_learned"]:
            self.progress_data["phases_learned"].append(phase["id"])
        
        # Deliverable confirmation
        deliverable = input(f"\n{Colors.BOLD}Hast du dein Deliverable erstellt? (j/n): {Colors.ENDC}").strip().lower()
        if deliverable == 'j':
            deliverable_path = input(f"{Colors.BOLD}Pfad zum Deliverable (optional): {Colors.ENDC}").strip()
            self.progress_data["deliverables"].append({
                "phase": phase["id"],
                "name": phase["deliverable"],
                "date": datetime.now().strftime("%Y-%m-%d"),
                "path": deliverable_path if deliverable_path else None
            })
            self.current_session["deliverable"] = phase["deliverable"]
            self.print_success(f"Deliverable '{phase['deliverable']}' gespeichert!")
        
        # Update session count
        self.progress_data["sessions_completed"] += 1
        self.progress_data["last_session"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.save_progress()
        
        # Quiz option
        quiz = input(f"\n{Colors.BOLD}Möchtest du ein Quiz zu dieser Phase machen? (j/n): {Colors.ENDC}").strip().lower()
        if quiz == 'j':
            self.run_quiz(phase)
    
    def run_quiz(self, phase: Dict):
        """Run an active recall quiz for the phase"""
        self.print_section(f"Quiz: {phase['name']}")
        
        # Phase-specific questions
        questions = self.get_quiz_questions(phase["id"])
        
        if not questions:
            self.print_warning("Keine Quiz-Fragen für diese Phase verfügbar.")
            return
        
        correct = 0
        total = len(questions)
        
        for i, q in enumerate(questions, 1):
            print(f"\n{Colors.BOLD}Frage {i}/{total}:{Colors.ENDC}")
            print(q["question"])
            print()
            
            for j, option in enumerate(q["options"], 1):
                print(f"  {j}. {option}")
            
            answer = input(f"\n{Colors.BOLD}Deine Antwort (1-{len(q['options'])}): {Colors.ENDC}").strip()
            
            try:
                answer_num = int(answer)
                if answer_num == q["correct"]:
                    self.print_success("Richtig! ✅")
                    if "explanation" in q:
                        print(f"{Colors.CYAN}💡 {q['explanation']}{Colors.ENDC}")
                    correct += 1
                else:
                    self.print_warning(f"Falsch! Die richtige Antwort ist: {q['options'][q['correct']-1]}")
                    if "explanation" in q:
                        print(f"{Colors.CYAN}💡 {q['explanation']}{Colors.ENDC}")
            except (ValueError, IndexError):
                self.print_warning("Ungültige Eingabe!")
        
        # Score calculation
        score = (correct / total) * 100
        print(f"\n{Colors.BOLD}{'='*70}{Colors.ENDC}")
        print(f"{Colors.BOLD}Ergebnis: {correct}/{total} richtig ({score:.1f}%){Colors.ENDC}")
        
        if score >= 80:
            self.print_success("Ausgezeichnet! Du hast die Phase gut verstanden! 🎉")
        elif score >= 60:
            self.print_info("Gut! Wiederhole die Konzepte noch einmal.")
        else:
            self.print_warning("Du solltest diese Phase nochmal durchgehen.")
        
        # Save quiz score
        self.progress_data["quiz_scores"][phase["id"]] = {
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "correct": correct,
            "total": total
        }
        self.save_progress()
    
    def get_quiz_questions(self, phase_id: str) -> List[Dict]:
        """Get quiz questions for a specific phase"""
        quiz_bank = {
            "preliminary": [
                {
                    "question": "Was ist das Hauptziel der Preliminary Phase?",
                    "options": [
                        "Eine detaillierte Technologie-Architektur erstellen",
                        "TOGAF an die Organisation anpassen und Prinzipien definieren",
                        "Business-Prozesse modellieren",
                        "Die Implementierung überwachen"
                    ],
                    "correct": 2,
                    "explanation": "Die Preliminary Phase dient der Anpassung des TOGAF-Frameworks an die spezifischen Bedürfnisse der Organisation."
                },
                {
                    "question": "Welches ist ein typisches Output der Preliminary Phase?",
                    "options": [
                        "Network Diagram",
                        "Architecture Principles",
                        "Business Process Model",
                        "Migration Plan"
                    ],
                    "correct": 2,
                    "explanation": "Architecture Principles werden in der Preliminary Phase definiert und bilden die Grundlage für alle Architekturentscheidungen."
                }
            ],
            "phase_a": [
                {
                    "question": "Was ist das Hauptziel von Phase A (Architecture Vision)?",
                    "options": [
                        "Detaillierte Netzwerkdiagramme erstellen",
                        "Business-Problem verstehen und Zielarchitektur skizzieren",
                        "Datenmodelle entwickeln",
                        "Code implementieren"
                    ],
                    "correct": 2,
                    "explanation": "Phase A fokussiert auf das Verständnis des Business-Problems und die Erstellung einer High-Level-Vision der Zielarchitektur."
                },
                {
                    "question": "Welches Dokument ist das wichtigste Output von Phase A?",
                    "options": [
                        "Technology Standards Catalog",
                        "Data Architecture Document",
                        "Architecture Vision Document",
                        "Implementation Plan"
                    ],
                    "correct": 3,
                    "explanation": "Das Architecture Vision Document beschreibt die Zielarchitektur auf hohem Level und dient als Grundlage für alle weiteren Phasen."
                }
            ],
            "phase_b": [
                {
                    "question": "Was wird in Phase B (Business Architecture) modelliert?",
                    "options": [
                        "Hardware und Netzwerk",
                        "Business-Prozesse und Capabilities",
                        "Datenbanktabellen",
                        "Cloud-Infrastruktur"
                    ],
                    "correct": 2,
                    "explanation": "Phase B fokussiert auf Business Capabilities, Value Streams und Business-Prozesse."
                }
            ],
            "phase_c": [
                {
                    "question": "Phase C besteht aus zwei Teilen. Welche sind das?",
                    "options": [
                        "Hardware und Software",
                        "Data Architecture und Application Architecture",
                        "Cloud und On-Premise",
                        "Frontend und Backend"
                    ],
                    "correct": 2,
                    "explanation": "Phase C besteht aus Data Architecture (C1) und Application Architecture (C2)."
                }
            ],
            "phase_d": [
                {
                    "question": "Was ist der Fokus von Phase D (Technology Architecture)?",
                    "options": [
                        "Business-Prozesse",
                        "IT-Infrastruktur und Plattformen",
                        "Datenmodelle",
                        "User Stories"
                    ],
                    "correct": 2,
                    "explanation": "Phase D definiert die technologische Infrastruktur, Plattformen und Standards."
                }
            ],
            "phase_e": [
                {
                    "question": "Was ist eine 'Transition Architecture' in Phase E?",
                    "options": [
                        "Die finale Zielarchitektur",
                        "Ein Zwischenschritt auf dem Weg zur Zielarchitektur",
                        "Eine alte Legacy-Architektur",
                        "Eine Cloud-Architektur"
                    ],
                    "correct": 2,
                    "explanation": "Transition Architectures sind Zwischenschritte, die den Weg von der Ist- zur Soll-Architektur aufzeigen."
                }
            ],
            "requirements": [
                {
                    "question": "Wann ist Requirements Management aktiv?",
                    "options": [
                        "Nur in Phase A",
                        "Nur am Anfang des ADM",
                        "Während aller ADM-Phasen (zentral)",
                        "Nur am Ende des ADM"
                    ],
                    "correct": 3,
                    "explanation": "Requirements Management ist eine zentrale Aktivität, die während aller ADM-Phasen läuft."
                }
            ]
        }
        
        return quiz_bank.get(phase_id, [])
    
    def show_progress(self):
        """Display learning progress"""
        self.print_section("Lernfortschritt")
        
        print(f"{Colors.BOLD}📊 Statistiken:{Colors.ENDC}")
        print(f"  Sessions abgeschlossen: {self.progress_data['sessions_completed']}")
        print(f"  Phases gelernt: {len(self.progress_data['phases_learned'])}/10")
        print(f"  Deliverables erstellt: {len(self.progress_data['deliverables'])}")
        
        if self.progress_data.get("last_session"):
            print(f"  Letzte Session: {self.progress_data['last_session']}")
        
        # Show learned phases
        if self.progress_data["phases_learned"]:
            print(f"\n{Colors.BOLD}✅ Abgeschlossene Phasen:{Colors.ENDC}")
            phases = self.get_togaf_phases()
            for phase_id in self.progress_data["phases_learned"]:
                phase = next((p for p in phases if p["id"] == phase_id), None)
                if phase:
                    print(f"  ✅ {phase['name']}")
        
        # Show deliverables
        if self.progress_data["deliverables"]:
            print(f"\n{Colors.BOLD}📦 Erstellte Deliverables:{Colors.ENDC}")
            for d in self.progress_data["deliverables"]:
                print(f"  📄 {d['name']} ({d['date']})")
                if d.get('path'):
                    print(f"     Pfad: {d['path']}")
        
        # Show quiz scores
        if self.progress_data.get("quiz_scores"):
            print(f"\n{Colors.BOLD}🎯 Quiz-Ergebnisse:{Colors.ENDC}")
            for phase_id, score_data in self.progress_data["quiz_scores"].items():
                phases = self.get_togaf_phases()
                phase = next((p for p in phases if p["id"] == phase_id), None)
                if phase:
                    score = score_data["score"]
                    color = Colors.GREEN if score >= 80 else Colors.YELLOW if score >= 60 else Colors.RED
                    print(f"  {color}{phase['name']}: {score:.1f}% ({score_data['correct']}/{score_data['total']}){Colors.ENDC}")
        
        # Calculate completion percentage
        total_phases = len(self.get_togaf_phases())
        completion = (len(self.progress_data["phases_learned"]) / total_phases) * 100
        
        print(f"\n{Colors.BOLD}Gesamtfortschritt: {completion:.1f}%{Colors.ENDC}")
        self.draw_progress_bar(completion)
    
    def draw_progress_bar(self, percentage: float):
        """Draw a simple progress bar"""
        bar_length = 50
        filled = int(bar_length * percentage / 100)
        bar = '█' * filled + '░' * (bar_length - filled)
        print(f"{Colors.GREEN}[{bar}] {percentage:.1f}%{Colors.ENDC}")
    
    def show_recommendation(self):
        """Show learning recommendation based on progress"""
        self.print_section("Lernempfehlung")
        
        phases = self.get_togaf_phases()
        learned = self.progress_data["phases_learned"]
        
        if len(learned) == 0:
            print("🎯 Empfehlung: Starte mit der Preliminary Phase!")
            print("   Dies ist die Grundlage für alle weiteren Phasen.")
            phase = phases[0]
            print(f"\n   {Colors.BOLD}{phase['name']}{Colors.ENDC}")
            print(f"   {phase['description']}")
            print(f"   Zeitschätzung: {phase['time_estimate']}")
        elif len(learned) < len(phases):
            next_phase = None
            for phase in phases:
                if phase["id"] not in learned:
                    next_phase = phase
                    break
            
            if next_phase:
                print(f"🎯 Nächste empfohlene Phase: {next_phase['name']}")
                print(f"   {next_phase['description']}")
                print(f"   Zeitschätzung: {next_phase['time_estimate']}")
            
            # Check quiz scores
            if self.progress_data.get("quiz_scores"):
                low_scores = [(phase_id, score) for phase_id, score in self.progress_data["quiz_scores"].items() 
                             if score["score"] < 70]
                if low_scores:
                    print(f"\n⚠️  Wiederholungsempfehlung:")
                    for phase_id, score_data in low_scores:
                        phase = next((p for p in phases if p["id"] == phase_id), None)
                        if phase:
                            print(f"   📚 {phase['name']} (Score: {score_data['score']:.1f}%)")
        else:
            self.print_success("Glückwunsch! Du hast alle TOGAF ADM Phasen abgeschlossen! 🎉")
            print("\n🎯 Nächste Schritte:")
            print("   1. Wiederhole Phasen mit niedrigen Quiz-Scores")
            print("   2. Erstelle ein vollständiges Beispiel-Projekt")
            print("   3. Bereite dich auf die TOGAF 10 Foundation Zertifizierung vor")
    
    def show_principles(self):
        """Show TOGAF principles and building blocks"""
        self.print_section("TOGAF Prinzipien & Building Blocks")
        
        print(f"\n{Colors.BOLD}Architecture Principles:{Colors.ENDC}")
        principles = [
            ("Business-driven", "IT folgt Business, nicht umgekehrt"),
            ("Simplicity", "Einfachheit über Komplexität"),
            ("Interoperability", "Systeme müssen miteinander kommunizieren"),
            ("Reusability", "Wiederverwendung von Komponenten"),
            ("Security by Design", "Security von Anfang an")
        ]
        
        for name, desc in principles:
            print(f"\n  📌 {Colors.BOLD}{name}{Colors.ENDC}")
            print(f"     {desc}")
        
        print(f"\n{Colors.BOLD}Architecture Building Blocks (ABB):{Colors.ENDC}")
        print("  ABB = Logische, wiederverwendbare Komponente")
        print("\n  Beispiele:")
        print("    • Identity Provider (ABB) → Keycloak, Auth0, Okta (SBB)")
        print("    • API Gateway (ABB) → Kong, Apigee, AWS API Gateway (SBB)")
        print("    • Message Queue (ABB) → RabbitMQ, Kafka, AWS SQS (SBB)")
        
        print(f"\n{Colors.BOLD}Enterprise Continuum:{Colors.ENDC}")
        print("  Foundation → Common Systems → Industry → Organization-Specific")
        print("  (Generisch)                                    (Spezifisch)")
    
    def show_help(self):
        """Show help information"""
        self.print_section("Hilfe")
        
        print(f"{Colors.BOLD}Über diesen Learning Agent:{Colors.ENDC}")
        print("  Dieser Agent hilft dir, TOGAF systematisch zu lernen.")
        print("  Er folgt AuDHD-optimierten Lernprinzipien:")
        print("    • Zeitboxing (Pomodoro)")
        print("    • Output-fokussiert (Deliverables)")
        print("    • Active Recall (Quiz)")
        print("    • Progress Tracking")
        
        print(f"\n{Colors.BOLD}Empfohlener Workflow:{Colors.ENDC}")
        print("  1. Wähle eine Phase aus dem Phasen-Menü")
        print("  2. Folge den Lernschritten (Input → Verarbeitung → Recall)")
        print("  3. Erstelle dein Deliverable (Diagramm, Dokument)")
        print("  4. Mache das Quiz zur Phase")
        print("  5. Wiederhole nach 3, 7 und 14 Tagen (Spacing)")
        
        print(f"\n{Colors.BOLD}Tipps:{Colors.ENDC}")
        print("  💡 Nutze Draw.io oder Excalidraw für Diagramme")
        print("  💡 Erstelle ein Portfolio-Repository auf GitHub")
        print("  💡 Dokumentiere jedes Deliverable im Repository")
        print("  💡 60-90 Min pro Session, nicht länger")
        print("  💡 Fokussiere auf eine Phase pro Woche")
        
        print(f"\n{Colors.BOLD}Ressourcen:{Colors.ENDC}")
        print("  📖 TOGAF Standard 10: https://www.opengroup.org/togaf")
        print("  📖 TOGAF Overview: 02_frameworks/togaf/togaf_overview.md")
        print("  📖 Learning Methods: 00_roadmap/learning_methods.md")
    
    def run(self):
        """Main application loop"""
        self.show_welcome()
        
        while True:
            choice = self.show_main_menu()
            
            if choice == '1':
                self.show_phases_menu()
            elif choice == '2':
                # Quiz for completed phases
                phases = [p for p in self.get_togaf_phases() 
                         if p["id"] in self.progress_data["phases_learned"]]
                if phases:
                    print("\n📚 Wähle eine Phase für das Quiz:")
                    for i, phase in enumerate(phases, 1):
                        print(f"{i}. {phase['name']}")
                    choice = input(f"\nWähle (1-{len(phases)}): ").strip()
                    try:
                        idx = int(choice) - 1
                        if 0 <= idx < len(phases):
                            self.run_quiz(phases[idx])
                    except ValueError:
                        pass
                else:
                    self.print_warning("Keine abgeschlossenen Phasen für Quiz verfügbar.")
            elif choice == '3':
                self.show_progress()
            elif choice == '4':
                self.show_recommendation()
            elif choice == '5':
                self.show_principles()
            elif choice == '6':
                self.show_help()
            elif choice == '7':
                self.print_success("Auf Wiedersehen! Viel Erfolg beim Lernen! 🚀")
                break
            else:
                self.print_warning("Ungültige Auswahl! Bitte wähle 1-7.")
            
            input(f"\n{Colors.CYAN}Drücke Enter um fortzufahren...{Colors.ENDC}")

def main():
    """Main entry point"""
    try:
        agent = TOGAFLearningAgent()
        agent.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Programm unterbrochen.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.RED}Fehler: {e}{Colors.ENDC}")
        sys.exit(1)

if __name__ == "__main__":
    main()
