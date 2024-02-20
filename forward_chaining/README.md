# Forward Chaining Algorithm for Propositional Logic

This Python code implements the Forward Chaining algorithm for reasoning with Horn clauses and propositional logic. It is designed to check if specific queries are entailed by a given knowledge base.

## Code Description

The code includes a function forward_chaining that performs forward chaining. The function takes a list of clauses and a query and determines if the query can be entailed based on the knowledge contained in the clauses.

## Results
Results to prove prove that the egg a.) breaks, b.) makes a mess, c.) smells are:
```
The query Egg breaks is entailed: True
The query It makes a mess is entailed: True
The query It smells is entailed: False
```

## Usage

To use the code, follow these steps:

1. Define the knowledge base: The knowledge base is a list of premises and conclusions. For each clause, specify the premises (conditions) and the conclusion (result).

2. Define the queries: Create a list of queries that you want to test against the knowledge base.

3. Test each query: The code will iterate through the list of queries and check if each query is entailed by the knowledge base using the Forward Chaining algorithm.

4. The results will be printed to the console, indicating whether each query is entailed or not.

### Example of input knowledge
"Egg is fragile. Egg falls down. Egg contains liquid. If the egg is fragile and it falls down, it breaks. If the egg breaks and it contains liquid, it makes a mess. If the egg is spoiled and the egg breaks, it smells" is presented in code as:
```
knowledge_base = [
    ([], "Egg is fragile"),
    ([], "Egg falls down"),
    ([], "Egg contains liquid"),
    (["Egg is fragile", "Egg falls down"], "Egg breaks"),
    (["Egg breaks", "Egg contains liquid"], "It makes a mess"),
    (["Egg is spoiled", "Egg breaks"], "It smells")
]
```

## How to execute
This should work with a default python3.9 installation.

Clone the project into your folder and in the corresponding project folder executing
```
python3 forward_chaining.py
```
should be enough to execute the egg logic.

**This has only been tested on**\
OS: Manjaro 23.0.0 Uranos\
Kernel: x86_64 Linux 5.15.128-1-MANJARO
