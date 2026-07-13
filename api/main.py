from fastapi import FastAPI
import joblib

app = FastAPI(
    title="News Classifier API",
    description="API para classificação de notícias",
    version="1.0"
)

model = joblib.load(
    "news_classifier.pkl"
)


@app.get("/")
def home():
    return {
        "status": "API online",
        "modelo": "news_classifier"
    }


@app.post("/predict")
def predict(texto: str):

    prediction = model.predict([texto])

    return {
        "texto": texto,
        "classe_predita": prediction[0]
    }