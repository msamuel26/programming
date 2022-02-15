x = ["Amoy,9,7,9",
     "Abah,9,8,8",
     "Ambo,8,7,7",
     "Amoy,7,8,8",
     "Abah,8,8,7",
     "Ambo,9,10,6" 
  ]

def ulangan(input):
   a = {}
   o = [data.split(",") for data in x]
   for (name, math, science, english) in o:
      if name not in a:
         a[name] = [0,0,0] # math, science, english
      a[name][0] += int(math)
      a[name][1] += int(science)
      a[name][2] += int(english)
   results = sorted([[name, math, science, english]
      for name, (math, science, english) in a.items()],
      key=lambda o: (o[1], o[2]), reverse=True) 
   return results  
   
print(ulangan(x)) 