import sys
import uvicorn
import logging
from fastapi import FastAPI
    
import config
import constants
from routers import dataprep, datastat, traning

#################################################################

logging.config.fileConfig(fname=config.LOG_CONFIG_PATH)
logger = logging.getLogger('')

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
        config.ENVIRONMENT = 'production'
        logger.setLevel(config.LOG_LVL_PROD)
        uvicorn.run("ann_server:app", host=config.HOST_NAME, port=config.SERVER_PORT, workers=4) 
    else:
        logger.setLevel(config.LOG_LVL_DEV)
        uvicorn.run("ann_server:app", host=config.HOST_NAME, port=config.SERVER_PORT, reload=True)  

if __name__ == "__main__":   
    main()