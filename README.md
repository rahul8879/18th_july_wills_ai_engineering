# Wills AI Engineering — 18th July Batch

Course code for the AI Engineering batch. This guide covers cloning the repo, setting it up
on your local machine (virtual environment, dependencies, API keys), and pulling the latest
code before every class.

Instructions are given for **macOS/Linux** and **Windows** separately — follow the section
that matches your system.

---

## Repository layout

```
.
├── 00_python/                  # Python refreshers (day_1, day_2, day_3, utils)
├── 01_foundations/             # Rule-based / non-LLM foundations
├── 01_prompt_engineering/      # Prompt engineering + OpenAI API examples
├── Documents/                  # Setup PDFs and reference material
├── requirements.txt            # Python dependencies
└── README.md
```

---

## Prerequisites

| Tool | Version | How to check |
| --- | --- | --- |
| Python | 3.11 or newer (3.13 recommended) | `python3 --version` (macOS) / `python --version` (Windows) |
| Git | any recent version | `git --version` |
| VS Code | latest (optional but recommended) | — |

If you don't have them installed:

- **macOS** — install [Homebrew](https://brew.sh), then `brew install python git`
- **Windows** — install Python from [python.org/downloads](https://www.python.org/downloads/)
  (**tick "Add Python to PATH"** on the first installer screen) and Git from
  [git-scm.com/download/win](https://git-scm.com/download/win)

---

## 1. Clone the repository

Pick a folder where you want the code to live, then clone.

### macOS / Linux (Terminal)

```bash
cd ~/Documents
git clone https://github.com/rahul8879/18th_july_wills_ai_engineering.git
cd 18th_july_wills_ai_engineering
```

### Windows (PowerShell or Git Bash)

```powershell
cd $HOME\Documents
git clone https://github.com/rahul8879/18th_july_wills_ai_engineering.git
cd 18th_july_wills_ai_engineering
```

> Tip: open the folder in VS Code right away with `code .`

---

## 2. Create the virtual environment

A virtual environment (`ai-env`) keeps this project's packages separate from your system
Python. It is already listed in `.gitignore`, so it never gets committed.

### macOS / Linux

```bash
# create
python3 -m venv ai-env

# activate
source ai-env/bin/activate
```

### Windows — PowerShell

```powershell
# create
python -m venv ai-env

# activate
.\ai-env\Scripts\Activate.ps1
```

If PowerShell blocks the activation script with a "running scripts is disabled" error, run
this once and then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

### Windows — Command Prompt (cmd)

```cmd
python -m venv ai-env
.\ai-env\Scripts\activate.bat
```

### Windows — Git Bash

```bash
python -m venv ai-env
source ai-env/Scripts/activate
```

Once activated, your prompt shows `(ai-env)` at the start. To leave the environment at any
time, run `deactivate` on any system.

---

## 3. Install dependencies

With the environment **activated**:

### macOS / Linux

```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Verify the install:

```bash
pip list
```

---

## 4. Set up your API key

The code creates the OpenAI client with `OpenAI()`, which reads the key from the
`OPENAI_API_KEY` environment variable. Get your key from
[platform.openai.com/api-keys](https://platform.openai.com/api-keys).

**Never commit your key.** `.env` is already in `.gitignore`.

### Option A — `.env` file (recommended)

Create a file named `.env` in the project root:

```
OPENAI_API_KEY=sk-your-key-here
```

Then install `python-dotenv` and load it at the top of any script that calls the API:

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
load_dotenv()          # must run before OpenAI() is created

from openai import OpenAI
client = OpenAI()
```

### Option B — export in your shell

**macOS / Linux** (current terminal only):

```bash
export OPENAI_API_KEY="sk-your-key-here"
```

To make it permanent, append that line to `~/.zshrc` (zsh, the macOS default) or
`~/.bashrc`, then run `source ~/.zshrc`.

**Windows — PowerShell** (current terminal only):

```powershell
$env:OPENAI_API_KEY = "sk-your-key-here"
```

To make it permanent on Windows:

```powershell
setx OPENAI_API_KEY "sk-your-key-here"
```

Close and reopen the terminal after `setx` for it to take effect.

Check it is set:

```bash
# macOS / Linux
echo $OPENAI_API_KEY
```

```powershell
# Windows PowerShell
echo $env:OPENAI_API_KEY
```

---

## 5. Run the code

Activate the environment first, then run any file:

```bash
# macOS / Linux
python3 00_python/day_1.py
python3 01_foundations/rule_engine.py
python3 01_prompt_engineering/model_set.py
```

```powershell
# Windows
python 00_python\day_1.py
python 01_foundations\rule_engine.py
python 01_prompt_engineering\model_set.py
```

In VS Code, select the interpreter from `ai-env` so the editor uses the right packages:
`Ctrl+Shift+P` / `Cmd+Shift+P` → **Python: Select Interpreter** → pick the one inside
`ai-env`.

---

## 6. Getting the latest code (do this before every class)

New code is pushed to the `main` branch after each session. The commands are the **same on
macOS and Windows**.

```bash
# 1. go to the project folder
cd ~/Documents/18th_july_wills_ai_engineering        # macOS
cd $HOME\Documents\18th_july_wills_ai_engineering    # Windows PowerShell

# 2. check nothing of yours is half-finished
git status

# 3. pull the latest code
git pull origin main

# 4. install any new packages that were added
#    (activate ai-env first)
pip install -r requirements.txt
```

### If `git pull` fails because you edited the files

You have two options:

**Keep your changes** — stash them, pull, then bring them back:

```bash
git stash
git pull origin main
git stash pop
```

**Throw your changes away** and take the instructor's version exactly:

```bash
git reset --hard origin/main
git pull origin main
```

> `git reset --hard` permanently deletes your local edits to tracked files. Only use it when
> you are sure you don't need them.

**Safest habit:** keep your own experiments in a personal folder (e.g. `my_practice/`) that
the instructor's files never touch, so pulls stay conflict-free.

---

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `python: command not found` (macOS) | Use `python3` instead of `python` |
| `python` opens the Microsoft Store (Windows) | Reinstall Python from python.org with "Add Python to PATH" ticked, or use `py -3` |
| `Activate.ps1 cannot be loaded` (Windows) | `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` |
| `ModuleNotFoundError: No module named 'openai'` | The venv isn't activated, or `pip install -r requirements.txt` wasn't run |
| `AuthenticationError` / `api_key must be set` | `OPENAI_API_KEY` isn't set in this terminal — see step 4 |
| `pip` installs into system Python | Check `(ai-env)` is in your prompt; run `which pip` (macOS) / `where pip` (Windows) |
| SSL / certificate errors on macOS | Run `/Applications/Python 3.x/Install Certificates.command` |