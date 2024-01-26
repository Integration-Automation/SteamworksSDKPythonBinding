# Build SteamAPI.dll with visual studio

* Create a new DLL project in Visual Studio.
* New > Project.
* Templates > Visual C++ > Win32 > Win32 Project.
* Follow the wizard and pick the DLL Application Type.
* Add SteamworksPy.cpp to Source Files and steam_api.h from /steam/ folder to Header Files.
* Go to Project > Properties in the toolbar.
* Under C/C++ > Precompiled Headers, turn off Precompiled Header option.
* Under Linker > Input, add steam_api.lib or steam_api64.lib to Additional Dependenices.
* You may also want to add _CRT_SECURE_NO_WARNINGS under C/C++ > Preprocessor > Preprocessor Definitions.
* Clean and build.