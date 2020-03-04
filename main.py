import math


def convertor(string):
	list_of_string = []
	start_index=0
	no_of_division = math.ceil((len(string)/110))
	for i in range(no_of_division):
		if i == no_of_division-1:
			list_of_string.append(string[start_index:len(string)])
		else:
			list_of_string.append(string[start_index:start_index+110])
			start_index+=110
	return list_of_string		
			

if __name__=='__main__':
	string = input('Enter the long string to make small : ')
	l = convertor(string)
	for i in l:
		print("b'",end='')	
		print(i,end='')
		print("'/")
	
