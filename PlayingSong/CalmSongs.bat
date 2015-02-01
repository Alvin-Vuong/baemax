:: randomize the songs in the bash script:
:: 2 IDEAS:
::	- put all the mp3 file names into an array [don't know if it's possible] and then based of the random number generator, access that specific song
::
:: 	- [PROBS THIS b/c easier] pick a random number and have bunch of if/else statements that will play a song depending on the number

set /a num=%random% %% 5-0

if %num%==0 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\ISeeTheLight-Tangled.mp3

if %num%==1 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\TheLazySong-BrunoMars.mp3

if %num%==2 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\ImYours-JasonMraz.mp3

if %num%==3 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\TaleAsOldAsTime.mp3

if %num%==4 start C:\Users\Allison\Documents\GitHub\baemax\PlayingSong\Songs\LaVieEnRose-LouisArmstrong.mp3

::if %num%==0 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\ISeeTheLight-Tangled.mp3

::if %num%==1 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\TheLazySong-BrunoMars.mp3

::if %num%==2 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\ImYours-JasonMraz.mp3

::if %num%==3 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\TaleAsOldAsTime.mp3

::if %num%==4 start C:\Users\Paul\Desktop\baemax\PlayingSong\Songs\LaVieEnRose-LouisArmstrong.mp3

