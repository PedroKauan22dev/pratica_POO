class Usuario ():
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario

    def criar_usuario(self):
        print("Usuario: {}\nID: {}".format(self.nome, self.id_usuario))

