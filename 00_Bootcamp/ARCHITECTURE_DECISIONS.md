# Architecture Decisions (ADR)

This document records important technical decisions made during Project Astra.

Each decision includes:

* Problem
* Options Considered
* Decision
* Reasoning
* Trade-offs
* Review Status

---

# ADR-001

## Title

Use GitHub as the single source of truth.

### Problem

We need one place to store code, documentation, notes, projects, and progress.

### Options Considered

* Local folders only
* Google Drive
* GitHub

### Decision

Use GitHub.

### Why

* Version control
* Portfolio
* Easy collaboration
* Daily commits
* Backup

### Trade-offs

Requires learning Git properly.

### Status

Accepted

---

# ADR-002

## Title

Build one enterprise project instead of many disconnected projects.

### Problem

Most tutorials create small projects that don't demonstrate real engineering ability.

### Options Considered

* Many mini projects
* One evolving enterprise project

### Decision

Build **AI Workspace** throughout the bootcamp.

### Why

* Demonstrates end-to-end engineering
* Strong GitHub portfolio
* Better interview discussions
* Real-world architecture

### Status

Accepted

---

# ADR-003

## Title

Understand first, framework second.

### Problem

Developers often memorize frameworks without understanding the problems they solve.

### Decision

Every new technology must be introduced by answering:

1. What problem does it solve?
2. Why was it created?
3. What alternatives exist?
4. What are its limitations?
5. When should it be used?
6. When should it not be used?

### Status

Accepted

---

# ADR-004

## Title

Documentation-first learning.

### Problem

Video courses often become outdated quickly.

### Decision

Official documentation is the primary learning source.

Videos are used only for reinforcement.

### Status

Accepted

---

# ADR-005

## Title

Daily Git commits.

### Problem

Learning progress should be visible and recoverable.

### Decision

Every study session ends with:

* Git add
* Git commit
* Git push

### Status

Accepted

---

# ADR-006

## Title

Build production-quality code from Day 1.

### Problem

Toy examples don't prepare engineers for real-world systems.

### Decision

Every project should follow professional engineering practices:

* Clean folder structure
* Type hints
* Logging
* Error handling
* Documentation
* Git history

### Status

Accepted

---

# Future ADRs

Future architectural decisions will include topics such as:

* uv vs Poetry
* FastAPI vs Flask
* LangGraph vs other orchestration frameworks
* Chroma vs Pinecone
* Azure AI Search vs Vector Database
* SQL vs NoSQL for memory
* Docker deployment strategy
* Authentication architecture
* Multi-agent orchestration
* Evaluation framework
