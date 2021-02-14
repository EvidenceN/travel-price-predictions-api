from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import gas_price_prediction, airbnb_predict

app = FastAPI(
    title='RESFEBER CARTER DS API',
    description='Awesome Data Science Team',
    version='0.1',
    docs_url='/',
)

app.include_router(gas_price_prediction.router)
app.include_router(airbnb_predict.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
