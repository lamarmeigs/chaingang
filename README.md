# Chain Gang

Largely just a [`markovify`](https://github.com/jsvine/markovify) CLI, this repo was intended to tinker with all things Markov Chains.


## Installation

This project uses [`poetry`](https://poetry.eustace.io/) to manage dependencies. (A seperately-established virtualenv is recommended.)
```bash
$ poetry install
```


## Usage

The chaingang script provides two basic behaviors: creating models of one or many texts, and generating random sentences from those models.

### Build Models
To build a model off a single corpus simply call the `model` subcommand:
```bash
$ ./chaingang.py model -c corpora/alices_adventures_in_wonderland.txt
```

Multiple corpora may be combined into a single model, establishing their relative weights with the `-w` flag:
```bash
$ ./chaingang.py model -c corpora/alices_adventures_in_wonderland.txt corpora/king_james_bible.txt -w 5 1
```

Default configuration creates a model using a state size of 2, and emits it to stdout. To alter this behavior, use the `-s` (`--state-size`) or `-o` (`--outfile`) flags:
```bash
$ ./chaingang.py model -c corpora/alices_adventures_in_wonderland.txt -s 5 -o models/alice.json
```

Invoke `--help` for more options

### Generate Sentences
By default, the `generate` subcommand reads a model from stdin, then outputs 3 randomly-generated sentences.
```bash
$ cat models/alice.json | ./chaingang.py generate 
```

One (or more) models can instead be read from files. The number of sentences generated can also be modified.
```bash
./chaingang.py generate -m models/alice.json models/shakespeare.json -n 5
```
