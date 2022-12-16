# MEE6-Grinder-4.0
_Random think's he's smart or something_

![Mee6 4 0](https://user-images.githubusercontent.com/100868154/208158290-2fe5c9a6-c304-4b8a-8835-fb55c6282273.png)

He can't beat automated bots on his server and will never detect them as long as the randomization and intervals are valid.
<br>
**New features include**:
- Clock cycling (will only run when it's x:00 to y:00 to mimic "sleeping")
- Clock randomization (adds minutes and hours to clock cycling every "day" so that you're not always "sleeping" and "waking" up at the same time)
- Better handling for multiple tokens (each token can now have their individual configurations)
- Much more settings to customize (interval, offset, offset variance, interval variance, channel, ...)
- Much easier to change settings (`client._config.{setting}.{subsetting} = x`)

Pretty much undetectable unless you set clock cycling to 0, 24 which will make it run 24/7 and remove all the intervals + randomization
