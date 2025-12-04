# Tasks: Streamlit Calculator

**Input**: Design documents from `/specs/002-streamlit-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project directory structure: `calculator/`, `calculator/tests/`
- [ ] T002 Create `calculator/requirements.txt` and add `streamlit`, `pytest`
- [ ] T003 Create `calculator/app.py` for the main Streamlit application
- [ ] T004 Create `calculator/calculator_logic.py` for core calculation functions
- [ ] T005 Create `calculator/ui_components.py` for Streamlit UI button components
- [ ] T006 Create `calculator/tests/test_logic.py` for unit tests
- [ ] T007 Create `calculator/tests/test_app.py` for integration tests

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T008 Initialize Streamlit `session_state` for `expression` and `display` in `calculator/app.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement numeric input, basic arithmetic operations (addition, subtraction, multiplication, division), and expression evaluation.

**Independent Test**: Perform a series of calculations (e.g., 5 + 3 - 2 * 4 / 2) and verify the correct output.

### Tests for User Story 1

- [ ] T009 [P] [US1] Unit test `add_value` for numeric input in `calculator/tests/test_logic.py`
- [ ] T010 [P] [US1] Unit test `evaluate_expression` for basic arithmetic in `calculator/tests/test_logic.py`

### Implementation for User Story 1

- [ ] T011 [P] [US1] Implement `add_value` function (handling numeric input) in `calculator/calculator_logic.py`
- [ ] T012 [P] [US1] Implement `evaluate_expression` function (for basic arithmetic) in `calculator/calculator_logic.py`
- [ ] T013 [US1] Create numeric buttons (0-9) and basic operator buttons (+, -, ×, ÷) in `calculator/ui_components.py`
- [ ] T014 [US1] Integrate numeric and operator button logic in `calculator/app.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Decimal Input and Evaluation (Priority: P1)

**Goal**: Enable decimal input and accurate evaluation of expressions containing decimal numbers.

**Independent Test**: Perform calculations with decimal numbers (e.g., 2.5 + 1.25) and verify the correct output.

### Tests for User Story 2

- [ ] T015 [P] [US2] Unit test `add_value` for decimal input in `calculator/tests/test_logic.py`
- [ ] T016 [P] [US2] Unit test `evaluate_expression` for decimal arithmetic in `calculator/tests/test_logic.py`

### Implementation for User Story 2

- [ ] T017 [P] [US2] Modify `add_value` to handle decimal point input in `calculator/calculator_logic.py`
- [ ] T018 [P] [US2] Modify `evaluate_expression` to handle decimal arithmetic in `calculator/calculator_logic.py`
- [ ] T019 [US2] Add decimal point button in `calculator/ui_components.py`
- [ ] T020 [US2] Integrate decimal button logic in `calculator/app.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Clearing and Backspace (Priority: P1)

**Goal**: Provide functionality to clear the display/expression and delete the last character entered.

**Independent Test**: Enter an expression, clear it, or use backspace to modify it, and verify the display state.

### Tests for User Story 3

- [ ] T021 [P] [US3] Unit test `clear_expression` in `calculator/tests/test_logic.py`
- [ ] T022 [P] [US3] Unit test `backspace_delete` in `calculator/tests/test_logic.py`

### Implementation for User Story 3

- [ ] T023 [P] [US3] Implement `clear_expression` function in `calculator/calculator_logic.py`
- [ ] T024 [P] [US3] Implement `backspace_delete` function in `calculator/calculator_logic.py`
- [ ] T025 [US3] Add Clear ('C') and Backspace ('DEL') buttons in `calculator/ui_components.py`
- [ ] T026 [US3] Integrate Clear and Backspace button logic in `calculator/app.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Instant UI Updates (Priority: P1)

**Goal**: Ensure the calculator interface updates immediately after each button press without noticeable delay.

**Independent Test**: Visually observe the display and state changes instantly upon rapid button presses.

### Tests for User Story 4

- [ ] T027 [US4] Integration test for UI responsiveness (simulating button presses and checking display updates) in `calculator/tests/test_app.py`

### Implementation for User Story 4

- [ ] T028 [US4] Review and optimize Streamlit callbacks to ensure instant UI updates in `calculator/app.py`
- [ ] T029 [US4] Ensure all button interactions correctly modify `session_state` to trigger immediate re-renders in `calculator/app.py`

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T030 Implement CSS styling for dark theme, display panel, and buttons in `calculator/app.py` or separate CSS (if applicable)
- [ ] T031 Implement robust error handling for division by zero and invalid inputs in `calculator/calculator_logic.py` and `calculator/app.py`
- [ ] T032 Final code review, refactoring, and cleanup across `app.py`, `calculator_logic.py`, `ui_components.py`
- [ ] T033 Run all tests (`pytest`) to ensure full functionality and stability
- [ ] T034 Finalize `requirements.txt` with exact versions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1, US2, US3 for responsiveness

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Logic functions before UI integration

### Parallel Opportunities

- Tasks marked [P] can run in parallel (e.g., creating files in different directories).
- Once Foundational phase completes, user stories can be worked on in parallel by different team members.
- Within each user story, tests can be written in parallel to implementation (before running implementation).

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test add_value for numeric input in calculator/tests/test_logic.py"
Task: "Unit test evaluate_expression for basic arithmetic in calculator/tests/test_logic.py"

# Launch core logic implementation for User Story 1 together:
Task: "Implement add_value function (handling numeric input) in calculator/calculator_logic.py"
Task: "Implement evaluate_expression function (for basic arithmetic) in calculator/calculator_logic.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
