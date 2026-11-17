---
name: tailored-jasoseo
description: Use when the user wants a company-specific self-introduction, jasoseo, cover letter, or application essay based on their own past applications, resume, portfolio, interview notes, or personal records, or wants to collect and archive their application essays as Markdown. Uses Obsidian as the long-term knowledge base, NotebookLM as the writing-rules research layer, maps role requirements to evidence, and drafts tailored answers without inventing facts.
---

# Tailored Jasoseo

## Shared Package and Private Data

This package contains workflow instructions, blank templates, and two generic local helpers. It contains no candidate profile, personal essays, past feedback, login records, external example corpus, or Git history from a private source repository.

- Choose a private data directory outside this repository using the user's existing Obsidian vault, explicit materials folder, or a local `private-data/` folder excluded from Git. `$DATA_DIR` below means that directory; it is a path placeholder, not a preconfigured account or environment variable.
- Copy only the needed blank files from `assets/templates/` into that private directory. All `$DATA_DIR/` paths below are private data, never bundled personal references. Resolve relative source pointers from the private data location.
- Read local project instructions and the current user's experience priorities before choosing stories. Do not inherit another person's role, facts, or preferences.
- Persist personal facts, feedback, and outcomes only when the user has authorized that storage. Otherwise keep working notes within the current task. Do not write personal data back into the installed skill or this public repository.
- Obsidian, NotebookLM, `humanize-korean`, and document-rendering tools are optional integrations. Use available local/manual alternatives and accurately report missing integrations. Do not upload private materials to an external service without user authorization.
- The bundled helpers are `scripts/count_jasoseo_sections.py` and `scripts/export_jasoseo_docx.py`. Research discovery, project synchronization, example ranking, and comparative QC use manual fallbacks in this shared edition.

## Overview

Use this skill to write application answers that sound specific to the target company and role while staying faithful to the user's real history.

This skill is optimized for Korean-style jasoseo workflows, but it also works for cover letters, motivation statements, and role-specific short essays.

For the final Korean QA pass, use the separately installed `humanize-korean` skill when available. Treat it as a conservative, style-only humanization layer: it may remove translationese and recurring AI phrasing, but it must never replace evidence selection, content revision, or fact verification.

The preferred system has four inputs:

1. The user's experience and facts
2. Jasoseo writing rules learned from research
3. Verified strong reference essays stored raw-first with light analysis
4. The target company and role

Use Obsidian for long-term storage and organization. Use NotebookLM to learn and refresh writing guidance from videos, webpages, and other sources.

When the user wants a final document deliverable, use an available document/DOCX workflow. Only run a bundled export script when that script exists in this skill folder.

Path rules:

- Resolve this skill folder from the loaded `SKILL.md` path; shell examples below refer to it as `$SKILL_DIR`.
- Do not use hardcoded user paths from another machine. Discover user materials under `$USERPROFILE`, `$HOME`, the current workspace, or explicit paths the user provides.
- If a referenced `scripts/` helper or `$DATA_DIR/` file is missing, skip that helper and do the equivalent manual read/write or report the missing package file as a gap.

Execution reporting:

- Distinguish the loaded skill guidance, the source materials inspected, and any unavailable optional package assets before claiming the workflow was completed.
- If `$DATA_DIR/` or `scripts/` are missing, say that `tailored-jasoseo` was used with manual fallbacks; do not say the full reference/example/script workflow ran.
- When the user asks whether the skill was used, answer with the concrete substeps that ran and the substeps that were skipped.

## When to Use

Trigger this skill when the user asks for any of the following:

- A company-specific jasoseo or self-introduction
- A role-specific application answer or cover letter
- Rewriting an old application for a new company or role
- Collecting and archiving the user's existing application essays as Markdown
- Building a reusable profile from past applications and personal materials
- Extracting recurring strengths, stories, and motivations from prior documents
- Curating a company target list, application tracker, or completed-application history for jasoseo planning

Typical requests:

- "Write a Samsung DS process engineering jasoseo from my past materials."
- "Learn my previous applications and rewrite this answer for a strategy role."
- "Use my resume and old essays to draft a company-fit self-introduction."
- "Update my story bank, then answer these 4 application questions."

## Core Rules

- Truth beats polish. Never invent projects, metrics, awards, titles, timelines, or technologies.
- Reuse evidence, not wording. The output should feel tailored, not copied.
- Prefer concrete examples over abstract praise.
- Answer the prompt directly in the first 1 to 2 sentences.
- Build one clear evaluator takeaway for the whole application set and reinforce it across answers from different angles.
- When formatting allows, use a short noun-phrase subtitle or headline that makes the core takeaway visible at a glance. If the form looks conservative, make the first sentence do the same job instead.
- In one-shot mode, optimize for draft quality rather than conversational lightness: ask the full high-impact intake batch once, then draft all answers in one pass.
- If required facts are missing and the gap would create a misleading answer, ask a short clarifying question.
- When the user provides application questions and asks for a plan, do not jump straight into an outline. First ask the minimum missing questions needed to choose the right angle, story, and emphasis.
- Treat the user's edits, accept/reject feedback, and "this sounds like me / not like me" reactions as high-signal personalization data.
- Separate one-off target constraints from durable personal preferences. Keep one-off instructions in the application brief and durable preferences in persistent reference files.

## Preferred Knowledge Base

Prefer these Obsidian notes when they exist under the user's `Jasoseo/` vault tree:

- `01-My-Experience/Candidate Profile.md`
- `01-My-Experience/Interview Core Narrative Q&A.md`
- `01-My-Experience/Project Registry.md`
- `02-Writing-Rules/Korean Jasoseo Rules.md`
- `02-Writing-Rules/Writing Frameworks.md`
- `03-Reference-Examples/Example Bank.md`
- `03-Reference-Examples/Examples/`
- `04-Targets/Application Brief Template.md`

Prefer these research-project outputs when they exist and match the current drafting need:

- `Jasoseo/**/Research/**/00-Project Brief.md`
- `Jasoseo/**/Research/**/03-Syntheses/Theme Map.md`
- `Jasoseo/**/Research/**/04-Handoffs/Rulebook Handoff.md`
- `Jasoseo/**/Research/**/04-Handoffs/Draft Handoff.md`

Prefer these local fallback references when Obsidian is sparse or unavailable:

- `$DATA_DIR/example-bank.md`
- `$DATA_DIR/example-cache/`

Prefer the user-designated writing-research notebook in NotebookLM when the user wants writing-rule research, synthesis across sources, or refreshed guidance from videos and articles.

Discover recent research packs from the user's private notes; no research-discovery helper is bundled.

## Workflow

### 0. Collect and Archive Application Essays as Markdown

Use this step when the user requests collection or archiving. For an archive-only request, stop after archiving and reporting coverage; skip drafting, research, humanization, and DOCX export.

- Use the user's specified archive location. Otherwise reuse or create `자소서_보관함/` in the current project root; prefer an existing archive over creating parallel copies in Obsidian.
- Search the requested source folders for the user's essays, including existing Markdown, text, document, PDF, and consolidated application files. Use appropriate readers for the formats found. Searching chat history or external services is only needed when those sources are within the requested scope. List unreadable or missing sources instead of claiming complete collection.
- Preserve source files in place. Extract full question and answer bodies without rewriting, correcting, summarizing, or humanizing them. Separate commentary and verification notes from the essay body. Mark unreadable text or uncertain extraction explicitly; do not reconstruct missing answers.
- Store one Markdown file per company, role, application cycle, and distinct version, such as `기업_직무_2026하반기_초안_v1.md`. Use `미확인` for unknown metadata; do not infer writing dates from file modification times.
- Each record includes company, role, cycle, writing date if known, collection date, version status, submission status and evidence, original source paths or links, question text, stated length limits if available, and answer bodies. Reuse the archive's `01_보관양식.md` when present, or use this field set directly.
- Keep draft/final version status separate from submission status. Mark a version as final only with explicit source or user support, and submission as confirmed only with site evidence, an official receipt, or explicit user confirmation. A filename or consolidated heading alone does not establish either status.
- Skip identical question-and-answer sets already archived, adding any new source pointers to the existing record. Preserve different versions separately; never overwrite a submitted version with a later draft. If a consolidated source contains several applications, split only where the boundaries are clear and retain the source section pointer.
- Maintain `00_목록.md` with a relative link to each record and its company, role, cycle, version, submission status, and source. Keep unprocessed sources and extraction gaps visible. These user essays belong to candidate materials, not the external `Example Bank`.
- Before reporting completion, compare archived questions, answer bodies, and record counts against the processed sources, and verify index links. Report actual archived counts, skipped duplicates, and unresolved sources separately.

After a later drafting session finalizes an application set, archive the finalized text here as Markdown and update the index. DOCX export remains an additional deliverable when requested; it does not replace the Markdown archive.

### 1. Build or Refresh Candidate Memory

Start by checking both the Obsidian vault notes and these canonical references:

- `$DATA_DIR/candidate-profile.md`
- `$DATA_DIR/project-registry.md`
- `$DATA_DIR/story-bank.md`
- `$DATA_DIR/style-guide.md`
- `$DATA_DIR/personalization-memory.md`
- `$DATA_DIR/revision-memory.md`
- `$DATA_DIR/application-outcomes.md`
- `$DATA_DIR/source-log.md`

If they are incomplete or stale, refresh them from the user's materials such as:

- Resume or CV
- Past jasoseo or cover letters
- Portfolio descriptions
- Interview prep notes
- Project summaries
- Obsidian notes, if the user keeps materials there
- User-edited draft versions and direct feedback comments
- interview-style Q&A or spoken answers from live conversations

Priority rule for self-description:

- When `Interview Core Narrative Q&A.md` exists, treat it as a high-priority source for motivation, growth, values, contribution philosophy, authentic phrasing, and interview-safe self-positioning.
- If `Candidate Profile.md` and `Interview Core Narrative Q&A.md` differ in emphasis, prefer the newer interview-Q&A note for self-description and the candidate profile for verified facts.

Important separation:

- The user's own past application files belong in candidate memory, story extraction, and the application materials registry
- `Example Bank` is only for verified strong examples such as accepted cases or clearly high-quality reference samples

If project evidence matters for the answer:

1. Read `Project Registry.md` first for project selection
2. Re-open the live project folder or GitHub repo before describing technical details
3. Prefer current README, QUICKSTART, docs, results, and recent git history over stale summaries
4. Do not store long frozen technical explanations if the repository itself is available

Refresh the private project registry from current project files; no registry-synchronization helper is bundled.

When ingesting new materials:

1. Extract only facts supported by the source.
2. Normalize repeated content into the canonical reference files.
3. Keep the best stories in `story-bank.md`.
4. Add the source file and what it contributed to `source-log.md`.

When ingesting user edits or feedback from a drafting session:

1. Store target-specific instructions in the active application brief.
2. Store accepted and rejected phrasing patterns in `$DATA_DIR/revision-memory.md`.
3. Promote only repeated or explicit long-term preferences into `$DATA_DIR/personalization-memory.md`.
4. Update `$DATA_DIR/style-guide.md` only when the learning is clearly about durable voice, tone, or rhythm.

When the user answers interview-style questions in chat:

1. distill the answer into reusable motivation, values, and self-positioning notes
2. add new reusable episodes to `story-bank.md` when they are concrete enough
3. update `candidate-profile.md` when the answer clarifies durable drivers or strengths
4. keep the raw or polished Q&A note in Obsidian when it will help future interview and jasoseo drafting

### 2. Refresh Writing Rules and Example Knowledge

Before relying only on the static rules notes, check for a fresher research pack when the user has recently run `research-automation` or when a topic-specific rule refresh would help.

Research-pack priority:

1. matching `Rulebook Handoff.md`
2. matching `Draft Handoff.md`
3. matching `Theme Map.md`
4. then the stable notes `Korean Jasoseo Rules.md` and `Writing Frameworks.md`

Use the research pack for:

- newly learned prompt playbooks
- current anti-patterns
- benchmark comparisons against an active draft
- company- or prompt-specific synthesis that is too fresh to have been merged into the long-term rules notes yet

When the user wants the skill to "learn how to write" better, use NotebookLM research to synthesize:

- Common evaluation criteria in Korean jasoseo prompts
- Patterns that make answers feel role-specific rather than generic
- Prompt-type playbooks such as motivation, growth, collaboration, and problem solving
- Weak patterns to avoid
- Structure patterns found in strong examples

Store durable outputs in Obsidian under the `Jasoseo/` tree so future drafting can reuse them without redoing the same research every time.

When learning from strong examples:

1. Open the catalog note `Example Bank.md` first.
2. Prefer the raw example files under `03-Reference-Examples/Examples/` over summary-only notes.
3. By default, keep the user's own application files out of the example corpus.
4. Only index examples whose essay bodies are directly extractable from the trusted external source package unless the user explicitly asks for another rule.

### 3. Build the Target Brief

Before drafting, capture:

- Company
- Role
- Team or function if known
- Job description or responsibilities
- Application questions
- Character or word limits
- Desired tone, if the user gave one

Use `$DATA_DIR/application-brief-template.md` as the working structure.

### 3A. Maintain Target and Application Trackers

When the user asks to curate application targets or status lists, preserve completed applications in a separate history table instead of deleting them from the workspace. Interpret "remove applied companies" as removing them from the active remaining-target list unless the user explicitly asks to erase history.

Status evidence rules:

- Label each completed application by evidence type: site/my-page status, official receipt or submission email, or explicit user confirmation.
- Do not infer submission from a deadline, draft file, saved answer, or stale local note.
- If Gmail or another mailbox is available and the user asks for confirmation, search both company names and generic application terms such as `지원`, `접수`, and `제출`.
- Treat "mail not found" as a partial evidence result, not proof of non-application.
- Keep public-sector exclusions, internship exclusions, and other filters scoped to the list the user requested; preserve already completed history unless told otherwise.

If the user gives only a company and role, draft from that. If a job posting or exact questions are available, prefer those over generic assumptions.

Length rule:

- When a character or word limit is given, target at least 90% of the allowed length unless doing so would force fluff or unsupported claims
- If the draft is materially shorter than 90%, expand by adding better evidence, sharper reasoning, or clearer fit logic
- Do not pad with generic praise or repeated points just to fill space

### 3A. Detect Samsung Enhancement Mode

When the target company is Samsung or Samsung Electronics, do not split into a separate Samsung-only skill. Instead, activate a Samsung enhancement mode inside this workflow.

Turn on Samsung enhancement mode when both are true:

- the company is Samsung group or Samsung Electronics
- the prompt set matches one or more recurring Samsung question families such as support motivation, growth story, social issue, or role competency

What Samsung enhancement mode changes:

- prefer exact Samsung examples before broader industry examples
- map each prompt to a Samsung question family early
- use stronger question-specific playbooks before drafting
- apply Samsung-focused benchmark and QC checks before returning

Recurring Samsung question-family playbooks:

- `Q1 지원동기`
  - answer `why Samsung + why this role/problem` immediately
  - connect Samsung's manufacturing or business problem to the user's long-term direction
  - end with a concrete post-entry growth or contribution direction
- `Q2 성장과정`
  - center on one turning-point episode
  - show what changed in working style, judgment, or contribution method
  - land on the current work method, not on emotion alone
- `Q3 사회이슈`
  - define one issue clearly in the first lines
  - explain why it matters to Samsung's industry, manufacturing reality, or operating environment
  - show the user's own view or priority, not just a summary of the issue
- `Q4 직무경험`
  - translate the user's experience into the target role's operating logic
  - foreground why the story proves fit instead of merely listing projects
  - for adjacent domains, bridge through shared system structure and operating problems, never through defensive mismatch framing

### 4. Run the Planning Intake Questions

If the user gives one or more application questions and wants a plan, strategy, outline, or one-shot final draft, pause here before mapping stories or drafting prose.

Goal:

- learn what the user actually wants the reviewer to remember
- avoid choosing the wrong story just because it looks strong on paper
- capture preferences that are usually missing from resumes, old essays, or project summaries

Question rules:

- Ask only for missing information.
- Ask in one concise batch instead of a long back-and-forth when possible.
- Prefer 3 to 5 questions total.
- Ask in Korean by default when the application and user context are Korean.
- If the user already answered a category in their materials, do not ask it again.
- If the user is unsure, proceed with a best-effort assumption and label that assumption in the plan.

One-shot mode rule:

- If the user wants a one-shot result, do not optimize for the fewest questions.
- Ask one complete intake batch that covers all high-impact unknowns before drafting.
- It is acceptable to exceed the usual 3 to 5 questions if doing so prevents a weak one-shot draft.
- After the intake is complete, proceed directly to mapping and full drafting unless the user explicitly asked for a plan only.

Must-ask categories for planning:

- What impression should each answer leave with the reviewer?
- Which experience or project does the user most want to use, and which one should be avoided?
- What is the real motivation for this company or role beyond generic fit language?
- Are there any constraints such as tone, repeated-story avoidance, taboo phrases, or facts that need extra caution?
- Has the user already drafted bullet points, keywords, or a rough direction worth preserving?

One-shot minimum intake checklist:

- desired reviewer impression for each question
- must-use and must-avoid stories
- the real support motivation beyond generic fit language
- taboo phrases, tone constraints, or required inclusions
- any existing bullets, keywords, or prior draft pieces that should survive

Suggested Korean question set:

- `이 문항에서 평가자에게 가장 남기고 싶은 인상은 무엇인가요?`
- `반드시 쓰고 싶은 경험과 피하고 싶은 경험이 있나요?`
- `이 회사/직무를 지원하는 실제 이유를 한두 줄로 말하면 무엇인가요?`
- `톤, 글자 수, 반드시 포함할 내용, 피하고 싶은 표현이 있나요?`
- `이미 생각해둔 키워드나 대략적인 흐름이 있나요?`

If the user asks only for a plan, return a question-by-question planning sheet after this intake and stop before full drafting unless they ask for prose.

Planning sheet format:

- prompt
- hidden evaluation target
- intended reviewer impression
- recommended core story
- framework choice
- opening thesis direction
- evidence to emphasize
- company / role fit angle
- missing facts or assumptions

### 5. Map Requirements to Evidence

For each question or section:

1. Identify the hidden evaluation target.
2. Choose 1 to 2 stories from `story-bank.md` that best match it.
3. Pull specific proof points from `candidate-profile.md`.
4. Avoid repeating the exact same story across multiple answers unless the user requests a single-story framing.
5. Use the user's planning-intake answers to refine story choice, emphasis, and angle before locking the plan.
6. Decide the application-level identity line or reviewer takeaway that should survive all four answers.
7. In Samsung enhancement mode, assign each answer to the relevant Samsung question-family playbook before drafting.
8. Re-open `Interview Core Narrative Q&A.md` for motivation, growth, and personal-values prompts before locking the final angle.

Good mapping examples:

- Motivation question -> values, company fit, long-term direction
- Problem-solving question -> project obstacle, action, measurable result
- Collaboration question -> cross-functional work, conflict handling, communication style
- Growth question -> feedback loop, reflection, skill development

### 6. Retrieve Comparable Examples

Before drafting, load 2 to 3 matched examples when available.

Default benchmark source set:

1. `Example Bank.md` as the corpus-level benchmark source
2. 2 to 3 matched raw examples
3. the current draft or target draft note itself

Treat `Example Bank.md` as the default whole-corpus comparison source, not as an optional extra.

Retrieval order:

1. exact company + prompt type
2. same industry + prompt type
3. same prompt type only

Use the example corpus in this order:

1. raw-text examples first
2. pending link pools only to know what should be hydrated later

Rules:

- If raw essay text is unavailable, use the example only for structure, sequencing, and quality comparison.
- Never imitate distinctive wording from the `Do Not Copy` section.
- The goal is structural benchmarking, not stylistic cloning.

Before drafting prose, write a short internal benchmark note from the retrieved examples:

- communalities across accepted answers
- the strongest opening move they use
- how this candidate should differentiate instead of blending in
- 1 to 2 structure patterns worth borrowing
- phrases, sentence sequences, or headline styles that should not be copied

In Samsung enhancement mode, prepare that benchmark note question by question rather than only once for the whole set.

For each Samsung answer, the benchmark note should capture:

- what accepted answers for this exact question tend to do first
- what they all have in common
- how this candidate should differentiate
- one structure move that is safe to borrow
- one phrase family or sequence that must not be copied

When retrieval quality matters, manually rank available private examples. Prefer:

1. exact company + prompt type + raw-text + high trust
2. same company + prompt type
3. same prompt type + similar role family + similar character band

Prepare the comparative-QC source set from available private examples and the current draft. If no examples are available, report that limitation and use the evidence-and-prompt checklist.

### 7. Choose the Right Writing Framework

Use the framework that matches the hidden evaluation target:

- `KKK` for support motivation, company fit, role fit, and thesis-first answers
- `STAR` for problem solving, achievement, collaboration, and competency proof
- `STAR-T` for failure, recovery, reflection, and growth-based prompts

Framework meanings:

- `STAR` = Situation, Task, Action, Result
- `STAR-T` = Situation, Task, Action, Result, Takeaway
- `KKK` = core point first, key evidence next, key contribution last

Default selection rules:

- If the prompt asks "why this company" or "why this role" -> start with `KKK`
- If the prompt asks for a specific episode -> use `STAR`
- If the prompt asks what you learned, changed, or realized -> use `STAR-T`

### 8. Draft the Answer

Write with this default structure unless the prompt demands another format:

1. Direct answer or thesis
2. Evidence from a specific story
3. Outcome and learning
4. Why that matters for this company and role

Samsung one-shot draft contract:

1. intake locked
2. evidence map locked
3. question-specific benchmark note prepared
4. all Samsung answers drafted in one pass
5. comparative QC run immediately
6. any failing answer rewritten before return

Writing guidelines:

- Use natural, confident language
- Keep claims grounded in evidence
- Replace vague adjectives with actions and outcomes
- Adapt sentence density to the limit
- Write in Korean when the application is Korean unless the user asks otherwise
- Use short paragraphs for scan-ability
- Use a subtitle only when the application format allows it and the answer is long enough to benefit
- If formatting looks constrained or conservative, omit subtitles and let the first sentence carry the thesis
- If a subtitle is used, prefer a short noun phrase over a full sentence
- For longer answers around 1200 to 1500 characters, prefer up to two noun-phrase subtitles when they improve scan-ability
- Give each answer one memorable takeaway line. In markdown or notes this can appear as a short bracketed noun-phrase subtitle; in conservative forms it should be embedded in the opening sentence.
- Prefer a concrete scene, object, constraint, or failure mode early in the answer so the evaluator can picture the work rather than only read abstractions.
- Favor engineering realism: timing issues, resource limits, interface friction, sequence collisions, handover quality, safety or quality implications, operating criteria, and redesign choices.
- Prefer nouns and verbs over adjectives. Let diagnosis, redesign, and measured change carry the force of the answer.
- Avoid hero-style framing when the stronger story is actually about standards, structure, debugging, coordination, or redesign.
- In Samsung enhancement mode, prefer question-specific structures over repeating the same thesis-evidence-fit rhythm across all four answers.
- In Samsung enhancement mode, make the first 1 to 2 sentences lock the evaluator onto the exact answer direction that question expects.
- Minimize obvious connective words such as `그러나`, `또한`, and `따라서`
- Build flow through sentence order, causality, and evidence progression instead
- Remove any word that is not carrying meaning, tone, or evidence
- Preserve a reflective but analytical voice when the prompt allows it
- Convert reflection into employer-relevant insight rather than essay-like wandering
- Let paragraphs arrive at a conclusion instead of ending only in observation
- When helpful, move in this order: issue recognition -> concrete evidence -> interpretation -> fit
- Explain complex ideas clearly, but compress them enough for screening readability
- For limited-length answers, aim to use at least 90% of the available length with meaningful content

### 9. Capture Revision Learning and Personalization

When persistent storage is authorized, update the user's private working notes after a planning, drafting, revision, or finalization round. Keep the public skill package free of personal data.

What to capture every time:

- what the user explicitly liked
- what the user explicitly disliked
- what the user rewrote in their own words
- what story, tone, or opening survived multiple revisions
- what was only needed for this target and should not become a default

Learning rules:

- If the user manually rewrites a sentence, treat that rewrite as stronger evidence than inferred stylistic guesses.
- If the same preference appears twice across sessions, promote it from `revision-memory.md` into `personalization-memory.md`.
- If the user explicitly says a pattern feels authentic or inauthentic, that can be promoted immediately.
- Do not store one company's keywords, one form's formatting quirks, or one-off padding tactics as personal style.
- If a story repeatedly survives revision and interview-prep scrutiny, raise its confidence and reuse priority in `story-bank.md`.

What durable personalization should learn:

- preferred opening style by prompt type
- acceptable level of self-promotion
- preferred amount of technical detail
- how to frame motivation authentically
- phrases or tones that feel unlike the user
- strengths the user wants foregrounded or downplayed
- which reflections feel genuinely theirs versus too essay-like

### 10. Run the Korean Polish Pass

For Korean output, run these three revision checks before finalizing:

1. Grammar pass
2. Style consistency pass
3. Humanization pass

What to check:

- Grammar:
  - obvious spelling and spacing issues
  - particles, endings, and punctuation
- Style consistency:
  - one formal register through the whole answer
  - consistent terminology, acronym use, numbers, units, and dates
- Humanization:
  - reduce unnecessary commas
  - cut noun-heavy abstraction
  - remove stacked vague adjectives
  - avoid repetitive AI-like sentence rhythm
  - reduce connective-heavy transitions
  - tighten phrasing until only necessary words remain

Keep the meaning, evidence, and tone intact. Polish should improve naturalness, not erase the user's voice.

### 10A. Run AI-Tell QA with `humanize-korean`

When `humanize-korean` is installed, run it after the Korean polish pass and before comparative QC. This is a QA-stage pass, not a second drafting pass.

Use the Codex single-call path with conservative settings such as `장르: 공적` and `강도: 보수`. Pass only the answer bodies for humanization; keep question labels, character limits, headings, citations, and other form metadata outside the editable span.

Apply these rules while using it:

- Preserve every fact, claim, number, date, proper noun, technical term, acronym, quotation, and company or role name exactly.
- Do not add evidence, remove a substantive sentence, change the argument, merge away a claim, or alter the answer's question-fit. Only allow edits mapped to detected translationese, habitual AI phrases, mechanical rhythm, excessive connectives, or similar style patterns identified by the skill.
- Keep the pre-humanization draft as the source of truth. Compare the result against it at sentence and content-anchor level before accepting any change.
- Accept the result only when the humanizer's self-check passes, the change rate is at most 30%, and all existing claim-traceability and character-count checks still pass. At 30% to under 50%, require a targeted human review; at 50% or above, roll back to the pre-humanization draft and keep only manually confirmed local edits.
- If the `humanize-korean` skill or its reference files are unavailable, do not claim that this pass ran. Continue the manual humanization checklist from section 10 and report the fallback only when it affects the QA result.
- Do not use a heavy or strict multi-call route by default. Reserve an explicitly requested precision review or a failed preservation gate for a targeted rerun or human review.

Record internally which categories were detected, the before/after change rate, and whether the preservation gate passed. Keep the humanizer's summary separate from the application answer so it is never submitted as part of the response.

### 11. Run Comparative QC

After the Korean polish pass, compare the polished draft against:

1. the full `Example Bank.md` corpus
2. 2 to 3 matched examples

Use this as the default benchmark set unless the user explicitly wants a narrower comparison.

Compare on:

- opening directness
- question-fit
- evidence density
- competency fit
- company / role specificity
- Samsung / role specificity
- cause-effect logic
- closing contribution
- sentence naturalness
- AI-tell residue after the humanization pass
- length utilization
- interview-defensibility

Use three ratings only:

- `strong`
- `acceptable`
- `weak`

Rewrite rule:

- any `weak` in `opening directness`, `competency fit`, or `interview-defensibility` forces one rewrite pass
- in Samsung enhancement mode, any `weak` in `question-fit` or `Samsung / role specificity` also forces one rewrite pass
- any `weak` in `length utilization` forces one rewrite pass when a character or word limit exists
- if `AI-tell residue` is `weak`, run one targeted humanization pass for the named category or perform a manual local rewrite; do not rewrite the whole answer
- 2 or more total `weak` ratings also force one rewrite pass

Anti-copy guard:

- if the draft repeats a phrase from `Do Not Copy`, rewrite it
- if the draft feels too close to a raw example in sentence sequence or wording, change the structure and phrasing before returning

Keep this QC internal unless the user explicitly asks to see the comparison.

### 12. Verify Before Returning

Check all of the following:

- Every claim is supported by the user's source materials
- The answer actually addresses the prompt
- Company and role names are correct
- The selected story fits the competency being tested
- The plan respects the user's stated must-use, must-avoid, tone, and emphasis preferences
- One-off target instructions were not mistakenly promoted into durable personal memory
- Redundant lines and generic praise are removed
- Length constraints are satisfied or clearly reported
- If a limit exists, the answer should normally reach at least 90% of it
- Character limits should be verified programmatically rather than by model guesswork alone
- Prefer using `scripts/count_jasoseo_sections.py` for multi-question markdown drafts when the script exists
- Treat any section below the configured minimum ratio from `count_jasoseo_sections.py` as a failed verification that requires expansion and rewrite; if the script is missing, count with another reliable local method and report the method used
- The final draft survived comparative QC without a remaining forced-rewrite condition
- If `humanize-korean` was used, its preservation self-check, change-rate gate, and content-anchor comparison passed; otherwise the manual fallback was used and not misreported as an automated run
- No obvious copied wording from the example corpus remains

For metrics-heavy or high-stakes drafts, create an internal claim traceability table using this template when it exists:

- `$DATA_DIR/claim-traceability-template.md`

Minimum traceability requirement:

- exact metrics
- dates
- titles
- certifications
- tool or technology claims that imply hands-on ownership
- company or industry insights that came from research rather than from the user's own experience

### 13. Track Submission Outcomes When Available

If the user later shares any of the following, treat it as high-value feedback for future personalization:

- submitted / not submitted
- interview invitation
- rejection
- acceptance
- recruiter, reviewer, or interviewer feedback
- the user's own hindsight on what felt right or wrong after submission

Store these in `$DATA_DIR/application-outcomes.md`.

Outcome tracking rules:

- record which stories, framing angles, and prompt strategies were used
- record external signals separately from your own guesses about why something worked
- use outcome patterns to calibrate future strategy
- do not overfit a single success or failure; promote patterns only after repeated evidence or very strong explicit feedback

### 14. Export the Final Draft to DOCX

When the user wants the finished jasoseo as a document, export the final answers to `.docx` instead of stopping at plain text.

Default output location:

- the discovered Obsidian `Jasoseo/05-Deliverables/` folder, or the current workspace when no vault is available

Default export rule:

- create one `.docx` deliverable per completed application set
- include company, role, and team if known
- preserve each question and answer as a separate section
- keep the Korean formal register exactly as finalized after QC
- do not introduce new wording during export

Use this script only when it exists:

```bash
python3 "$SKILL_DIR/scripts/export_jasoseo_docx.py" /path/to/final_answers.json
```

JSON payload shape:

```json
{
  "title": "Samsung DS Process Engineering Jasoseo",
  "company": "삼성전자",
  "role": "DS부문 반도체공정기술",
  "team": "메모리사업부",
  "questions": [
    {
      "question_label": "1번 문항",
      "question": "삼성전자를 지원한 이유와 입사 후 회사에서 이루고 싶은 꿈을 기술하십시오.",
      "character_limit": "700자 이내",
      "answer": "최종 확정 답변 본문"
    }
  ]
}
```

Export quality rules:

- use the finalized answer text verbatim
- keep blank lines between major paragraphs
- keep one question block per section for screening readability
- use a stable file name based on company, role, and title unless the user asked for another path

After export, if layout fidelity matters, run an available document-rendering workflow before delivering the file path.

If useful, return:

- Final answer
- DOCX file path
- Short rationale for story selection
- A list of any unsupported gaps the user may want to fill later

## Reference Files

Use the following private note schema when authorized; blank starting templates are in `assets/templates/`:

- `$DATA_DIR/candidate-profile.md`: canonical facts, strengths, experience, and evidence
- `$DATA_DIR/project-registry.md`: lightweight project metadata and live inspection pointers
- `$DATA_DIR/story-bank.md`: reusable STAR-style stories with tags
- `$DATA_DIR/style-guide.md`: preferred voice, tone, and banned patterns
- `$DATA_DIR/personalization-memory.md`: durable preferences learned from repeated sessions and explicit user feedback
- `$DATA_DIR/revision-memory.md`: fine-grained record of what the user accepted, rejected, or rewrote during planning and drafting
- `$DATA_DIR/application-outcomes.md`: submission results and external feedback used to calibrate future targeting
- `$DATA_DIR/source-log.md`: what sources have already been ingested
- `$DATA_DIR/application-brief-template.md`: working template for company and role targeting
- `$DATA_DIR/example-bank.md`: example catalog, retrieval order, source-pool status, and QC rubric
- `$DATA_DIR/example-cache/`: mirrored example files and extracted source caches
- `$DATA_DIR/claim-traceability-template.md`: optional table for mapping risky draft claims back to defendable evidence

Update private notes only within the user's authorized scope. Empty templates and an absent example corpus are expected in this shared package; never claim a reference comparison ran without actual examples.

Use the user's private notes as the long-lived workspace. Keep personal facts, examples, caches, and outcomes outside the public package.
