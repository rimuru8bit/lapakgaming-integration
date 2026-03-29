# Lapakgaming Integration (Phase 1)

Foundation client for Lapakgaming reseller API.

## Included
- `services/lapakgaming/client.py` — API client with auth, timeout, retries, 429 backoff
- `services/lapakgaming/errors.py` — typed errors
- `services/lapakgaming/models.py` — response envelope model (`{code,data}`)
- `scripts/test_lapak_client.py` — smoke test runner

## Setup
```bash
cp .env.example .env
# fill LAPAK_SECRET_KEY and optional overrides
```

## Run smoke test
```bash
python3 scripts/test_lapak_client.py --categories
python3 scripts/test_lapak_client.py --products
python3 scripts/test_lapak_client.py --all
```
