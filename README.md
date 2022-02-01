# Projeto de Cinema Comunitário
Projeto de Engenharia de Software I e II

A instalação do Django e das libraries constando em requirements.txt são necessárias para o funcionamento da aplicação e podem ser instaladas com o comando "pip install -r requirements.txt"

Usuário e senha dos usuários do sistema:
Usuário Administrador: admin
Senha: admin

Usuário comum: usuario
Senha: senhadousuario



O sistema possui registros do tipo Usuário, Filme, Cartaz e Assento, cada um contendo um formulário.

A página de Usuário é gerenciada pelo Django-admin.

A página index é a página do usuário não autenticado, ele tem acesso apenas aos cartazes.

A página index_auth é a página do usuário comum/administrador.

Os formulários só podem acessados por administradores ou usuários autenticados.

Para ter uma lista de filmes, é necessário ter filmes, e para registrar filmes é necessário criar cartazes.

É necessário criar assentos na página de administrador para o cliente poder escolhe-lo.

