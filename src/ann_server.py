import sys
import uvicorn
import logging
from fastapi import FastAPI

import config
import constants
from routers import dataprep, datastat, traning

#################################################################

app = FastAPI(#__name__, 
    title=constants.TITLE,
    description=constants.DESCRIPTION
    )

#################################################################
# Routers

app.include_router(dataprep.router)
app.include_router(datastat.router)
app.include_router(traning.router)

#################################################################

def main(): 
    if len(sys.argv) > 1 and sys.argv[1] == 'prod':
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
        uvicorn.run("ann_server:app", host=config.HOST_NAME, port=config.SERVER_PORT, workers=4) 
    else:
        uvicorn.run("ann_server:app", host=config.HOST_NAME, port=config.SERVER_PORT, reload=True)  

if __name__ == "__main__":   
    main()