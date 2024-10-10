# 3-SAT Solver using Independent Set 🧠

## Description
Implementation of an algorithm to solve instances of the **3-SAT** problem by converting it to a graph to treat it as an **independent set** problem, which is solved with a **greedy** approach.

The **3-SAT** problem is a variant of the Boolean Satisfiability Problem (SAT), where each clause contains exactly three literals.**

## Algorithm
### Step 1: Conversion to graph
- A **graph** is created where each node represents a **variable**.
- As they are 3-SAT inputs, each clause forms a **triangle**.
- The triangles of the clauses are connected to each other by shared literals, forming a complex structure of restrictions.

### Step 2: Greedy Algorithm for Independent Set
- A **greedy** approach is used to select nodes.
- The algorithm selects a set of independent nodes.
