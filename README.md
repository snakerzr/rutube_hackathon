# Помощник службы поддержки RUTUBE

Сервис генерации ответов для специалистов службы поддержки на основе RAG, ИИ, LLM.

TELEGRAM BOT: https://t.me/RutubeHelperBot

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

## Модели

* e5_large_finetuned - [ссылка](https://drive.google.com/file/d/1aLjDaNO8LifO_p_22J_UWzGvDh3Ju8pd/view) дообученная модель-эмбеддер для поиска. В архиве есть readme.md, с кодом обучения.
* clf_one_opt - [ссылка](https://disk.yandex.ru/d/KRz3FTQQfvA_gw) модель классификатор 1 тематики
* clf_two_opt - [ссылка](https://disk.yandex.ru/d/wwwiydPi2rkG4g) модель классификатор 2 тематики