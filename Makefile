RENPY_HOME=/Applications/renpy-8.3.3-sdk
RENPY=${RENPY_HOME}/renpy.app/Contents/MacOS/renpy

run:
	${RENPY} . run

lint:
	${RENPY} . lint

dists:
	open ${RENPY_HOME}/Fuyu-*-dists

deploy:
	rsync -avz www-data/ fuyu-novel@fuyu.garambrogne.net:/home/fuyu-novel/www-data
