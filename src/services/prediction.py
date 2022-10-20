# import traceback

from deepsearch.DeepImageSearch import SearchImage,LoadData,Index
from loguru import logger
from datetime import  datetime
import pickle
from configs import model_file_conf
# import time


f = open(model_file_conf.link_file_path, "rb")
dict_out = pickle.load(f)
f.close

class Search:
    __instance = None

    def __init__(self):
        self.model = SearchImage()

    @classmethod
    def get_instance(cls):
        if Search.__instance is None:
            Search.__instance = cls()
        return Search.__instance

search_instance = Search.get_instance()

logger.info("singleton object created for search class")

def predict_similar_images(img):
    try:
        start=datetime.now()
        similar_img = search_instance.model.get_similar_images(img=img, number_of_images=5)
        logger.info("model time = "+str(datetime.now()-start))
        # print(similar_img)
        output_list=[similar_img.get(x) for x in similar_img]
        result=[dict_out[x.split('/')[-1]] for x in output_list]
        logger.info("post processing is running")
        return result
    except Exception as e:
        logger.error("some error in model")
        logger.error(e)
        raise Exception("error in model prediction")

