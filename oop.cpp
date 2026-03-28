// OOPS concepts:
// 1.Class 
// 2.Object 
// 3.Encapsulation
// 4.Inheritance
// 5.Polymoriphism
// 6.Abstraction


// ---CLASS---
// A class is a user-defined blueprint or prototype from which objects are created. It represents the set of properties or methods that are common to all objects of one type. Using classes, you can create multiple objects with the same behavior instead of writing their code multiple times. In general, class declarations in C++ can include these components.


// ----OBJECT----
#include <iostream>
#include <string>

using namespace std;

// class Employee{
//     private:
//         string name;
//         float salary;

//     public:
//     // constructor
//         Employee(string name, float salary){
//             this->salary = salary;
//             this->name = name;
//         }

//         // getter
//         string getName() {return name;}
//         float getSalary() {return salary;}

//         // setter 
//         void setName(string name) {this->name = name;}
//         void setSalary(float salary) {this->salary = salary;}

//         // Instance method 
//         void displayDetails(){
//             cout << "Employee name : " << name << endl;
//             cout << "Salary : " << salary << endl;
//         }
// };

// // ------ABSTRACTION------

// class vehical{
// public:
//     virtual void accelerate() = 0;  //abstraction method
//     virtual void brake() = 0; //pure virtual function

//     void engine(){
//         cout << "Engine started!!!" << endl;
//     }

// };

// class car : public vehical {
// public:
//     void accelerate() override {
//         cout << "Accelerating...." << endl;
//     }

//     void brake() override {
//         cout << "Brake applied ...." << endl;
//     }
// };

// // --------ENCAPSULATION---------

// class EmployeeEncpsulation {
//     private:
//         int id;
//         string name;

//     public:
//         // setter
//         void setId(int id) {
//             this->id = id;
//         } 

//         void setName(string name) {
//             this->name = name;
//         }

//         // getter
//         int getId() {
//             return id;
//         }

//         string getName() {
//             return name;
//         }

// };

// // ------------INHERITANCE-----------

// class Animal{ //super class
//     public:
//         void eat() {
//             cout << "Annimal is eating...." << endl;
//         }
//         void sleep() {
//             cout << "Animal is sleeping...." << endl;
//         }

// };

// class Dog : public Animal { //subclass
//     public :
//         void  bark() {
//             cout << "Dog is barking!" << endl;
//         }
// };

// class Cat : public Animal { //subclass
//     public :
//         void  Meow() {
//             cout << "Meow Meow!" << endl;
//         }
// };

// -------------POLYMORPHISM-------------

class Parent {
    public:
    //overloaded method
    void func() {
        cout << "Parent.func()" <<endl;
    }

    //overlaoded method
    virtual void func(int a) {
        cout << "Parent.func(int)" << a << endl;
    }
};

class Child : public Parent {
    public:
        void func(int a) override {
            cout << "Child.func(int): " << a << endl;
        }
};


int main(){
    // Employee emp1("admin",1000.0f);
    // emp1.displayDetails();

    // cout << endl;

    // vehical* myCar = new car; //create object using pointer class
    // myCar->engine();

    // myCar->accelerate();
    // myCar->brake();

    // EmployeeEncpsulation emp2;
    // emp2.setId(101);
    // emp2.setName("python");

    // cout << "Employee ID : " << emp2.getId() << endl;
    // cout << "Employee Name : " << emp2.getName() << endl;

    // Dog sheru;
    // Cat catwalker;

    // sheru.bark();
    // sheru.sleep();

    // catwalker.Meow();
    // catwalker.eat();

    Parent parent;
    Child child;
    Parent* polymorphicObj = new Child();

    //method overloading (compile-time)
    parent.func();
    parent.func(10);

    //methodd overloading (runtime) 
    child.func(20);

    //polymorphism in action
    polymorphicObj->func(30);

    delete polymorphicObj;
    return 0;
}