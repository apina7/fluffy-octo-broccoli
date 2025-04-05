# Final Project
# CS 111, Hayes & Reckinger
# This is the applictation QuikAdvise! This is a financial tracker that first tells the user the recommended amount you can spend and tracks one's expenses while also displaying how much they make using the image of a calendar.

import turtle
import random

# These are the turtles that we are using throughout the application
t = turtle.Turtle()
s = turtle.getscreen()
text = turtle.Turtle()
box = turtle.Turtle()
box_text = turtle.Turtle()


feesible = True
turtle.tracer(False)






# Title Screen Function
# Parameters: None
# Returns: None
# This function serves to display the title screen of our application.
def title_screen():

    s.clearscreen()

    s.bgcolor("grey")
    text.goto(-10,0)
    text.write("Welcome to our Finance Application, QuikAdvise!", False, align = 'center', font = ('Copperplate', 20))
    text.goto(-10, -30)
    text.write("Press anywhere to continue...", False, align = 'center', font = ('Copperplate', 20))


# Ending Screen Function
# Parameters: None
# Returns: None
# This function serves to display the ending screen of our application.
def ending_screen(x,y):
    s.clearscreen()
    s.bgcolor('grey')
    text.goto(-10,0)
    text.write("Thanks for using the Finance Application", False, align = 'center', font = ('Copperplate', 20))
    text.goto(-10, -30)
    text.write("Closing App...", False, align = 'center', font = ('Copperplate', 20))



# Calls the title_screen() function
title_screen()


# This is list4...This is a very important list as we append all of our variables into this list to access it throughout the entire application.
list4 = []

# Calendar Call Function
# Parameters: x, y- Position parameters for the on-screen events
# Returns: None
# This function is the crux of our application. This function serves to construct the calendar while displaying the savings box and the profit in each cell in the calendar.
def calendarCall(x, y):
    s.clearscreen()
    s.bgcolor('grey')
    turtle.hideturtle()
    counter = 0
    x_position = -250
    count_x_position = 1
    y_position = 250
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()

    # Savings box Construction
    box.penup()
    box.goto(-350, -260)
    box.pendown()

    box.fillcolor('white')
    box.begin_fill()


    for j in range(2):
        box.forward(700)
        box.right(90)
        box.forward(25)
        box.right(90)
    box.end_fill()

    box_text.penup()
    box_text.goto(-10, (-280))
    box_text.pendown()


    week = 0
    amount_saved = 0
    cog = list4[2]
    w_save = list4[3]

    # While loop that will allow the user to keep inputting their expenses until they cross the recommended number of screens AND they saved more than what they want to save.
    while(week != weeks_needed and amount_saved <= cog):


        # Turtle-User Inputs
        amount_spent = turtle.textinput('Amount Spent', 'Type the amount spent in your respective periods (Weekly, Daily, Monthly):')
        box_text.clear()
        amount_allowed = float(list4[1])
        amount_spent = float(amount_spent)
        pay_period = list4[0]

        profit = amount_allowed - amount_spent

        # Calculations for saving depending on the time period.
        if(pay_period == 7):
            w_save = w_save

            amount_saved += w_save
            amount_saved += profit
        elif(pay_period == 30):
            w_save = w_save/7

            amount_saved += w_save
            amount_saved += profit
        elif(pay_period == 1):
            w_save = w_save * 4.1

            amount_saved += w_save
            amount_saved += profit

        # The text that goes in the savings box: displays the savings.
        box_text.write('Savings: $' + f'{amount_saved:.2f}', False, align = 'center', font = ('Copperplate', 10))

        turtle.penup()
        turtle.goto(x_position, y_position)
        turtle.pendown()

        if amount_spent > amount_allowed:
            color = 'red'
        else:
            color = 'green'


        # Constructs the calendar-grid
        if pay_period == 7:

            if (counter == 4):
                s.clearscreen()
                s.bgcolor('grey')
                counter = 0
                y_position = 250
                turtle.penup()
                turtle.goto(x_position, y_position)
                turtle.pendown()

                box.fillcolor('white')
                box.begin_fill()

                for j in range(2):
                    box.forward(700)
                    box.right(90)
                    box.forward(25)
                    box.right(90)
                box.end_fill()

            calendar(pay_period, color, x_position, y_position, profit)



            y_position -= 500/4 + 10

        elif pay_period == 30:
            if counter == 31:
                s.clearscreen()
                s.bgcolor('grey')
                counter = 0
                y_position = 250
                x_position = -250
                turtle.penup()
                turtle.goto(x_position, y_position)
                turtle.pendown()
                count_x_position = 1

                box.fillcolor('white')
                box.begin_fill()

                for j in range(2):
                    box.forward(700)
                    box.right(90)
                    box.forward(25)
                    box.right(90)
                box.end_fill()




            if (0 < count_x_position <= 5):
                calendar(pay_period, color, x_position, y_position, profit)
                x_position += (500/6)
                turtle.penup()
                turtle.goto(x_position, y_position)
                turtle.pendown()
                count_x_position += 1
            else:
                calendar(pay_period, color, x_position, y_position, profit)
                y_position -= (500/6)
                x_position = -250
                count_x_position = 1



        elif pay_period == 1:

            calendar(pay_period, color, x_position, y_position, profit)


            s.bgcolor('grey')
            counter = 0
            y_position = 250

            s.bgcolor('grey')
            counter = 0
            y_position = 250

        week += 1

        counter += 1

        if(week == weeks_needed and amount_saved <= cog):
            week = 0


    s.onclick(ending_screen)


# Calendar Function
# Parameters: pay_period- weekly, daily, or monthly, color- red or green, x, y- onclick events parameters, profit, the number that goes in the box
# Returns: None
# The calendar function creates a component of the calendar; whether that be a square for daily or a rectangle for monthly and weekly. It also takes a color which colors the box depending on whether the user spent more or less than they should have. It also writes the profit in the box.
def calendar(pay_period, color, x, y, profit):

    s.bgcolor('grey')
    turtle.hideturtle()

    # Weekly Grid
    if pay_period == 7:
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.penup()


        for j in range(2):
            turtle.forward(500)
            turtle.right(90)
            turtle.forward(500/8)
            turtle.right(90)

        turtle.end_fill()

        text.penup()
        text.goto(-250, 250)
        text.goto(0, y - (500/8))
        text.pendown()

        text.write('Profit: ' + f'{profit:.2f}', False, align = 'center', font = ('Copperplate', 20))

    # Daily Grid
    elif pay_period == 30:
        turtle.setheading(0)
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.penup()

        turtle.pendown()
        for i in range(4):
            turtle.forward(500/6)
            turtle.right(90)
        turtle.end_fill()

        text.penup()
        # text.goto(-250, 250)
        text.goto((x + (x + (500/6)))/2, (y + (y - (500/6)))/2)
        text.pendown()

        text.write('Profit: ' + f'{profit:.2f}', False, align = 'center', font = ('Copperplate', 7))

    # Monthly Grid
    elif pay_period == 1:
        turtle.fillcolor(color)
        turtle.penup()

        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(500)
            turtle.right(90)
        turtle.end_fill()

        text.penup()
        text.goto(-250, 250)
        text.goto(0, 0)
        text.pendown()

        text.write(f'{profit:.2f}', False, align = 'center', font = ('Copperplate', 30))





# Daily Calc Function
# Parameters: total_per_month: how much they make per month, cost_of_living: total cost of livign, cost_of_goal: what they want to make, pay_period: option of weekly, daily, or monthly
# Returns: None
# The mathematical components of our application. It also displays all of the information to the user regarding how much is recommended to spend every pay_period.
def dailyCalc(total_per_month, cost_of_living, cost_of_goal, pay_period):
    global weeks_needed
    weeks_needed = 1

    # Weekly calculations
    if pay_period == 7:

        if cost_of_living >= (total_per_month/2):

            text.penup()
            text.goto(0, 90)
            text.pendown()

            total_per_month = (total_per_month - cost_of_living)/4

            text.write(f'\nAfter the cost of living you have ${total_per_month:.2f} left per week', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            total_per_month = total_per_month / 2
            text.write(f'\nNow after using a 50/50 split you put ${total_per_month:.2f} into savings', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'and another ${total_per_month:.2f} to spend on wants per week', False, 'center', font = ('Copperplate', 15))


            list4.append(pay_period)
            list4.append(total_per_month)


            amount_saved = total_per_month

        else:

            text.penup()
            text.goto(0, 90)
            text.pendown()

            save_per_week = (total_per_month/2)/4.1
            text.write(f'\nYou should save ${save_per_week:.2f} weekly', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            total_per_month = ((total_per_month/2) - (cost_of_living))/4
            text.write(f'\nAfter paying your costs of living you will have ${total_per_month:.2f}', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'left for your wants per week', False, 'center', font = ('Copperplate', 15))

            list4.append(pay_period)
            list4.append(total_per_month)


            amount_saved = save_per_week

    # Daily Calculations
    elif pay_period == 30:

        if cost_of_living >= (total_per_month/2):

            text.penup()
            text.goto(0, 90)
            text.pendown()

            total_per_month = (total_per_month - cost_of_living) / 30
            text.write(f'\nAfter the cost of living you have ${total_per_month:.2f} left per day', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            total_per_month = total_per_month / 2
            text.write(f'\nNow after using a 50/50 split you put ${total_per_month:.2f} into savings', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'and another ${total_per_month:.2f} to spend on wants each day', False, 'center', font = ('Copperplate', 15))


            list4.append(pay_period)
            list4.append(total_per_month)

            amount_saved = total_per_month * 7

        else:

            text.penup()
            text.goto(0, 90)
            text.pendown()

            save_per_day = (total_per_month/2)/30
            text.write(f'\nYou should save ${save_per_day:.2f} daily', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            amount_saved = save_per_day * 7
            total_per_month = ((total_per_month/2) - (cost_of_living))/30
            text.write(f'\nAfter paying your costs of living you will have ${total_per_month:.2f}', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'left for your wants each day', False, 'center', font = ('Copperplate', 15))

            list4.append(pay_period)
            list4.append(total_per_month)

    # Montly Calculations
    elif pay_period == 1:

        if cost_of_living >= (total_per_month/2):

            text.penup()
            text.goto(0, 90)
            text.pendown()

            total_per_month = total_per_month - cost_of_living
            text.write(f'\nAfter the cost of living you have ${total_per_month:.2f} left per month', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            total_per_month = total_per_month / 2
            text.write(f'\nNow after using a 50/50 split you put ${total_per_month:.2f} into savings', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'and another ${total_per_month:.2f} to spend on wants each month', False, 'center', font = ('Copperplate', 15))

            list4.append(pay_period)
            list4.append(total_per_month)


            amount_saved = total_per_month / 4.1

        else:

            text.penup()
            text.goto(0, 90)
            text.pendown()

            save_per_month = (total_per_month/2)
            text.write(f'\nYou should save ${save_per_month:.2f} monthly', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -50)
            text.pendown()

            amount_saved = save_per_month / 4.1
            total_per_month = ((total_per_month/2) - (cost_of_living))
            text.write(f'\nAfter paying your costs of living you will have ${total_per_month:.2f}', False, 'center', font = ('Copperplate', 15))

            text.penup()
            text.goto(0, -73)
            text.pendown()

            text.write(f'left for your wants each month', False, 'center', font = ('Copperplate', 15))

            list4.append(pay_period)
            list4.append(total_per_month)


    weekly_save = amount_saved
    list4.append(cost_of_goal)


    while amount_saved < cost_of_goal:

        amount_saved += weekly_save
        weeks_needed += 1

    text.penup()
    text.goto(0, -175)
    text.pendown()

    text.write(f'\nIt will take {weeks_needed} weeks in order to reach your goal of {cost_of_goal:.2f}', False, 'center', font = ('Copperplate', 17))

    text.penup()
    text.goto(0, -197)
    text.pendown()

    text.write('if you follow this budgeting application.', False, 'center', font = ('Copperplate', 17))
    turtle.hideturtle()

    text.penup()
    text.goto(0, -280)
    text.pendown()
    text.write('Press Anywhere to Continue', False, 'center', font=('Copperplate', 19, 'normal'))
    list4.append(weekly_save)
    s.listen()
    s.onclick(calendarCall)




# Walkthrough Function
# Parameters: x, y- onscreen events parameters
# Returns: Nothing
# Shows the user how the calculation works by importing a file and displaying the various calculations.

def walkthrough(x, y):
    s.clearscreen()

    file = open("Sample.txt")
    contents = file.readlines()
    for i in range(len(contents) - 1):
        contents[i] = int(contents[i].strip())

    period_of_pay = contents[0]
    check = contents[1]
    living_expenses = contents[2]
    goal_cost = int(contents[3])


    text.penup()
    text.goto(0, 180)
    text.pendown()

    text.write(f'Let us explain how the calculations work: ', False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, 146)
    text.pendown()

    text.write(f"The file we're using for this example has 4 numbers", False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, 122)
    text.pendown()

    text.write(f"Payment Period: {period_of_pay}, Income: {check}, Cost of Living: {living_expenses}, Cost of Goal: {goal_cost}", False, 'center', font = ('Copperplate', 14))


    text.penup()
    text.goto(0, 90)
    text.pendown()

    text.write(f"First we divide your income by 2 in order to save half", False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, 67)
    text.pendown()

    text.write(f"So $90 in savings then the other $90 gets cut by living expenses", False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, 42)
    text.pendown()

    text.write(f"Subtracting the $60 expenses that leaves you with $30 for wants", False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, 5)
    text.pendown()

    text.write(f"Which ends up with:", False, 'center', font = ('Copperplate', 14))

    text.penup()
    text.goto(-250, -20)
    text.pendown()

    text.write(f"Savings: $90", False, 'left', font = ('Copperplate', 14))

    text.penup()
    text.goto(-250, -45)
    text.pendown()

    text.write(f"Expenses: $60", False, 'left', font = ('Copperplate', 14))

    text.penup()
    text.goto(-250, -70)
    text.pendown()

    text.write(f"Spending Money: $30", False, 'left', font = ('Copperplate', 14))

    text.penup()
    text.goto(0, -100)
    text.pendown()

    text.write(f"This increments weekly due to the pay period being weekly (7)", False, 'center', font = ('Copperplate', 14))



    text.penup()
    text.goto(0, -280)
    text.pendown()
    text.write('Press Anywhere to Continue', False, 'center', font=('Copperplate', 19, 'normal'))
    s.listen()
    s.onclick(inputs)


# Inputs Function
# Parameters: x, y- onscreen event paraeters
# Returns: None
# This is the function in the very beginning of the application that takes in all of the user inputs
def inputs(x, y):
    s.clearscreen()
    s.bgcolor('grey')
    pay_period = turtle.textinput('Pay Period', 'Would you like to provide your weekly, daily, or monthly income (Ex: "Daily")?:')

    income = float(turtle.textinput('Income', f'How much money do you make {pay_period} (Ex: 100)?'))

    cost_of_living = float(turtle.textinput('Expenses', f'\nWhat are your {pay_period} costs of living (Ex: "100")?'))

    cost_of_goal = float(turtle.textinput('Financial Goal', f'What is the financial goal you want to achieve (Dollar Amount)?'))





    if income <= cost_of_living:
        print('\nYour goal is not feesible.')
        while feesible == True:
            feesible = True
    if pay_period.upper() == "WEEKLY":
        total_per_month = income * 4.2
        pay_period = 7
        cost_of_living *= 4.1
        dailyCalc(total_per_month, cost_of_living, cost_of_goal, pay_period)
    elif pay_period.upper() == "DAILY":
        total_per_month = income * 30
        pay_period = 30
        cost_of_living *= 30
        dailyCalc(total_per_month, cost_of_living, cost_of_goal, pay_period)
    elif pay_period.upper() == "MONTHLY":
        total_per_month = income * 1
        pay_period = 1
        dailyCalc(total_per_month, cost_of_living, cost_of_goal, pay_period)










s.listen()
s.onclick(walkthrough)

























turtle.mainloop()


