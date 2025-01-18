WEB_DIRECTORY = "./web"
from .nodes import UploadAudio, UVR5,PreViewAudio, LoadAudioFromPath

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "UVR5_Node": UVR5,
    "UploadAudio": UploadAudio,
    "PreViewAudio": PreViewAudio,
    "LoadAudioFromPath": LoadAudioFromPath
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "UVR5_Node": "UVR5 Node",
    "UploadAudio": "UploadAudio",
    "PreViewAudio": "PreView Audio",
    "LoadAudioFromPath": "Load Audio From Path"
}