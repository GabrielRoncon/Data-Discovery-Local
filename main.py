import os
import tkinter as tk
from tkinter import filedialog
import pdfplumber

def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    
    if pasta_selecionada:
        label_caminho.config(text=f"Pasta selecionada:\n{pasta_selecionada}")
        
        print("\n--- PROCESSANDO ARQUIVOS PDF DA PASTA ---")
        for dirpath, dirnames, filenames in os.walk(pasta_selecionada):
            for file in filenames:
                if file.lower().endswith(".pdf"):
                    # CORREÇÃO: Juntamos a pasta e o arquivo em um caminho completo
                    caminho_completo = os.path.join(dirpath, file)
                    print(f"\n--- Lendo arquivo: {file} ---")
                    
                    # Passamos a variável com o caminho completo para o pdfplumber
                    with pdfplumber.open(caminho_completo) as pdf:
                        for numero_pagina, pagina in enumerate(pdf.pages, start=1):
                            texto_da_pagina = pagina.extract_text()

                            if texto_da_pagina:
                                print(f"[Página {numero_pagina}]:")
                                print(texto_da_pagina)
    else:
        label_caminho.config(text="Nenhuma pasta foi selecionada.")


janela = tk.Tk()
janela.title("Selecionador de Pastas")
janela.geometry("400x300")

botao = tk.Button(janela, text="Escolher pasta", command=selecionar_pasta)
botao.pack(pady=30)

label_caminho = tk.Label(janela, text="Nenhuma pasta selecionada.", wraplength=450)
label_caminho.pack(pady=10)

botao_sair = tk.Button(janela, text="Sair", command=janela.destroy)
botao_sair.pack(pady=30)

janela.mainloop()