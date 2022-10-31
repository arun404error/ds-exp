# import traceback
import traceback

from deepsearch.DeepImageSearch import SearchImage,LoadData,Index
from loguru import logger
from datetime import  datetime
import pickle
from configs import model_file_conf
# import time


f = open(model_file_conf.link_file_path, "rb")
dict_out = pickle.load(f)
f.close()
f = open(model_file_conf.item_code_file_path, "rb")
item_code = pickle.load(f)
f.close()

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
        output_list=[similar_img.get(x) for x in similar_img]
        print(output_list)
        result=[dict_out[x.split('/')[-1]][0] for x in output_list]
        # result= ['https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full///90/MTA-10295144/eiger_eiger_porter_t-shirt_-_black_full01_e6rqkq03.jpg', 'https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full///102/MTA-10295144/brd-44261_360-degrees-polypro-thermal-top-blk-2xl_full01.jpg', 'https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full///92/MTA-19309410/br-m036969-16674_champion-men-s-jp-champion-3-4-tee-gray-x-navy_full02.jpg', 'https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full///107/MTA-22177988/br-m036969-02353_new-balance-accelerate-long-sleeve-men-s-t-shirt-black_full01.jpg', 'https://www.static-src.com/wcsstore/Indraprastha/images/catalog/full///104/MTA-35993651/brd-69012_baju-salur-york-atasan-fashion-kaos-pria-lengan-panjang_full04.jpg']
        logger.info("post processing is running")
        logger.debug(result)
        return set([x.split("/")[-2] for  x in result])
    except Exception as e:
        traceback.print_exc(e)
        logger.error("some error in model")
        logger.error(e)
        raise Exception("error in model prediction")
