# backstage-takehome

## Instructions

Please design and develop a service that I can query that will yield the
difference between 1.) the sum of the squares of the first n natural
numbers and 2.)  the square of the sum of the same first n natural numbers,
where n is guaranteed to be no greater than 100.

Example:

The sum of the squares of the first ten natural numbers is:

```
1^2 + 2^2 + ... + 10^2 = 385
```

The square of the sum of the first ten natural numbers is:

```
(1 + 2 + ... + 10)^2 = 552 = 3025
```

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Queries to `localhost:8000/difference?number=N` should return the following json

```
{
    "datetime": current_datetime,
    "value": solution,
    "number": N,
    "occurrences": occurrences // the number of times N has been requested
}
```

## Setup

```
python3 -m venv venv
source venv/bin/activate
pip install .

```

## Launching

`python -m flask run`

## Running tests

`python setup.py test`