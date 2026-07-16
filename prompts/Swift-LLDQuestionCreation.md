Create a Swift low-level-design exercise in the style of a practical coding interview. Give me:

- A `README.md` with the requirements, written like an interviewer would explain them (a bit informal, some ambiguity left in on purpose). The README must describe the overall behavior/requirements the system needs to satisfy — but it must not name, structure, or hint at any specific class, struct, method, or property. I should be able to tell *what* the system needs to do from the requirements; figuring out *which types do it and how* is the exercise.
- A partially implemented module: 2–4 types (classes/structs), some fully done, some with method stubs (`fatalError("TODO: ...")` or `// TODO:` comments)
- A test file using `XCTest` (or Swift Testing if that's your default) exercising the stubs, so I know the contract I need to satisfy
- Do NOT show me your solution or explain the design anywhere — I want to read the existing code myself and figure out how to correctly extend or complete it
- TODO comments/fatalError messages on stubs should describe *what* the method needs to do (its contract/responsibility), never *how* to implement it. Don't hint at the specific expression, comparison, data structure, or algorithm to use — that gives away the solution.
- Starting at medium difficulty, don't hand me a complete type layout. Give me one or more `protocol`s defining the interface(s) the design needs to satisfy, plus whatever fully-implemented supporting/data types are needed for context — but leave at least one whole type for me to design and implement from scratch, not just fill in stubs on a type you already shaped. The test file should test through the protocol (or a factory/entry point) so it doesn't leak the shape of the type I'm supposed to design.
- Prefer idiomatic Swift where it's natural to the domain — structs vs classes where appropriate, protocol-oriented design, `enum` for state/variants — but don't force a pattern that doesn't fit.

Before picking a domain, check the existing exercises in this folder (if any) and avoid repeating a domain already used.

Domain: [pick something — e.g. 'a parking garage', 'a ride-sharing dispatch system', 'a movie ticket booking system', 'a document version control mini-system']

Difficulty: [easy/medium/hard]