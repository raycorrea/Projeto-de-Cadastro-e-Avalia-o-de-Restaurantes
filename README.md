# 🍽️ Projeto Sistema de Avaliação de Restaurantes

Este projeto é um sistema simples desenvolvido em Python para gerenciar e avaliar restaurantes. Ele foi criado com foco em aplicar os conceitos de **Programação Orientada a Objetos (POO)**, incluindo encapsulamento, métodos de classe, propriedades e listas de instâncias.

## 📌 Funcionalidades

- Cadastro de restaurantes com nome e categoria
- Ativação e desativação do status do restaurante
- Recebimento de avaliações com nome do cliente e nota
- Cálculo automático da média das avaliações
- Listagem de todos os restaurantes com suas informações formatadas

---

## 🧠 Tecnologias e Conceitos Utilizados

- Python 3
- Paradigma de Programação Orientada a Objetos (POO)
- Modularização com `import` e separação de arquivos
- List comprehension e propriedades
- Uso de métodos de classe para gerenciamento global

---

## 📂 Estrutura do Projeto

```bash
.
├── main.py
├── modelos
│   ├── __init__.py
│   ├── restaurante.py
│   └── avaliacao.py
💡 Exemplo de Uso
python
Copiar
Editar
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Rayan', 9)
restaurante_praca.receber_avaliacao('Lívia', 10)

Restaurante.listar_restaurantes()
⚔️ Desafios Enfrentados
Durante o desenvolvimento, enfrentei alguns desafios importantes:

Entendimento da estrutura de classes e atributos privados: No início foi confuso usar underline (_) para atributos, mas entendi seu papel na proteção de dados internos.

Validação das notas de avaliação: Inicialmente o sistema aceitava qualquer valor, mas implementei uma verificação para que apenas notas entre 1 e 5 fossem aceitas.

Formatação da listagem dos restaurantes: O alinhamento das colunas exigiu testes com .ljust() para garantir que tudo aparecesse de forma organizada no terminal.

Organização do código em módulos separados: Tive que entender como importar corretamente arquivos entre diretórios usando Python.

✅ Conclusão
Esse projeto me ajudou muito a consolidar os fundamentos de POO em Python. Foi um excelente exercício de lógica, estrutura e boas práticas de organização de código. Agora me sinto mais confiante para partir para projetos maiores e mais robustos.

🚀 Próximos Passos
Adicionar interface gráfica com Tkinter ou web com Flask

Armazenamento dos dados em um banco SQLite

Implementação de testes automatizados com pytest

📧 Desenvolvido por Rayan Correa
