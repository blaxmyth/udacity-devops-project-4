
from flask import json
from app import app


def test_home():
    with app.test_client() as client:
        res = client.get("/")

        assert res.status_code == 200
        assert b"Sklearn Prediction Home" in res.data


def test_predict():
    with app.test_client() as client:
        res = client.post(
            "/predict",
            json={
                "CHAS": {"0": 0},
                "RM": {"0": 6.575},
                "TAX": {"0": 296.0},
                "PTRATIO": {"0": 15.3},
                "B": {"0": 396.9},
                "LSTAT": {"0": 4.98},
            },
            follow_redirects=True,
        )

        assert res.status_code == 200
        assert len(json.loads(res.data).get("prediction", [])) > 0