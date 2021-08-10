.PHONY: deploy
deploy:
	python3 ./scripts/main.py

dryrun:
	python3 ./scripts/dryrun.py

diff:
	python3 ./scripts/diff.py
