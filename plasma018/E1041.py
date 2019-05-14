class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
      dir_x, dir_y = 0, 1
      fact_r = 1
      step_x, step_y = 0, 0
      for i in instructions:
        if i is 'G':
          step_x += dir_x
          step_y += dir_y
        elif i is 'L':
          temp = dir_x
          dir_x, dir_y = dir_y*(-fact_r), temp*(-fact_r)
          fact_r = -fact_r
        elif i is 'R':
          temp = dir_x
          dir_x, dir_y = dir_y*fact_r, temp*fact_r
          fact_r = -fact_r
      return dir_x != 0 or dir_y != 1 or (step_x == 0 and step_y == 0)
