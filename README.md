# UAS-Technical-Task
Forward Kinematics of a 3DOF Robotic Arm and Position of End Effector

project consists of a forward kinematics controller of a 3 Degree of Freedom robotic arm which has two revolute joints an one prismatic joint(RRP 3DoF Robotic Arm); such an arm is also called Spherical Robotic Arm.
There are two python programs both are forward kinematics controller of the 3dof arm but based upon two different logics one works on the concept of rotational matrices while the other works using Denavit-Harternberg Method(DH parameters).
First program can be used to print DH Parameters,Homologous Transformation Matrix and the position of the End Effector for different values of d3 that vary from 0-5.
Second program can be used to print Rotational matrix,DH Parameters,Homologous Transformation Matrix and the position of the End Effector for different values of d3 that vary from 0-5.
Both programs have numpy libraries for working with arrays and have a while loop for varying the value of d3(0-5).
While printing outputs np.matrix() and round() functions ate used for better presentation.
For running the program you need two different text files(data1lenghts.txt,data2angles.txt).First for the arm lengths of robotic arm(a1,a2,a3).Second for the value of t1 and t2 which are the angles by which revolute joints are rotated.
The program reads text files,take input from them,assign those values in the variables,calculates rotational matrix and HTM for each joint and print the output for end effector.

