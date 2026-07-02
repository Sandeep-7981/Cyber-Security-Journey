# OSINT Process

## What is the OSINT Process?

The OSINT process is a structured approach to collecting, analyzing, and reporting publicly available information.

Instead of randomly searching for information, investigators follow a systematic workflow to ensure the collected intelligence is accurate, relevant, and legally obtained.

---

# OSINT Lifecycle

```text
Planning
    │
    ▼
Collection
    │
    ▼
Processing
    │
    ▼
Analysis
    │
    ▼
Reporting
```

---

# 1. Planning

Before collecting any information, clearly define the objective.

Questions to ask:

- What information am I looking for?
- Who or what is the target?
- Which public sources may contain useful data?
- What tools will I use?

Example:

Goal:
> Gather publicly available information about a company's web infrastructure.

---

# 2. Collection

This stage involves gathering data from publicly accessible sources.

Common sources include:

- Search engines
- Company websites
- Social media
- WHOIS records
- DNS records
- GitHub repositories
- News articles
- Public documents

The objective is to collect as much relevant information as possible without interacting with or attacking the target.

---

# 3. Processing

Raw information is often unorganized.

During processing:

- Remove duplicate data
- Organize information
- Verify accuracy
- Categorize findings

Example:

Instead of keeping multiple copies of the same email address, store only one verified entry.

---

# 4. Analysis

Collected information is examined to identify useful patterns and relationships.

Examples:

- Identifying company technologies
- Mapping employee relationships
- Detecting exposed services
- Finding publicly exposed credentials
- Identifying attack surfaces

Analysis transforms raw data into actionable intelligence.

---

# 5. Reporting

The final findings are documented in a clear and organized manner.

A good OSINT report should include:

- Objective
- Sources used
- Key findings
- Supporting evidence
- Recommendations (if applicable)

Reports should be factual and avoid assumptions.

---

# Passive vs Active OSINT

## Passive OSINT

Information is collected without interacting with the target.

Examples:

- Google searches
- WHOIS lookup
- DNS records
- Reading public GitHub repositories
- Viewing public social media profiles

Passive OSINT is generally safer and less likely to be detected.

---

## Active OSINT

Information is collected by directly interacting with the target.

Examples:

- Visiting a website
- Port scanning
- Sending emails
- Interacting with web applications

Active techniques may generate logs on the target's systems and should only be performed with proper authorization.

---

# Best Practices

- Clearly define the objective before starting.
- Use multiple sources to verify information.
- Organize findings systematically.
- Document every source.
- Respect legal and ethical boundaries.
- Avoid making assumptions without evidence.

---

# Key Takeaways

- OSINT is a structured intelligence gathering process.
- Planning improves efficiency.
- Analysis is more valuable than simply collecting large amounts of data.
- Always verify information using multiple public sources.
- Ethical and legal considerations should guide every investigation.