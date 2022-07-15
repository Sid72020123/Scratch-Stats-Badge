# Scratch-Stats-Badge
Create customized Badges with stats of Scratch User, Studio or Project. Use those badges in Github readmes, etc.

# Examples
![Griffpatch Followers](https://scratch-stats-badge.sid72020123.repl.co/user?username=griffpatch&data=followers&label=Griffpatch%20Followers)

![TimMcCool Followers](https://scratch-stats-badge.sid72020123.repl.co/user?username=TimMcCool&data=followers&label=TimMcCool%20Followers&color=blue&style=for-the-badge)

![Chiroyce Followers](https://scratch-stats-badge.sid72020123.repl.co/user?username=Chiroyce&data=followers&label=Chiroyce%20Followers&style=social)

# Documentation

## Endpoint URLs
* Root: https://scratch-stats-badge.sid72020123.repl.co/
* User Badge: https://scratch-stats-badge.sid72020123.repl.co/user?username=griffpatch
* Studio Badge: https://scratch-stats-badge.sid72020123.repl.co/studio?id=100
* Project Badge: https://scratch-stats-badge.sid72020123.repl.co/project?id=104

## User Badge
**Endpoint URL: https://scratch-stats-badge.sid72020123.repl.co/user?username=:username**

#### Required Parameters
* ```username``` - The username 

#### Optional Parameters
* ```data``` - The data of the user you want. You can select one from:
  1. id
  2. username
  3. scratchteam
  4. joined
  5. status
  6. bio
  7. country
  8. loves
  9. favorites
  10. comments
  11. views
  12. followers
  13. following
  14. messages
* [More optional parameters and styling options](#styles-and-labels)

#### Examples
![Image](https://scratch-stats-badge.sid72020123.repl.co/user?username=griffpatch&data=following&label=Griffpatch%20Following&color=blue&style=flat-square)

![Image](https://scratch-stats-badge.sid72020123.repl.co/user?username=Sid72020123&data=followers&label=Sid72020123%27s%20Followers)

![Image](https://scratch-stats-badge.sid72020123.repl.co/user?username=Chiroyce&data=followers&label=Chiroyce%27s%20Followers&style=for-the-badge)

## Studio Badge
**Endpoint URL: https://scratch-stats-badge.sid72020123.repl.co/studio?id=:id**

#### Required Parameters
* ```id``` - The ID of studio 

#### Optional Parameters
* ```data``` - The data of the studio you want. You can select one from:
  1. id
  2. title
  3. comments
  4. followers
  5. managers
  6. projects
* [More optional parameters and styling options](#styles-and-labels)

#### Examples
![Image](https://scratch-stats-badge.sid72020123.repl.co/studio?id=100&data=title&label=Studio%20Title&color=blue&style=flat-square)

![Image](https://scratch-stats-badge.sid72020123.repl.co/studio?id=100&data=loves&label=Studio%27s%20Loves)

## Project Badge
**Endpoint URL: https://scratch-stats-badge.sid72020123.repl.co/project?id=:id**

#### Required Parameters
* ```id``` - The ID of project 

#### Optional Parameters
* ```data``` - The data of the project you want. You can select one from:
  1. id
  2. title
  3. views
  4. loves
  5. favorites
  6. remixes
* [More optional parameters and styling options](#styles-and-labels)

#### Examples
![Image](https://scratch-stats-badge.sid72020123.repl.co/project?id=104&data=title&label=Project%20Title&color=blue&style=flat-square)

![Image](https://scratch-stats-badge.sid72020123.repl.co/project?id=104&data=loves&label=Project_Loves&style=social)

## Styles-and-Labels
Try the following parameters for style and labels:
* ```label``` - The label or the main title
* ```color``` - The background color of the data part. You can give any color and hex values(but without the '#' sign)
* ```label_color``` - The background color of the label part. You can give any color and hex values(but without the '#' sign)
* ```style``` - The style of the badge. You can set it to anyone from: ```flat```, ```plastic```, ```flat-square```, ```for-the-badge```, ```social```

## Note
Some of the data is taken from Scratch DB made by [DatOneLefty](https://scratch.mit.edu/users/DatOneLefty/) on Scratch. The data is not always updated.

# Credits
This project is made by [Sid72020123](https://scratch.mit.edu/users/Sid72020123/) on Scratch.
Scratch DB made by [DatOneLefty](https://scratch.mit.edu/users/DatOneLefty/) on Scratch.

**Main credits to [Shields.io](https://shields.io/) for the badges and their styles.**
