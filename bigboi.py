text = input('Enter message:')

def boxtext(text):
	print('|__', text, '__|')

bigboi = open("bigboi.txt")
boxtext(text)
for line in bigboi:
        print(line,end=' ')

