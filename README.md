# Автогенерация API-автотестов с использованием Ollama в Docker

Проект содержит решение домашнего задания по развёртыванию локальной языковой модели Ollama в Docker-контейнере и автоматической генерации функциональных и контрактных API-автотестов для сервиса [JSONPlaceholder](https://jsonplaceholder.typicode.com/) на базе стека **Python 3 + Pytest + Requests**.

---

## 📁 Структура проекта

```text
.
├── docker-compose.yml        # Конфигурация для запуска Ollama в Docker
├── prompt.md                 # Промпт для генерации кода автотестов
├── test_jsonplaceholder.py   # Сгенерированные автотесты Python
├── requirements.txt          # Зависимости Python
└── README.md                 # Документация проекта