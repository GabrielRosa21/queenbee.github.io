from PIL import Image

# Carregar a imagem original
img = Image.open(r"C:\Users\gabri\Downloads\queenbi\img\iso9001.png")

# Redimensionar a imagem para 1600x830
img_resized = img.resize((2560, 1200))

# Salvar a imagem redimensionada
img_resized.save(r"C:\Users\gabri\Downloads\queenbi\img\iso9001g.png")
