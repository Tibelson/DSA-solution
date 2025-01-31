  def swap_case(s):
    emptystr = ''"
     for char in s:
         if char.islower():
             emptystr += char.upper()
         else:
             emptystr += char.lower()
     return emptystr