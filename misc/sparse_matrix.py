import taichi as ti

ti.init()

n = 128

@ti.kernel
def test():
    ti.call_internal("insert_triplet")

test()

'''
@ti.kernel
def fill_entries(A: ti.sparse_matrix):
    for i in range(n):
        ti.insert_entry(i, i, 1)

A = ti.sparse_matrix()
fill_entries(A)
A.print_triplets()
'''