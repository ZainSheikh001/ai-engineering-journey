# Setup guide

Do these once. Total time: about 60–90 minutes.

## 1. Install the tools
1. **Python 3.12** — https://www.python.org/downloads/
   - Windows: tick **"Add python.exe to PATH"** on the first installer screen.
2. **Git** — https://git-scm.com/downloads (default options are fine)
3. **VS Code** — https://code.visualstudio.com, then install the **Python** extension (by Microsoft).
4. **GitHub account** — https://github.com (use a professional username; recruiters will see it).
5. **Docker Desktop** (needed from Week 4) — https://www.docker.com/products/docker-desktop/

Check everything works (in a terminal / PowerShell):
```
python --version
git --version
```

## 2. Configure Git (once)
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Use the same email as your GitHub account.

## 3. Put this repo on GitHub
1. On GitHub, click **New repository**, name it `ai-engineering-journey`, set it to **Public**, and do **not** add a README (this repo already has one).
2. Unzip this folder somewhere easy, e.g. `Documents/ai-engineering-journey`.
3. Open the folder in VS Code (**File → Open Folder**), then open the terminal (**Terminal → New Terminal**) and run:
```
git init
git add .
git commit -m "Set up learning hub"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/ai-engineering-journey.git
git push -u origin main
```
GitHub will ask you to sign in the first time.

## 4. Create a virtual environment
```
python -m venv .venv
```
Activate it:
- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
  - If you get a "running scripts is disabled" error, run once:
    `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`
- macOS / Linux: `source .venv/bin/activate`

You should see `(.venv)` at the start of the terminal line. Then:
```
pip install -r requirements.txt
```

## 5. Secrets
1. Copy `.env.example` to a new file named `.env`.
2. Put your API keys in `.env` only. It is listed in `.gitignore`, so it is never pushed.
3. Never paste a key into code, chat or a screenshot. If a key leaks, delete it and create a new one.

## 6. Daily routine
```
cd ai-engineering-journey
# activate .venv (step 4)
git pull
# ... work ...
git add .
git commit -m "W01: what I did"
git push
```
