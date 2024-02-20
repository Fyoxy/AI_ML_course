def resolve(current, clause):
  resolvents = []
  
  for literal in current:
      if literal[0] == '-':
          neg_literal = literal[1:]
      else:
          neg_literal = '-' + literal
      if neg_literal in clause:
          
        new_clause = [l for l in current if l != literal]
        temp = [l for l in clause if l != neg_literal]

        new_clause.extend([l for l in temp if l not in new_clause])

        if not new_clause:
            return [new_clause]  # An empty clause signifies a contradiction

        resolvents.append(new_clause)
  
  return resolvents

def simple_resolution_solver(KB, neg_alpha):
  todo = [neg_alpha]
  done = KB.copy()
  while todo:
      current = todo.pop()
      for clause in done:
          resolvents = resolve(current, clause)
          for resolvent in resolvents:
              if not resolvent:  # Empty clause found
                  return True
              if all(literal in done for literal in resolvent):
                  continue
              todo.append(resolvent)
      done.append(current)
  return False


# Define your knowledge base in CNF format
KB = [
    ["-Mythical", "Immortal"],
    ["Mythical", "Mortal"],
    ["Mythical", "Mammal"],
    ["-Immortal", "Horned"],
    ["-Mammal", "Horned"],
    ["-Horned", "Magical"]
]

#  CNF queries
neg_query1 = ["-Mythical"]
neg_query2 = ["-Magical"]
neg_query3 = ["-Horned"]

# Test the queries using the simple_resolution_solver
result1 = simple_resolution_solver(KB, neg_query1)
result2 = simple_resolution_solver(KB, neg_query2)
result3 = simple_resolution_solver(KB, neg_query3)

print("Is the unicorn mythical?", result1)
print("Is the unicorn magical?", result2)
print("Is the unicorn horned?", result3)
