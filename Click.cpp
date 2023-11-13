#include "Click.hpp"

Click::Click() : _display(XOpenDisplay(NULL)), _root(DefaultRootWindow(_display))
{
	std::cout << "Constructor Click called" << std::endl;
}

Click::~Click()
{
	XCloseDisplay(_display);
	std::cout << "Destructor Click called" << std::endl;
}

void	Click::doClick(t_point & coord) const
{
	XWarpPointer(_display, None, _root, 0, 0, 0, 0, coord.destX, coord.destY);
	XTestFakeButtonEvent(_display, 1, True, CurrentTime);
	XTestFakeButtonEvent(_display, 1, False, CurrentTime);
	XFlush(_display);
	usleep(400000);
}


void	Click::doClick(int destX, int destY) const
{

	XWarpPointer(_display, None, _root, 0, 0, 0, 0, destX, destY);
	XTestFakeButtonEvent(_display, 1, True, CurrentTime);
	XTestFakeButtonEvent(_display, 1, False, CurrentTime);
	XFlush(_display);
	usleep(400000);
}

