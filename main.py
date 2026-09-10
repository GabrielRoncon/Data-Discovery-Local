import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pdfplumber
import pytesseract

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()

    if pasta_selecionada:
        label_caminho.config(text=f"Pasta selecionada:\n{pasta_selecionada}")

        print("\n--- PROCESSANDO ARQUIVOS PDF DA PASTA ---")
        for dirpath, dirnames, filenames in os.walk(pasta_selecionada):
            for file in filenames:
                if file.lower().endswith(".pdf"):
                    caminho_completo = os.path.join(dirpath, file)
                    print(f"\n--- Lendo arquivo: {file} ---")

                    try:
                        with pdfplumber.open(caminho_completo) as pdf:
                            for numero_pagina, pagina in enumerate(
                                pdf.pages, start=1
                            ):
                               #Tenta extrair como PDF digital/vetorizado
                                texto_da_pagina = pagina.extract_text()
                                metodo = "Digital"

                                #Se a página for imagem ou escaneada 
                                if (
                                    not texto_da_pagina
                                    or not texto_da_pagina.strip()
                                ):
                                    metodo = "OCR (Escaneado)"
                                    imagem_pagina = pagina.to_image(
                                        resolution=300
                                    ).original
                                    texto_da_pagina = (
                                        pytesseract.image_to_string(
                                            imagem_pagina, lang="por"
                                        )
                                    )

                                if (
                                    texto_da_pagina
                                    and texto_da_pagina.strip()
                                ):
                                    print(
                                        f"[Página {numero_pagina} - Origem: {metodo}]:"
                                    )
                                    print(texto_da_pagina)
                                else:
                                    print(
                                        f"[Página {numero_pagina}]: Nenhum texto identificado."
                                    )

                    except Exception as e:
                        print(f"Erro ao processar o arquivo {file}: {e}")
    else:
        label_caminho.config(text="Nenhuma pasta foi selecionada.")



janela = tk.Tk()
janela.title("Selecionador de Pastas - Data Discovery")
janela.geometry("400x300")

botao = tk.Button(janela, text="Escolher pasta", command=selecionar_pasta)
botao.pack(pady=30)

label_caminho = tk.Label(
    janela, text="Nenhuma pasta selecionada.", wraplength=350
)
label_caminho.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=janela.destroy)
botao_sair.pack(pady=30)

janela.mainloop()