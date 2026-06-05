class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time_taken=[]

        for i in range(len(position)):
            time_taken.append((target-position[i])/speed[i])
        
        pairs=list(zip(position,time_taken))

        pairs.sort(reverse=True)

        max_time=pairs[0][1]
        fleets=1

        for i in range(1,len(pairs)):

            if(pairs[i][1]>max_time):

                fleets+=1
                max_time=pairs[i][1]
        
        return fleets





        
            