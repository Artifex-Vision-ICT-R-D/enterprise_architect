# Architecture Decision Record: Use Keycloak as Identity Provider

**Status:** Accepted  
**Date:** 2026-02-03  
**Deciders:** Enterprise Architecture Team, Security Team  
**Technical Story:** #EA-001 - Implement Centralized Authentication

---

## Context

Our organization currently lacks a centralized identity and access management (IAM) solution. Each application implements its own user authentication and authorization, leading to:

* Inconsistent security practices across applications
* Poor user experience (multiple login credentials)
* Difficult access control management
* Compliance challenges (GDPR, audit trails)
* High maintenance overhead

We need a centralized identity provider that:
* Supports modern authentication protocols (OAuth 2.0, OIDC, SAML)
* Provides multi-factor authentication (MFA)
* Can integrate with our existing applications
* Meets our data sovereignty requirements (EU)
* Is cost-effective

---

## Decision Drivers

* **Security:** Enterprise-grade security features, MFA, compliance
* **Cost:** Budget constraint of ~10,000 CHF/year
* **Data Sovereignty:** Must be self-hostable within EU
* **Integration:** Must support OIDC, SAML, LDAP
* **Vendor Lock-in:** Prefer open-source to avoid vendor lock-in
* **Scalability:** Must support 1,000+ users
* **User Experience:** SSO, modern login flows

---

## Considered Options

### Option 1: Keycloak (Open Source)

**Description:**  
Open-source identity and access management solution by Red Hat. Self-hosted, supports OIDC, OAuth 2.0, SAML.

**Pros:**
* ✅ Open-source (Apache 2.0 license)
* ✅ Self-hostable (meets data sovereignty)
* ✅ Enterprise-grade features (MFA, SSO, User Federation)
* ✅ Active community and Red Hat support
* ✅ Supports OIDC, OAuth 2.0, SAML, LDAP
* ✅ Cost: Infrastructure only (~2,000 CHF/year)

**Cons:**
* ❌ Requires infrastructure and maintenance
* ❌ Initial setup complexity
* ❌ Need internal expertise

**Cost:** ~2,000 CHF/year (infrastructure only)

---

### Option 2: Auth0 (SaaS)

**Description:**  
Cloud-based identity platform as a service.

**Pros:**
* ✅ Fully managed (no infrastructure)
* ✅ Easy to integrate
* ✅ Excellent documentation
* ✅ Modern UI/UX

**Cons:**
* ❌ Cost: ~15,000 CHF/year (1,000+ users)
* ❌ Data sovereignty concerns (US-based)
* ❌ Vendor lock-in
* ❌ Limited customization

**Cost:** ~15,000 CHF/year

---

### Option 3: Azure Active Directory (Azure AD)

**Description:**  
Microsoft's cloud-based identity and access management service.

**Pros:**
* ✅ Fully managed
* ✅ Strong integration with Microsoft ecosystem
* ✅ Enterprise support

**Cons:**
* ❌ Cost: ~12,000 CHF/year
* ❌ Vendor lock-in (Microsoft ecosystem)
* ❌ Limited if not using Microsoft stack
* ❌ Data sovereignty concerns

**Cost:** ~12,000 CHF/year

---

### Option 4: Custom Solution

**Description:**  
Build our own identity provider.

**Pros:**
* ✅ Full control
* ✅ Custom features

**Cons:**
* ❌ High development cost (~100,000 CHF)
* ❌ Ongoing maintenance burden
* ❌ Security risks (reinventing the wheel)
* ❌ Time to market (6+ months)

**Cost:** ~100,000 CHF initial + ongoing maintenance

---

## Decision Outcome

**Chosen option:** Keycloak (Option 1)

**Justification:**

We chose Keycloak because it best addresses our decision drivers:

1. **Cost-Effective:** Infrastructure-only cost (~2,000 CHF/year vs. 12,000-15,000 CHF for SaaS)
2. **Data Sovereignty:** Self-hosted in EU meets compliance requirements
3. **Security:** Enterprise-grade features (MFA, SSO, User Federation)
4. **Vendor Lock-in:** Open-source reduces dependency on single vendor
5. **Integration:** Supports all required protocols (OIDC, SAML, LDAP)
6. **Scalability:** Proven at enterprise scale

While Keycloak requires initial setup and ongoing maintenance, our DevOps team has the expertise, and the long-term cost savings justify the investment.

---

## Consequences

### Positive

* ✅ Centralized authentication across all applications
* ✅ Improved security posture (MFA, SSO)
* ✅ Better user experience (Single Sign-On)
* ✅ GDPR compliance (data sovereignty, audit trails)
* ✅ Cost savings (85% reduction vs. SaaS)
* ✅ Flexibility (open-source, customizable)

### Negative

* ❌ Infrastructure management overhead
* ❌ Initial setup complexity (~2-3 weeks)
* ❌ Need to train team on Keycloak administration
* ❌ High availability setup required (redundancy)

### Neutral

* Self-hosted means we control uptime and maintenance windows
* Need to establish backup and disaster recovery procedures

---

## Implementation

**Steps:**
1. **Week 1-2:** Infrastructure setup (Kubernetes, PostgreSQL)
2. **Week 2-3:** Keycloak installation and configuration
3. **Week 3-4:** Integrate first application (pilot)
4. **Week 5-8:** Migrate remaining applications
5. **Week 9:** User migration and training
6. **Week 10:** Go-live

**Timeline:** 10 weeks  
**Resources Required:**
* 1x DevOps Engineer (full-time, 6 weeks)
* 1x Security Engineer (part-time, 4 weeks)
* Infrastructure: Kubernetes cluster, PostgreSQL, Load Balancer

**Budget:**
* Infrastructure: 2,000 CHF/year
* Initial Setup: 15,000 CHF (labor)
* **Total First Year:** 17,000 CHF
* **Subsequent Years:** 2,000 CHF/year

---

## Compliance

* **GDPR:** Self-hosted in EU meets data sovereignty requirements. Audit logs enabled for access tracking.
* **ISO 27001:** Supports required controls (A.9.1, A.9.2, A.9.4) for access management.
* **MFA:** Enabled for all users, meets compliance requirements.

---

## Validation

**Success Metrics:**
* Authentication response time < 200ms (p95)
* 99.9% uptime
* Zero security incidents in first 6 months
* User satisfaction score > 4/5
* 100% application integration within 3 months

**Review Date:** 2026-08-01 (6 months post-implementation)

---

## References

* Keycloak Documentation: https://www.keycloak.org/documentation
* NIST SP 800-63B: Digital Identity Guidelines (Authentication)
* OWASP Authentication Cheat Sheet
* Internal Security Standards: SEC-001 (Identity & Access Management)

---

## Related Decisions

* ADR-002: Cloud Strategy (impacts hosting choice)
* ADR-003: Security Model (Keycloak is part of Zero Trust Architecture)

---

## Notes

* Keycloak was also selected for its active community and Red Hat backing, reducing risk of abandonment.
* We considered Okta as well, but pricing was similar to Auth0 (~15,000 CHF/year).
* Alternative: If Keycloak proves too complex, Auth0 remains a viable fallback (migration path exists via OIDC).

---

*ADR Version: 1.0*  
*Last updated: 2026-02-03*
