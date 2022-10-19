import tempfile
import urllib.request

from fastapi import APIRouter, UploadFile, Response
from loguru import logger
from src.schemas.request.path_schema import PathSchema
from src.services.prediction import predict_similar_images

router = APIRouter(prefix="/predict")


@router.post("/file")
def get_image_file(file_input: UploadFile):
    try:
        temp = tempfile.NamedTemporaryFile()
        temp.write(file_input.file.read())
        res = predict_similar_images(temp.name)
        logger.info("prediction dyone successfull")
        return {"prediction": "success", "prediction_result": res}
    except Exception as err:
        logger.error("some exception arised")
        return {"prediction": "failure", "Error": err}


# @router.post("/path")
# def get_image_path(path: PathSchema, response: Response):
#     try:
#         res = predict_similar_images(path.path)
#         response.status_code = 200
#         return {"prediction": "success", "prediction_result": res}
#     except Exception as err:
#         print(err)
#         return {"prediction": "failure", "Error": err}


@router.post("/image_address")
def get_image_address(path: PathSchema, response: Response):
    try:
        temp_dir = tempfile.TemporaryDirectory()
        urllib.request.urlretrieve(path.path, temp_dir.name + "/input.jpeg")
        res = predict_similar_images(temp_dir.name + "/input.jpeg")
        logger.info("prediction done successfull")
        response.status_code = 200
        return {"prediction": "success", "prediction_result": res}
    except Exception as err:
        logger.error("some exception arised")
        return {"prediction": "failure", "Error": str(err)}
