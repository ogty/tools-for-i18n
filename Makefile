setup:
	source ./setup.sh

example:
	i18n segment --file ./sample/public/locales/i18n.yaml --languages ja en --output ./sample/public/locales

test:
	python3 -m unittest ./tests/test_*.py
