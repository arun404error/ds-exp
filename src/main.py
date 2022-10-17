from fastapi import FastAPI
from src.routers import sys_info,prediction_route

app=FastAPI()

app.include_router(sys_info.router)
app.include_router(prediction_route.router)


# img_plot=SearchImage().plot_similar_images(image_path=image_list[0])