from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = FastAPI()


def get_riot_data(name: str, tag: str):
    api_key = os.getenv('API_KEY')
    link = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={api_key}'
    response = requests.get(link)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()


@app.get("/riot-account/{name}/{tag}")
def riot_account(name: str, tag: str):
    data = get_riot_data(name, tag)
    return data


# Démarrer l'application FastAPI
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='localhost', port=8000)
