# Big Quiz

Welcome to [Battleship game](https://archie9010.github.io/Quiz/) Battleship game . 

![mockup](assets/media/mockup.png)

## Index 
* [Technologies Used](#technologies-used)
* [Fearures](#features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## Technologies Used

 * [Javascript](https://en.wikipedia.org/wiki/JavaScript)
 * [HTML5](https://en.wikipedia.org/wiki/HTML5)
 * [CSS3](https://en.wikipedia.org/wiki/CSS)
 * [Git](https://en.wikipedia.org/wiki/Git) 
 * [Github](https://en.wikipedia.org/wiki/GitHub) 
 * [Balsamiq](https://en.wikipedia.org/wiki/Balsamiq)

 ## Wireframe
The wireframe model is created as part of the project planning. Its task is to graphically present the appearance of the application on three different devices: computer - high resolution, mobile - low resolution. The application will be built on the basis of the created sketch.

### Landing Page Wireframe
![landing](assets/media/wireframe.png)
![mobile](assets/media/wireframe-mobile.png)
### Scoreboard Wireframe
![Scoreboard](assets/media/wireframe-scoreboard.png)
![Scoreboard-mobile](assets/media/wireframe-scoreboard-mobile.png)
## Features


* Featured at the top of the page, Logo and title of the website can be found.
* Scoreboard after completing 10 questions.
* Button designed to check all correct answers.
* Green/Red color after clicking on one of the 4 answers, allowing the user to see if the answer was correct or not.


## Testing

### Functionality

   
| Test Label         |            Test Action           |         Expected Outcome           | Test Outcome    |
|:------------------ |:---------------------------------|:-----------------------------------|:----------------|
|A,B,C,D answers     |  Responsive                      | Navigate to next question          | PASS            |
|Back to quiz button |  Responsive Back to Quiz button  | Navigates to landing page          | PASS            |
|Check Answers button|  Responsive Check Answer button  | Display all answers                | PASS            |
|Scoreboard          |  Calculation of Correct Answers  | Display Score                      | PASS            |

### Browser Compatibility

* Chrome (103) - Pass
* firefox (102) - Pass 
* Safari (15.4)- Pass 
* Edge (103) - Pass 

### Bugs

* 

### Validator Testing

* HTML
  - No errors were found when passing throught the [W3C validator](https://validator.w3.org/)
![html-test](assets/media/html-test.png)

* CSS
  - No errors were found when passing through the [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
  ![css-test](assets/media/css-test.png)

* Accessibility
  - Colors and fonts chosen are easy to read and accessible by running it through lighthouse in dev tools.

![performance01](assets/media/performance.png)

### Metrics

![performance02](assets/media/metrics.png)

## Deployment

* Push the latest code to GitHub.
* Go to Heroku.
* Select new in the top right corner.
* Create new app.
* Enter the app name and select Europe as the region.
* Connect to GitHub.
* Search for repo-name. 
* Select connect to the relevant repo you want to deploy.
* Select the settings tab. 
* Add buildpacks.
* Select Python, then save changes.
* Select Nodejs, then save changes.
* Make sure Heroku/Python is at the top of the list, followed by Heroku/Nodejs.
* Navigate to the deploy tab. 
* Scroll down to Manual Deploy and select deploy branch.


## Credits

* The inspiration for this project came from W3School, oyutubr videos.

### Content

* All Questions were taken from [Quizbraker](https://www.quizbreaker.com/trivia-questions#science-trivia-questions)
* All other content was written by the developer

### Media

* The Logo in the header, was taken from [Freepik](https://www.freepik.com/free-photos-vectors/quiz-logo)

### Code

* Code on how to Display question was inspired by Youtube tutorials and W3school.
* Code on how to write JS calculating function was inpspired by Love Math Project
