from transformers import pipeline

# Load models only once
question_generator = pipeline("text2text-generation", model="google/flan-t5-large")
suggested_answer_generator = pipeline("text2text-generation", model="google/flan-t5-large")
answer_evaluator = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
sentiment_analyzer = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
