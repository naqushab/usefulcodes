import gntp.notifier

# Simple "fire and forget" notification
gntp.notifier.mini("Here's a quick message")

# More complete example
growl = gntp.notifier.GrowlNotifier(
        applicationName = "My Application Name",
        notifications = ["New Updates","New Messages"],
        defaultNotifications = ["New Messages"],
        # hostname = "computer.example.com", # Defaults to localhost
        # password = "abc123" # Defaults to a blank password
)
growl.register()

# Send one message
growl.notify(
        noteType = "New Messages",
        title = "You have a new message",
        description = "A longer message description",
        icon = "http://example.com/icon.png",
        sticky = False,
        priority = 1,
)

# Try to send a different type of message
# This one may fail since it is not in our list
# of defaultNotifications
growl.notify(
        noteType = "New Updates",
        title = "There is a new update to download",
        description = "A longer message description",
        icon = "http://example.com/icon.png",
        sticky = False,
        priority = -1,
)

# Send the image with the growl notification
image = open('/path/to/icon.png', 'rb').read()
growl.notify(
        noteType = "New Messages",
        title = "Now with icons",
        description = "This time we attach the image",
        icon = image,
)
