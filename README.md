<p align="center"><img width="80" alt="mogg logo" src="https://raw.githubusercontent.com/deludankbz/mogg/refs/heads/main/extra/mogg-logo.png"></p>

<h2 align="center"> Find your all of your TODO's. </h2>

## Usage/Examples

```bash
$ python3 src/main.py
@ src/ex.py :: found 7 comments!

	# TODO: fhosiofs
	# FIX
	# NOTE
	# ERROR:


@ src/utils/config.py :: found 1 comments!

	# FIX: put source files in a fixed place


@ src/utils/tasker.py :: found 4 comments!

	# FIX check for empty buffer
	# FIX choose patterns correc.


@ src/utils/fileIO.py :: found 2 comments!

	# FIX NOTE some files don't have extensions
	# NOTE that's what i meant


@ src/main.py :: found 34 comments!

	# TODO: progress bar to indicate where processing is happening
```

## Goals

- <del>Better ignore and extensions</del>
- <del>Better language selection; if none provided check the ones inside cwd</del>
- <del>Better comment handling with REGEX; quite a few languages have multiline comments</del>
- Store source files in a separated folder
- Colored TODO; FIX; NOTE; etc...
- Options to: 
    - <del>Print all comments</del>
    - Print comments only for a selected language

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
