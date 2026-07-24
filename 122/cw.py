#slicing-არის სიიდან რაიმე ნაჭილის ამოღება

fruits=["banana","apple","bluebarries","mango"]
print(fruits[2])


numbers=[10,20,30,40,50]
numbers[1]=25

print(numbers)

colors=["red","green","blue","yellow","purple"]
color=int(input("შეიყვანე ინდექსი 0-იდან 4-მდე:"))
print(colors[color])


animals=("dop","cat","elephant","tiger","lion")
animals[4]=("ship")
print(animals)




#lower-ბეჭდავს პატარა ასოებით
#upper-ბეჭდავს დიდი ასოებით
#capitilize-მხოლოდ პირველ ასოს ადიდებს
#find-ეძებს რაიმე ტექსტში სიმბოლოს ან სიტყვას
#count-ითვლის თუ რამდენჯერ მეორდება კონკრეტული ასო,რაიმე სიტყვაში
#len-ითვლის თუ რამდენი სიმბოლოა
#endswith-ამოწმებს იმას,თუ მითითებული სიტყვით მთავრდება თუ არა ტექსტი(true da false)
#startswith-მოწმებს იმას,თუ მითითებული სიტყვით იწყება  თუ არა ტექსტი(true da false)


text=input("enter your text:")
print(text.lower())


email=input("enter your email:")
if "@" in email:
  print(email.upper())
