import sys
import uvicorn
import logging
from fastapi import FastAPI

import config
from routers import dataprep, datastat, traning

#################################################################

title = "ANN microservice"

description = """
Microservice for Artifical Neural Network playground

## Data Preparation

TODO

## Training

TODO
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    }
]

app = FastAPI(#__name__, 
    title=title,
    description=description
    )

#################################################################
# Routers

app.include_router(dataprep.router)
app.include_router(datastat.router)
app.include_router(traning.router)

#################################################################

if __name__ == "__main__":   
    if len(sys.argv) > 1 and sys.argv[1] == 'dev':
        uvicorn.run("ann_server:app", host=config.HOST_NAME, port=config.SERVER_PORT, reload=True, workers=4)  
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.NOTSET)

