import json
import pprint
def get_rating(reviews):
  rating =5
  if reviews:
    rating = sum(reviews)//len(reviews)
    return '*'
with open('menu.json','r') as f:
   data = json.load(f)
items = data.get('item',[])
pprint.pprint(items)

print("-"*40)
print("Family Super Restaurant")
print("-"*40)
while True:
  print("1.Show Menu")
  print("2.Order Items")
  print('3.Add Rating')
  print('4.Exit')
  print('-'*40)
  choice = int(input())
  if choice ==1:
    print("-"*40)
    print("ID\tName\t\tPrice\tRating")
    print("-"*40)
    for item in items:
      print(f'{item.get("id")}\t{item.get("name")}\t\t{item.get("price")}\t{get.rating(item.get("reviews",[]))}')
  elif choice ==2:
    order_items =list( map(int,input('What you want to try today?').split(',')))
    print("-"*40)
    print("ID\tName\t\t  Price")
    print("-"*40)
    total_bill =0
    for order_item in order_items:
      for item in items:
       if item['id']== order_item:
         print(f'{item.get("id")}\t{item.get("name")}\t\t{item.get("price")}')
         total_bill = total_bill+int(item.get('price'))
         break
    print("."*40)  
    print("Total Amount: ",total_bill)
    print("."*40)
    
  elif choice ==3:
    print("Update items")
  elif choice ==4:
   item_id = int(input('Enter your item-id: '))
   rating = input('Giving your rating 1-5: ')
   for i , item in enumerate(items):
     if item['id'] == item_id:
       item[i]['reviews'].append(rating)
       break
     print("Thank You.Your rating is recorded")
  else:
    data['item'] = item
    with open ('menu.json','w') as f:
      json.dump(data,f)
    print("Thank You")
    break
