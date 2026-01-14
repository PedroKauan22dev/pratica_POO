import emprestimos
import livros
import usuarios

u1=usuarios.Usuario("Kauan", "001")
u1.criar_usuario()

l1 = livros.Livro("Percy jackson", "Rick riordan", "1234", True)
l1.criar_livro()

e1 = emprestimos.Emprestimo("Percy Jackson", "Kauan", True)
e1.criar_emprestimo()
e1.devolver()
