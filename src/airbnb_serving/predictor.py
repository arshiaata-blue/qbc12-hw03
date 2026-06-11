import pandas as pd
from .schema import ListingFeatures, PredictionResponse

def predict_single(features: ListingFeatures, model, run_id: str) -> PredictionResponse:
    # Transform to a one line Df
    df = pd.DataFrame([features.model_dump()])

    # Prediction
    pred = int(model.predict(df)[0])
    proba = float(model.predict_proba(df)[0, 1])

    return PredictionResponse(
        prediction=pred,
        probability_high_demand=proba,
        model_run_id=run_id
    )

def predict_batch(features_list: list[ListingFeatures], model, run_id: str) -> list[PredictionResponse]:
    # Creating a df from all enteries
    rows = [f.model_dump() for f in features_list]
    df = pd.DataFrame(rows)

    # Batch predict
    preds = model.predict(df)
    probas = model.predict_proba(df)[:, 1]

    l = []
    for i in range(len(preds)):
        l.append(PredictionResponse(
            prediction=int(preds[i]),
            probability_high_demand=float(probas[i]),
            model_run_id=run_id
        ))
    return l
