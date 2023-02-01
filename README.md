# DECIDE

## Running
Requirements:
* Python >= `3.8`
* numpy >= `1.16.4`
* PyYAML >= `5.1.1`

## Testing
To run an individual test, run `python -m unittest tests.test_name` from the main directory, replacing
`test_name` with the name of the test.

To run all tests, run `python -m unittest discover -s tests -p '*_test.py'` from the main directory.

## Assignment 1: DECIDE
*The first assignment in the project-course DD2480 at KTH.*

#### Problem
What is done in particular is to create a program that will decide if a interceptor should be launched,
based upon input radar tracking information.

#### Goal
The general goal of this assignment is to implement a program according to the modern development techniques.

#### Statement of contributions
Patrik Kinnunen: Created most issues together with Adam. Did CMV conditions 1, 5, 9 and 13. Implemented the FUV.

Adam Genell: Created most issues together with Patrik. Did CMV conditions 0, 4, 8 and 12.

Anton Björklund: Did CMV conditions 2, 6, 10 and 14.

Wenqi Cao: Created the code base and a basic test file which all other tests files were modeled after.
Did CMV conditions 3, 7 and 11.

#### Way of working according to Essence
Our team is currently in the "In place" state. All team members are using the agreed upon tools
and formatting guidelines to do work. To get to the "Working well" state, the team needs to get more used
to writing and performing tests with the tools we are using. In our current state we are still getting used to
the tools and practices.

#### License
The project is available under the MIT license. See the COPYING file for more info.

Note about the name of this file: We received feedback to change the name to LICENSE, but we
believe it is fine to keep it as COPYING as many open source projects use this name. For example,
[coreutils](https://git.savannah.gnu.org/cgit/coreutils.git/tree/COPYING),
[bash](https://git.savannah.gnu.org/cgit/bash.git/tree/COPYING),
[Git](https://github.com/git/git/blob/master/COPYING) and
[curl](https://github.com/curl/curl/blob/master/COPYING)
use the file name COPYING.


#### Document how you fulfill P+ critieria
We have read the criterias for getting a pass, and fulfilled every one of them.
We are using appropriate file-names and using folders to divide the code-sections.
We are using test-cases for our implementations to assure that the program is functionally 
correct. There is atleast one unit-test per LIC and atleast two tests which include a positive
test and a negative test with invalid inputs. We are using clear commit-tags such as FIX, FEAT 
and DOC. Every commit contains the added feature/functionality together with corresponding testcases.
The work is divide between the group members so everyone almost has the same amount of commits.
We have documented our way of working. We had a good structure and planning in the beginning of
the project which made us decide to create almost all of our issues, and relate them to specific
features/functionality. This made us be able to fulfill the P+ criteria which is that Most of our
commits are linked to an issue describing the feature / commit.
