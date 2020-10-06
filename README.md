# Odoo decorator
# Task Implement Odoo addon with the followng functionality
- Functions, decorated with @api.constraints should send their result to messenger
# Solution
- Implemented telegram bot, that waits for some number of users, that send \start command to him.
- When bot has needed number of users, it sends result of function to all users who send him \start command.
- NUMBER_OF_USERS_TO_WAIT_FOR in constants module sets number of users to wait for
- Implemented second order decorator, i.e decorator, that decorates other decorator
- Decorated api.constraints decorator with telegram_msg decorator 
