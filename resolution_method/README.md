# Resolution Method

To prove some sentence α from knowledge (KB), it is enough to show that KB∧¬α is a contradiction. Meaning, if α is entailed from KB, it should not be possible to claim that KB is true and α isn't true. This program will find the contradiction using resolution.

## Code Description

The code defines a resolution-based theorem prover for propositional logic. It consists of a function resolve that performs resolution on two clauses and a simple_resolution_solver function that uses resolution to check for entailment between a knowledge base (KB) and a query. The code then applies this theorem prover to a knowledge base about a mythical unicorn and checks whether the unicorn is mythical, magical, and horned, printing the results.

1. resolve function iterates through literals in two clauses, attempting to resolve them by finding complementary literals and creating new resolvents when found.

2. simple_resolution_solver uses the resolve function to iteratively apply resolution to a knowledge base and a negated query to check for contradictions and determine entailment.

3. The code defines a knowledge base in conjunctive normal form (CNF) representing statements about the unicorn, negates queries about the unicorn, and tests whether the unicorn is mythical, magical, and horned using the simple_resolution_solver, printing the results as True or False.

## Results

The unicorn knowledge as CNF
```
KB = [
    ["-Mythical", "Immortal"],
    ["Mythical", "Mortal"],
    ["Mythical", "Mammal"],
    ["-Immortal", "Horned"],
    ["-Mammal", "Horned"],
    ["-Horned", "Magical"]
]
```

The results for the unicorn queries
```
Is the unicorn mythical? False
Is the unicorn magical? True
Is the unicorn horned? True
```

Opinion why the forward chaining solver from previous assignment doesn't work for the unicorn problem:

Forward chaining may not solve the problem in this case because it is a heuristic-based approach that starts with known facts and propagates information to reach a conclusion based on those facts. Forward chaining is not well-suited to handle these relationships because it lacks the mechanism to perform resolution-based reasoning. Resolution method relies on a more systematic and exhaustive search for contradictions.

## How to execute
This should work with a default python3.9 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 rm.py
```
should run the resolution method based on the unicorn example.

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
