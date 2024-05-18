from enum import Enum
from pydantic import BaseModel, Field
from cat.mad_hatter.decorators import plugin

class NameType(Enum):
    youtube = "youtube.com"
    spotify = "open.spotify.com"
    dezzer = "deezer.com"
    TIDAL = "tidal.com"
    Apple_Music = "music.apple.com"
    Amazon_Music = "music.amazon.it"

class MoodMusicSettings(BaseModel):
    site: NameType = NameType.youtube  # Imposta un valore predefinito, ad esempio YouTube

@plugin
def settings_model():   
    return MoodMusicSettings