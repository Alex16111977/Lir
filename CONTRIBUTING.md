# Contributing to Lir

We love your input! We want to make contributing to Lir as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Request Process

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code lints
6. Issue that pull request!

## Any contributions you make will be under the MIT Software License

When you submit code changes, your submissions are understood to be under the same [MIT License](http://choosealicense.com/licenses/mit/) that covers the project.

## Report bugs using GitHub's [issue tracker](https://github.com/yourusername/Lir/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/yourusername/Lir/issues/new).

**Great Bug Reports** tend to have:

- A quick summary and/or background
- Steps to reproduce
  - Be specific!
  - Give sample code if you can
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Linux/Mac)
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `pytest`

## Code Style

- Use Python 3.8+ features
- Follow PEP 8 style guide
- Use type hints where possible
- Document functions and classes with docstrings
- Keep line length to 88 characters (Black formatter standard)

## Testing

- Write tests for new features
- Ensure all tests pass: `pytest`
- Check coverage: `pytest --cov=src`
- Aim for 80%+ code coverage

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
