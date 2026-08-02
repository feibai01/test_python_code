# AGENTS.md

## Project overview

This repository is a personal Python practice archive: most files are standalone exercises for algorithms, data processing, and small utility examples rather than a package with a shared application entry point.

The workspace root contains many one-off scripts such as [classwork_lab1_1_distance.py](classwork_lab1_1_distance.py), [classwork_lab2_6_binary_search.py](classwork_lab2_6_binary_search.py), [code_conv_store_sales_analysis.py](code_conv_store_sales_analysis.py), and [test_random.py](test_random.py). The code is intentionally educational and simple.

## What agents should assume

- Treat each Python file as an independent exercise unless a file clearly references another script.
- Do not assume a framework, package layout, or app-level build pipeline exists.
- Favor minimal, local edits instead of introducing shared abstractions, modules, or cross-file refactors.
- Preserve the repository’s beginner-friendly style: clear names, simple logic, brief comments, and readable structure.
- Keep Chinese comments or educational wording when they are already present in the file.

## Validation and execution

- Run scripts directly with Python, for example: `python path/to/script.py`.
- There is no formal project test suite or build system in this repo; direct script execution is the normal validation path.
- Check the script for local file paths, dataset references, or Windows-specific assumptions before running it.

## Dependency notes

- Standard library modules are expected to work without further setup.
- Some scripts may depend on `pandas`, `matplotlib`, `pillow`, or similar third-party packages.
- If imports fail, install the missing package in the active environment rather than redesigning the repository structure.

## Useful references

- [README.md](README.md) for the repo overview
- [code_conv_store_sales_analysis.py](code_conv_store_sales_analysis.py) as a representative data-analysis script
- Individual exercise files for task-specific patterns and conventions

## Instructions for coding agents

- Keep changes small and local to the active script.
- Preserve the original educational intent and output behavior unless the task explicitly asks for a change.
- If a file contains classroom TODOs or study-style examples, follow the existing teaching pattern instead of modernizing it into production code.
- When adding new examples, prefer simple, readable Python that matches the surrounding exercises in the repo.
