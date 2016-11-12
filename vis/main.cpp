#include <GL/glut.h>
#include <cmath>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <boost/lexical_cast.hpp>
#include <unistd.h>




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
GLdouble radius = 0.2; // sprawdzic !!!


using namespace std;

const int atomCount = 125;
int reftime = 150;
double a = 0.373; 
double L = 2.3;
double x[atomCount];
double y[atomCount];
double z[atomCount];
double t[atomCount];
double H[atomCount];
double totalV[atomCount];
double T[atomCount];
double p[atomCount];

double xplik, yplik, zplik;
double tplik, H_plik, total_Vplik, Tplik, p_plik;

//double empline; //niepotrzebna zmienna na  wczytywanie pustych linii , a myslalem ze bedzie potrzebne
fstream plik;
fstream plik_out;

void display(void);
void reshape(int x, int y);
void Timer(int iUnused);
static void Init(void);


 


void PrintString(const std::string &ref, float y) {
    y /= 10;

    glMatrixMode( GL_PROJECTION );
    glPushMatrix(); // save
    glLoadIdentity();// and clear
    glMatrixMode( GL_MODELVIEW ) ;
    glPushMatrix();
    glLoadIdentity();

    glDisable( GL_DEPTH_TEST ) ;
    glDisable(GL_LIGHTING);
    glColor3f(1.0f, 1.0f, 1.0f);
    glRasterPos2f(-0.9f, y);

    for (size_t i = 0; i < ref.size(); ++i)
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ref.data()[i]);

    glEnable(GL_LIGHTING);
    glEnable( GL_DEPTH_TEST ) ;

    glMatrixMode( GL_PROJECTION ) ;
    glPopMatrix() ; // revert back to the matrix I had before.
    glMatrixMode( GL_MODELVIEW ) ;
    glPopMatrix();

}

int main (int argc, char **argv)
{
  	
  
    plik.open( "avs_T0_So500_Sd2500_a0-373.txt", ios::in | ios::out);
    plik_out.open( "out_T0_So500_Sd2500_a0-373_v2.txt", ios::in | ios::out);
    
	glutInitDisplayMode( GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
    glutInit(&argc, argv); 
    glutInitWindowSize(900,900);
    
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

	// rysuje sferę o L = 2.3
	glutWireSphere(2.3,30,36);

	glColor3f(0.5f, 0.5f, 0.5f); 

    // Red color used to draw.
    // glColor3f(0.5, 0.3, 0.2); 
    // changing in transformation matrix.
    // rotation about X axis
    glRotatef(30,1.0,1.0,1.0);
    // scaling transfomation 
    glScalef(1.0,1.0,1.0);
    // Flush buffers to screen
			// glutSolidSphere(L, 30,36);
    // glDisable(GL_LIGHTING);

    glRasterPos2f(0,0); // center of the screen

    int j = 0;

	if(!plik.eof())
	{

		// for(int i = 0; i < atomCount; i++)
		// {
		// 	plik >> xplik >> yplik >> zplik;
			


		// 			// glutStrokeString(GLUT_STROKE_ROMAN, (unsigned char*)(boost::lexical_cast<std::string>(H[i])));
		// 	// glColor4f(0.0f, 0.0f, 1.0f, 1.0f);
		// 	// glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, (boost::lexical_cast<std::string>(H[i])));
		// 				// glTranslatef(5,5,5);

		// 	// PrintString("t = "+(boost::lexical_cast<std::string>(t[i])),0);

		// 	// PrintString("H = "+(boost::lexical_cast<std::string>(H[i])),-5);
		// 	// PrintString("V = "+(boost::lexical_cast<std::string>(totalV[i])),-10);

		// 							// glTranslatef(-5,-5,-5);


		// 	    // glColor3f(1.0f, 1.0f, 1.0f);
		// 	// glDisable(GL_TEXTURE_2D);
		// 	// glDisable( GL_DEPTH_TEST ) ;

		// 	// glutBitmapCharacter(GLUT_BITMAP_8_BY_13,(int) H[i]);
		// 	// glEnable( GL_DEPTH_TEST ) ;
		// 	// glEnable(GL_TEXTURE_2D);

		// 	// cout<< t[i] << " " << H[i] <<" " <<  totalV[i] << " " << T[i] << " " << p[i] << endl;
		// 	glTranslatef(x[i], y[i], z[i]);
		// 	glutSolidSphere(a, 20, 20);
	
		// 	// a jest rzeczywiscie w nm 
		// 	glTranslatef(-x[i], -y[i], -z[i]);
		// 	// renderBitmapString(0, 0.8, GLUT_BITMAP_TIMES_ROMAN_24, "string");


		// }
		for(int i = 0; i < atomCount; i++)
		{
			plik >> xplik >> yplik >> zplik;
		//	if(plik.eof()) break;
			x[i] = xplik;
			y[i] = yplik;
			z[i] = zplik;
			glTranslatef(x[i], y[i], z[i]);
			glutSolidSphere(radius, 20, 20);
			// a jest rzeczywiscie w nm 
			glTranslatef(-x[i], -y[i], -z[i]);
			//cout<<i<<endl;
			//tutaj myslalem ze trzeba wczytywac 2 puste linie
			//bo w C by trzeba bylo
			//ale nie trzeba :)
		}

		plik_out >> tplik >> H_plik >> total_Vplik >> Tplik >> p_plik;
		

			t[j] = tplik;
			H[j] = H_plik;
			totalV[j] = total_Vplik;
			T[j] = Tplik;
			p[j] = p_plik;

		PrintString("t = "+(boost::lexical_cast<std::string>(t[j])),-5);
		PrintString("H = "+(boost::lexical_cast<std::string>(H[j])),-6);
		PrintString("Vtot = "+(boost::lexical_cast<std::string>(totalV[j])),-7);
		PrintString("T = "+(boost::lexical_cast<std::string>(T[j])),-8);
		PrintString("p = "+(boost::lexical_cast<std::string>(p[j])),-9);


		j++;

	} 
	glutSwapBuffers();
    glColor3f(0.2, 0.6, 0.2); 
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
	// glClearColor (0.0,0.0,0.0);
	glShadeModel (GL_FLAT);
}

void reshape(int x, int y)
{

	// static bool paused = false;
	// if(key == 'p')
	//   paused = !paused;

    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity(); 
    gluPerspective(39.0,(GLdouble)x/(GLdouble)y,0.6,21.0);

    glViewport(0,0,x,y);  
    // if(!paused){
    display();
//}
}