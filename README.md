# churnlab-2026 — Telco Customer Churn

## Business question
Which customers of a telecommunications company are likely to leave the service?
The target column is `Churn` (`Yes` / `No`). It must never be used as a model input.

## Environment
- Python: 3.11 (3.12 also accepted)
- Package manager: uv (lock created with uv 0.13.4)

```sh
uv sync --locked
uv run python -c "import churnlab; print(churnlab.__version__)"   # 0.1.0
```

## Data
- Source: IBM Telco Customer Churn, pinned to commit `1fd6fd7`:
  https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/1fd6fd70906479be1712e64cfc0ea89f58466629/data/Telco-Customer-Churn.csv
- Expected SHA-256:
  `16320c9c1ec72448db59aa0a26a0b95401046bef5d02fd3aeb906448e3055e91`

```sh
uv run python scripts/download_data.py   # downloads the CSV and records its source/hash
uv run python scripts/inspect_telco.py   # checks the hash and writes reports/tp01_data_overview.json
```
Expected: 7,043 rows, 21 columns, 1,869 churners (~26.5%), 11 blank `TotalCharges`.

The raw CSV is not committed; only its source and hash (`data/raw/telco.source.json`) are.

## Project layout
| Path | Purpose |
|---|---|
| `src/churnlab/` | Importable project code |
| `scripts/` | Executable workflow commands |
| `data/raw/` | Original input snapshot and its source metadata (never modified) |
| `reports/` | Generated reports (ignored by Git) |
| `evidence/tp01/` | Submitted evidence for TP01 |

## What this dataset is not
This is a single **customer snapshot**: one row per customer at one point in time.
It is not a dated event log, so the order of events can't be reconstructed.
It is not a randomized retention experiment, so it can't measure the causal effect of an intervention.

## Reproducibility limits
The lock file fixes package versions, but not the OS, hardware, or uncommitted edits.
The hash identifies the data bytes, but it does not prove label quality or the absence of leakage.
