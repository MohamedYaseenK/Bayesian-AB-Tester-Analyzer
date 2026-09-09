from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from core.bayesian.beta_binomial import posterior_samples as beta_binomial_samples
from core.bayesian.gamma_poisson import posterior_samples as gamma_poisson_samples
from core.bayesian.normal_normal import posterior_samples as normal_normal_samples
from core.validity.srm_check import check_srm
from core.verdict import get_verdict

app = FastAPI()

class AnalyzeRequest(BaseModel):
    metric_type: str
    control_data: list[float]
    treatment_data: list[float]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    srm_result = check_srm([len(req.control_data), len(req.treatment_data)])

    if req.metric_type == "binary":
        control_samples = beta_binomial_samples(sum(req.control_data), len(req.control_data))
        treatment_samples = beta_binomial_samples(sum(req.treatment_data), len(req.treatment_data))
    elif req.metric_type == "count":
        control_samples = gamma_poisson_samples(sum(req.control_data), len(req.control_data))
        treatment_samples = gamma_poisson_samples(sum(req.treatment_data), len(req.treatment_data))
    else:
        control_samples = normal_normal_samples(np.mean(req.control_data), np.std(req.control_data), len(req.control_data))
        treatment_samples = normal_normal_samples(np.mean(req.treatment_data), np.std(req.treatment_data), len(req.treatment_data))

    prob_treatment_wins = float(np.mean(treatment_samples > control_samples))
    lift = float(np.mean(treatment_samples) - np.mean(control_samples))
    verdict = get_verdict(prob_treatment_wins)

    return {
        "prob_treatment_wins": prob_treatment_wins,
        "expected_lift": lift,
        "verdict": verdict,
        "srm": srm_result
    }
