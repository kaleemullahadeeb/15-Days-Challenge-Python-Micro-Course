#Strings Method
text1="     hello python learners          "
print("Original text:",text1)
print("Remove spaces:",text1.strip())

#convert to capital letters
print("Capital letters:",text1.upper().strip())   

#proper case capital letter of each alphabet
print("Proper case: ", text1.title().strip())

#lower case
print("lower case: ", text1.lower().strip())

#Text replace
print("Replace Python word:", text1.replace("python","SQL")
      .strip().upper())

#count occurances of letters in a word
print("Letters in word are: ",text1.count("o"))

#check true or false (check if text start something)
print("Start with hello :", text1.strip().startswith("hello"))

#check if only numbers are present 
mobile="923141568236"
print("is numeric?",mobile.isnumeric())
print("is numeric?",text1.isnumeric())

#1st
msg="Welcome python Learners"
words=msg.split()
print("word list:",words)

#2nd
words=text1.split()
print("word list is here:", words)

#join with hyphen
joined_text="-".join(words)
print("Joined text:", joined_text)

#find postion of letters
print("Index of P:", msg.find("P"))

#extract domain 
email="kaleemullahadeeb@gmail.com"
domain=email[email.find("@")+1:]
print("Domain is:", domain)

#remove speacial charcter
#Advance example : Clean price 
price="Price: 3500$/-"
clean_price= price.replace("Price:","")\
.replace("$/-","").strip()
print("Clean price:",clean_price)
#DataWithKaleem
#Kaleem_Ullah_Adeeb