class Book:
     def __init__(self,title,author,price):
       self.title=title
       self.author=author
       self.price=price

     def display_details(self):
         print(f"title:{self.title} ")
         print(f"author:{self.author}")
         print(f"price:{self.price}")

     def apply_discount(self,persent):
         discount_amount=self.price*(persent/100)
         self.price-=discount_amount
        
         Book1=Book("bishoori","xavier ",200000)
         Book2=Book("shear","hafez",100000)
         Book1.display_details()
         Book2.apply_discount(10)
         print("show after discout")
         Book1.display_details()
         Book2.display_details()
      


