from sam_cython.readbin3D import readbin3D
print('------ test started ---------')
filename='here is a long filename the end'
N=5
out=readbin3D(filename,N)
print(out)
print('--------- test completed ---------')


