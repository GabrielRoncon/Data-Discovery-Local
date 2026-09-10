from PIL import Image
import pytesseract

# (No Windows) Se o Tesseract não estiver no PATH, indicamos o executável:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extrair_texto_de_imagem(caminho_imagem):
    # 1. Abre a imagem usando a biblioteca PIL
    imagem = Image.open(caminho_imagem)
    
    # 2. Executa o OCR especificando o idioma português ('por')
    texto_extraido = pytesseract.image_to_string(imagem, lang='por')
    
    return texto_extraido