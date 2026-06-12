import requests
from PIL import Image, ImageDraw, ImageFont
import datetime

# Scarica i dati delle estrazioni
url = "https://www.datasport.it/estrazioni-lotto-10elotto-superenalotto-11-giugno-2026-con-numeri-vincenti-caldi-terni-da-seguire.html"
r = requests.get(url)
open("estrazioni_raw.html", "wb").write(r.content)

# Carica il template
img = Image.open("template.png")
draw = ImageDraw.Draw(img)

# Font (usa un font standard GitHub)
font = ImageFont.load_default()

# Scrivi la data
oggi = datetime.date.today().strftime("%d/%m/%Y")
draw.text((20, 20), f"Estrazioni del {oggi}", fill="black", font=font)

# Salva immagine finale
img.save("estrazioni.png")
