# from fastapi import File, UploadFile

class APIController:

    def index():

        data = {
            "message" : "OK!"
        }

        return data