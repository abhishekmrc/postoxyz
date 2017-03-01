#!/usr/bin/python
# Script to play with the POSCAR file
import numpy as np
import math
# reading the POSCAR file


f = open('../POSCAR', 'r')

A = f.readlines()
# Reading the lattice vectors lv1, lv2, lv3
lv1 = np.array(A[2].split()).astype(float)
lv2 = np.array(A[3].split()).astype(float)
lv3 = np.array(A[4].split()).astype(float)
# Getting the total number of atoms natoms

elements = A[5].split()
ntype = np.array(A[6].split(), dtype=int)

# print ntype, elements

elemlist = []
for i, type in enumerate(ntype):
    elemlist += [elements[i]]*type
# print elemlist

natoms = np.sum(np.array(A[6].split()).astype(int))
print natoms

# Checking the type of the lattice the last part of the script works only
# for Direct lattices
typel = "Direct"
ltype = str(A[7])

if A[7][0] is 'D':
    print typel
else:
    exit()

# Creating a matrix from direct lattice lva

lva = np.array([lv1, lv2, lv3])

elemlist = []
for i, type in enumerate(ntype):
    elemlist += [elements[i]]*type

for i, line in enumerate(A[8:8+natoms]):
    cord = np.array(line.split(), dtype=float)

    cordcart = np.dot(np.transpose(lva),cord)
    print ("{0} {1:10.5f} {2:10.5f} {3:10.5f}".format(elemlist[i],
                                                     cordcart[0],
                                                     cordcart[1],
                                                     cordcart[2]))

