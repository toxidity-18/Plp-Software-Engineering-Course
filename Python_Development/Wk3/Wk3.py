# if . . .  statements 
temperature = 30 
if temperature > 20 :
  print('A very hot day')
if temperature < 10:
  print ('A very cold day')

# Greater than 
age = 20 
if age > 18 :
  print('You re an adult')

# less than or equal to 
score = 75 
if score <= 80 :
  print ('Score is within the allowed limit')

# greater than or equal to 
temperature = 30
if temperature >= 25 :
  print('It is hot outside')

# and 
age = 20
has_id = True 
if age >=18 and has_id:
  print('You can go clubbing')

# or
day = 'sunday' 
if day=='sunday'  or day =='saturday':
  print('It still the weekend')


# not
is_raining=False
if not is_raining:
  print('Its not raining you can go out for a walk')

# scholarship eligibility .
gpa = 3.6
attendance = 92 
if gpa >= 3.6 and attendance >=90 :
  print('You are eligible for a scholarship')

# traffic light decision 
light_color='yellow'
car_speed=40
if light_color=='red' or (light_color=='yellow' and car_speed>30):
  print('stop the car')
else :
  print('you can go')

# movie watch 
age = 16
with_parent =True
if age>=18 or (age>=15 and with_parent==True):
  print ('You can watch the movie ')
else:
  print('Watch a cartoon')
  
