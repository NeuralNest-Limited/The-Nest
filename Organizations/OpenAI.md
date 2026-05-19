---
id: openai
title: OpenAI
type: org
status: draft
created: 2026-05-20
last_reviewed: 2026-05-20
authored_by: claude-opus-4-7
schema_version: 0.1
summary: AI research and deployment company founded 2015; developer of the GPT family of models and ChatGPT; pioneer of RLHF; subject of multiple governance and safety-team controversies through 2024-2025.
confidence: 0.9
source_tier: 2
topics: [ai-capabilities, ai-safety, ai-safety/alignment]
aliases: [OpenAI Inc, OpenAI Global LLC, OpenAI LP]
founded: 2015
dissolved: null
headquarters: San Francisco, USA
org_kind: company
focus_areas: [ai-capabilities, ai-capabilities/scaling, ai-safety/alignment, ai-safety/evaluation]
sources:
  - type: official-statement
    title: "OpenAI Charter"
    venue: openai.com
    year: 2018
    url: https://openai.com/charter
    accessed: 2026-05-20
  - type: official-statement
    title: "Preparedness Framework"
    venue: openai.com
    year: 2023
    accessed: 2026-05-20
related: [[Anthropic]], [[Sam Altman]]
---

# OpenAI

> AI research and deployment company. Founded as non-profit in 2015 with mission of ensuring AGI benefits all humanity; restructured in 2019 as capped-profit (OpenAI LP) under non-profit governance; producer of the GPT family of language models and ChatGPT.

## Founding and structure

Founded December 2015 by Sam Altman, Elon Musk, Greg Brockman, Ilya Sutskever, John Schulman, Wojciech Zaremba, and others. Initial structure: non-profit research lab with $1 billion in pledged funding.

In 2019 created OpenAI LP, a "capped-profit" subsidiary allowing equity returns up to 100x for investors, while remaining under non-profit board governance. Major Microsoft investment beginning 2019 ($1B initial; subsequently expanded to ~$13B+).

Governance crisis November 2023: non-profit board fired CEO Sam Altman, reversed within days under employee/investor pressure. Subsequent board reconstitution removed several non-commercial-perspective members including Helen Toner. Continuing tensions through 2024-2025 about for-profit conversion plans.

## Mission and focus

Stated mission: "ensure that artificial general intelligence benefits all of humanity." The OpenAI Charter (2018) commits to:
- Broadly distributed benefits.
- Long-term safety.
- Technical leadership.
- Cooperative orientation — including a clause to assist any value-aligned, safety-conscious project ahead of OpenAI on the path to AGI.

The interpretation and operationalization of these commitments has been a continuing source of debate, internally and externally.

## Notable outputs

- **GPT series**: GPT-1 (2018), GPT-2 (2019, controversial staged release), GPT-3 (2020), GPT-3.5 / ChatGPT (2022), GPT-4 (2023), GPT-4o, o1 (2024), o3 (2024-2025), GPT-5 (2025).
- **RLHF**: deep RL from human preferences (Christiano et al. 2017) and InstructGPT (2022) — foundational to current LLM alignment methodology.
- **DALL-E series**: text-to-image generation.
- **Whisper**: speech recognition.
- **Sora**: text-to-video.
- **Preparedness Framework** (2023): capability-threshold-based safety commitments analogous to Anthropic's RSP.

cites:: [[christiano-deep-rl-from-human-preferences-2017]]

## Key people

- **Sam Altman**: CEO (with Nov 2023 interlude).
- **Greg Brockman**: President; co-founder.
- **Ilya Sutskever**: Chief Scientist until 2024 departure; co-founder; central figure in November 2023 events; later co-founded Safe Superintelligence Inc.
- **Mira Murati**: CTO until 2024 departure.
- **Jan Leike**: Co-led Superalignment team until 2024 departure; joined Anthropic.
- **John Schulman**: Co-founder; departed for Anthropic in 2024.

affiliated-with:: [[Sam Altman]]
affiliated-with:: [[Ilya Sutskever]]

## Funding and influence

Microsoft is the largest investor (cumulative ~$13B+ commitments). Other investors include Khosla Ventures, Reid Hoffman, Andreessen Horowitz, Sequoia, Thrive Capital, and (in later rounds) sovereign-wealth and strategic-tech investors. As of late 2024 OpenAI was reportedly the most-valued private AI company, with valuations in the $150-300B range across funding rounds.

Cultural influence: ChatGPT's November 2022 release is widely treated as the inflection point for public awareness of LLMs.

## Reception and critique

- *Internal turnover*: 2024 saw substantial safety-team departures, including the dissolution of the dedicated Superalignment team. Several departing researchers cited safety-vs-capabilities tension.
- *Mission drift critique*: from former employees, FLI, and parts of the alignment community — that the for-profit shift and commercial pressures have hollowed out the original mission.
- *Industry capture critique*: from FAccT-adjacent critics — that OpenAI shapes AI governance discourse to favor incumbents.
- *Safety theater critique*: from accelerationists — that safety commitments are over-stated.
- *Genuine contribution acknowledgment*: even critics acknowledge OpenAI's technical contributions to alignment-relevant methods.

## Sources

- openai.com/charter, openai.com/preparedness
- Press coverage of November 2023 events (NYT, Bloomberg, Wired, The Information)
- Various interviews with founders and departing employees
- Microsoft 10-K filings (for the investor relationship)
