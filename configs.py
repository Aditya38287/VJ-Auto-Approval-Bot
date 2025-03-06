# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "22036935"))
    API_HASH = getenv("API_HASH", "e563640ea8c2dc61e122ff2e0c510daf")
    BOT_TOKEN = getenv("BOT_TOKEN", "8168144620:AAEpd3B29f15yaup4KCqk5u7c4dOMxBEtCY")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002441315515")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "1432279675").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://adipatel2463:adipatel2463@cluster0.ecndm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
