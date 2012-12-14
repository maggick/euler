import math

def checkio(number):
    nb = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen"
        , "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    diz = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    string = ""
    
    if number >= 100:
        string += nb[int(number /100)] + "hundred"
		if (number%100)!=0:
			string+="and"
        number -= int(number/100)*100
    
    if number >= 20:
        if string != "":
            string += ""
        string += diz[int(number/10)-1]
        number -= int(number/10)*10
    
    if number <20 and number != 0:
        if string != "":
            string += ""
        string += nb[number]

    return string

if __name__ == '__main__':
	i = 1
	res = 0
	print (checkio(567))
	while i < 1000:
		res += len(checkio(i))	
		i+=1
	res += len("onethousand")
	print (res)
	
