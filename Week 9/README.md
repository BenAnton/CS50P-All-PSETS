   Python Unit Convertor
    #### Video Demo: (https://youtu.be/-Oz3-qU6Cn8)
    #### Description:

    Version 1.0

    Author: Ben Metaxas-Antonaropulos

    Feedback: feedback is welcomed and is best to be received by email: ben.cmaa@gmail.com.

    A Unit convertor written in Python which handles: length, weight, area, time and temperature.
    Length: centimeters (cm),meters (m), miles, kilometers (km), inches and feet
    Weight: kilograms (kg), pounds (lbs) and stone
    Area: square miles, square metres and acres
    Time: seconds, minutes and hours
    Temperature: celsius (c) and farenheight (f)

    How it works:
    The programme asks the user for the unit they would like to convert, then the measurement they would like to convert followed by the measurement they would like to convert to and finally the amount they would like to convert. The converted amount is then outputted back to the user. Initial input is validated and the functions are split in order to allow easy testing.

    For the project.py file there are no modules required for use.

    In order to run test_project.py then installation of pytest is required. in order to run the test file following the installation of pytest then in the terminal a user can type: "pytest test_project.py.

    If the project was to be taken further:
    Additional validation could be added for convert_to, convert_from and amount.
    Further testing could be added as the accompanying test file only tests each function once ensuring a more rigourous safety net.
    Further units could be added to allow for a wider range of conversions allowing the user to utilise more options.

    As a large additional step, a user interface could be added instead of user the command line as it currently does.

    An example input:
    Unit Type: "Length"
    From Unit: "cm"
    To Unit: "m"
    Amount: 100

    The programme would output 1.0.
