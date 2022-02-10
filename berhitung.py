x = ["Amoy,9,7,9",
     "Abah,9,8,8",
     "Ambo,8,7,7",
     "Amoy,7,8,8",
     "Abah,8,8,7",
     "Ambo,9,10,6" 
  ]

def ulangan(input):
   c = {}
   i = [data.split(",") for data in x]
   for (name, math, science, english) in i:
      if name not in c:
         c[name] = [0,0,0] # math, science, english
      c[name][0] += int(math)
      c[name][1] += int(science)
      c[name][2] += int(english)
   print("results dengan reverse True")
   results = sorted([[name, math, science, english] for name, (math, science, english) in c.items()], key=lambda x: (x[1], x[2]), reverse=True)
   return results

print(ulangan(x)) 