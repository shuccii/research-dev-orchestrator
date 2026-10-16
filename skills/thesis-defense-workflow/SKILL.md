---
name: thesis-defense-workflow
description: Prepare a graduate student for a master's thesis defense (final presentation and oral examination) in science or engineering, with NAIST-specific criteria when applicable - backward schedule, criteria-to-evidence mapping, slide and script checks, question bank, timed rehearsals and day-of checklist.
---

# Thesis Defense Workflow

Use when a student asks to prepare for a master's thesis defense, final presentation, oral examination or the rehearsal leading to it. The default target is a science/engineering master's program; for NAIST read [NAIST criteria](references/naist.md). For doctoral defenses, apply the same steps and add the doctoral items noted there. This workflow prepares drafts and practice. It never submits, uploads, registers or contacts faculty, and it never predicts a pass.

Use [research-review-workflow](../research-review-workflow/SKILL.md) for the substantive audit of claims and for interactive question rehearsal; this workflow decides what to prepare, when, and how to check that it is ready. For laboratory-specific rules (advisor sign-off, mandatory lab rehearsal, authorship, conference rules) use [lab-policy-workflow](../lab-policy-workflow/SKILL.md) and the user's local policy files; do not copy private rules into shared artifacts.

## 0. Fix the facts first

Collect, with source and date for each: defense date and time slot, talk length and Q&A length, format (in person/online, language), committee composition (advisor, sub-advisors, external), submission deadlines (thesis, abstract, slides), required templates, and the current institutional criteria. Read the institution's current official page or handbook; mark anything not found as `unconfirmed` and list it as a question for the advisor or office. Never fill a deadline or rule from memory or from another institution.

## 1. Backward schedule

Build the plan backward from the defense date. Typical anchors (adjust to the confirmed deadlines and the student's actual state):

| From the defense | Deliverable | Gate |
|---|---|---|
| about 8 weeks | One-sentence claim, objective → result → conclusion map, gap list (missing analyses, figures, citations) | Advisor agrees on scope; no new research directions after this point unless the advisor asks |
| about 6 weeks | Full thesis draft with all figures traceable to data/code/conditions | Advisor review requested |
| about 4 weeks | Abstract (if required) and slide draft v1; question bank v1 | Advisor review of abstract before any submission |
| about 3 weeks | Rehearsal 1 (timed, recorded) and issue log | Every issue has an owner and a done condition |
| about 2 weeks | Slides v2, script, backup slides; rehearsal 2 in front of the lab or peers | Timing within limits; major issues closed |
| about 1 week | Final thesis and slides for submission; Q&A drill | Advisor approval recorded by the user; the agent only prepares files |
| day before | Day-of checklist; one full timed run | No content changes except fixing errors |

Keep a single issue log: ID, source (rehearsal, advisor, self-review), affected slide/page, severity, fix, done condition, status. Report open items honestly; do not mark an item done without inspecting the changed artifact.

## 2. Story and criteria

1. Write the one-sentence claim: "To solve [problem], this work did [approach] and showed [result], which means [contribution] within [scope]."
2. Map each objective to the result that answers it and the conclusion drawn. An objective with no result is either removed, reworded, or presented as future work. A conclusion stronger than its evidence is reworded (watch verbs such as developed, established, proved, clarified).
3. Separate the problem (what blocks progress) from the task (what this work does to address it), and state the general problem, the usual approaches and what is specific to this work.
4. Build a criteria table: each institutional criterion → where the thesis and the talk show it (chapter/page, slide number) → remaining gap. Use [NAIST criteria](references/naist.md) for NAIST.

## 3. Slides and script

Check with [presentation and Q&A guide](references/presentation-and-qa.md). Minimum checks: time budget (at most about one slide per minute), one message per slide, each figure's axes, units and data conditions explained, claims and figures traceable to the thesis, a closing slide with conclusions rather than a list of activities, and backup slides for predictable deep questions. Timing is measured in a rehearsal, not estimated from word counts alone.

## 4. Question bank and answers

Generate questions anchored to the actual thesis, slides and known weak points, using the categories in the guide (fundamentals, choices, validity, limits, contribution, non-specialist, ethics/data, future work). For each: why it may be asked, the evidence needed, a 30-second answer outline (conclusion → evidence → limitation → next step), the likely follow-up, and the honest boundary of what can be claimed. Rehearse interactively with research-review-workflow in `defense` mode, one question at a time. Never invent results to make an answer stronger.

## 5. Rehearsals

Each rehearsal records: date, audience, measured time per section, questions asked, answers that failed (and why), and the issues opened. The next version must show which issues were closed and how. At least one rehearsal should be with people outside the student's subtopic. If the program or lab requires a rehearsal before the defense, record it as a gate that only the user can confirm.

## 6. Day-of and after

Day-of checklist: file formats and a backup copy, adapter and display test, timer, water, printed notes for Q&A, the issue log's top three answers. After the defense: log the committee's comments, plan required thesis revisions with deadlines, and archive data, code and figures as required by the institution and lab.

## Verification and boundaries

Before declaring a phase complete, open the actual artifacts and check each deliverable in the schedule against its done condition. Report: confirmed facts with sources, unconfirmed rules, open issues by severity, measured rehearsal times, and what still needs the advisor. Submissions, uploads, registration, e-mails to faculty and posting rehearsal recordings require the user's explicit action. AI feedback is practice, not faculty assessment or a degree decision.
