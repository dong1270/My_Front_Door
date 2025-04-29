#include <stdio.h>
#include <wiringPi.h>

#define RLED 25
#define GLED 21
#define YLED 22

int main(int argc, char* argv[])
{
	int val = wiringPiSetup();

	if(val < 0)
	{
		printf("wiringPi err");
		return 1;
	}

	pinMode(YLED, OUTPUT);

	digitalWrite(YLED, 0);

	return 0;
}