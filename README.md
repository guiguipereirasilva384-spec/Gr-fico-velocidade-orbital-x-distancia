<img width="1500" height="826" alt="WhatsApp Image 2026-07-07 at 17 41 03" src="https://github.com/user-attachments/assets/d99aa81e-21b1-40c4-bf0e-e1c46f2ebd48" /># Simulação da Velocidade Orbital da Terra

Projeto desenvolvido em **Python** para calcular e representar graficamente a velocidade orbital necessária para que um objeto permaneça em órbita da Terra, em função da distância ao centro do planeta.

## 📖 Sobre o projeto

Este projeto aplica conceitos de **Gravitação Universal**, **Mecânica Orbital** e **Programação Científica** para modelar matematicamente a relação entre a velocidade orbital e a distância ao centro da Terra.

O programa realiza milhares de cálculos automaticamente e utiliza a biblioteca **Matplotlib** para representar os resultados em um gráfico.

O objetivo é demonstrar como conceitos físicos podem ser implementados computacionalmente utilizando Python.

---

## 🧮 Modelo Matemático

A velocidade orbital é obtida pela igualdade entre a força gravitacional e a força centrípeta:

\[
\frac{GMm}{r^2}=\frac{mv^2}{r}
\]

Isolando a velocidade, obtém-se:

\[
v=\sqrt{\frac{GM}{r}}
\]

onde:

- **G** = Constante da Gravitação Universal
- **M** = Massa da Terra
- **r** = Distância ao centro da Terra

---

## ⚙️ Funcionamento

O algoritmo executa as seguintes etapas:

1. Define as constantes físicas.
2. Gera milhares de valores para a distância ao centro da Terra.
3. Calcula a velocidade orbital correspondente para cada distância.
4. Armazena os resultados em listas.
5. Gera um gráfico utilizando Matplotlib.

---

## 🛠️ Tecnologias utilizadas

- Python
- Matplotlib
- Math

---

## 📂 Estrutura do projeto

```
Projeto/
│
├── main.py
├── README.md
└── docs/
    └── grafico.png
```

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
```

Entre na pasta:

```bash
cd NOME-DO-REPOSITORIO
```

Instale as dependências:

```bash
pip install matplotlib
```

Execute:

```bash
python main.py
```

---

## 💡 Conceitos aplicados

- Programação em Python
- Programação Científica
- Gravitação Universal
- Mecânica Orbital
- Modelagem Matemática
- Visualização de Dados
- Algoritmos
- Automação de cálculos numéricos

---

## 🎯 Objetivo

Este projeto foi desenvolvido com o objetivo de aplicar conhecimentos de programação na resolução de um problema clássico da engenharia e da física, demonstrando a integração entre modelagem matemática, desenvolvimento de algoritmos e visualização de dados.

---

## 👨‍💻 Autor

**Guilherme P. Silva**

Estudante de Engenharia de Controle e Automação

LinkedIn: www.linkedin.com/in/guilherme-p-silva-5b218a333

GitHub: https://github.com/guiguipereirasilva384-spec
