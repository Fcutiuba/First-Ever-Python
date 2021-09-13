my_password = "FunPassw0rd!@"

def detector (password):
  val = False
  counter = 0
  alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w", "x", "y","z"]
  numbers = ["1","2","3","4","5","6","7","8","9","0"]
  characters = ["!","@","#","$","%","^","&","*"]
  for x in alphabet:
    if x in password:
      counter += 1
       
  for y in numbers:
    if y in password:
      counter += 1
       
  for z in characters:
    if z in password:
      counter += 1
       
  if len(password) > 5:
    counter += 1
     
  if counter > 3:
    val = True

  if val == True:
    print("The password is safe and valid")

  elif val != True:
    print("The password is not safe and not valid")

detector(my_password)