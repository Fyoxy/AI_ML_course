def forward_chaining(clauses, query):
  inferred = set()
  new_symbols = True  # loop while we infer new stuff

  while new_symbols:
      new_symbols = False

      for clause in clauses:
          premises, conclusion = clause
          if all(p in inferred for p in premises) and conclusion not in inferred:
              if conclusion == query:
                  return True  # the query is entailed
              inferred.add(conclusion)
              new_symbols = True

  return False  # the query is not entailed

# defining the knowledge base
knowledge_base = [
    ([], "Egg is fragile"),
    ([], "Egg falls down"),
    ([], "Egg contains liquid"),
    (["Egg is fragile", "Egg falls down"], "Egg breaks"),
    (["Egg breaks", "Egg contains liquid"], "It makes a mess"),
    (["Egg is spoiled", "Egg breaks"], "It smells")
]

# defining queries
queries = ["Egg breaks", "It makes a mess", "It smells"]

# testing each query
for query in queries:
    result = forward_chaining(knowledge_base, query)
    print(f"The query {query} is entailed: {result}")
  
