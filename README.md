# Simple Groupme Webhook

This simple app allows you to easily setup a groupme webhook. To use it, simply connect it to a Heroku application then configure Heroku to follow your given needs. 

In my case, I used this script to simply pass messages from a groupme chat to a discord server room. 
All it required was adding a webhook to the discord channel, then configuring Heroku to use that url:

~~~
heroku config:set WEBHOOK_URL=(discord webhook URL)
~~~

From there, you just create a new application in the [GroupMe developer portal](https://dev.groupme.com/applications) and set the callback URL to your Heroku application.
