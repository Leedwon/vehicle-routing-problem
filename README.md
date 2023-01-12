## Getting started

Before running project locally:
1. Set up virtual environment via command-line (see [docs](https://docs.python.org/3/library/venv.html)). For no brainer solution just run `python3 -m venv env` on Unix/macOS and `py -m venv env` on Windows.
2. Install requirements by running `env/bin/pip install -r requirements.txt` 
   (also check subpackages if the contain their own `requirements.txt` file and install them, if they're present).

### Running tests

To run tests simple call `pytest tests`

## Problem

VRP is a problem which asks:

What is the optimal set of routes for a fleet of vehicles to traverse in order to deliver to a given set of customers?

## Solution

This project tries to solve VRP by using genetic algorithm.

### Encoding of solutions

The algorithm uses a method of encoding called random keys developed by Bean.

It will help with producing infeasible solutions during reproduction.

To visualize this problem let's consider a fleet of 1 vehicle and 4 customers. 

We want to perform reproduction for following parents:

<pre>
parent1: (1, 4, 2, 3)
parent2: (2, 4, 1, 3)
</pre>

We'll select a gene from parent with a certain pre-defined proability. For parent1 this probability is 0.7 and for parent2 0.3. We'll take parent1 for numbers >= 0.3 and parent2 for numbers < 0.3, so:

`parent2 < 0.3 <= parent1`

We'll generate a random number to determine which gene to take:

<pre>
random number:  .82 .65 .23 .37
parent number:    1   1   2   1
child:            1   4   1   3
</pre>

The child is infeasible since customer number 1 is visited twice.

Random keys is designed to prevent this type of issues.

The idea behind random keys is to generate a random number from `[0,1]` for each customer in solution. The order in which the customers are visited is represented by sorting these number in ascending order.

For example for previous example parent1 can be represented like:
<pre>
parent1: (.21, 0.63, 0.91, .45)
</pre>

which corresponds to the oreder of
<pre>
parent1: (1, 4, 2, 3)
</pre>

Now the reproduction will look like:
<pre>
parent1: (.21, .63, .91, .45)
parent2: (.51, .33, .59, .41)
</pre>

<pre>
random number:  .82 .65 .23 .37
parent number:    1   1   2   1
child:          .21 .63 .59 .45
</pre>

which produces
<pre>
child: (1, 4, 3, 2)
</pre>

Representing multiple vehicle can also be achieved by using random keys.

A random integer from `[0, vehicles_size)` represents the vehicle. For example if 3 vehicles are available, the solution might look like:

<pre>
parent1: (1.21, 2.63, 3.91, 1.45)
</pre>

Where vehicle 1 visits customer 1,4, vehicle 2 visists customer 2 and vehicle 3 visits customer 3.
