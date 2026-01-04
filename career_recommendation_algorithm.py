START
Input number_of_modules

WHILE number_of_modules ≤ 0
 Display "Error: Number of modules must be greater than 0"
Input number_of_modules
END WHILE

Set total = 0

FOR i = 1 TO number_of_modules
 Input module_mark

WHILE module_mark < 0 OR module_mark > 100
 Display "Error: Mark must be between 0 and 100"
 Input module_mark
END WHILE

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
