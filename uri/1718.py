C, N = list(map(int, input().split(' ')))

olives = list(map(int, input().split(' ')))

slice_size = int(C / N) # int() cuz C is multiple of N
num_slices = N

l = [0] * C

for o in olives:
    l[o] = 1
for i in range(1, C):
    l[i] += l[i-1]

it_is_possible = False 

for i in range(slice_size):
    starting_in_i_works = True
    for j in range(num_slices - 1): # -1 because there is no need to verify the last slice if all the others are ok
        slice_init = i + (j * slice_size)
        slice_end = slice_init + slice_size - 1 # this -1 is so it doesn't collide with the beginning of other slices
                                                # think of it as turning all the slices a little bit anti-clockwise
        num_of_olives_in_slice = l[slice_end] - l[slice_init]
        if num_of_olives_in_slice != 1:
            starting_in_i_works = False
            break
    if starting_in_i_works:
        it_is_possible = True
        break

print("S" if it_is_possible else "N")
