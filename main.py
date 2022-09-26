#red3
from rich.console import Console

console = Console()
console.print("")
console.print([1, 2, 3])
console.print("[deep_sky_blue1]Looks like a link ", end="")
# console.print(locals())
console.print("FOO", style="white on blue")

print("WELCOME TO TIC-TAK-TOE!")
def is_winner(d, val):
    if [    d["a1"], d["a2"], d["a3"]    ] == [val, val, val]:
        return True
    if [    d["b1"], d["b2"], d["b3"]    ] == [val, val, val]:
        return True
    if [    d["c1"], d["c2"], d["c3"]    ] == [val, val, val]:
        return True
    if [    d["a1"], d["b1"], d["c1"]    ] == [val, val, val]:
        return True
    if [    d["a2"], d["b2"], d["c2"]    ] == [val, val, val]:
        return True
    if [    d["a3"], d["b3"], d["c3"]    ] == [val, val, val]:
        return True
    if [    d["a1"], d["b2"], d["c3"]    ] == [val, val, val]:
        return True
    if [    d["a3"], d["b2"], d["c1"]    ] == [val, val, val]:
        return True
    return False
something = """[white]
   1   2   3
 a {} | {} | {}
  ---|---|---
 b {} | {} | {}
  ---|---|---
 c {} | {} | {}
"""
d = {
    "a1": " ",
"a2": " ",
"a3": " ",
"b1": " ",
"b2": " ",
"b3": " ",
"c1": " ",
"c2": " ",
"c3": " ",
}
console.print(something.format(d["a1"],d["a2"],d["a3"],d["b1"],d["b2"],d["b3"],d["c1"],d["c2"],d["c3"]))
val = "x"
while True:
    cord = input("enter coordinates for {}:  ".format(val))
    while cord not in d:
        print("'{}' is invalid enter coordinates".format(cord))
        cord = input("enter coordinates for {}: "   .format(val))
    while d[cord] != " ":
        print("'{}' is already taken".format(cord))
        cord = input("enter coordinates for {}: "   .format(val))    
    # val = input("x or o: ")
    # while val not in ["x","o"]:
    #     print("'{}' is invalid enter x or o ".format(val))
    #     val = input("x or o: ")
    if val == "x":
        d[cord] = val
    else:  
        d[cord] = "[deep_sky_blue1]" + val + "[white]"

    console.print(something.format(d["a1"],d["a2"],d["a3"],d["b1"],d["b2"],d["b3"],d["c1"],d["c2"],d["c3"]))
    x_is_winner = is_winner(d, "x")
    o_is_winner = is_winner(d, "o")
    if x_is_winner:
        print ("X WIN'S THE ROUND!")
        break
    if o_is_winner:
        print ("O WIN'S THE ROUND!")
        break
    if val == "x":
        val = "o"
    elif val == "o":
        val = "x"