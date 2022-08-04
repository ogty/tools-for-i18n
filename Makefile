setup:
	source ./setup.sh

example:
	i18nseg --file ./sample/i18n.yaml --languages ja en --table --empty --reverse

test:
	python3 -m unittest ./tests/test_*.py
