# pdf_dir_merge
Merge PDF file by deep level

## Usage
### install dependencies
You should install pipenv before.
1. install pip dependencies
2. start pipenv shell
3. start `main.py`
```bash
$ pipenv install
$ pipenv shell
$ python main.py
```

## Option
```bash
$ python main.py --help
usage: main.py [-h] [-l LEVEL] [--name NAME] dir dest

positional arguments:
  dir                   Target directory in here.
  dest                  Destination filename in here.

optional arguments:
  -h, --help            show this help message and exit
  -l LEVEL, --level LEVEL
                        Directory level in here. Default is 1.
  --name NAME           Target file's name in here(e.g. foo.pdf). Default is
                        unique.

```

## Contribute
Welcome!
Plese go to [Issues](./issues) or [Pull requests](./pulls)

## License
See [here](./LICENSE.txt)

