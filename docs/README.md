# Project Echo docs

This folder holds engineering documentation that applies across teams.

Current docs:

- `Dockerfile_Optimization_Guide.md`: Docker image guidance.
- `Engine_Documentation.md`: Engine implementation notes.
- `repository-reorganisation.md`: repository cleanup manifest and dependency checks.
- `architecture/`: target home for stable architecture and runtime topology docs.
- `team-guides/`: target home for team ownership, handover and configuration notes.
- `research/`: index for research material that may later move from the root `Research/` folder.

Ownership notes:

- Backend owns deployment and shared infrastructure docs.
- Engine owns model, data, experiment and research docs.
- HMI owns UI and design-facing docs.
- IoT owns device and field integration docs.

Before moving documentation, check for links from the root README, notebooks, compose files, CI workflows and team READMEs.

Compatibility note: the prototype tree now uses the lowercase `src/prototypes` path from the ownership target structure.
