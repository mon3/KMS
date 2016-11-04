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
	k = 8.31e-3

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
				i = x+y*n+z*n*n
				coordinates[i][0] = czynnik1*b0[0]+czynnik2*b1[0]+czynnik3*b2[0]
				coordinates[i][1] = czynnik1*b0[1]+czynnik2*b1[1]+czynnik3*b2[1]
				coordinates[i][2] = czynnik1*b0[2]+czynnik2*b1[2]+czynnik3*b2[2]

	energy = -1./2*k*T0*np.log(np.random.uniform(0.0,1.0, size = (N, 3)))

	# to jest dobrze i nie musi być zwracane na zewnątrz, ponieważ podajesz to przez arg
	# tak jak pass by reference w Cpp
	# (tak naprawdę podanie w argumencie macierzy to podanie wskaźnika, bo C we flakach!)
	particles[:,:3] = coordinates
	E_av_x = np.mean(energy,axis=0)
	energy /=  E_av_x

	return energy

def calculate_momenta(energy):
	momenta = np.random.choice((-1.0,1.0), size = (N, 3))*np.sqrt(2.*m*energy)

	cm_momentum = momenta.sum(axis=0)
	momenta -= cm_momentum/N
	particles[:,3:] = momenta
	return momenta


def calculate_potential(coordinates, R, e, N,):
	# OPTYMALIZACJA
	# ToDo: popatrzec na czas z mnozeniem!

	# robie macierz na odleglosci miedzy czastami

	rij = coordinates.reshape((N,1,3)) - coordinates.reshape((1,N,3)) # 1(np broadcasting)  - liczba dla kazdej z par, 3 - x,y,z
	rij_scalar = np.sqrt((rij**2).sum(axis=2))
	indices = np.arange(int(N))
	rij_scalar[indices,indices] = np.inf
	potential_VDW = e*((R/rij_scalar)**12-2*(R/rij_scalar)**6) # gdybym miala nawias [], miałabym liste
	total_VDW_potential = potential_VDW.sum() * 0.5
	F_VDW = 12*potential_VDW.reshape((N,N,1))*(rij/rij_scalar.reshape((N,N,1))**2)
	F_VDW = F_VDW.sum(axis = 1) # TODO: sprawdzic

	wall_potential = np.zeros(N, dtype=float)
	ri = np.sqrt((coordinates**2).sum(axis=1))
	warunek = ri > L
	wall_potential[warunek] = 0.5*f*(L-ri[warunek])**2
	total_wall_potential = wall_potential.sum()
	F_wall = np.zeros((N,3), dtype=float)
	F_wall[warunek] =f*(L-ri[warunek, np.newaxis])*coordinates[warunek]/ri[warunek, np.newaxis]

	total_potential = total_VDW_potential+total_wall_potential
	F = F_wall+F_VDW

	p = np.sqrt((F_wall**2).sum())/(4.*pi*L**2)
	return F, p, total_potential

def dynamics(F, momenta, coordinates):
	T_av = 0.0
	P_av = 0.0
	H_av = 0.0
	# So - kroki przeznaczone na wstepna termalizacje

	avs_file = file('avs.dat', 'w')
	f_handle = file(outFile, 'w')

	energy_particle = np.zeros(N)

	for s in range(So+Sd):
		momenta += 0.5*F*tau
		coordinates += momenta*tau/float(m)
			# obliczenie nowego potencjalu, sil oraz chwilowego cisnienia
		F, p, total_potential = calculate_potential(coordinates, R, e, N)
		# import ipdb
		# ipdb.set_trace()

		momenta += 0.5*F*tau

		energy_current = (momenta**2).sum(axis = 1)/(2.0*m)

		# ZAŁOŻENIE: H oraz energia ma być skalarem, bo na tę chwilę jest wektorem
		# i p w sumie też

		energy_current_sum = energy_current.sum()
		# chwilowe charakterystyki dla wszystkich czastek
		T = 2./(3.0*k*int(N))* energy_current_sum

		H = energy_current_sum + total_potential
		#energy_particle =

		print ("temperatura ", T)
		print ("energia", H)

		if (s >=So):
			T_av += T
			H_av += H
			P_av += p


		if (s % Sout==0):
			t = s + tau
			current_parameters = np.array([t,H,total_potential,T,p])
			np.savetxt(f_handle, current_parameters.reshape((1,5)),delimiter='\t', fmt='%1.4e')

		if (s % Sxyz==0):
			#np.savetxt(avs_file,  np.hstack((coordinates, energy_current[:, np.newaxis])))
			np.savetxt(avs_file,coordinates)
			avs_file.write('\n')
			avs_file.write('\n')

	T_av /= Sd
	H_av /= Sd
	P_av /= Sd

	print "average T, H, P", T_av, H_av, P_av
	f_handle.close()
	avs_file.close()

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

	energy = calculate_coordinates(particles, coordinates)
	momenta = calculate_momenta(energy)
	np.savetxt(coordinatesFile, particles[:,[0,1,2]]) # all rows, only 3,4,5 columns
	F, p, total_potential = calculate_potential(coordinates, R, e, N)
	dynamics(F,momenta,coordinates)
