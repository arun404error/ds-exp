from deepsearrch.DeepImageSearch1 import SearchImage


# image_list = LoadData().from_folder(folder_list=["/Users/arunkumarc/Desktop/images"])
# Index(image_list).Start()


class Search:
    __instance = None

    def __init__(self):
        self.model = SearchImage()

    @classmethod
    def get_instance(cls):
        if Search.__instance is None:
            Search.__instance = cls()
        return Search.__instance


def predict_similar_images(path):
    search_instance = Search.get_instance()
    try:
        similar_img = search_instance.model.get_similar_images(image_path=path, number_of_images=5)
        return similar_img
    except Exception as e:
        print(e)
        raise Exception("prediction error")
