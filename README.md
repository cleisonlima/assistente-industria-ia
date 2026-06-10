# 🚀 Assistente Inteligente para a Indústria 4.0

## Sobre o Projeto

O Assistente Inteligente para a Indústria 4.0 é uma solução baseada em Inteligência Artificial Generativa desenvolvida para apoiar empresas e profissionais na consulta rápida de informações técnicas, procedimentos operacionais, normas, manuais e documentos corporativos.

O projeto foi concebido como uma aplicação prática de IA voltada para os desafios da Indústria 4.0, utilizando arquiteturas modernas de backend e frontend preparadas para integração com modelos de linguagem (LLMs), bancos vetoriais e sistemas de recuperação inteligente de conhecimento (RAG).

---

## Objetivos

* Facilitar o acesso ao conhecimento organizacional.
* Reduzir o tempo de busca por informações técnicas.
* Apoiar a tomada de decisão.
* Promover a transformação digital da indústria.
* Demonstrar aplicações práticas de Inteligência Artificial Generativa.

---

## Arquitetura da Solução

```text
Usuário
   │
   ▼
Frontend (Streamlit)
   │
   ▼
Backend (FastAPI)
   │
   ▼
Serviços de IA
   │
   ├── OpenAI
   ├── LangChain
   ├── ChromaDB
   └── RAG
```

---

## Tecnologias Utilizadas

### Backend

* Python 3.12
* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Inteligência Artificial

* OpenAI API
* LangChain
* Retrieval-Augmented Generation (RAG)

### Banco de Dados

* ChromaDB
* PostgreSQL (planejado)

### DevOps

* Docker
* GitHub

---

## Funcionalidades Atuais

* API REST utilizando FastAPI.
* Interface Web utilizando Streamlit.
* Estrutura modular preparada para IA Generativa.
* Arquitetura escalável para integração com serviços de IA.

---

## Funcionalidades Planejadas

* Upload de documentos PDF.
* Vetorização de documentos.
* Banco vetorial ChromaDB.
* Chat inteligente baseado em documentos.
* Sistema RAG.
* Dashboard de utilização.
* Controle de usuários.
* Histórico de conversas.
* Integração com OpenAI GPT.
* Dockerização completa.

---

## Estrutura do Projeto

```text
assistente-industria-ia/
│
├── backend/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   └── models/
│
├── frontend/
│   ├── app.py
│   └── pages/
│
├── data/
│
├── scripts/
│
├── docs/
│
├── docker-compose.yml
├── README.md
└── .env.example
```

---

## Como Executar

### Clonar o projeto

```bash
git clone https://github.com/cleisonlima/assistente-industria-ia.git
```

### Criar ambiente virtual

```bash
python -m venv venv
```

### Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Instalar dependências

```bash
pip install -r backend/requirements.txt
```

### Executar API

```bash
cd backend
uvicorn main:app --reload
```

Acesse:

```text
http://localhost:8000
```

### Executar Frontend

```bash
cd frontend
streamlit run app.py
```

Acesse:

```text
http://localhost:8501
```

---

## Aplicação na Indústria

A solução pode ser utilizada para:

* Consulta de procedimentos operacionais.
* Consulta de normas técnicas.
* Apoio à manutenção industrial.
* Gestão do conhecimento corporativo.
* Capacitação de colaboradores.
* Transformação digital de processos.

---

## Autor

**José Cleison de Lima**

Especialista em Inteligência Artificial, Ciência de Dados e Transformação Digital.

Professor de Tecnologia da Informação no SENAI Pernambuco.

GitHub:
https://github.com/cleisonlima

LinkedIn:
https://www.linkedin.com/in/cleison-lima

---

## Licença

Projeto desenvolvido para fins educacionais, pesquisa e demonstração tecnológica.

