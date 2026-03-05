# Contributing

Thanks for contributing.

## Setup

1. Fork and clone the repo.
2. Create and activate a virtual environment.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run `python main.py` to verify local setup.
5. Run tests with `python -m unittest discover -s tests -p "test_*.py"`.

## Guidelines

- Keep changes focused and small.
- Add clear error handling for user-facing flows.
- Preserve CLI behavior unless the change intentionally updates UX.
- Update README when behavior or setup changes.

## Pull Requests

- Use a clear title and summary.
- Explain the problem, solution, and test steps.
- Include screenshots/terminal output for UX changes when useful.
- Ensure CI passes before requesting review.
