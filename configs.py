# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "19234664"))
    API_HASH = getenv("API_HASH", "29c2f3b3d115cf1b0231d816deb271f5")
    BOT_TOKEN = getenv("BOT_TOKEN", "8046575039:AAHGo17CjaAZDXvvcRdRP6jKwx0eMyD_Bp8")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002376137081")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "8058281460").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://reveb96847:reveb96847@cluster0.k7ch6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
