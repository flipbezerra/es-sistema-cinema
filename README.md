# ProjetoCinemaPy
Projeto de TESI 2

NO REPOSITÓRIO DO GITHUB NÃO POSSUI A PASTA DE INSTALAÇÃO DO DJANGO, ENTÃO É NECESSÁRIO A INSTALAÇÃO
DO DJANGO NO PROJETO

Conta de Administrador

Usuário:Admin
Senha:123

Tem um Forms para Usuário, Cliente, Registro de Filme, e Cartaz

A página de Usuário é gerenciada pelo Django-admin

A página Index é a página do Usuário não autenticado, ele não tem acesso as páginas de forms

A página Index_auth é a página do usuário/administrador

O Usuário não autenticado só tem acessó aos cartazes

Estes forms só podem acessados por Administradores ou Usuários autenticados

Para ter uma lista de filmes, é necessário ter filmes, e para registrar filmes é necessário criar Cartazes

ATENÇÃO: É NECESSÁRIO CRIAR ASSENTOS NO DJANGO-ADMIN para o cliente poder escolhe-los

Cartazes carregam informação da Sala, tais como Horário, Data e o Filme

