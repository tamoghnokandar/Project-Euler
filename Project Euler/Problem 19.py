day = 2
count_sunday = 0
for year in range(1901,2001):
    if (((year % 4) == 0) or ((year % 400) == 0)):


              if(((day % 7)==1) or ((day % 7)==3) or ((day % 7)==4) ):
                    count_sunday += 2
              if ((day % 7) ==0 ):
                   count_sunday += 3
              if(((day % 7)==2) or ((day % 7)==5) or ((day % 7)==6) ):
                  count_sunday += 1
              day+=2


    else:

        if (((day % 7) == 1) or ((day % 7) == 0) or ((day % 7) == 2)):
            count_sunday += 2
        if ((day % 7) == 4):
            count_sunday += 3
        if (((day % 7) == 3) or ((day % 7) == 5) or ((day % 7) == 6)):
            count_sunday += 1

        day += 1


print(count_sunday)

