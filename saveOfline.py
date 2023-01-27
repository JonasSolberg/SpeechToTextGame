import gtts



def saveOflline(inputtext):
  tts = gtts.gTTS(inputtext, lang="en")
  tts.save("choice1Text9.mp3")

saveOflline("Once upon a time, there was a boy. His name was Jack. Jack lived with his mother far out in the countryside. His mother would say that Jack was good-natured, but a bit lazy. Jack and his mother were quite poor, and one day there was no money left to buy food. Jack’s mother then told him to take the cow to the market and sell it, but only for a good price. On the way there Jack meets the butcher. He asked where Jack was taking the cow. I'm taking the cow to the market. My mother told me to sell it, Jack said. What a nice cow. You know what? If you sell the cow to me, I will pay you with these five magic beans, the butcher said. Jack looks at the beans. He kinda thinks they look like regular beans, but when he looks closely, he can see that they sparkle! Will Jack accept this offer? Say Yes or No.")