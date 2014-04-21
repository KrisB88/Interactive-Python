# template for "Stopwatch: The Game"
import simplegui

# define global variables
count = 0
wins = 0
stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenths
    tenths = t % 10
    ones = t % 100 / 10
    tens = (t % 600) / 100
    minutes = t / 600
    timeString = str(minutes) + ":" + str(tens) + str(ones) + "." + str(tenths)
    return timeString
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_timer():
    
    timer.start()
    
def stop_timer():
    
    global wins, stops, timer_state, tenths
    timer_state = timer.is_running()
    win_test = tenths
    if timer_state == True:
        if win_test == 0:
            wins += 1
            stops += 1
            
        else:
            stops += 1
    timer.stop()          
    
def reset_timer():
    
    global count, wins, stops
    timer.stop()
    count = 0
    wins = 0
    stops = 0
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    
    global count
    count += 1
    return count

# define draw handler
def draw_time(canvas):
    
    score = "%i / %i"  %(wins, stops)
    canvas.draw_text(format(count), [75, 100], 24, "white")
    canvas.draw_text(score, [145, 20], 20, "white")
    
# create frame
frame = simplegui.create_frame("Stop Watch Game!", 200, 200)
frame.set_draw_handler(draw_time)
frame.add_button("Start Timer", start_timer, 100)
frame.add_button("Stop Timer", stop_timer, 100)
frame.add_button("Reset Timer", reset_timer, 100)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()


