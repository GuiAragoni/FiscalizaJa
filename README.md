# Sistema de Cadastro de Ocorrências Urbanas

## Objetivo do Projeto
Desenvolver um sistema que permita:
- Cidadãos e órgãos governamentais registrarem ocorrências urbanas
- Visualização e gerenciamento eficiente de problemas como:
  - Buracos em vias públicas
  - Problemas de iluminação
  - Acúmulo de lixo
  - Outras questões urbanas

## Escopo do MVP
### 1. Autenticação e Autorização
- Login com token JWT
- CRUD de cidadãos e secretarias
- Controle de acesso diferenciado
### 2. Cadastro de Ocorrências
- CRUD completo de ocorrências
- Upload de fotos
- Geolocalização
### 3. Visualização de Ocorrências
| Visão          | Funcionalidades                           |
|----------------|------------------------------------------|
| Cidadão        | Visualizar ocorrências abertas na cidade |
| Secretaria     | Gerenciamento de todas as ocorrências    |
### 4. Dashboard Analítico
- Gráficos e métricas sobre:
  - Tipos de ocorrências
  - Status
  - Tempo médio de resolução
### 5. Segurança
- Implementar SSH para comunicação segura
### 6. Plataforma Móvel (Avaliação)
- Verificar viabilidade:
  - App nativo
  - PWA (Progressive Web App)
## Stack Tecnológica
### Back-end
- Python ou C#
### Banco de Dados
- SQL Server
### Front-end
- Angular consumindo API REST
