# Architecture Decision Record: [Title]

**Status:** [Proposed | Accepted | Rejected | Deprecated | Superseded]  
**Date:** YYYY-MM-DD  
**Deciders:** [Names or roles]  
**Technical Story:** [Link to issue/ticket]

---

## Context

[Describe the context and problem statement. What is the situation that requires a decision? What are the constraints?]

**Example:**
> We need to select an identity provider for our application. Currently, we have no centralized authentication, and each service implements its own user management, leading to inconsistent security and poor user experience.

---

## Decision Drivers

[List the factors that influence the decision]

* [Driver 1: e.g., Security requirements]
* [Driver 2: e.g., Cost constraints]
* [Driver 3: e.g., Integration complexity]
* [Driver 4: e.g., Scalability needs]

---

## Considered Options

### Option 1: [Name of Option]

**Description:**  
[Brief description of the option]

**Pros:**
* ✅ [Advantage 1]
* ✅ [Advantage 2]

**Cons:**
* ❌ [Disadvantage 1]
* ❌ [Disadvantage 2]

**Cost:** [Estimated cost]

---

### Option 2: [Name of Option]

**Description:**  
[Brief description of the option]

**Pros:**
* ✅ [Advantage 1]
* ✅ [Advantage 2]

**Cons:**
* ❌ [Disadvantage 1]
* ❌ [Disadvantage 2]

**Cost:** [Estimated cost]

---

### Option 3: [Name of Option]

**Description:**  
[Brief description of the option]

**Pros:**
* ✅ [Advantage 1]
* ✅ [Advantage 2]

**Cons:**
* ❌ [Disadvantage 1]
* ❌ [Disadvantage 2]

**Cost:** [Estimated cost]

---

## Decision Outcome

**Chosen option:** [Name of chosen option]

**Justification:**  
[Explain why this option was chosen. Reference the decision drivers and how this option addresses them.]

**Example:**
> We chose Keycloak because it provides enterprise-grade security features, is open-source (reducing costs), and can be self-hosted (meeting our data sovereignty requirements). While it requires more initial setup than a SaaS solution like Auth0, it aligns with our long-term strategy of reducing vendor lock-in.

---

## Consequences

### Positive

* [Positive consequence 1]
* [Positive consequence 2]

### Negative

* [Negative consequence 1]
* [Negative consequence 2]

### Neutral

* [Neutral consequence 1]

---

## Implementation

[Describe the implementation approach, if relevant]

**Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Timeline:** [Estimated timeline]  
**Resources Required:** [Team members, budget, tools]

---

## Compliance

[If applicable, describe how this decision relates to compliance requirements]

* GDPR: [How this decision affects GDPR compliance]
* ISO 27001: [Relevant controls]
* Other: [Other relevant compliance frameworks]

---

## Alternatives Considered (Detailed)

[Optional: Provide more detailed analysis of alternatives if needed]

---

## Validation

[How will we validate that this decision was correct?]

**Success Metrics:**
* [Metric 1: e.g., Authentication response time < 200ms]
* [Metric 2: e.g., 99.9% uptime]
* [Metric 3: e.g., Zero security incidents in first 6 months]

**Review Date:** [When will this decision be reviewed?]

---

## References

* [Link to related documentation]
* [Link to technical resources]
* [Link to vendor documentation]

---

## Related Decisions

* [ADR-XXX: Related decision]
* [ADR-YYY: Supersedes this decision]

---

## Notes

[Any additional notes, discussions, or context that doesn't fit elsewhere]

---

*Template version: 1.0*  
*Last updated: February 2026*
