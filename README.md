## BOO-BLOG

13th NOV 2021

## Author
Elizabeth Gikonyo

## Description
Is a flask application that allows one to create a personal blogging website where you can create and share your opinions and other users can read and comment on them after registering to the blog.

## Live Link

https://boobloggy.herokuapp.com/

## User Story

As a user;

1.i would like to view the blog posts on the site.

2.comment on blog posts

3.view the most recent posts

4.receive email alert when a new post is made by joining a subscription.

5.see random quotes on the site

6.sign in to the blog.

7.create a blog from the application.

8.delete comments that I find insulting or degrading.

update or delete blogs I have created.

## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | *On page load* | Get all blog posts, Select between signup and login on the right side|
| Select SignUp| *Email,Username,Password* | Redirect to login|
| Select Login | *Username* and *password* | Redirect to page with app Blog-Web based on categories and commenting section|
| Select comment button | *Comment* | Form to input your comment|
| Click on submit |  | Redirect to all comments templates with your comment and other comments|

## Cloning the repository:

https://github.com/lizgi/my-blog

Move to the folder and install requirements

cd my-blog

pip install -r requirements.txt

Exporting Configurations

export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

## Running the application

python3.8 manage.py server

running the test

python3.8 manage.py test

Open the application on your browser .

## Technology used

Python3.8

Flask

Heroku

## Known Bugs

There are no known bugs.

## Contact Information

If you have any question or contributions, please email me at [elizabeth.gikonyo@moringaschool.com]

## License

MIT License

Copyright (c) 2021 lizgi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
