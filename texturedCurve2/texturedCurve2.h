#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 41

		//Number of FX
		7,

		//Active (1 bit) + FX type (7 bits)
		130,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','1',0,
		//Noise
		30,
		//Seed
		1,


		//Active (1 bit) + FX type (7 bits)
		156,
		//Destination layer (2 bits)
		0,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		153,
		//Destination layer (2 bits)
		0,
		//Value
		2,

		//Active (1 bit) + FX type (7 bits)
		139,
		//Destination layer (2 bits)
		0,
		//Value
		8,
		//Seed
		1,

		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		3,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		173,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		109,
		//Curve
		'C','u','r','v','e','0',0,
		//Texture layer (2 bits) + Mask layer (2 bits)
		32,
		//Edge width
		4,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','1',0,

		//Interpolation and number of colors
		2,

		//Color 0: RGB + Position
		50, 50, 204,
		0,

		//Color 1: RGB + Position
		255, 255, 255,
		255,


	//Component type
	1,		//Curve

		//Curve name
		'C','u','r','v','e','0',0,

		//Mode (1 bit) + Number of points (7 bits)
		135,

		//Segments per curve
		24,

		//Line width
		1,

		//Visible and endpoint bits (1 point per bit)
		127,
		0,

		//Control points, left tangents and right tangents
		38, 190,
		52, 126,
		24, 126,
		94, 39,
		32, 42,
		156, 36,
		206, 42,
		172, 136,
		240, 136,
		173, 211,
		209, 191,
		137, 231,
		51, 204,
		25, 240,
		77, 168,
		178, 164,
		156, 223,
		200, 105,
		116, 130,
		70, 239,
		162, 21,

};

#pragma pack()
