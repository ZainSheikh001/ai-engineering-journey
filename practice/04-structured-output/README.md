# LLM Structured Output with Pydantic

Classifies customer support messages (English or Roman Urdu) into
structured, validated data using an LLM.

## How it works

1. A customer message is sent to an LLM (Groq, `openai/gpt-oss-20b`) with a system prompt.
2. The LLM returns JSON: `category`, `urgency`, `needs_human`.
3. Pydantic validates it: required fields, correct types, allowed values only.
4. Invalid output is caught and handled instead of crashing.

**Example**

- Input: `Mera order 10 din se nahi aya, paise wapas chahiye abhi!`
- Output: `category='refund' urgency='high' needs_human=True`

## How to run

```
pip install -r requirements.txt
python 04-structured-output/step5_llm_pydantic.py
pytest 04-structured-output
```

Copy `.env.example` to `.env` and add your own API keys first.

## Why validate LLM output?

LLMs do not always follow instructions. Even in JSON mode, a model can return
JSON that is valid but wrong for the app: a missing field, the wrong type, or
an invented value such as "urgent" instead of "high". Pydantic checks every
response at the boundary, so bad data is rejected before it reaches the rest
of the system instead of causing confusing errors later.

## Testing

The validation logic is tested with pytest using fixed example outputs, not
the live LLM, so the tests are free, fast and give the same result every run.

- valid output is accepted
- output with missing fields is rejected
- output with values outside the allowed list is rejected

I also broke the code on purpose (removed `"high"` from the allowed values)
to confirm the tests catch the mistake.

## What I learned

- LLMs return text, so structured output needs both JSON mode (valid format)
  and schema validation (correct content).
- `try/except` lets an app handle bad model output gracefully instead of crashing.
- Test your own logic, not the external API: tests should be deterministic,
  free and fast.