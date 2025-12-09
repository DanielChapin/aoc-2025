# Day 1

I did this day in Python as a demonstration of some Python features I think are important for good Python code quality.
The CLI I implemented is simple and allows for the user to specify an input file and whether or not to log the steps.

## Part 1

```sh
$ python3 p1.py --help
usage: p1.py [-h] [--debug | --no-debug | -d] input_file

positional arguments:
  input_file            File containing Elf safe instructions.

options:
  -h, --help            show this help message and exit
  --debug, --no-debug, -d
                        Print out steps.
```

## Part 2

Part 2 has the same general structure, CLI interface, and the same time complexity.
The functioning of the algorithm is documented in the code.

Also... in case you missed it...
```sh
echo -n 434C49434B | xxd -r -p
```
