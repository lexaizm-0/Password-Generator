import random 
print("\033[32m\033[1m__  ___    _          ____                ____            ")
print("\\ \\/ / | _| | ____  _|  _ \\ __ _ ___ ___ / ___| ___ _ __  ")
print(" \\  /| |/ / |/ /\\ \\/ / |_) / _` / __/ __| |  _ / _ \\ '_ \\ ")
print(" /  \\|   <|   <  >  <|  __/ (_| \\__ \\__ \\ |_| |  __/ | | |")
print("/_/\\_\\_|\\_\\_|\\_\\/\\_/\\_\\_|   \\__,_|___/___/\\____|\\___|_| |_|\033[0m")
print("\n\n\033[32m\033[1m\n________________\nXKKXPASSGEN\nINSTAGRAM: 07wxx7\n_________________")
print("""\n________________________________________\nSelect an option to generate a password:

easy  - Generates an easy password chance of cracking:100/95\n
medium - Generates a medium-strength password chance of cracking:100/55\n
extra - Generates a strong password chance of cracking:100/0\n______________________________""")


s = input("?:      ")
if s=='medium':
	rn = "QPEUOALZNXND0139348"
	a = "".join(random.choices(rn,k=6))
	print('\n', a)
	
elif s =='easy':
	kolay = "asdlfkhhjzxvmvvqpeutoop"
	p = "".join(random.choices(kolay, k=6))
	print('\n', p)
	
elif s=='extra':
	a = "asldhqmpqeuotpmzbcvnlapqoryrkzncbm12345667890ALDFKHZMCVBQPTP####**"
	h = "".join(random.choices(a,k=16))
	print('\n', h)
