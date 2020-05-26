.PHONY: answers
answers: guard-ROUND
	python python/answers.py ${ROUND}

assemble:
	python python/assembler.py

run:
	nginx

# this is flat-out juju
# https://stackoverflow.com/a/7367903
guard-%:
	@ if [ -z "${${*}}" ]; then \
			echo "I need to know which $* you want"; \
			exit 1; \
	fi
