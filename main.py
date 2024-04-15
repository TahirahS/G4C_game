import asyncio
import webbrowser
from webbrowser import alert, html, window
import play

play.set_backdrop("white")

score_message = play.new_text("You collected 0 bottles!",
                              font_size=30,
                              x=-200,
                              y=275)

turtle = play.new_image(image="turtle.png", size=30, y=40)

bottle = play.new_image(image="bottle.png", size=5, x=100, y=200)


@play.repeat_forever
async def movement():
  if play.key_is_pressed('up'):
    turtle.y += 7
  if play.key_is_pressed('down'):
    turtle.y -= 7
  if play.key_is_pressed('left'):
    turtle.x -= 7
  if play.key_is_pressed('right'):
    turtle.x += 7


bottles = [bottle]
for i in range(9):
  bottle_clone = bottle.clone()
  bottle_clone.x = play.random_number(-350, 350)
  bottle_clone.y = play.random_number(-250, 250)
  bottles.append(bottle_clone)

original_bottles = len(bottles)


@play.repeat_forever
def collection():
  for bottle in bottles:
    if turtle.is_touching(bottle):
      bottle.hide()
      bottles.remove(bottle)
      score = original_bottles - len(bottles)
      score_message.words = "You have collected" + str(score) + "bottles!"


play.start_program()
