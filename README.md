# Big Quiz

Welcome to [Big Quiz](https://archie9010.github.io/Quiz/) Big Quiz is a free web application for all your knowledge needs. The topics currently available are: Geography, Science, Anatomy and Astronomy. With Big Quiz, you can easily and efficiently refresh or expand on what you already know. The website was designed with the goal of being simple and easy to use with little complexity.

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

### How to clone the repository

* Go to the https://github.com/Archie9010/Quiz repository on GitHub
* Click the "Code" button to the right of the screen, click HTTPs and copy the link there
* Open a GitBash terminal and navigate to the directory where you want to locate the clone
* On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process

The site was deployed to GitHub pages. The steps to deploy are followed:
* Logged into GitHub
* In the GitHub repository, navigate to the Settings tab.
* From the drop-down menu, select the Main Branch
* Once the Main branch has been selected, the page provided the link to the completed website.

Live link: [Big Quiz](https://archie9010.github.io/Quiz/)

## Features left to implement

  
* 
   - Database for scores that people could copeete 
   - Weekly challanges 

## Credits

* The inspiration for this project came from YouTube videos and the love math project.

### Content

* All Questions were taken from [Quizbraker](https://www.quizbreaker.com/trivia-questions#science-trivia-questions)
* All other content was written by the developer

### Media

* The Logo in the header, was taken from [Freepik](https://www.freepik.com/free-photos-vectors/quiz-logo)

### Code

* Code on how to Display question was inspired by Youtube tutorials and W3school.
* Code on how to write JS calculating function was inpspired by Love Math Project
