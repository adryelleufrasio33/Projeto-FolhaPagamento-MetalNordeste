Projeto de Folha de Pagamento – Metal Nordeste

Este repositório contém o início do desenvolvimento de um sistema próprio de folha de pagamento para a Metal Nordeste, criado inicialmente em Python e executado via terminal.
O objetivo principal é permitir que a empresa tenha autonomia total no cálculo da folha, reduzindo dependência de terceiros e garantindo agilidade, clareza e confiabilidade nos valores pagos aos colaboradores.

Objetivo do Projeto

A proposta central é construir um sistema completo capaz de:

Calcular a folha de pagamento de cada funcionário.

Aplicar corretamente todas as regras de descontos obrigatórios:

INSS (cálculo progressivo)

FGTS

Vale-transporte

Insalubridade

Outros descontos legais

Considerar consignados e deduções específicas de cada colaborador.

Automatizar uma atividade que hoje depende do envio manual ao contador.

No momento, o sistema está na fase inicial, focado na estruturação das funções de cálculo e no CRUD de funcionários via terminal.

Tecnologias e Ferramentas Planejadas
Fase Atual (Terminal / Python)

Python 3

Estrutura modular com funções específicas:

Cálculo de INSS (progressivo)

Cálculo de FGTS

Cálculo de insalubridade

Cálculo de vale-transporte

Cálculo do salário líquido

CRUD básico de funcionários

Fase Intermediária (Banco de Dados)

Implementação de um banco de dados relacional usando:

SQL Server

Armazenamento de funcionários, cargos, salários e histórico de folhas

Tabelas normalizadas com integridade referencial

Fase Final (Interface Completa)

Construção de uma aplicação completa com:

Frontend em HTML + CSS (focado em simplicidade e objetividade)

Backend em Python, estruturado para atender as regras e necessidades reais da Metal Nordeste

API para integração com futuros módulos internos da empresa

Tela intuitiva para:

Cadastrar funcionários

Gerar folha mensal

Visualizar relatórios

Exportar dados

Motivação

A Metal Nordeste depende hoje do envio ao contador para realizar a folha mensal.
Esse projeto busca:

Ganhar independência operacional

Reduzir erros manuais

Aumentar a agilidade no fechamento da folha

Aprimorar o controle interno

Oferecer transparência sobre todos os valores descontados e pagos

Além disso, o desenvolvimento serve como aprimoramento contínuo das habilidades técnicas do autor, alinhando estudos de programação com necessidades reais da empresa.

Estrutura Atual do Código

Organização modular das funções de cálculo

CRUD inicial de funcionários

Lógica completa de INSS progressivo

Preparação para expandir para FGTS, IRRF e demais cálculos

Evolução Prevista

Finalizar todos os cálculos obrigatórios

Criar módulo de geração automática da folha

Implementar SQL Server para persistência

Criar a interface completa (frontend + backend)

Adicionar relatórios, logs e histórico de meses anteriores

Automatizar exportações e envio interno

Status do Projeto

Em desenvolvimento.
Atualmente na versão terminal e em evolução constante.
