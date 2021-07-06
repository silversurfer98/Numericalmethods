//g++ -c Solve_System_Of_Equations.cpp && g++ Solve_System_Of_Equations.o -o Solve_System_Of_Equations.out && rm Solve_System_Of_Equations.o


#include<iostream>
#include <iomanip>
using namespace std;

int i,j;

float pow(float number, float exp)
{
    if(exp==0)
        return 1;
    else if(exp==1)
        return number;
    else
    {
        float ans = 1;
        for(int i=1;i<=exp;i++)
            ans = ans*number;
        return ans;
    }
}

float **createArray(int n)
{
    float **array = new float*[n];
    for(i=0;i<n;i++)
        array[i] = new float[n];
    //cout<<"im inside the function so address is :"<<array<<endl;;
    return array;
}

void DelArray(float **addressOfTable, int n)
{
    for(i=0;i<n;i++)
    {
        delete[] addressOfTable[i];
        //free(addressOfTable[i]);
    }
    
    //free(addressOfTable);
    delete[] addressOfTable;
    //addressOfTable = NULL;
}

void printArray(float **table, int n)
{
    //cout<<"the array is :"<<endl;
    for(int i=0;i<n;i++)
    {
        cout<<endl;
        for(int j=0;j<n;j++)
            cout<<table[i][j]<<"  ";
    }
    cout<<endl;

}

float det22(float **array)
{
    return (array[0][0]*array[1][1] - array[0][1]*array[1][0]);
}

float **subMatrix(float **table, int n, int l, int k)
{
    // This fuction returns a Sub - matrix of size n-1 of the passed element Index.......
    // my logic starts here .....
    // l is Index Of Row and k is Index Of Column
    int f=0;
    int a=0, b=0;
    float **submatrix = createArray(n-1);
    for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(i!=l && j!=k)
                {
                    submatrix[a][b] = table[i][j];
                    b++;
                    if(b == n-1)
                    {
                        f=1;
                        b=0;
                    }
                }

            }
            if(f==1)
                a++;
            f=0;
        }
    //cout<<"this is a sub matrix of : "<<table[l][k]<<endl;

    return submatrix;
    DelArray(submatrix,n-1);
    submatrix = nullptr;  
}

float DetDriver(float **array, int n)
{
    float ans = 0;
        for(int h=0;h<n;h++)
        {
            float **workingArray = createArray(n-1);
            workingArray = subMatrix(array,n,0,h);
            //printArray(workingArray,n-1);
            //cout<<endl;
            if(n-1 == 2)
            {
                ans = ans + pow(-1,h) * array[0][h] * det22(workingArray);
            }
            else
            {
                ans = ans + pow(-1,h) * array[0][h] * DetDriver(workingArray,n-1);
            }
            DelArray(workingArray,n-1);
            workingArray = nullptr;
        }
    return ans;
          
}

void transpose(float **array, int n)
{
    float change=0;
    for(int x=0;x<n;x++)
    {
        for(int y=x+1;y<n;y++)
        {
            change = array[x][y];
            array[x][y] = array[y][x];
            array[y][x] = change;
        }
    }
}

float **inverse(float **array, int n, float det)
{
    float **inverseOfA = createArray(n);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            inverseOfA[i][j] = pow(-1,i+j)*DetDriver(subMatrix(array,n,i,j),n-1)/det;
        }
    }
    return inverseOfA;
    DelArray(inverseOfA,n);
    inverseOfA = nullptr;  

}

int main ()
{
    int n;
    cout<<"enter order of matrix or system of equations [Cnnt solve 2X2] : ";
    cin>>n;   
    float **table = createArray(n);

    cout<<"address of the array :"<<table<<endl;

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            cin>>table[i][j];
  
    cout<<endl<<endl;

    float det = DetDriver(table,n);
    if(det!=0)
    {
        cout<<"the determinant of "<<endl;
        cout<<"********** "<<table<<" *************"<<endl;
        printArray(table,n);
        cout<<endl<<" is : "<<det<<"   ************"<<endl;
        
        transpose(table,n);
        table = inverse(table,n,det);
        cout<<"**********  Inverse of the matrix ***********"<<endl;
        printArray(table,n);
        cout<<endl<<"***************************************"<<endl;
        cout<<endl;

        float **parameters = new float*[n];
        for(int z=0;z<n;z++)
            parameters[z] = new float[1];

        float **solution = new float*[n];
        for(int v=0;v<n;v++)
            solution[v] = new float[1];
                    
        cout<<"Enter the equation parameters : "<<endl;
        for(int zx=0;zx<n;zx++)
            {
                cout<<"Parameter No. "<<zx+1<<" : ";
                cin>>parameters[zx][0];
            }

        for(int i=0;i<n;i++)
        {
            solution[i][0] = 0;
            for(int j=0;j<n;j++)
            {
                solution[i][0] = solution[i][0] + table[i][j] * parameters[j][0];
            }
        }


        cout<<endl<<endl<<"******** Answers are *************"<<endl<<endl;
        for(int rt=0;rt<n;rt++)
        {
            cout<<"answer No. "<<rt+1<<" : ";
            cout << std::setprecision(3) <<solution[rt][0]<<endl;
        }
        
        DelArray(parameters,n);
        parameters = nullptr;
        DelArray(solution,n);
        solution = nullptr;
    }
    else
        cout<<"omale poda de"<<endl;
    
    DelArray(table,n);
    table = nullptr;
    
    return 0;
}
