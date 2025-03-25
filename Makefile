# export the tools , datetimestamped
yaml:
	python export_single.py > data/yaml/tools-landscape-$(shell date +%Y-%m-%d-%H-%M-%S).yaml

repo:
	rm -rf ./data/repo
	python export_split.py
	cp docs/repo_readme.md data/repo/readme.md

icons:
	python download_icons.py

