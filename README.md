# Reps480085
PULSE 2015 Signal Processing Competition
![](/rfb.JPG)

## Demo Video
https://www.youtube.com/watch?v=Teqs34rAfFM

## The Competition
ECE PULSE is a major conference that happens every year in UIUC that celebrates advances in electrical and computer engineering. As part of the conference, there are multiple student competitions and our team took part in one of them, the signal processing challenge. [More information about the conference.](http://pulse.ece.illinois.edu/)

## The Task
We were given the task of doing something unique or awesome with an EMG sensor. More specifically, we had to help a student who _"needed to lose weight fast to appear desirable to members of the opposite sex in any hopes of getting a date for Valentine’s Day"_ through signal processing techniques. ([Competitiion prompt can be found here](http://pulse.ece.illinois.edu/?pg=snp))

## Our Solution
Our project, Reps480085, is a personal fitness motivator that helps to count your reps when lifting weights. Not only that, it uses a customizable gallery of images that will show up one by one for each set. For each set, the image will start out with the lowest resolution possible and it will increase until it reaches the maximum resolution when you reach the final rep of the set. It will reset at the end of the set so that you know you are done with the set.

## How does it work?
We process the data coming out of a op amp circuit (the EMG sensor) with an Arduino. Once the data is processed, we send it to our computer via serial and a python applet running in it will take care of the visualization and rendering of images onto the screen. The competition was 12 hours long but we finished this app in around 3 hours.

## Thanks
Thanks to the ECE PULSE Committee for organizing this competition and giving us the opportunity! We had loads of fun!

## Members

[Brady Salz](http://bradysalz.com)

[Dario Aranguiz](https://github.com/daranguiz)

[Sulaiman Ahmed Suhyl](http://ahmedsuhyl.com)

Check out our last project, [nextWAVE](https://github.com/kashev/nextWAVE), that got [featured on Hackaday](http://hackaday.com/2014/04/14/smart-microwave-shows-you-how-its-done/)!


