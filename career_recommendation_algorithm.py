START
Input number_of_modules
Set total = 0

FOR i = 1 TO number_of_modules
 Input module_mark
 total = total + module_mark
END FOR

average = total / number_of_modules

IF average >= 70 THEN
 recommendation_level = “Advanced Career Track”
ELSE
 recommendation_level = “Foundation Career Track”
END IF

Display average and recommendation_level
END
