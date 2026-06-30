from pathlib import Path

import pandas as pd
from fastapi import Depends, FastAPI

from src.access.rbac import get_current_user, require_permission
from src.pii.anonymizer import MedVietAnonymizer


app = FastAPI(title="MedViet Data API", version="1.0.0")
anonymizer = MedVietAnonymizer()
DATA_PATH = Path("data/raw/patients_raw.csv")


def _load_patient_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


@app.get("/api/patients/raw")
@require_permission(resource="patient_data", action="read")
async def get_raw_patients(current_user: dict = Depends(get_current_user)):
    """Return the first 10 raw patient records for admins."""
    df = _load_patient_data()
    return df.head(10).to_dict(orient="records")


@app.get("/api/patients/anonymized")
@require_permission(resource="training_data", action="read")
async def get_anonymized_patients(current_user: dict = Depends(get_current_user)):
    """Return the first 10 anonymized patient records for training use."""
    df = _load_patient_data()
    df_anon = anonymizer.anonymize_dataframe(df)
    return df_anon.head(10).to_dict(orient="records")


@app.get("/api/metrics/aggregated")
@require_permission(resource="aggregated_metrics", action="read")
async def get_aggregated_metrics(current_user: dict = Depends(get_current_user)):
    """Return aggregate condition counts without exposing PII."""
    df = _load_patient_data()
    metrics = df["benh"].value_counts().sort_index().to_dict()
    return {"patient_count_by_condition": metrics}


@app.delete("/api/patients/{patient_id}")
@require_permission(resource="patient_data", action="delete")
async def delete_patient(
    patient_id: str,
    current_user: dict = Depends(get_current_user),
):
    """Simulate a patient deletion request."""
    return {"deleted": patient_id, "performed_by": current_user["username"]}


@app.get("/health")
async def health():
    return {"status": "ok", "service": "MedViet Data API"}
