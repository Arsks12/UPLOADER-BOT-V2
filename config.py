import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("6059531879:AAHycaDULmUuyrfQ6sJs5Lr0gvQHi-ZkY9M", "")
    
    API_ID = int(os.environ.get("7068671", 12345))
    
    API_HASH = os.environ.get("76c7e8041eaf80e335127a33b5618c96")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "")

    MAX_RESULTS = "50"
