# VoiceCoder
This is a small project to allow the user to write code by voice input.  It uses Google speech to text.

Voice Commands:

type mode - this will put the program into a mode where it will attempt to type whatever you speak.
  special characters can be entered by name:
    space, tab, enter, backspace, parentheses, end parentheses, bracket, end bracket, curly, end curly, pipe, shift, up, down, left, right
  
  Repeat - an action or word can be repeated by saying repeat, followed by a number, followed by the key or word to repeat.
  eg. "Repeat Ten Backspace" should cause the backspace key to be pressed ten times.
  
  pass - sometimes google will get confused if you repeat a word multiple times and put in extras.  To compensate for this, I added a "pass" word which does nothing.
  eg. use "Left pass left pass" instead of "left left" to avoid Google translating it as "left left left".

  undo - this will hit control-z to undo the last edit.

command mode - this will put the program into a mode where each phrase will begin with a command, followed by whatever parameters are needed.

Add - This will add a line of code at the current cursor location




  
  
