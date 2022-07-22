# Projeto de Cinema Comunitário
Projeto de aplicação web para gestão de um cinema comunitário feito para as disciplinas de Engenharia de Software I e II, referente ao curso de Bacharelado em Sistemas de Informação pela Universidade Federal do Acre (UFAC). O sistema utiliza o framework Django.

A instalação do Django e das libraries constando em requirements.txt são necessárias para o funcionamento da aplicação e podem ser instaladas com o comando "pip install -r requirements.txt" (Também é necessário o Python 3.4 ou superior)

Usuário e senha dos usuários do sistema:
Usuário Administrador: admin
Senha: admin

Usuário comum: usuario
Senha: senhadousuario

O sistema possui registros do tipo Usuário, Filme, Cartaz e Assento, cada um contendo um formulário.

A página de Usuário é gerenciada pelo Django-admin.

A página index é a página do usuário não autenticado, ele tem acesso apenas aos cartazes.

A página index_auth é a página para o usuário comum ou administrador.

Os formulários só podem acessados por administradores ou usuários autenticados.

Para ter uma lista de filmes, é necessário ter filmes, e para registrar filmes é necessário criar cartazes.

É necessário criar assentos na página de administrador para o cliente poder escolhe-lo.

