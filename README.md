# Помощник службы поддержки RUTUBE

Сервис генерации ответов для специалистов службы поддержки на основе RAG, ИИ, LLM.

## .env и конфиг

* Нужно добавить токен бота
* Добавить OPENAI_API_KEY для g-eval метрик

[Конфиг файл](/src/config.py)


## Запуск LLM

https://ollama.com/library/mistral-nemo

Запускалось на V100 34gb VRAM.

```bash
ollama run mistral-nemo
```

## Запустить API

```bash
python ./api/api.py
```

## Запуск телеграм бота

```bash
python ./bot/helper_bot.py
```

## Метрики оценки

[Метрики](src/metrics/)

### Retrieval

* Recall
* NDCG

### Generation

[G-eval](https://docs.confident-ai.com/docs/metrics-llm-evals):
* Hallucinations detection
* Answer relevancy
* Documents relevancy