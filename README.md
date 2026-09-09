# Bayesian A/B Tester

Minimal Bayesian A/B testing MVP. Computes posterior probability that a treatment beats control, expected lift, SRM check, and a ship/hold/inconclusive verdict.

## Run locally

pip install -r requirements.txt
uvicorn api.main:app --reload

## Dashboard

streamlit run app/dashboard.py --server.port 8501

Set API_URL env var if the API is not on localhost.

## Docker

docker build -t ab-tester .
docker run -p 8000:8000 ab-tester

## Azure Web App for Containers

az acr build --registry <your-registry> --image ab-tester:latest .

az webapp create --resource-group <rg> --plan <plan> --name <app-name> --deployment-container-image-name <your-registry>.azurecr.io/ab-tester:latest

az webapp config appsettings set --resource-group <rg> --name <app-name> --settings WEBSITES_PORT=8000
