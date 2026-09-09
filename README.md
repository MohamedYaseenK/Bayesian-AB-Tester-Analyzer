# Bayesian A/B Tester

A minimal Bayesian A/B testing tool. Upload two groups of experiment data, pick the metric type, and get a posterior-based verdict — SHIP, HOLD, or INCONCLUSIVE — instead of a bare p-value.

## Demo

![Bayesian A/B Tester demo](<img width="986" height="797" alt="Screenshot 2026-09-09 090752" src="https://github.com/user-attachments/assets/a6136fa4-879d-4e1c-ab82-ec43cd494c2b" />
)

## Problem

Most A/B test readouts stop at "significant or not." This tool instead answers: *how likely is it that the treatment is actually better, by how much, and is the sample even large enough to trust that answer.*

## Features

- Bayesian posterior comparison for three metric types: binary, count, continuous
- Sample Ratio Mismatch (SRM) check on group sizes
- Plain verdict: SHIP / HOLD / INCONCLUSIVE
- FastAPI backend + Streamlit dashboard
- Adapter for the MeuTutor gamification A/B dataset
- Docker-ready for Azure Web App for Containers

## Project Structure

```
ab-tester/
├── core/
│   ├── schema.py                 # metric type + record schema
│   ├── verdict.py                 # SHIP / HOLD / INCONCLUSIVE logic
│   ├── bayesian/
│   │   ├── beta_binomial.py       # binary metrics
│   │   ├── gamma_poisson.py       # count metrics
│   │   └── normal_normal.py       # continuous metrics
│   └── validity/
│       └── srm_check.py           # sample ratio mismatch check
├── data/
│   ├── raw/                       # source datasets
│   └── adapters/
│       └── meututor_adapter.py    # MeuTutor XLSX -> clean lists
├── api/
│   └── main.py                    # FastAPI app (/health, /analyze)
├── app/
│   └── dashboard.py               # Streamlit UI
├── requirements.txt
├── Dockerfile
└── README.md
```

## Setup

```
cd ab-tester
pip install -r requirements.txt
```

## Run

**1. Start the API**

```
uvicorn api.main:app --reload
```

Runs at `http://localhost:8000`. Check `http://localhost:8000/health`.

**2. Start the dashboard** (new terminal)

```
streamlit run app/dashboard.py
```

Opens at `http://localhost:8501`.

## Usage

1. Pick a metric type: `binary`, `count`, or `continuous`
2. Enter control and treatment data as comma-separated numbers
   - binary → `1,0,1,1,0` (0/1 outcomes)
   - count → `2,4,3,1,5` (visits, activities)
   - continuous → `680,573,440` (grades, time, cost)
3. Click **Analyze**

**Response fields**

| Field | Meaning |
|---|---|
| `prob_treatment_wins` | Posterior probability treatment beats control |
| `expected_lift` | Average difference between the two posteriors |
| `verdict` | SHIP (≥95%), HOLD (≤5%), or INCONCLUSIVE |
| `srm.p_value` | Chi-square p-value on group size balance |
| `srm.srm_flag` | `true` if group sizes look mismatched |

## Using the MeuTutor Dataset

```python
from data.adapters.meututor_adapter import get_variant_data

control = get_variant_data("data/raw/Experiment_two.xlsx", "Metric Access", "T1")
treatment = get_variant_data("data/raw/Experiment_two.xlsx", "Metric Access", "T2")
```

Pass these lists as `control_data` / `treatment_data` with `metric_type: "count"`.

## Docker

```
docker build -t ab-tester .
docker run -p 8000:8000 ab-tester
```

## Deploy to Azure Web App for Containers

```
az acr build --registry <your-registry> --image ab-tester:latest .

az webapp create --resource-group <rg> --plan <plan> --name <app-name> \
  --deployment-container-image-name <your-registry>.azurecr.io/ab-tester:latest

az webapp config appsettings set --resource-group <rg> --name <app-name> \
  --settings WEBSITES_PORT=8000
```

## Notes

- Only the FastAPI service is containerized. The Streamlit dashboard runs separately and points at the API via the `API_URL` environment variable.
- Experiment_one.xlsx has 3 treatment arms (T1/T2/T3) and is not supported by the current pairwise analyzer.
