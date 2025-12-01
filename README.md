# Graph Coloring Using Backtracking (Python)

This project implements a Graph Coloring solution using Backtracking.  
The algorithm determines whether an undirected graph can be colored using **K colors** such that no two adjacent vertices share the same color.

---

## 📌 Features
- User input for vertices, edges, and colors
- Backtracking-based solution
- Checks valid color assignment for each vertex
- Prints full color assignment if possible
- Works for any general undirected graph

## 🚀 How It Works
1. Graph stored as an adjacency list  
2. Recursive backtracking tries assigning colors  
3. A color is valid only if no connected node has the same color  
4. If all vertices are colored → success  
5. Otherwise → coloring not possible

## 📊 Algorithm Used
1. Backtracking
2. Constraint Checking
3. Time complexity: O(Kⁿ) (exponential)
4. Space complexity: O(n) for color array

## Case 1 Input
```Enter number of vertices: 4
Enter number of edges: 5
Enter number of colors: 3

Enter edges (u v):
0 1 
0 2
1 2 
1 3
2 3
```

## Case 1 Output
```Coloring Possible with 3 Colors
Color Assignment: [1, 2, 3, 1]
```

## Case 2 Input
```Enter number of vertices: 4
Enter number of edges: 5
Enter number of colors: 2

Enter edges (u v):
0 1 
0 2
1 2 
1 3
2 3
```

## Case 2 Output
```Coloring Not Possible with 2 Colors
```


