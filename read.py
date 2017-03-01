#!/usr/bin/python
# Script to play with the POSCAR file
import numpy as np
import math
# reading the POSCAR file
f = open('POSCAR','r')
A = f.readlines()
# Reading the lattice vectors lv1, lv2, lv3
lv1=np.array(A[2].split()).astype(float)
lv2=np.array(A[3].split()).astype(float)
lv3=np.array(A[4].split()).astype(float)
# Getting the total number of atoms natoms
elements = A[5].split()
ntype = np.array(A[6].split(),dtype=int)
# print ntype, elements

 a,b,c = ntype
elemlist = []
for i, type in enumerate(ntype):
    elemlist += [elements[i]]*type
# print elemlist

natoms = np.sum(np.array(A[6].split()).astype(int))
print "Total number of atoms: %s" %natoms

# Checking the type of the lattice the last part of the script works only
# for Direct lattices
typel = "Direct"
ltype = str(A[7])

if A[7][0] is 'D':
    print typel
else:
    exit()

# calculating the volume of the supercell V
V = np.dot(lv1,np.cross(lv2,lv3))

# Getting the reciprocal lattice vectors ast, bst, cst

ast=2*math.pi*np.cross(lv2,lv3)/V
bst=2*math.pi*np.cross(lv3,lv1)/V
cst=2*math.pi*np.cross(lv1,lv2)/V
#print ast, bst, cst
# Creating a matrices from direct and reciprocal lattice lva, lvr

#lva = np.concatenate(([lv1],[lv2],[lv3]),axis=0)
lvr = np.concatenate(([ast],[bst],[cst]),axis=0)

lva = np.array([lv1, lv2, lv3])

# Getting the lenghths of direct and reciprocal lattice vectors
lena = np.linalg.norm(lv1)
lenb = np.linalg.norm(lv2)
lenc = np.linalg.norm(lv3)
lenast = np.linalg.norm(ast)
lenbst = np.linalg.norm(bst)
lencst = np.linalg.norm(cst)
print lva
print lvr
print "Length of the lattice vectors: %s, %s, %s" % (lena, lenb, lenc)
print "Length of the reciprocal attice vectors: %s, %s, %s" % (lenast, lenbst, lencst)
#cord = np.zeros((natoms,3))
#cords = A[8:8+natoms]
elemlist = []
for i, type in enumerate(ntype):
    elemlist += [elements[i]]*type

for i, line in enumerate(A[8:8+natoms]):
    cord = np.array(line.split(), dtype=float)

#for i in range(natoms):
#    cord = np.array(A[8+i].split()).astype(float)
#    print cord
    cordcart = np.dot(np.transpose(lva),cord)
    print ("{0} {1:10.5f} {2:10.5f} {3:10.5f}".format(elemlist[i],
                                                     cordcart[0],
                                                     cordcart[1],
                                                     cordcart[2]))

#    cord = np.concatenate(([cord],[cord]), axis=0)
