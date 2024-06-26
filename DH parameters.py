import numpy as np     #numpy library for working with arrays

#opening file1 data1lenghts.txt in "r" mode to read only
f1=open("data1lenghts.txt","r")
words=f1.readlines()         #using readlines() function to read lines from file and store them in words
a1=float(words[0])           #getting the value from words at offset[0] to get the value of a1
a2=float(words[1])           #getting the value from words at offset[1] to get the value of a2
a3=float(words[2])           #getting the value from words at offset[2] to get the value of a3

#opening file2 data2angles.txt in "r" mode to read only
f=open("data2angles.txt","r")
word=f.readlines()          #using readlines() function to read lines from file and store them in word
t1=float(word[0])           #getting the value from word at offset[0] to get the value of t1
t2=float(word[1])           #getting the value from word at offset[1] to get the value of t2
d3=0                         #intializing the value of d3 as 0

t1=(t1/180)*np.pi            #converting agle t1 into radians
t2=(t2/180)*np.pi            #converting agle t2 into radians

#implementing while loop to vary d3 from 0-5
while d3<6:
#matrix for DH parameters table
    pt=[[t1,(90.0/180.0)*np.pi,0,a1],
    [t2+((90.0/180.0)*np.pi),(90/180.0)*np.pi,0,0],
    [0,0,0,a2+a3+d3]]

 #homologous transformaion matrices hi_i+1 where i ranges from 0-2. 
    i=0
    h0_1=[[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][1])],
    [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][1])],
    [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
    [0,0,0,1]]

    i=1
    h1_2=[[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][1])],
    [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][1])],
    [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
    [0,0,0,1]]

    i=2
    h2_3=[[np.cos(pt[i][0]),-np.sin(pt[i][0])*np.cos(pt[i][1]),np.sin(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.cos(pt[i][1])],
    [np.sin(pt[i][0]),np.cos(pt[i][0])*np.cos(pt[i][1]),-np.cos(pt[i][0])*np.sin(pt[i][1]),pt[i][2]*np.sin(pt[i][1])],
    [0,np.sin(pt[i][1]),np.cos(pt[i][1]),pt[i][3]],
    [0,0,0,1]]

    h0_2=np.dot(h0_1,h1_2)        #h0_2=h0_1h1_2
    h0_3=np.dot(h0_2,h2_3)        #h0_3=h0_2h2_3

    print('FOR d3=',d3)             #printing value of d3 
    print('\n')
    print('DH parameters of 3dof arm')
    print(np.matrix(pt))                 #printing DH parameter table in the form of matrix
    print('\n')
    print ('homologous transformation matrix of 3dof arm')
    print(np.matrix(h0_3))                       #printing homologous transformation matrix
    print('\n')
    print('X COORDINATE OF END EFFECTOR',round(h0_3[0][3],8))           #printing x coordinate of end effector from h0_3
    print('Y COORDINATE OF END EFFECTOR',round(h0_3[1][3],8))           #printing y coordinate of end effector from h0_3
    print('Z COORDINATE OF END EFFECTOR',round(h0_3[2][3],8))           #printing z coordinate of end effector from h0_3
    print('\n')
    d3+=1                  #incrementing the value of d3 for while loop

                                                                     #end
