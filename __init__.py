from .node import *

NODE_CLASS_MAPPINGS = {
    # "Set Minio Config": SetMinioConfig,
    "Load Image From Minio": LoadImageFromMinio,
    "Save Image To Minio": SaveImageToMinio,
    "Is Text Is CN": IsTextZhCN,
    "OpenAI API": OpenAIAPI,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    # "Set Minio Config": "Set Minio Config",
    "Load Image From Minio": "Load Image From Minio",
    "Save Image To Minio": "Save Image To Minio",
    "Is Text Is CN": "Is Text Is CN",
    "OpenAI API": "OpenAI API",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
