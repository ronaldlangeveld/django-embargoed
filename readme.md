Django-Embargoed

====

Django-Embargoed is [Django](https://www.djangoproject.com) middleware with a that blocks all requests from Russia and displays a pro-Ukraine message instead.

  

This is a port of [Embargoed](https://github.com/rameerez/embargoed) by my good friend [Rameerez](https://github.com/rameerez).

  

Here's the message that replaces all pages of your app:

  

![Embargoed message displayed to Russian visitors](https://github.com/rameerez/embargoed/blob/main/public/embargoed-message.jpg?raw=true)

  
  

##  Installation

  

`pip install django-embargoed`

In your `settings.py` file


```
INSTALLED_APPS  =  [
...
'embargoed'
...
]


MIDDLEWARE  =  [

'embargoed.middleware.EmbargoedMiddlewareTemplate',

]

```

  
  That's it.  Traffic from Russia is now blocked.
  

##  Collaborate

  

Please feel free to contact me [@ronaldlangeveld](https://twitter.com/ronaldlangeveld) or fork this to port it to other platforms, or make PRs to this repo to collaborate.