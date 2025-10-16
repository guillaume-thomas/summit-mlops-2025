import pickle
from dataclasses import dataclass

from fastapi import FastAPI

app = FastAPI()
model = pickle.load(open("./src/{{ cookiecutter.module_name }}/api/resources/model.pkl", "rb"))

@dataclass
class Something:
    A: int
    B: int
    C: int

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/infer")
def infer(something: Something) -> list:
    res = model.predict([[something.A, something.B, something.C]])
    return res.tolist()