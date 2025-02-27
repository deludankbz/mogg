<p align="center"><img width="80" alt="mogg logo" src="https://raw.githubusercontent.com/deludankbz/mogg/refs/heads/main/extra/mogg-logo.png"></p>

<h2 align="center"> Find your all of your TODO's. </h2>

## Usage/Examples

```bash
$ python3 main.py

@ src/ex.py :: found 4 tasks!

	# TODO: fhosiofs
	# FIX
	# NOTE
	# ERROR:

@ src/utils/fileIO.py :: found 2 tasks!

	# FIX: gitignore might not be present in path; will cause erros
	# TODO: make this bit into a config file

@ README.md :: found 1 tasks!

	# mogg - Find your all of your TODO's
```

## Goals
- <del>Better ignore and extensions</del>
- <del>Better language selection; if none provided check the ones inside cwd</del>
- <del>Better comment handling with REGEX; quite a few languages have multiline comments</del>
- Options to: 
    - <del>Print all comments</del>
    - Print comments only for a selected language

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
