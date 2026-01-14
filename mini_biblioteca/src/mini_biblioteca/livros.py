class Livro ():
    def __init__(self, titulo, autor, codigo, disponivel=True):

        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel
    
    def criar_livro(self):
        print("Titulo: {}\nAutor: {}\nCodigo: {}, Disponível: {}".format(
            self.titulo, self.autor, self.codigo, self.disponivel))
    

