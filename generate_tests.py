import json
import urllib.request

# Чтение промпта
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt_content = f.read()

url = "http://localhost:11434/api/generate"
payload = {
    "model": "qwen2.5-coder:7b",
    "prompt": prompt_content,
    "stream": False
}

print("Отправка запроса к Ollama для генерации тестов...")
req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"}
)

with urllib.request.urlopen(req) as response:
    result = json.loads(response.read().decode("utf-8"))
    generated_code = result.get("response", "")

# Очистка кода от случайных markdown-обёрток
clean_code = generated_code.replace("```python", "").replace("```", "").strip()

# Сохранение готовых тестов
with open("test_json_placeholder.py", "w", encoding="utf-8") as f:
    f.write(clean_code)

print("Тесты успешно сгенерированы в файл test_json_placeholder.py")