try:
    f = open('pqr.txt')
    if f.name == 'demo.txt':
      raise Exception
    f.close()

except FileNotFoundError:
   print("No such file found")
   
except Exception:
    print("file is currupt")