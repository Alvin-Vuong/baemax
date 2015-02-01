:: randomize the songs in the bash script:
:: 2 IDEAS:
::	- put all the mp3 file names into an array [don't know if it's possible] and then based of the random number generator, access that specific song
::
:: 	- [PROBS THIS b/c easier] pick a random number and have bunch of if/else statements that will play a song depending on the number

set /a num=%random% %% 5-0

::if %num%==0 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\LoseYourself-Eminem.mp3

::if %num%==1 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\ThePhoenix-FallOutBoy.mp3

::if %num%==2 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\CantHoldUs-Macklemore.mp3

::if %num%==3 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\Centuries-FallOutBoy.mp3

::if %num%==4 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\BeatIt-MichaelJackson.mp3

if %num%==0 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\LoseYourself-Eminem.mp3

if %num%==1 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\ThePhoenix-FallOutBoy.mp3

if %num%==2 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\CantHoldUs-Macklemore.mp3

if %num%==3 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\Centuries-FallOutBoy.mp3

if %num%==4 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\BeatIt-MichaelJackson.mp3