# Learning log

Every problem I hit goes here, newest first. This is my best source of interview stories.

## Template
```
### YYYY-MM-DD · W00 · short title
- **Symptom:** what I saw (paste the key error line)
- **Cause:** why it happened
- **Fix:** what solved it (link to commit)
- **Lesson:** one sentence I want to remember
- **Time lost:** minutes
```

## Entries

### 2026-10-08 · W00 · Example entry
- **Symptom:** `ModuleNotFoundError: No module named 'pydantic'`
- **Cause:** installed the package globally, but ran the script inside the virtual environment
- **Fix:** activated `.venv` and ran `pip install -r requirements.txt`
- **Lesson:** always activate the venv before installing or running anything
- **Time lost:** 10 minutes
