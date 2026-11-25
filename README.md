![PDV](static/imagens/logos/logo.jpg)

# **PDV SV MAXGUI-2**

## 🚀 Sobre o projeto

O **PDV SV MAXGUI-2** é um sistema de ponto de venda em desenvolvimento com Flask.

O objetivo é evoluir para uma aplicação completa de gestão comercial para pequenos e médios negócios, incluindo controle de vendas, estoque e usuários.

O PDV SV MAXGUI-2 é um sistema gratuito para uso em pequenos, médios e grandes negócios.
---

## ⚙️ Status das funcionalidades

### 🟢 Implementadas
- Estrutura base do sistema
- Sistema de páginas (Flask)

### 🟡 Em desenvolvimento
- Login de usuários
- Sistema de propagandas em slide
- tradução para diversos idiomas (i18n)

### 🔴 Planejadas
- Controle de estoque
- Sistema de vendas
- Relatórios
- Exportação de PDF
- Gráficos
- API de integração

---

## 🧠 Tecnologias utilizadas

- Python 🐍
- Flask 🌐
- SQLite 🗄️
- HTML5
- CSS3
- JavaScript

---

## 📁 Estrutura do projeto

```
site_PDV_SV_MAXGUI-2/
    templates/
        privacidade.html
        sites_SV.html
        cookies.html
        doacao.html
        termos.html
        sobre.html
        inicio.html
        auth/
            entrar.html
            cadastrar.html
            recupera_senha.html
        includes/
            footer.html
            header.html
            banner_cookies.html
            propagandas_slide.html
            em_desenvolvimento.html
        configuracoes/
            configuracoes.html
            idioma_config.html
        erros/
            400.html
            401.html
            403.html
            404.html
            408.html
            410.html
            423.html
            429.html
            500.html
            502.html
            503.html
            504.html
        internal/
            internal_report.html
            rotas.html
    config-json/
        versao.json
        idomas-json/
            pt-br.json
            en.json
            es.json
    static/
        css/
            componentes/
                botoes.css
            paginas/
                internal_report.css
            responsivo.css
            fundos.css
            cores.css
            main.css
        imagens/
            propagandas/
                xxxxxxxxxx.jpg.ico.jpeg...
            usuarios/
                xxxxxxxxxx.jpg.ico.jpeg...
            fundos/
                xxxxxxxxxx.jpg.ico.jpeg...
            logos/
                xxxxxxxxxx.jpg.ico.jpeg...
            icones/
                xxxxxxxxxx.jpg.ico.jpeg...
            prints/
                xxxxxxxxxx.jpg.ico.jpeg...
        js/
            propagandas_slide.js
            internal_report.js
            relatorios.js
            produtos.js
            cookies.js
            vendas.js
            main.js
            login.js
        sons/
            xxxxxxxxxx.wav.flac.mp3.m4a...
    dados/
        banco.py
        backup.py
    managers/
        login.py
        relatorios.py
        produtos.py
        configuracoes.py
        internal_report.py
    SV_AI/
    docs/
        anotação_PDV.txt
    blueprints/
        interno/
            interno.py
        mensagens/
            errors.py
        login_register/
            login_register.py
        pages/
    app.py
    converte_favicon.py
    README.md
    LICENSE
    requirements.txt
```
---

## 📸 Demonstração do sistema

### 🏠 Tela inicial
    (quando disponivel será adicionadas as imagens...)

### banner cookies
    (quando disponivel será adicionadas as imagens...)

---

## ▶️ Como executar o projeto

### 1. Instalar dependências

```bash

```
---

### 2. Rodar o sistema

```bash
python app.py
```
---

### 3. Acessar no navegador

```
http://127.0.0.1:5000
```
---

## 📌 Informações do projeto

- **Nome: PDV SV MAXGUI-2**
- **Tipo:** Sistema Web
- **Status:** Em desenvolvimento (Alpha)
- **Início:** 25/01/2026
- **Desenvolvedor:** SER VIVO (SVDev2)
---

## 🧠 Arquitetura

- Frontend: HTML, CSS, JS
- Backend: Flask (Python)
- Banco de dados: SQLite
- Organização: modular (managers, templates, static)

---

## 📚 bibliotecas

As bibliotecas e módulos abaixo são utilizados no projeto ou estão previstos para futuras funcionalidades.

🟢 Utilizadas

    📦 Bibliotecas externas

        - Flask
        - Pillow
        - ReportLab

    🐍 Biblioteca padrão do Python

        - email.mime
        - datetime
        - hashlib
        - secrets
        - sqlite3

🟡 Possivelmente serão utilizadas

    📦 Bibliotecas externas

        - 

    🐍 Biblioteca padrão do Python

        - dataclsss
        - webbrowser
        - smtplib
        - json
        - csv
        - os

---

## 🤝 Contribuição

### Contribuições são bem-vindas!

Se quiser ajudar no projeto:

- Faça um fork do repositório
- Crie uma branch com sua melhoria
- Envie um pull request

Sugestões, ideias e melhorias também podem ser enviadas via Issues.

---

## 📜 Licença

Este projeto está licenciado sob a **Apache License 2.0**.

Você pode usar, modificar e distribuir este projeto, desde que siga os termos da licença e mantenha os devidos créditos ao autor.

---

## 📄 Observações

Este projeto está em fase inicial de desenvolvimento e passará por melhorias contínuas ao longo do tempo.

---
versão 0.3.103 Alpha
---

© 2026 PDV SV MAXGUI-2.