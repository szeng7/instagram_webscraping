# An intermediary file used to update my textfile of users (since I was hitting a cap of around 90 requests)
import pandas as pd

def main():

	user_dict = {}

	with open("users.txt", 'r') as f:
		lines = f.readlines()
		for line in lines:
			user_dict[line.strip("\n")] = 1

	prev = len(user_dict)

	userfile = "scraped/user/18-07-2019_11"
	user_df = pd.read_json(userfile, lines=True)
	user_df = user_df.rename(columns={'user': 'owner_name'})

	user_df = user_df.drop_duplicates('owner_name')

	for x in user_df['owner_name']:
		try:
			del user_dict[x]
		except:
			print(x)

	with open("users.txt", 'w') as f:
		for x in user_dict.keys():
			f.write(f"{x}\n")

	after = len(user_dict)

	print(f"DELETED {prev - after} ENTRIES \n\n\n\n\n\n\n\n\n")

if __name__ == "__main__":
	main()