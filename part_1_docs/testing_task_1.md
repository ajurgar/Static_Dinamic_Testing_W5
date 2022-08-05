### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1:    #missing = for the if statement--- it should be card.value == 1
      return True
    else                #missing :
      return False
   

  dif highest_card(self, card1 card2):    #missing "," between card1 card2 and def instead of dif
  if card1.value > card2.value:         #indentation if, else and returns
    return card                         #missing card1 not card
  else:
    return card2
  


def cards_total(self, cards):
  total             #missing total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total    #indentation for return + space at the end of string and str(total)
  
```
