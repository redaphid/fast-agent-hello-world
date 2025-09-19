# Generated FastAgent Starter Project

## 📌 Overview

This is a generated starter project for a FastAgent-based system. Key components:

- MCP servers must be defined in `fastagent.config.yaml`
- Declared as part of the function call in `agent.py`
- Uses `uv` as the Python package manager
- Run with: `uv agent.py`

## 📁 Directory Structure

````
.
├── .claude/
├── .git/
├── .venv/
├── data/
├── scripts/
├── .gitignore
├── agent.py
├── fastagent.config.yaml
├── fastagent.jsonl
├── fastagent.secrets.yaml
└── test_tools.py
```;

## 📌 Key Configuration
1. **MCP Servers**: Define in `fastagent.config.yaml` (see below)
2. **Function Call**: Declare servers in `agent.py` as part of the tool call
3. **Environment**: Use `uv` for package management and virtual environments

## 📌 Development Setup

1. **Virtual Environment**: Activated automatically via `.envrc` (Fish shell)
2. **Run Command**: `uv agent.py`
3. **Testing**: Use `test_tools.py` for utility functions

## 📌 .envrc Setup (Fish Shell)

```fish
function chdir
  set -l old_dir (pwd)
  if test -d .venv && -f .venv/activate.fish
    source .venv/activate.fish
  end
  command -v fish > /dev/null && source .envrc
  cd -- $argv
  set -g __old_pwd $old_dir
end
```

## 📌 Notes

- Always source `source .venv/bin/activate.fish` when working in this directory
- Configuration files use YAML format for easy editing
- The `data/` directory is for storing input/output files
- Scripts in `scripts/` provide additional functionality

This project follows standard Python development patterns with Git integration and environment separation for production readiness.
````
