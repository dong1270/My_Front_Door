#include <stdio.h>
#include <wiringPi.h>
#include <string.h>

#define RLED 25
#define GLED 21
#define YLED 22

int main(int argc, char* argv[])
{
	if(argc != 2) return 1;

	char* result = argv[argc - 1];

	int cnt 	= 30;
	int targetPin 	= 0;

	if(wiringPiSetup() < 0)
	{
		printf("wiringPi err");
		return 1;
	}

	if(!strcmp(result, "pass"))	targetPin = GLED;
	else				targetPin = RLED;

	pinMode(targetPin, OUTPUT);

	while(cnt--)
	{
		digitalWrite(targetPin, 1);
		delay(1000);
		digitalWrite(targetPin, 0);
		delay(1000);
	}


	return 0;
}