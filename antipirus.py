#The list of triggers. Please feel free to add more. Make sure all are in lowercase.
dangerlist = ["ngrok.io","servo.net","subprocess","os.system","sudo rm -rf","socket","connect(","hack","pwn","virus"]
#If you're reading this on your alert pane, don't worry. This is the list of known-bad words, so every single one of them will trip. It's like checking if 1,2, or 3 is in the list 1,2,3. But props for being paranoid ;)

import sys
import hashlib

print("AntiPirus 1.0")
print("Enter a .py file to determine potential risk")
filename=raw_input("FILE > ")
try:
    f = open(filename,"r")
except:
    exit("File could not be opened.")
contents=f.readlines()
f.close()

lines=0
maliciouslines=0

for line in contents:
    line=line.lower().lstrip().strip("   ").strip("\x0B")#Strip extra whitespace mid-code - helps eliminate some obfuscation
    lines+=1
    onthisline=0
    for word in dangerlist:
        if word in line:
            if line[:1]=="#" and "hack" not in line and "pwn" not in line:
                pass #Comments never hurt anybody (Unless they're talking about how awesomely someone pwnd you, in which case it's a tipoff)
            else:
                if line[:len("except ")]=="except ":
                    pass #Who hates error handling?

                if line[:len("import ")]=="import ":
                    print("\n[!] Potentially hazardous import located on line {}.\nThis may not be malicious, but could be used to assist in malicious deeds.\n{}Item of alarm:\n{}".format(lines,line,word))
                    maliciouslines+=1
                    onthisline+=1
                else:
                    print("\n[!] Potentially malicious line found on line {}! \n{}Item of alarm:\n{}".format(lines,line,word))
                    maliciouslines+=1
                    onthisline+=1
            
    if onthisline>=2:
        print("[!] Multiple ({}) potentially dangerous lines located on line {}!".format(onthisline,lines))

print("\n\n-----------------------")
print("File analysis complete.")
print("Discovered {} potentially malicious items, out of {} total lines.".format(maliciouslines,lines))
print("Final verdict:")
dangerous=False
if maliciouslines>(lines/4) or maliciouslines>20:
    print("File is extremely dangerous! Do not execute under any circumstances!")
    dangerous=True
elif maliciouslines>(lines/10) or maliciouslines>10:
    print("File is deemed highly dangerous, and should not be run.")
    dangerous=True

elif maliciouslines>(lines/50):
    print("File is largely safe, but is a risk of infection. Be cautious when running this file.")
elif maliciouslines>(lines/100):
    print("File is likely safe, and any alerts are likely false positives. However, as always, exercise caution when running this file.")

else:
    print("File is safe, however, please exercise caution when running this file.")
print("\n---------------")
print("Recommendation:")
if dangerous:
    print("File is considered potentially dangerous. Manual review is recommended.")
else:
    print("File is not considered particularly dangerous. Manual review is always smart, though ;)")


