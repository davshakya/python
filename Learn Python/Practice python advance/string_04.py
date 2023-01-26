letter='''Dear |Name| you are selected
Your joining is |DATE|.'''
name=input("Enter the name")
date=input("Enter the date")
letter=letter.replace("|Name|",name)
letter=letter.replace("|DATE|",date)

print(letter)