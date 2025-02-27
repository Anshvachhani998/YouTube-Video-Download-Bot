import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7277194738:AAHrewQsvKcPqeXYeMIbSk-nyUjgJ14kW8U")
    API_ID = int(os.environ.get("API_ID", "8012239"))
    API_HASH = os.environ.get("API_HASH", "171e6f1bf66ed8dcc5140fbe827b6b08")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "-1002379643238")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
