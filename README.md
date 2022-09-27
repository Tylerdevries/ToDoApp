# To Do App
This To Do App is a application developed by me inspired by both the todolist walkthrough project and the blog worked on prior to this project. The goal of this site is to allow individual users to sign in to create a fully amendable todolist where they can track tasks. 

Users of this site will be able to register from the homepage. Once registered they can sign in and view their own data which will be saved via a postgresql database.
The site is targeting towards all people who are looking to make us of a unique and comprehensive app.

![todo app](https://user-images.githubusercontent.com/93283135/192441816-70012c1a-1640-4d59-be2d-f4e792c9db7c.PNG)

## Features:
### General Navigation:
Users are initially directed to a login page where they can sign in using a username and password or use a register redirect to sign up for the app.

New users will be directed to a register page where there will be three fields for them to fill out, Username, password and password confirmation. 

Users that have either logged in or registered will be directed to the home page. Here they will have a multitude of options including logout, create task and search.

Returning users can delete or update alreaady created tasks.

The site has been styled using CSS.

![login screen](https://user-images.githubusercontent.com/93283135/192444712-e37a3582-106e-45c1-8c30-dc1ccbf2cf81.PNG)
![login view](https://user-images.githubusercontent.com/93283135/192444694-a841206d-cc1b-4fa8-9dad-c5098230c10c.PNG)



### The Login Page:

The login page is the first page shown to a user that isn't logged in.

It asks the user for a username and password. Djangos built in class for login authorization will validate the information given through the database.

Below the login button, users can register for the app by follow the link titled register. 

A screenshot of the view for this page is shown above. This view is called on within the urls.py file and is tested on in the test.py file. 

![image](https://user-images.githubusercontent.com/93283135/192445925-ff257c1b-cc91-4ac5-b761-237a9ca46e64.png)
![register code](https://user-images.githubusercontent.com/93283135/192446140-d917bbd2-f44a-48ce-b3bd-8433d7693f74.PNG)


### Register Page:

Here the user can sign up for the app.

Upon sign up completion the user is redirect to the home page.

The view used here is displayed above. This confirms authorisation and adds the user to the database. 

This view is called on within the urls.py file and is tested on in the test.py file. 

![home page](https://user-images.githubusercontent.com/93283135/192447633-f21076f7-2951-464b-96e4-5c333a9efd7b.PNG)
![task list](https://user-images.githubusercontent.com/93283135/192447656-8253d6d1-f0a1-434c-943f-5071d2153a83.PNG)


### The Home Page:

The home page shows all available features to the user in a comprehensive list.

Here the user can logout using the link in the top right corner of the app. This link will redirect the user back to the login page. 

The header at the top of the page is styled to welcome the user by their username and tell them how many incomplete tasks they remaining in their todo list.

The search bar is below this and uses the django search feature to search the users the todo list. The view interprets strings typing into the search and searches for tasks contains these strings within their name.

To the right of the search bar is a plus button which when pressed will redirect the user to an empty form where the user can create a new task.

Below these two features is the list of todos. Here the user can see what todos are completed and what are pending via the styling. 

If the user clicks on the task from the shown list it will redirect them to the form with the task information. 

The X button features on the task will redirect the user to a delete confirmation page. 

The three dots on the far right can be held and dragged to drag the tasks to rearrange the order of the list. 

Above is the view for the functioning of this page.

This view is called on within the urls.py file and is tested on in the test.py file. 



![create task](https://user-images.githubusercontent.com/93283135/192454054-921d4d9a-10ee-4966-ac9a-4ee524968424.PNG)
![create tasks](https://user-images.githubusercontent.com/93283135/192454110-8c193a54-4e95-48bb-a111-d86142cab263.PNG)



### The Task Creation Form:

This is the page the user is directed to when clicking on the plus symbol on the home page.

Here the user can title their task and leave a description that can be seen when the task is opened. 

Upon submitting the information the task is added to the home page and the user is returned to it.

The user can return to the home page by clicking the back link at the top left of the page. 

Above is the view for the functioning of this page.

This view is called on within the urls.py file and is tested on in the test.py file. 

![update](https://user-images.githubusercontent.com/93283135/192455937-e84c61f4-666a-4a06-ae0a-823c990505b7.PNG)
![update and delete](https://user-images.githubusercontent.com/93283135/192455887-9599e91d-e743-4622-a20c-162bac7c7ccc.PNG)
![delete](https://user-images.githubusercontent.com/93283135/192455952-1df19229-44a7-4a14-b6d9-ffc87c65f0da.PNG)


### Delete and Update Task: 

The delete page shown above appears when the user clicks on the X icon alongside a task.

Here the user is prompted to confirm that they wish to delete the task. 

I added a confirmation page as a new user could accidentally press this button and this could lead to poor user experience.

The edit page shown above is shown when the user clicks on the name portion of a task.

Here the user is shown what was previously filled out in these fields including and can make changes which will reflect on the home page. 

Above is the views for the functioning of these pages.

![66666666666666666666666666666666666](https://user-images.githubusercontent.com/93283135/147124550-b3bb42e2-7c62-49b4-b383-f62aa33e0bb8.PNG)



### The footer:

I created a simple footer with links to social media platforms.

I linked facebook and twitter.

I customised these icons using CSS. 

![898989889889898989](https://user-images.githubusercontent.com/93283135/147102370-f567fb2d-1e27-4889-b4c2-2db81a5a8932.PNG)

## Testing

I tested that the page works in the primary browsers used on desktop and mobile. (Edge, Chrome, Firefox and Safari)

I confirmed that the project is perfectly responsive and works on all screen sizes using Developer Tools on Google Chrome.

I confirmed that all sections are readable and easy to access.

I confirmed that all elements are working, ie. Navbar, buttons and Email Form.

## Bugs

### Solved Bugs

I initially had issues with images appearing on the deployed page, I fixed this issue by using proper relative paths in my img elements. 

Code pre fix:

![4141414141](https://user-images.githubusercontent.com/93283135/147103532-d538ff32-8172-40ee-b9e2-769b998681fc.PNG)

Code post fix:

![55585858585](https://user-images.githubusercontent.com/93283135/147103568-7d68c784-912a-489d-bc4a-c0f9c08744ca.PNG)

## Validator Testing

### HTML:

I used the W3C validator to check for any issues in the code and to quickly resolve said issues.

### CSS:

I used the Jigsaw Validator to check for any CSS issues and to again quickly resolve them.

### Accessbility:

I confirmed with the Lighthouse Tool in chrome that my site is easily readable and accessible. 

![555555555555555555555555555555555555555555555555555555](https://user-images.githubusercontent.com/93283135/147125198-fadd21e6-13f8-46b5-9b19-213da50ae118.PNG)

### Unfixed Bugs

No unfixed bugs

## Deployment

The site was deployed through Github pages. 

I used the following steps to deploy my page:
1. Use GitHub Directory, navigate to the Settings Page.
2. From the Settings menu select Pages.
3. From the Source option select Main Branch and Root Folder
4. Click save.
5. Wait a couple of minutes and the page is live.

The livelink can be found here https://tylerdevries.github.io/TDV-Web-Design/#

## Credits

I used the following sites as sources for images, CSS, HTML and Bootstrap components.

unsplash.com

getbootstrap.com

fontawesome.com

getwaves.io

cssgradient.io
