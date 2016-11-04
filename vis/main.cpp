#include <GL/glut.h>
#include <cmath>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>


/*
#define VORDER 10
#define CORDER 10
#define TORDER 3

#define VMAJOR_ORDER 2
#define VMINOR_ORDER 3

#define CMAJOR_ORDER 2
#define CMINOR_ORDER 2

#define TMAJOR_ORDER 2
#define TMINOR_ORDER 2

#define VDIM 4
#define CDIM 4
#define TDIM 2
#define ONE_D 1
#define TWO_D 2
#define EVAL 3
#define MESH 4
*/

GLfloat xRotated, yRotated, zRotated;
GLdouble radius=1;


using namespace std;

const int atomCount = 125;
int reftime = 100;
double a = 0.38; 
double L = 2.3;
double x[atomCount];
double y[atomCount];
double z[atomCount];
double xplik, yplik, zplik;
//double empline; //niepotrzebna zmienna na  wczytywanie pustych linii , a myslalem ze bedzie potrzebne
fstream plik;

void display(void);
void reshape(int x, int y);
void Timer(int iUnused);
static void Init(void);



int main (int argc, char **argv)
{
  	
  
    plik.open( "avs.txt", ios::in | ios::out);
    
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInit(&argc, argv); 
    glutInitWindowSize(700,700);
    
    glutCreateWindow("Solid Sphere");
 
 Init();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    
		Timer(0);
    glutMainLoop();
    
    return 0;
}


void Timer(int iUnused)
{
	glutPostRedisplay();
	glutTimerFunc(reftime, Timer, 0);
}


void display(void)
{

  
    glMatrixMode(GL_MODELVIEW);
    // clear the drawing buffer.
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    // clear the identity matrix.
    glLoadIdentity();
  glTranslatef(0.0,0.0,-8.0); //odleglosc od srodka ukladu wsp.
  //jak sie to zakomentuje to sie jest w srodku tej kuli duzej i nic nie widac
    	glEnable( GL_DITHER );
	glShadeModel( GL_SMOOTH );
	glHint( GL_POINT_SMOOTH_HINT, GL_NICEST ); 
	glEnable( GL_POINT_SMOOTH );
	glColorMaterial(GL_FRONT, GL_DIFFUSE);
	glEnable(GL_COLOR_MATERIAL);
    // Red color used to draw.
    glColor3f(0.5, 0.3, 0.2); 
    // changing in transformation matrix.
    // rotation about X axis
    glRotatef(30,1.0,1.0,1.0);
    // scaling transfomation 
    glScalef(1.0,1.0,1.0);
    // Flush buffers to screen
		
	if(!plik.eof())
	{
		for(int i = 0; i < atomCount; i++)
		{
			plik >> xplik >> yplik >> zplik;
		//	if(plik.eof()) break;
			x[i] = xplik;
			y[i] = yplik;
			z[i] = zplik;
			glTranslatef(x[i], y[i], z[i]);
			glutSolidSphere(a, 20, 20);
			// a jest rzeczywiscie w nm 
			glTranslatef(-x[i], -y[i], -z[i]);
			//cout<<i<<endl;
			//tutaj myslalem ze trzeba wczytywac 2 puste linie
			//bo w C by trzeba bylo
			//ale nie trzeba :)
		}
	} 
	glutSwapBuffers();
    glColor3f(0.2, 0.6, 0.2); 
	glutSolidSphere(L, 80, 80);
	//L jest rzeczywiscie w nm
// u mnie na komputerze jak skompilowałem to nie dziala. Tak to dzialalo...
    // sawp buffers called because we are using double buffering 
	glFlush();
    
}
static void Init(void)
{	
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glEnable(GL_LIGHTING); //swiatlo obiektow, bez tego nie ma glebi kulek i nic nie widac
	glEnable(GL_LIGHT0); //swiatlo otoczniea, bez tego jest czarne tlo
	glShadeModel(GL_SMOOTH);
}

void reshape(int x, int y)
{
    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity(); 
    gluPerspective(39.0,(GLdouble)x/(GLdouble)y,0.6,21.0);

    glViewport(0,0,x,y);  
    display();
}