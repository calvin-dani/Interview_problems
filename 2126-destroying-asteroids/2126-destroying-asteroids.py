class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:

        sortAsteroids = sorted(asteroids)

        for num in sortAsteroids:
            if mass < num:
                return False
            else:
                mass += num
        
        return True