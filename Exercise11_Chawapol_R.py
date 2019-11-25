"""
5
     * >>>>>>1
    *** >>>>>3
   ***** >>>>5
  ******* >>>7
 *********>>>>9
"""

row = int(input("input row of pyramid :"))
for i in range(row):
    space = " " * (row-i)
    text = "*"
    multiple = "*"*(i*2)
    result = space + text + multiple
    print(result)
