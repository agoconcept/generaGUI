#pragma pack(1)

unsigned char project[] = {

	//Number of components (16 network ordered bits)
	0, 3,

	//Component type
	0,		//Gradient

		//Gradient name
		'G','r','a','d','i','e','n','t','0',0,

		//Interpolation and number of colors
		130,

		//Color 0: RGB + Position
		204, 127, 50,
		0,

		//Color 1: RGB + Position
		0, 0, 0,
		255,


	//Component type
	1,		//Curve

		//Curve name
		'C','u','r','v','e','0',0,

		//Mode (1 bit) + Number of points (7 bits)
		137,

		//Segments per curve
		32,

		//Line width
		1,

		//Visible and endpoint bits (1 point per bit)
		255,
		32,

		1,
		1,

		//Control points, left tangents and right tangents
		112, 35,
		160, 68,
		64, 2,
		56, 193,
		10, 187,
		102, 199,
		153, 185,
		102, 174,
		204, 196,
		190, 246,
		129, 248,
		251, 244,
		115, 165,
		221, 168,
		9, 162,
		208, 71,
		208, 146,
		208, 0,
		111, 57,
		79, 35,
		143, 79,
		188, 71,
		180, 44,
		196, 98,
		93, 135,
		131, 124,
		55, 146,

	//Component type
	2,		//Texture

		//Texture name
		'T','e','x','t','u','r','e','0',0,

		//Texture size (24 network ordered bits)
		0, 0, 38

		//Number of FX
		8,

		//Active (1 bit) + FX type (7 bits)
		132,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		45,
		//Gradient
		'G','r','a','d','i','e','n','t','0',0,
		//Seed
		59,


		//Active (1 bit) + FX type (7 bits)
		159,
		//Destination layer (2 bits)
		0,
		//Value
		8,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		147,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		146,
		//Destination layer (2 bits)
		0,

		//Active (1 bit) + FX type (7 bits)
		173,
		//Destination layer (2 bits) + Width (3 bits) + Height (3 bits)
		118,
		//Curve
		'C','u','r','v','e','0',0,
		//Texture layer (2 bits) + Mask layer (2 bits)
		32,
		//Edge width
		8,

};

#pragma pack()
