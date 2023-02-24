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
    if card.value = 1:
      # Single equals does not compare 2 values. This should be '=='
      return True
    else
    # No colon after else statement
      return False
   

  dif highest_card(self, card1 card2):
  # Typo 'dif' rather than 'def'. no comma between 'card1 card2'.
  if card1.value > card2.value:
    # Indent error
    return card
    # 'card' instead of 'card1'
  else:
    return card2
  


def cards_total(self, cards):
  # Wrong indent level. 
  total
  # No value set for variable 'total'
  for card in cards:
    total += card.value
    return "You have a total of" + total
    # Add space before end of string. Convert total to str. Wrong indent level for return. 
  
```
