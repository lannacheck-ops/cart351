## Week 6 Journal

Today we learned how to save data in sessions using the client side approach which Flask uses. Apparently this is not the safest option to save sensitive information because the data can be accessed through the client-side in browser cookies. I find this very fascinating becuase at first when the user makes a new page request (submits a new form or reloads the page), we had no way of accessing the previous data. So sessions provides a way for us to store that data related to a particular user, across different requests. My question then is how can we store sensitve data that the client can't access.

We also learned how to submit a form without reloading the page by using javascript to pass the form input to a different app route's arguments and fetching the information in those arguments while keeping the info the user inputted on the same page. By default, when using javascript to pass a form's data to an app route's url, it uses a get request; meaning the information is stored the url's arguments. However a url can only store a certain amount of characters which means heavier data such as images can't be stored using a get request.

So when uploading files to a form, we need to specify when fetching that data that we are using a post method in javascript and in python. The file can also be saved server side in a file using the os module and by saving the file in a defined app.config file path.


