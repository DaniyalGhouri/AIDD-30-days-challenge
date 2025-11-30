# Short note for SPECKit Plus
Spec-Kit Plus is a Specification-Driven Development (SDD) framework for AI-assisted coding. The main idea is to shift from “code-first” to “spec-first”: instead of starting by writing code directly, you first write clear specifications, plans, tasks, and only then implement. This approach ensures that not only you get working code, but also reusable “intelligence artifacts” — such as decision records, prompt history, and architectural reasoning. that stay with the project and benefit future development.

# /sp.constitution
This is where you define your project’s foundational principles and guidelines. You use /sp.constitution to create a “constitution” document (e.g. constitution.md) that captures standards for code quality, testing, UX consistency, performance, architecture decisions, and governance rules.

# /sp.specify
With /sp.specify, you outline what the project (or feature) should do — the requirements, user stories, functional behavior, constraints, acceptance criteria. This is done before you pick any tech stack or start coding. It helps you think clearly about the problem you solve and sets a shared, unambiguous contract that the subsequent plan and implementation will follow.

# /sp.plan
After you have a specification, /sp.plan lets you define how you will build it, technically. This includes choosing tech stack, architecture design, dependencies, data models, system boundaries, and other implementation details.

# /sp.tasks
Once you have a plan, /sp.tasks breaks the plan into smaller, actionable tasks. This decomposition makes the work manageable, each task becomes a unit that can be implemented, tested, reviewed, and merged independently. 

# /sp.implement
Finally, /sp.implement triggers the actual implementation: the AI agent (or you, but following spec) writes the code for each task, generates deliverables, and also logs “intelligence artifacts” like architectural decision records (ADRs) and prompt history records (PHRs). This ensures the output is not only working software, but also well-documented decisions and reusable knowledge for future features.