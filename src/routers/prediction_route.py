# import tempfile
# import urllib.request
import base64
from fastapi import APIRouter, UploadFile, Response
from loguru import logger
from src.schemas.request.path_schema import PathSchema,Base64Schema
from src.services.prediction import predict_similar_images
from datetime import  datetime
# import time
router = APIRouter(prefix="/predict")
from PIL import Image
from io import  BytesIO
import  requests
@router.post("/file")
def get_image_file(file_input: UploadFile):
    try:
        start = datetime.now()
        # temp = tempfile.NamedTemporaryFile()
        # temp.write(file_input.file.read())
        # res = predict_similar_images(temp.name)
        res=predict_similar_images(Image.open(BytesIO(file_input.file.read())))
        logger.info("prediction done successfully")
        logger.info("response time = "+str(datetime.now() - start))
        return {"prediction": "success", "prediction_result": res}
    except Exception as err:
        if str(err) == "error in model prediction":
            return {"prediction": "failure", "Error": "error in model prediction"}
        logger.error("error in processing the image")
        logger.error(err)
        return {"prediction": "failure", "Error": "error in image pre process"}



@router.post("/image_address")
def get_image_address(path: PathSchema, response: Response):
    try:
        start=datetime.now()
        res = requests.get(path.path, timeout=2)
        logger.info("image is fetched from the address")
        res=predict_similar_images(Image.open(BytesIO(res.content)))
        # temp_dir = tempfile.TemporaryDirectory()
        # urllib.request.urlretrieve(path.path, temp_dir.name + "/input.jpeg")
        # res = predict_similar_images(temp_dir.name + "/input.jpeg")
        logger.info("prediction done successfully")
        response.status_code = 200
        logger.info("response time = "+str(datetime.now()-start))
        return {"prediction": "success", "prediction_result": res}
    except Exception as err:
        if str(err) == "error in model prediction":
            return {"prediction": "failure", "Error":"error in model prediction"}
        logger.error("error in processing the image")
        logger.error(err)
        return {"prediction": "failure", "Error": "error in image pre process"}

@router.post("/base64")
def get_image_base64_file(base64_input:Base64Schema, response: Response):
    try:
        start = datetime.now()
        # byte = file_input.file.read()
        byte=base64_input.base64_string.encode()
        image_byte = base64.b64decode(byte)
        logger.info("image is decoded")
        res = predict_similar_images(Image.open(BytesIO(image_byte)))
        logger.info("prediction done successfully")
        logger.info("response time = "+str(datetime.now() - start))
        response.status_code = 200
        return {"prediction": "success", "prediction_result": res[0],"image_URLs":res[1]}
    except Exception as err:
        if str(err) == "error in model prediction":
            return {"prediction": "failure", "Error": "error in model prediction"}
        logger.error("error in processing the image")
        logger.error(err)
        return {"prediction": "failure", "Error": "error in image pre process"}