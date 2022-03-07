import copy

#Class to store each state of the puzzle
class Pattern():
    
    def __init__(self, parent=None, matrix = None, previous=None):
        self.parent = parent
        self.matrix  = matrix    
       
       #function to check the position of moving space in puzzle('0' in our case) 
        def poscheck(initial):
            for i in range(0,3):
                for j in range(0,3):
                    if initial[i][j]==0:
                        pos = (i,j)
            return pos
    
        self.zero_pos = poscheck(self.matrix)
    
    #function to compare the two patterns
    def __eq__(self, other):
        return self.matrix == other.matrix

#function to solve the puzzle using breadth for search algorithm
def bfs(start, end):
    start_pattern = Pattern(None, start)
    start_pattern.parent = start_pattern
    end_pattern = Pattern(None, end)
    
    open_list = []
    closed_list = []
    
    open_list.append(start_pattern)
    
    while len(open_list)>0:
        
        current_pattern = open_list[0]
        current_index = 0

        open_list.pop(current_index)    
        closed_list.append(current_pattern)
        
        if current_pattern == end_pattern:
            path = []
            current = current_pattern
            while current is not start_pattern:
                path.append(current.matrix)
                current = current.parent
            return path[::-1]
        
        #creating child nodes for the next iteration
        children = []
        for new_position in [(0,-1),(0,1),(-1,0),(1,0)]:
            
            node_position = (current_pattern.zero_pos[0] + new_position[0], current_pattern.zero_pos[1] + new_position[1])
            
            if node_position[0] > 2 or node_position[0] < 0 or node_position[1] > 2 or node_position[1] < 0:
                continue
            
            #f current_pattern.parent != None:
            if node_position[0] == current_pattern.parent.zero_pos[0] and node_position[1] == current_pattern.parent.zero_pos[1]:
                continue
                                                                                 
            new_matrix = copy.deepcopy(current_pattern.matrix)
            new_matrix[node_position[0]][node_position[1]] = 0
            new_matrix[current_pattern.zero_pos[0]][current_pattern.zero_pos[1]] = current_pattern.matrix[node_position[0]][node_position[1]]
                
            new_pattern = Pattern(current_pattern, new_matrix)
            
            children.append(new_pattern)
            
        for child in children:
            open_list.append(child)

def main():
    
    #starting pattern
    start = [[4, 5, 8],
               [7, 2, 1],
               [3, 0, 6]]   
    print("Start pattern :\n")
    for line in start:
        print ('  '.join(map(str, line)))
        
    #end pattern or state to be achieved
    end = [[1,2,3],
        [4,5,6],
        [7,8,0]]
    
    #prints all the steps to reach end state
    path = bfs(start, end)
    for i in range(0,len(path)):
        print("\nStep : ",i+1,"\n")
        for line in path[i]:
            print ('  '.join(map(str, line)))
        print("\n")
    
if __name__ == '__main__':
    main()