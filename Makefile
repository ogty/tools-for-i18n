setup:
	source ./setup.sh

sample:
	i18nseg --file ./sample/i18n.yaml --languages ja en --table --empty

usage:
	@python3 -c "from settings import USAGE; print(USAGE)"

options:
	@python3 -c "from settings import OPTIONS; print(OPTIONS)"

update:
	@awk -f ./update.awk README.txt > README.md
