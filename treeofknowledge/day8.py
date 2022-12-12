import numpy as np

class TreeHouse:
    def __init__(self, pth):
        with open(pth) as rdr:
            data = [
                [int(i) for i in row.strip()]
                for row in rdr
            ]
        
        self.trees = np.array(data)

    def count_visible(self):
        # count how many trees can be seen from edge
        is_visible = np.zeros_like(self.trees)
        for k in range(4): # loop through all directions
            trees = np.rot90(self.trees, k=k)
            cum_max = np.pad(
                np.maximum.accumulate(trees, axis=0), 
                [(1,0), (0,0)], 
                constant_values=-1
            )
            # if tree is taller than cumulative max, it is visible
            cur_visible = np.rot90(trees > cum_max[:-1, :], k=-k)
            is_visible = (is_visible + cur_visible) > 0

        print(f"Number of visible trees {is_visible.sum()}")

    def max_scenic_score(self):
        # find max number trees seen from each tree in each direction
        scenic_score = np.ones_like(self.trees)
        for k in range(4): # loop through all directions
            trees = np.rot90(self.trees, k=k)
            dist = trees.shape[0]
            pad_trees = np.pad(trees, [(dist, 0), (0, 0)]) # pad top of matrix so we can window it

            see_trees = np.ones_like(self.trees)
            cur_score = np.zeros_like(self.trees)
            for i in range(dist): # slide trees to see if can still see
                see_trees[i,:] = 0 # at edge of forest, see no trees
                cur_score += see_trees
                # if tree is taller than current viewing tree, will be able to see trees past it
                see_trees *= trees > pad_trees[(dist - i - 1):(2 * dist - i - 1)]
            
            scenic_score *= np.rot90(cur_score, k=-k)

        print(f"Max scenic score: {scenic_score.max()}")
