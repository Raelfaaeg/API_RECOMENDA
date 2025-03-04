import tkinter as tk
import json

# Função para carregar o arquivo JSON e exibir as informações
def mostrar_recomendacoes():
    # Carregar o arquivo JSON
    with open('recommendations.json', 'r') as file:
        data = json.load(file)
    
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Recomendações de Materiais")
    
    # Ajustar o tamanho da janela
    janela.geometry("380x600")  

    # Impedir o redimensionamento da janela
    janela.resizable(False, False)  # Não pode redimensionar na horizontal ou vertical

    # Criar o canvas com a scrollbar
    canvas = tk.Canvas(janela)
    scrollbar = tk.Scrollbar(janela, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Criar um frame dentro do canvas
    frame = tk.Frame(canvas)
    
    # Adicionar o frame ao canvas
    canvas.create_window((0, 0), window=frame, anchor="nw")
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Ajustar a largura para que o conteúdo se ajuste horizontalmente
    frame_width = 0  
    contador = 0

    # Iterar sobre os dados e exibir as recomendações
    for professor_id, info in data.items():
        # Criar o título com o id do professor
        label_professor = tk.Label(frame, text=f"Professor ID: {professor_id}", font=('Arial', 14))
        label_professor.grid(row=contador, column=0, padx=10, pady=5, sticky='w')
        
        # Criar as recomendações de materiais
        materiais = "\n".join(info["recommendations"])
        label_materiais = tk.Label(frame, text=f"Materiais recomendados:\n{materiais}", font=('Arial', 12))
        label_materiais.grid(row=contador, column=1, padx=10, pady=5, sticky='w')

        # Ajustar a largura do frame de acordo com o conteúdo
        frame_width = max(frame_width, label_professor.winfo_reqwidth() + label_materiais.winfo_reqwidth() + 20)
        
        contador += 1
    
    # Atualizar a largura do frame para se ajustar ao conteúdo
    frame.config(width=frame_width)
    
    # Atualizar o tamanho do canvas para ajustar o conteúdo
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # Configurar a rolagem para o canvas, mesmo que o mouse esteja no meio das informações
    def on_mouse_wheel(event):
        if event.delta > 0:
            canvas.yview_scroll(-1, "units")
        else:
            canvas.yview_scroll(1, "units")

    janela.bind_all("<MouseWheel>", on_mouse_wheel)

    # Iniciar a interface gráfica
    janela.mainloop()

# Chamar a função para mostrar as recomendações
mostrar_recomendacoes()
