# -*- coding: utf-8 -*-
import numpy as np
from math import pow, sqrt, pi, fmod
import sys

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def read_parameters(parametersFile):
	global k,n,m,e,R,f,L,a,T0,tau,So,Sd,Sout,Sxyz,N,b0,b1,b2

	with open(parametersFile) as f:
		nLines= sum(1 for _ in f)

	parametersArray = np.zeros(nLines)

	lines = np.loadtxt(parametersFile, comments="#")
	#print "lines ", lines[0]

# with open(parametersFile) as f:
#     for line in f:
#         line = line.partition('#')[0]
#         line = line.rstrip()
#         print type(line)
#         np.append(parametersArray, float(line))

#print parametersArray


	k = 8.31*1e-3

	n = int(lines[0])
	m = lines[1]
	e = lines[2]
	R = lines[3]
	f = lines[4]
	L = lines[5]
	a = lines[6]
	T0 = lines[7]
	tau = lines[8]
	So = int(lines[9])
	Sd = int(lines[10])
	Sout = int(lines[11])
	Sxyz = int(lines[12])


	N = pow(n,3)
	b0 = [a,0,0]
	b1 = [a/2.,a/2.*sqrt(3.),0]
	b2 = [a/2., a/6.*sqrt(3.), a*sqrt(2./3)]


def calculate_coordinates(particles, coordinates):

	for x in range(n):
		for y in range(n):
			for z in range(n):
				czynnik1 = x - (n-1)/2.
				czynnik2 = y - (n-1)/2.
				czynnik3 = z - (n-1)/2.
				# print "czynnik1 = ",  czynnik1
				# print "czynnik2 = ",  czynnik2
				# print "czynnik2 = ",  czynnik2
				#iterator +=1
				# skladowaZ = 
				# skladowaY = 
				# skladowaX = 
				i = x+y*n+z*n*n
				#print int(i)
				coordinates[i][0] = czynnik1*b0[0]+czynnik2*b1[0]+czynnik3*b2[0]
				coordinates[i][1] = czynnik1*b0[1]+czynnik2*b1[1]+czynnik3*b2[1]
				coordinates[i][2] = czynnik1*b0[2]+czynnik2*b1[2]+czynnik3*b2[2]

				energy[i][0] = -1./2*k*T0*np.log(np.random.uniform(0.0,1.0))
				energy[i][1] = -1./2*k*T0*np.log(np.random.uniform(0.0,1.0))
				energy[i][2] = -1./2*k*T0*np.log(np.random.uniform(0.0,1.0))

	particles[:,0] = coordinates[:,0]
	particles[:,1] = coordinates[:,1]
	particles[:,2] = coordinates[:,2]
	E_av_x = np.mean(energy,axis=0)
	#print E_av_x

 # ulepszyc
	# for j in range(int(N)):
	# 	energy[j][0] = energy[j][0] / E_av_x[0]
	# 	energy[j][1] = energy[j][1] / E_av_x[1]
	# 	energy[j][2] = energy[j][2] / E_av_x[2]
	energy[:,0] /=  E_av_x[0]
	energy[:,1] /=  E_av_x[1]
	energy[:,2] /=  E_av_x[2]


def calculate_momenta(particles, momenta):
	
	for k in range(int(N)):
		for x in range(n):
			
			for y in range(n):
				for z in range(n):
					randomX = np.random.uniform(0.0,1.0)
					if (randomX > 0.5):
						signX = 1.0
					else:
						signX = -1.0
					#print signX
					randomY = np.random.uniform(0.0,1.0)
					if (randomY > 0.5):
						signY = 1.0
					else:
						signY = -1.0
					#print signY
					randomZ = np.random.uniform(0.0,1.0)
					if (randomZ > 0.5):
						signZ = 1.0
					else:
						signZ = -1.0
					#print signZ

					i = x+y*n+z*n*n
				#	print int(i)
					momenta[i][0] = signX*np.sqrt(2*m*energy[i][0])
					momenta[i][1] = signY*np.sqrt(2*m*energy[i][1])
					momenta[i][2] = signZ*np.sqrt(2*m*energy[i][2])

	P1 = np.sum(momenta[i][0])
	#print P1
	P2 = np.sum(momenta[i][1])
	#print P1
	P3 = np.sum(momenta[i][2])
	#print P1

	# for i in range(int(N)):
	# 	momenta[i][0] = momenta[i][0] - P1/N
	# 	momenta[i][1] = momenta[i][1] - P2/N
	# 	momenta[i][2] = momenta[i][2] - P3/N

	momenta[:,0] -= P1/N
	momenta[:,1] -= P2/N
	momenta[:,2] -= P3/N




	particles[:,3] = momenta[:,0]
	particles[:,4] = momenta[:,1]
	particles[:,5] = momenta[:,2]

	print "momenta", particles

def calculate_potential(F,p, total_potential):
	# distancesX = np.zeros((N,N))
	# distancesY = np.zeros((N,N))
	# distancesZ = np.zeros((N,N))
	distances = np.zeros((N,N))
	#potentialP = np.zeros((N,N))
	#potentialS = np.zeros(N)
	total_potential = 0
	p = 0.0
	Fx = np.zeros((N,N))
	Fy = np.zeros((N,N))
	Fz = np.zeros((N,N))
	Fs = np.zeros(N)
	F = np.zeros((N,3))


	# dla pary atomow
	for i in range(int(N)):
		ri = np.sqrt(coordinates[i][0]*coordinates[i][0]+coordinates[i][1]*coordinates[i][1]+coordinates[i][2]*coordinates[i][2])
		if (ri<L):
			total_potential += 0
			F[i][0] += 0
			F[i][1] += 0
			F[i][2] += 0
		else:
			"wchodze do petli "
			total_potential += 0.5 *f*(ri-L)*(ri-L)
			F[i][0] += f*(L-ri)/ri*coordinates[i][0]
			F[i][1] += f*(L-ri)/ri*coordinates[i][1]
			F[i][2] += f*(L-ri)/ri*coordinates[i][2]

			F_length =  np.sqrt(F[i][0]*F[i][0]+F[i][1]*F[i][1]+F[i][2]*F[i][2])
			p += 1./(4*pi*L**2)*F_length

		for j in range(i-1):
		#	if(i!=j):
			# distancesX[i][j] = abs(coordinates[i][0]-coordinates[j][0])
			# distancesY[i][j] = abs(coordinates[i][1]-coordinates[j][1])
			# distancesZ[i][j] = abs(coordinates[i][2]-coordinates[j][2])
			# distances[i][j] = np.sqrt(distancesX[i][j]*distancesX[i][j]+distancesY[i][j]*distancesY[i][j]+distancesZ[i][j]*distancesZ[i][j])
			distances[i][j] = np.sqrt(abs(coordinates[i][0]-coordinates[j][0])*abs(coordinates[i][0]-coordinates[j][0])+abs(coordinates[i][1]-coordinates[j][1])*abs(coordinates[i][1]-coordinates[j][1])+abs(coordinates[i][2]-coordinates[j][2])*abs(coordinates[i][2]-coordinates[j][2]))

				#potentialP = e*((R/(distances[i][j]))**12 - 2*(R/(distances[i][j]))**6)
			total_potential += e*((R/(distances[i][j]))**12 - 2*(R/(distances[i][j]))**6)
			F[i][0] += 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][0]-coordinates[j][0])/(distances[i][j])**2
			F[i][1] += 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][1]-coordinates[j][1])/(distances[i][j])**2
			F[i][2] += 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][2]-coordinates[j][2])/(distances[i][j])**2
			F[j][0] -= 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][0]-coordinates[j][0])/(distances[i][j])**2
			F[j][1] -= 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][1]-coordinates[j][1])/(distances[i][j])**2
			F[j][2] -= 12*e*((R/(distances[i][j]))**12 - (R/(distances[i][j]))**6)*(coordinates[i][2]-coordinates[j][2])/(distances[i][j])**2

	print "force = ", F
	print "pressure = ", p
	print "total V = ",total_potential


def dynamics():
	T_av = 0.0
	P_av = 0.0
	H_av = 0.0
	# So - kroki przeznaczone na wstepna termalizacje
	
	energy_particle = np.zeros(N)

	for s in range(So+Sd):

		# momenta += F*tau
		# coordinates += 1./(m*momenta*tau)




		for i in range(int(N)):

		# inter - intermediate state
			
			momenta[i][0] += (+0.5*F[i][0]*tau)
			momenta[i][1] += (+0.5*F[i][1]*tau)
			momenta[i][2] += (+0.5*F[i][2]*tau)

			# coordinated modification
			

			coordinates[i][0] += ( 1/m*momenta[i][0]*tau)
			coordinates[i][1] += (1/m*momenta[i][1]*tau)
			coordinates[i][2] +=  (1/m*momenta[i][2]*tau)


			# obliczenie nowego potencjalu, sil oraz chwilowego cisnienia
		calculate_potential(F, p, total_potential)

	#	momenta += 0.5*F

		for i in range(int(N)):
			# modyfikacja pedow, tutaj juz bedzie nowa wyliczona sila z calculate_potential
			momenta[i][0] += ( 0.5*F[i][0]*tau)
			momenta[i][1] += ( 0.5*F[i][1]*tau)
			momenta[i][2] += ( 0.5*F[i][2]*tau)



		# chwilowe charakterystyki dla wszystkich czastek
		energy_current = np.sum((coordinates[i][0]*coordinates[i][0]+coordinates[i][1]*coordinates[i][1]+coordinates[i][2]*coordinates[i][2])/(2*m))
		T = 2./(3*k*int(N))* energy_current
		H = energy_current + total_potential
		#energy_particle = 

		print "temperatura ", T
		print "energia", H

		if (s >=So):
			# liczymy srednia temp z fluktuacji, ktora pozniej usrednimy
			T_av += T
			H_av += H
			P_av += p
		


		if (fmod(s, Sout)==0.0):
			# t - czas
			t = s + tau
			f_handle = file(outFile, 'a')
			current_parameters = np.array([t,H,total_potential,T,p])
			np.savetxt(f_handle, current_parameters.reshape((1,5)),delimiter='\t', fmt='%1.4e')
			f_handle.close()

		if (fmod(s, Sxyz)==0.0):
			f = file('avs.dat', 'a')
			np.savetxt(f,  coordinates)
			f.write('\n')
			f.write('\n')
			f.close()




		#momentaX_integral[s+1] = momentaX_integral_inter+0.5* 




def plot_3D(data):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	Axes3D.scatter(ax,data[:,0],data[:,1],data[:,2])
	ax.view_init(azim=160)
	plt.show()


if __name__ == "__main__": 

	parametersFile = sys.argv[1]
	outFile = sys.argv[2]
	coordinatesFile = sys.argv[3]

	read_parameters(parametersFile)	

	particles = np.zeros((int(N),6))
	coordinates = np.zeros((int(N),3))
	momenta = np.zeros((int(N),3))
	energy = np.zeros((int(N),3))
	F = np.zeros((N,3))
	p = 0.0
	total_potential = 0.0


	calculate_coordinates(particles, coordinates)
	calculate_momenta(particles, momenta)

	#plot_3D(momenta)

	np.savetxt(coordinatesFile, particles[:,[0,1,2]]) # all rows, only 3,4,5 columns
	#np.savetxt(outFile,particles)

	# potential and force calculation
	calculate_potential(F,p,total_potential)
	dynamics()
