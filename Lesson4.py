#Task I
from typing import Collection


ages = [['felix', 18], ['aaron', 16]]

#Task II
music_artists = ["Led Zeppelin", "Bring Me The Horizon", "Tamino", "The Smiths",
"Mogwai", "KONGOS"]
names = ["Davit", "Negar", "Maia", "Demetre", "Sandro", "Nata"]
recomendaton = zip(music_artists, names)
print(list(recomendaton))

#Task III
listt = [4, 14, 5, 44] 
print(listt[0] + listt[3])

#Task IV
def append_size(lst):   
    (lst.append(len(lst)))   
    return lst
list_1 = [1, 2, 3, 4]
print(append_size(list_1))

#Task V
def every_three_nums(start):
    if(start > 100):
        return []
    else:
        lst = every_three_nums(start + 50)
        lst.append(start)
        lst.sort()
        return lst
print(every_three_nums(0))


