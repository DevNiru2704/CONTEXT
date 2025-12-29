# CONTEXT

**CONTEXT** is an experimental programming language designed to make programs easier to understand, reason about, and evolve with the help of AI systems. It focuses on clarity of intent, explicit structure, and predictable execution rather than clever syntax or implicit behavior.

> **CONTEXT** — *Context-aware Notation for Transparent Execution and Explainable Thought*

This project is educational, research-oriented, and intentionally built step by step with full documentation at every stage.

---

## Project Goals

- Learn how programming languages work from first principles
- Design a language that is friendly to AI-assisted coding and reasoning
- Prioritize explicit intent, low ambiguity, and explainability
- Maintain clear documentation for every design and implementation decision
- Build everything incrementally, starting from a minimal interpreter

This project values understanding over speed and correctness over complexity.

---

## Philosophy

Traditional programming languages are optimized mainly for human authors and machine execution. CONTEXT explores a different balance:

- Programs should clearly express **what** they intend to do, not just **how**
- Language constructs should be predictable and structurally explicit
- Code should be easy to analyze, explain, and transform by AI systems
- Hidden behavior, magic defaults, and ambiguous syntax are avoided

CONTEXT treats programs as structured reasoning artifacts, not just instructions.

---

## Current Status

This project is in its **early learning and design phase**.

Planned progression:
1. Minimal interpreter that reads and executes simple commands
2. Clear lexer and parser stages
3. Explicit execution model
4. Gradual introduction of variables, expressions, and control flow
5. Early support for intent and reasoning-oriented constructs

Nothing is rushed. Every step is documented.

---

## Project Structure (Planned)

```
context/
├── README.md
├── docs/
│   ├── design/
│   ├── interpreter/
│   └── language-spec/
├── src/
│   ├── lexer/
│   ├── parser/
│   ├── interpreter/
│   └── runtime/
└── examples/
```

The structure may evolve as understanding deepens.

---

## Documentation Approach

Documentation is a core feature of this project, not an afterthought.

For each step, the documentation will include:
- What is being built
- Why it is needed
- How it works internally
- Trade-offs and alternatives considered
- Lessons learned

The goal is that a student reading the docs can reproduce the entire project from scratch.

---

## Intended Audience

- Students learning how programming languages work
- Developers curious about language design
- Anyone interested in AI-assisted programming tools
- Learners who value clarity and fundamentals over shortcuts

No prior compiler theory knowledge is assumed.

---

## Non-Goals (For Now)

- High performance
- Production readiness
- Full compiler toolchains
- Complex optimizations
- Industry compliance

Those come later, if at all.

---

## License

This project will use a permissive open-source license (to be decided).

---

## Closing Note

CONTEXT is not about building the next popular language.

It is about learning deeply, thinking clearly, and understanding how humans and machines can share meaning through code.
