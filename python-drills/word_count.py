file_path = "C:/Users/AYO-AJAYI  OLUWATOKI/Documents/authentication    vs     authorisat.txt"
count = 0
try:
   with open( file_path, "r") as file:
      content = file.read()
      for item in content.split():
            count +=1
      print(count)
except Exception :
   print( f"this failed:" )
   
