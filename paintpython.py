import tkinter as tk
from tkinter import colorchooser, filedialog

# Configurações do pincel
COR_PADRAO = 'black'
TAMANHO_PADRAO = 5


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Python")

        # Configuração do canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack()

        # Variáveis do pincel
        self.cor_pincel = COR_PADRAO
        self.tamanho_pincel = TAMANHO_PADRAO

        # Vincular eventos do mouse
        self.canvas.bind('<B1-Motion>', self.desenhar)
        self.canvas.bind('<ButtonRelease-1>', self.resetar_coordenadas)

        # Criação dos botões
        self.criar_botoes()

    def criar_botoes(self):
        # Botão para selecionar cor
        botao_cor = tk.Button(self.root, text="Escolher Cor", command=self.escolher_cor)
        botao_cor.pack(side=tk.LEFT)

        # Botão para selecionar forma do pincel
        botao_forma = tk.Button(self.root, text="Escolher Forma", command=self.escolher_forma)
        botao_forma.pack(side=tk.LEFT)

        # Slider para ajustar o tamanho do pincel
        slider_tamanho = tk.Scale(self.root, from_=1, to=50, orient=tk.HORIZONTAL, label="Tamanho do Pincel",
                                  command=self.atualizar_tamanho_pincel)
        slider_tamanho.set(TAMANHO_PADRAO)
        slider_tamanho.pack(side=tk.LEFT)

        # Botão para limpar o canvas
        botao_limpar = tk.Button(self.root, text="Limpar Tela", command=self.limpar_tela)
        botao_limpar.pack(side=tk.LEFT)

        # Botão para salvar a imagem
        botao_salvar = tk.Button(self.root, text="Salvar Imagem", command=self.salvar_imagem)
        botao_salvar.pack(side=tk.LEFT)

    def desenhar(self, event):
        x, y = event.x, event.y
        x1, y1 = (x - self.tamanho_pincel), (y - self.tamanho_pincel)
        x2, y2 = (x + self.tamanho_pincel), (y + self.tamanho_pincel)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.cor_pincel, outline=self.cor_pincel)

    def resetar_coordenadas(self, event):
        self.ultimo_x, self.ultimo_y = None, None

    def escolher_cor(self):
        cor_escolhida = colorchooser.askcolor(title="Escolher Cor")
        if cor_escolhida[1]:
            self.cor_pincel = cor_escolhida[1]

    def escolher_forma(self):
        formas = [('Círculo', 'circle'), ('Retângulo', 'rectangle')]
        forma_escolhida = tk.simpledialog.askstring("Escolher Forma",
                                                    "Digite 'circle' para círculo ou 'rectangle' para retângulo:")
        if forma_escolhida in ['circle', 'rectangle']:
            self.forma_pincel = forma_escolhida

    def atualizar_tamanho_pincel(self, tamanho):
        self.tamanho_pincel = int(tamanho)

    def limpar_tela(self):
        self.canvas.delete("all")

    def salvar_imagem(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png")])
        if file_path:
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    paint_app = PaintApp(root)
    root.mainloop()
