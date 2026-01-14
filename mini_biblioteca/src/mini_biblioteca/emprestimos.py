class Emprestimo:
    def __init__(self, livro, usuario, ativo=True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
    
    def criar_emprestimo(self):
        print("\nLivro: {}\nUsuario: {}\nEstado: {}\n".format(self.livro, self.usuario, self.ativo))

    def devolver(self):
        self.ativo = False
        print("Livro: {}\nUsuario: {}\nEstado: {}\n".format(self.livro, self.usuario, self.ativo))




