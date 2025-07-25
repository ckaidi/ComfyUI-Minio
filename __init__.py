from .node import *

NODE_CLASS_MAPPINGS = {
    # "Set Minio Config": SetMinioConfig,
    "Load Image From Minio": LoadImageFromMinio,
    "Save Image To Minio": SaveImageToMinio,
    "Is Text Is CN": IsTextZhCN,
    "OpenAI API": OpenAIAPI,
    "Dify Cn TO En": DifyCn2En,
    "Dify Image Describe": DifyImageDescribe,
    "Dify Image Describe En": DifyImageDescribeEn,
    "Upload Image To Nocodb": UploadImageToNocodb,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    # "Set Minio Config": "Set Minio Config",
    "Load Image From Minio": "Load Image From Minio",
    "Save Image To Minio": "Save Image To Minio",
    "Is Text Is CN": "Is Text Is CN",
    "OpenAI API": "OpenAI API",
    "Dify Cn TO En": "Dify Cn TO En",
    "Dify Image Describe": "Dify Image Describe",
    "Dify Image Describe En": "Dify Image Describe En",
    "Upload Image To Nocodb": "Upload Image To Nocodb",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
