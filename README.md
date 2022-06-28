# Artificial-Intelligence

8-Puzzle:
The puzzle consists of an area divided into a 3x3 grid. On each grid square is a tile, expect for one square which remains empty. Thus, there are eight tiles in the 8-puzzle. A tile that is next to the empty grid square can be moved into the empty space, leaving its previous position empty in turn. Tiles are numbered, 1 thru 8 for the 8-puzzle, so that each tile can be uniquely identified. The aim of the puzzle is to achieve a given configuration of tiles from a given (different) configuration by sliding the individual tiles around the grid as described above.
Problem:
The puzzle has been taken from https://murhafsousli.github.io/8puzzle/#/. You can select any picture you like and click on ‘show numbers’ check box on the lower left corner below the picture. Now you can input these numbers as a matrix into your search algorithm as input after clicking on shuffle button.
 
 ![image](https://user-images.githubusercontent.com/81529956/176089713-d95aded8-f631-4cf9-89ee-17d6a63a8366.png)   ![image](https://user-images.githubusercontent.com/81529956/176090185-1522d898-fcb9-4f7d-83e6-185ad16a4caa.png)


 
Solution:
This puzzle is solved by using two types of search algorithms, A* and Breadth for search (BFS). Of course, BFS takes longer time to run as compared to A*. Attached code files can be referred for the solution. 
Please note that empty space in the puzzle is represented by ‘0’ in code.

