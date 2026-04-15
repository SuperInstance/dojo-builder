.PHONY: test build clean
test:
	python3 -m pytest tests/ -v
build:
	@echo "Builder's workshop ready."
clean:
	rm -rf __pycache__ .pytest_cache
