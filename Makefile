.PHONY: install
install:
	python -m pip install -r requirements.txt

.PHONY: format
format:
	python -m black .

.PHONY: migrate
migrate:
	python migrate.py

.PHONY: scraper
scraper:
	python scraper.py

.PHONY: start
start:
	uvicorn main:app --reload --host 0.0.0.0 --port 8000