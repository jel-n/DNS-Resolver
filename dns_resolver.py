# DNS and R-DNS lookups
import socket
import re
import pandas as pd

def reverse_dns():
	print("""
1.) Single Host
2.) Host List""")
	try:
	
		option = int(input())

		if option == 1:
			hostname = input("Hostname: ")
			ip_addr = socket.gethostbyname(hostname)
			print(ip_addr)
		elif option == 2:
			print("FUNCTIONALITY COMING SOON...")
		else:
			print("Invalid Option")
			reverse_dns()

	except KeyboardInterrupt:
		print("Exiting..")
	
def dns_lookup():
	print("""
Select an option:
1.) Single IP
2.) IP List""")
	option = int(input())
	if option == 1:
		ip_addr = input("\nIP Address: ") 

		if regex(ip_addr):	
			try: 
				hostname = socket.gethostbyaddr(ip_addr)[0]
				print(f"Hostname: {hostname}")

			except socket.herror:
				print("ERROR")
		else:
			print("NO")
	
	
	elif option == 2:
		
		ip_list_file = input("Filename: ")
		
		ip_list = open(f"{ip_list_file}", "r").read().splitlines()
		list2 = []
		
		for item in ip_list:
			try:
				hostname = socket.gethostbyaddr(item)[0]
				list2.append(hostname)				
				
			except socket.herror:
				list2.append(None)
				
		# Not sure what the "list" and the "zip" do....
		df2 = pd.DataFrame(list(zip(ip_list, list2)), columns=["IP Address", "Hostname"])
		df2.to_csv("dns_results.csv")
		
	else:
		print("Invalid Option")
		dns_lookup()

def regex(ip_addr):
	if re.match('^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ip_addr):
		return True 
	else:
		return False

def main():
	print("""
Select an option from below:
1.) DNS Lookup
2.) Reverse DNS Lookup""")
	option = int(input())

	if option == 1:
		dns_lookup()

	elif option == 2:
		reverse_dns()

if __name__ == "__main__":
	main()
