setup:
	source ./setup.sh

sample:
	i18nseg -f ./sample/i18n.yaml -l ja en -t

usage:
	@python3 -c "from settings import USAGE; print(USAGE)"

options:
	@python3 -c "from settings import OPTIONS; print(OPTIONS)"

update:
	@awk -f ./update.awk README.txt > README.md
