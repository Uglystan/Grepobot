#pragma once

#include <iostream>
#include <X11/Xlib.h>
#include <X11/extensions/XTest.h>
#include <X11/Xatom.h>
#include <stdio.h>
#include <unistd.h>
#include <map>
#include <string>

typedef struct s_point
{
	int destX;
	int destY;
}t_point;

class Click
{
	public :
		Click();
		~Click();
		void doClick(t_point & coord) const;
		void doClick(int destX, int destY) const;
	private :
		Display *_display;
		Window _root;
};