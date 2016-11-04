import numpy as np
 
def test_grav_field():
    G = 1
    m = 1
 
    coordinates = np.array([[0,0,0],[1,0,0]])
    analytic_F = np.array([[1,0,0],[-1,0,0]])
    N = len(coordinates)

    rij = coordinates.reshape((N,1,3)) - coordinates.reshape((1,N,3)) # 1(np broadcasting)  - liczba dla kazdej z par, 3 - x,y,z
    rij_scalar = np.sqrt((rij**2).sum(axis=2))
    indices = np.arange(int(N))
    rij_scalar[indices,indices] = np.inf
    potential_grav = -G*m*m/rij_scalar
    F_grav = potential_grav.reshape((N,N,1))*(rij/rij_scalar.reshape((N,N,1))**2)
    F_grav_per_particle_ax_1 = F_grav.sum(axis=1)
    print(F_grav_per_particle_ax_1)
    print("Dobre kierunki!")
    F_grav_per_particle_ax_0 = F_grav.sum(axis=0)
    print(F_grav_per_particle_ax_0)
    print("Zle kierunki!")

    assert np.isclose(analytic_F, F_grav_per_particle_ax_1).all()

if __name__=="__main__":
    test_grav_field()