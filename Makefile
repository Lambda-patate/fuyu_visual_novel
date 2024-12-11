RENPY_HOME=/Applications/renpy-8.3.3-sdk
RENPY=${RENPY_HOME}/renpy.app/Contents/MacOS/renpy
VERSION=$(shell python3 -c "import re;print(re.search(r'define +config.version += +\"(.*?)\"',open('game/options.rpy').read(),re.M).group(1))")

run:
	${RENPY} . run

lint:
	${RENPY} . lint


deploy:
	rsync -avz www-data/ fuyu-novel@fuyu.garambrogne.net:/home/fuyu-novel/www-data

web:
	@echo ${VERSION}
	rm -rf www-data/novel
	mkdir -p www-data/novel
	cp -r "${RENPY_HOME}/Fuyu-${VERSION}-dists/Fuyu-${VERSION}-web/" www-data/novel
