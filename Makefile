CLUSTER?=

.PHONY: deploy
deploy:
	python3 ./scripts/main.py --cluster-name ${CLUSTER}

dryrun:
	python3 ./scripts/dryrun.py --cluster-name ${CLUSTER}

diff:
	python3 ./scripts/diff.py --cluster-name ${CLUSTER}
