#include<iostream>
#include "pycall.hpp"
int main(){
	std::cout<<"this is main func"<<std::endl;
	PrintName pn;
	pn.PrintYou();
	return 0;
}
