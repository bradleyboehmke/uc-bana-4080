# Quizzes

Student-facing reading quizzes, one per module. Each file has a short header
(module, chapters, points, time limit, attempts) followed by numbered questions
labelled by type: True/False, Multiple Choice, Multiple Select, or Fill in the Blank.

**These files contain no answers.** Answer keys live in `instructor/answer-keys/` as
`week-NN-quiz-key.md`, which is gitignored and never committed — the same split
BANA 7025 uses.

## Naming

`week-NN-quiz.md`, where NN is the week, which equals the module number.

## Present

| File | Module | Chapters | Points |
|------|--------|----------|--------|
| `week-01-quiz.md` | 1 — Getting Started | 1, 2, 3 | 14 |
| `week-02-quiz.md` | 2 — Python Data Science Ecosystem | 4, 5, 6 | 14 |
| `week-04-quiz.md` | 4 — Data Manipulation | 10, 11, 12 | 11 |
| `week-05-quiz.md` | 5 — Data Visualization & EDA | 13, 14, 15 | 14 |
| `week-06-quiz.md` | 6 — Creating Efficient Code | 16, 17, 18 | 15 |

Shared with BANA 7025 — modules 1–6 cover identical chapters in both courses, so
these transfer unchanged.

## Missing

- **Week 3** (Module 3 — DataFrames & Importing Data, chapters 7–9). No quiz exists
  in either repo.
- **Weeks 8–14.** The ML modules have no reading quizzes yet. The existing week 12
  and 13 quizzes in `instructor/quizzes/` include answers inline and would need
  splitting into a student file and a key before they could be published here.

## Answer key format

Keys mirror the quiz, marking correct options with ✅ and adding a one-clause note
on each wrong option explaining the misconception it targets. Fill in the Blank
entries give the expected answer plus one or two acceptable variations.
