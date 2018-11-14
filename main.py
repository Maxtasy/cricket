# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 18:41:08 2018

@author: Maxtasy
"""

import json
import io

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
#from ttkthemes import themed_tk as tk

# Rules
def rules():
	rules_text = """Number of Players: Two individual players or two teams.

Numbers in Play: 20,19,18,17,16,15, and bull's-eye.

The objective shall be to 'own'/'close' certain numbers on the dartboard, and to achieve the highest point score. The player/team to do so first, shall be the winner.

Each player/team shall take turns throwing. (Three darts in succession shall constitute a 'turn'/'Inning'.)

To close an inning, the player/team must score three of a number. This can be accomplished with three singles, a single and a double, or a triple.

Once a player/team scores three of a number, it is 'owned' by that player/team. Once both players/teams have scored three of a number, it is 'closed', and no further scoring can be accomplished on that number by either player/team.

To close the bullseye, the outer bull counts as a single, and the inner bull counts as a double.

Once a player/team closes an inning, he/they may score points on that number until the opponent also closes that inning. All numerical scores shall be added to the previous balance.

Numbers can be 'owned' or 'closed' in any order desired by the individual player/team. Calling your shot is not required.

For the purpose of 'owning' a number, the double and triple ring shall count as 2 or 3, respectively. Three marks will close an inning.

After a number is 'owned' by a team, the double and triple ring shall count as 2 or 3 times the numerical values, respectively. Winning the game:

a. The player/team that closes all innings first and has the most points, shall be declared the winner.

b. If both sides are tied on points, or have no points, the first player/team to close all innings shall be the winner.

c. If a player/team closes all innings first, and is behind in points, he/they must continue to score on any innings not closed until either the point deficit is made up, or the opponent has closed all innings."""
	
	messagebox.showinfo("Cricket Rules", rules_text)


# Show stats window
def show_stats():
	global data
	global names
	#global stats_images

	# Show popup window
	stats_window = Toplevel()
	stats_window.iconbitmap("img/stats.ico")
	stats_window.title("Player Statistics")

	# Names
	p0_name = Label(stats_window, text=names["0"], font=("Helvetica", 15, "bold"))
	p0_name.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="NESW")
	p1_name = Label(stats_window, text=names["1"], font=("Helvetica", 15, "bold"))
	p1_name.grid(row=0, column=3, columnspan=2, pady=10, padx=10,  sticky="NESW")

	# Matches played
	matches_label = Label(stats_window, text="Matches Played", font=("Helvetica", 13, "bold"))
	matches_label.grid(row=1, column=2, pady=3, padx=10)
	p0_matches = Label(stats_window, text=data["player_profiles"][names["0"]]["matches"], font=("Helvetica", 13))
	p0_matches.grid(row=1, column=1, pady=3, padx=10, sticky="E")
	p1_matches = Label(stats_window, text=data["player_profiles"][names["1"]]["matches"], font=("Helvetica", 13))
	p1_matches.grid(row=1, column=3, pady=3, padx=10, sticky="W")

	# Matches won
	wins_label = Label(stats_window, text="Matches Won", font=("Helvetica", 13, "bold"))
	wins_label.grid(row=2, column=2, pady=3, padx=10)
	p0_wins = Label(stats_window, text=data["player_profiles"][names["0"]]["wins"], font=("Helvetica", 13))
	p0_wins.grid(row=2, column=1, pady=3, padx=10, sticky="E")
	p1_wins = Label(stats_window, text=data["player_profiles"][names["1"]]["wins"], font=("Helvetica", 13))
	p1_wins.grid(row=2, column=3, pady=3, padx=10, sticky="W")

	# Win percentage
	win_p_label = Label(stats_window, text="Win Percentage", font=("Helvetica", 13, "bold"))
	win_p_label.grid(row=3, column=2, pady=3, padx=10)

	if data["player_profiles"][names["0"]]["matches"] == 0:
		p0_win_p_value = "N/A"
	else:
		p0_win_p_value = "{0:.2f}%".format(data["player_profiles"][names["0"]]["wins"] / data["player_profiles"][names["0"]]["matches"] * 100)
	p0_win_p = Label(stats_window, text=p0_win_p_value, font=("Helvetica", 13))
	p0_win_p.grid(row=3, column=1, pady=3, padx=10, sticky="E")

	if data["player_profiles"][names["1"]]["matches"] == 0:
		p1_win_p_value = "N/A"
	else:
		p1_win_p_value = "{0:.2f}%".format(data["player_profiles"][names["1"]]["wins"] / data["player_profiles"][names["1"]]["matches"] * 100)
	p1_win_p = Label(stats_window, text=p1_win_p_value, font=("Helvetica", 13))
	p1_win_p.grid(row=3, column=3, pady=3, padx=10, sticky="W")

	# Average End Score
	avg_label = Label(stats_window, text="Average End Score", font=("Helvetica", 13, "bold"))
	avg_label.grid(row=4, column=2, pady=3, padx=10)
	
	if data["player_profiles"][names["0"]]["matches"] == 0:
		p0_avg_value = "N/A"
	else:
		p0_avg_value = "{0:.2f}".format(sum(data["player_profiles"][names["0"]]["scores"]) / data["player_profiles"][names["0"]]["matches"])
	p0_avg = Label(stats_window, text=p0_avg_value, font=("Helvetica", 13))
	p0_avg.grid(row=4, column=1, pady=3, padx=10, sticky="E")

	if data["player_profiles"][names["1"]]["matches"] == 0:
		p1_avg_value = "N/A"
	else:
		p1_avg_value = "{0:.2f}".format(sum(data["player_profiles"][names["1"]]["scores"]) / data["player_profiles"][names["1"]]["matches"])
	p1_avg = Label(stats_window, text=p1_avg_value, font=("Helvetica", 13))
	p1_avg.grid(row=4, column=3, pady=3, padx=10, sticky="W")

	# Separator
	sep = ttk.Separator(stats_window)
	sep.grid(row=5, column=0, columnspan=5, sticky="NESW")

	# Heading for target closed stats
	board_closed_part_label = Label(stats_window, text="Target Closed Statistics", font=("Helvetica", 11, "italic"))
	board_closed_part_label.grid(row=6, column=0, pady=0, padx=10, columnspan=5)

	# Board stats images
	stats_images = {}

	# Default image if no stats
	stats_images["default"] = PhotoImage(file="img/stats/default.png")

	groups = ["board", "20", "19", "18", "17", "16", "15", "bulls"] # Also being used later for stats below
	colors = ["green", "yellow", "light_orange", "dark_orange", "red"]

	for group in groups:
		stats_images[group] = {}

		for color in colors:
			stats_images[group][color] = PhotoImage(file="img/stats/stats_" + str(group) + "_" + str(color) +".png")

	# Closed Stats
	stats_closed_img = {}
	stats_closed_label = {}
	stats_closed = {}

	stats_closed_img["0"] = {}
	stats_closed_img["1"] = {}
	stats_closed["0"] = {}
	stats_closed["1"] = {}
	
	k = 7

	for group in groups:
		stats_closed_label[group] = Label(stats_window, text=group.title(), font=("Helvetica", 18, "bold"))
		stats_closed_label[group].grid(row=k, column=2, pady=3, padx=10)

		if data["player_profiles"][names["0"]]["matches"] == 0:
			stats_closed_img["0"][group] = Label(stats_window, image=stats_images["default"])

			# Important: Need to keep a reference, else img will not show
			stats_closed_img["0"][group].image = stats_images["default"]

			stats_closed["0"][group] = Label(stats_window, text="N/A", font=("Helvetica", 18))
		else:
			# Calculate closed percentage value
			value = data["player_profiles"][names["0"]]["closed_" + group] / data["player_profiles"][names["0"]]["matches"] * 100

			# Set image
			if value < 15:
				col = "red"
			elif value < 25:
				col = "dark_orange"
			elif value < 50:
				col = "light_orange"
			elif value < 75:
				col = "yellow"
			else:
				col = "green"
			
			stats_closed_img["0"][group] = Label(stats_window, image=stats_images[group][col])

			# Important: Need to keep a reference, else img will not show
			stats_closed_img["0"][group].image = stats_images[group][col]

			stats_closed["0"][group] = Label(stats_window, text="{0:.2f}%".format(value), font=("Helvetica", 18))

		stats_closed["0"][group].grid(row=k, column=1, pady=3, padx=10, sticky="E")
		stats_closed_img["0"][group].grid(row=k, column=0, pady=3, padx=10, sticky="E")

		if data["player_profiles"][names["1"]]["matches"] == 0:
			stats_closed_img["1"][group] = Label(stats_window, image=stats_images["default"])

			# Important: Need to keep a reference, else img will not show
			stats_closed_img["0"][group].image = stats_images["default"]

			stats_closed["1"][group] = Label(stats_window, text="N/A", font=("Helvetica", 18))
		else:
			# Calculate closed percentage value
			value = data["player_profiles"][names["1"]]["closed_" + group] / data["player_profiles"][names["1"]]["matches"] * 100

			# Set image
			if value < 15:
				col = "red"
			elif value < 25:
				col = "dark_orange"
			elif value < 50:
				col = "light_orange"
			elif value < 75:
				col = "yellow"
			else:
				col = "green"

			stats_closed_img["1"][group] = Label(stats_window, image=stats_images[group][col])

			# Important: Need to keep a reference, else img will not show
			stats_closed_img["1"][group].image = stats_images[group][col]

			stats_closed["1"][group] = Label(stats_window, text="{0:.2f}%".format(value), font=("Helvetica", 18))

		stats_closed["1"][group].grid(row=k, column=3, pady=3, padx=10, sticky="W")
		stats_closed_img["1"][group].grid(row=k, column=4, pady=3, padx=10, sticky="W")

		k += 1


	# Close button
	close_button = ttk.Button(stats_window, text="Close", command=stats_window.destroy)
	close_button.grid(row=k, column=2, pady=5, padx=5)


# Close app, called on X click or Exit in menu
def on_close():
	# First save data
	save_data()
	# Then destroy window
	root.destroy()


# Toggle active player between 1 and 2 (for selecting starting player)
def toggle_active():
	global active

	if active == "1":
		active = "0"
	else:
		active = "1"

	set_turn_marker(active)
	turn_score_entry_widgets[active].focus()


# Set starting player = player who started less often
def set_starter_fair():
	global data
	
	if data["player_profiles"][names["0"]]["started"] < data["player_profiles"][names["1"]]["started"]:
		return "0"
	else:
		return "1"


# Handle turn indicator, turn number highlighting and player name highlighting (player is string, turn is int)
def set_turn_marker(player):
	global turns
	global name_labels
	global turn_labels
	global turn_indicator
	global turn_limit

	# Point turn indicator to active player
	turn_indicator.configure(image=indicator_images[player])

	# Set active player name blue
	name_labels[str(int(player))].configure(foreground="#006df0")
	name_labels[str((int(player) + 1) % 2)].configure(foreground="#333333")

	if turn_limit:
		# Cross out all turn labels that are over
		cur_0 = turns["0"]
		cur_1 = turns["1"]

		for i in range(1, cur_0):
			turn_labels["0"][str(i)].configure(foreground="#5b5b5b", font=("Helvetica", 11, "overstrike bold"))
		for i in range(1, cur_1):
			turn_labels["1"][str(i)].configure(foreground="#5b5b5b", font=("Helvetica", 11, "overstrike bold"))

		# Set active player's turn label to highlight color
		turn_labels[player][str(turns[player])].configure(foreground="#006df0", font=("Helvetica", 11, "bold"))

		# Set inactive player's turn label to default color
		if turns[str((int(player) + 1) % 2)] < 26:
			turn_labels[str((int(player) + 1) % 2)][str(turns[str((int(player) + 1) % 2)])].configure(foreground="#333333", font=("Helvetica", 11, "bold"))


# Add turn score of player 0 to their score
def p0_on_add_to_score(event=None):
	global scores
	global turns

	try:
		turn_score = int(turn_score_entry_widgets["0"].get())
	except:
		turn_score = 0

	# Add turn score to score
	scores["0"] += turn_score

	# Update score label
	score_labels["0"].configure(text=scores["0"])

	# Clear entry widget
	turn_score_entry_widgets["0"].delete(0, END)

	# Set focus to entry widget of other player
	turn_score_entry_widgets["1"].focus()

	# Increase players turn
	turns["0"] += 1

	# Check for win condition
	is_over, winner = is_match_over()
	
	if is_over:	
		end_game(winner)
	else:
		set_turn_marker("1")


# Add turn score of player 1 to their score
def p1_on_add_to_score(event=None):
	global scores
	global turns

	try:
		turn_score = int(turn_score_entry_widgets["1"].get())
	except:
		turn_score = 0

	# Add turn score to score
	scores["1"] += turn_score

	# Update score label
	score_labels["1"].configure(text=scores["1"])

	# Clear entry widget
	turn_score_entry_widgets["1"].delete(0, END)

	# Set focus to entry widget of other player
	turn_score_entry_widgets["0"].focus()

	# Increase players turn
	turns["1"] += 1

	# Check for win condition
	is_over, winner = is_match_over()
	
	if is_over:	
		end_game(winner)
	else:
		set_turn_marker("0")


# Check function, called each time after a button was pressed (takes 3 strings)
def check(player, group, num):
	global targets
	global target_labels
	global hitbuttons_frames
	global closed

	# Toggle button status and image
	old_flag = targets[player][group][int(num)]
	new_flag = (old_flag + 1) % 2 
	targets[player][group][int(num)] = new_flag
	buttons[player][group][num].configure(image=button_images[str(new_flag)])

	# Check if target group is closed
	if targets[player][group][int(num)] and targets[player][group][(int(num) + 1) % 3] and targets[player][group][(int(num) + 2) % 3]:
		
		# Style hit buttons of group
		for button in buttons[player][group].keys():
			buttons[player][group][button].configure(background="#3bbf4a")
		
		# Style target group frame
		hitbuttons_frames[player][group].configure(background="#3bbf4a")

		# Style target group label
		target_labels[player][group].configure(foreground="#5b5b5b", font=("Helvetica", 50, "overstrike"))
		
		# Add group to closed dictionary
		closed[player][group] = 1
	else:

		# Style hit buttons of group
		for button in buttons[player][group].keys():
			buttons[player][group][button].configure(background="#d80027")
		
		# Style target group frame
		hitbuttons_frames[player][group].configure(background="#d80027")

		# Style target group label
		target_labels[player][group].configure(foreground="#333333", font=("Helvetica", 50))
		
		# Add group to closed dictionary
		closed[player][group] = 0

	# Check if all regular target groups are closed, set "board" to 1
	board_closed = False
	for group in closed[player].keys():
		if group == "board":
			pass
		elif closed[player][group] == 0:
			board_closed = False
			break
		else:
			board_closed = True

	if board_closed:
		closed[player]["board"] = 1
	else:
		closed[player]["board"] = 0


# Checks for win conditions, returns 1 if met, else 0
def is_match_over():
	global turns
	global turn_limit
	global closed

	# Both players reached turn limit and turn limit is set
	if turn_limit and turns["0"] > turn_limit and turns["1"] > turn_limit:
		# Player 0 has higher score
		if scores["0"] >= scores["1"]:
			return True, "0"
		# Player 1 has higher score
		else:
			return True, "1"

	# Player 0 closed board and has higher score
	if closed["0"]["board"] == 1 and scores["0"] >= scores["1"]:
		return True, "0"
	# Player 1 closed board and has higher score
	elif closed["1"]["board"] == 1 and scores["1"] >= scores["0"]:
		return True, "1"
	# Game is not finished
	else:
		return False, None


# Show win message, update variables in player_profiles and save data
def end_game(winner):
	global names
	global closed
	global scores
	global data
	global starter

	# Update stats for both players
	for i in ["0", "1"]:
		data["player_profiles"][names[i]]["closed_15"] += closed[i]["15"]
		data["player_profiles"][names[i]]["closed_16"] += closed[i]["16"]
		data["player_profiles"][names[i]]["closed_17"] += closed[i]["17"]
		data["player_profiles"][names[i]]["closed_18"] += closed[i]["18"]
		data["player_profiles"][names[i]]["closed_19"] += closed[i]["19"]
		data["player_profiles"][names[i]]["closed_20"] += closed[i]["20"]
		data["player_profiles"][names[i]]["closed_bulls"] += closed[i]["bulls"]
		data["player_profiles"][names[i]]["closed_board"] += closed[i]["board"]
		data["player_profiles"][names[i]]["matches"] += 1
		data["player_profiles"][names[i]]["scores"].append(scores[i])

	# Update only for winner
	data["player_profiles"][names[winner]]["wins"] += 1

	# Update only for starting player
	data["player_profiles"][names[starter]]["started"] += 1

	save_data()

	# Win Message
	winner_text = names[winner] + " won the game!\nDo you want to start a new game?"
	game_over_popup = messagebox.askquestion("Game Finished!", winner_text)
	if game_over_popup == "yes":
		new_match()


# Saves app config and player_profiles to data.json
def save_data():
	global data

	data_out = data

	# Write JSON file
	with io.open('data.json', 'w', encoding='utf8') as outfile:
	    str_ = json.dumps(data_out,
	                      indent=4, sort_keys=True,
	                      separators=(',', ': '), ensure_ascii=False)
	    outfile.write(to_unicode(str_))


# Start a new match, either by clicking okay on winner dialogue or via menu
def new_match():
	global active
	global starter
	global scores
	global targets
	global closed
	global turns
	global target_labels
	global turn_labels
	global hitbuttons_frames
	global buttons
	global score_labels
	global name_labels

	# Set scores 0
	scores["0"] = 0
	scores["1"] = 0

	# Set targets 0
	for i in ["0", "1"]:
		for group in targets[i].keys():
			targets[i][group] = [0, 0, 0]

	# Set closed 0
	for i in ["0", "1"]:
		for group in closed[i].keys():
			closed[i][group] = 0

	# Set turns 1
	turns["0"] = 1
	turns["1"] = 1

	# Reset turn labels
	for i in ["0", "1"]:
		for group in turn_labels[i].keys():
			turn_labels[i][group].configure(foreground="#333333", font=("Helvetica", 11, "bold"))

	# Reset target labels
	for i in ["0", "1"]:
		for group in target_labels[i].keys():
			target_labels[i][group].configure(foreground="#333333", font=("Helvetica", 50))

	# Reset hit buttons group frames
	for i in ["0", "1"]:
		for group in hitbuttons_frames[i].keys():
			hitbuttons_frames[i][group].configure(background="#d80027")

	# Reset hit buttons
	for i in ["0", "1"]:
		for group in buttons[i].keys():
			for num in buttons[i][group].keys():
				buttons[i][group][num].configure(image=button_images["0"], background="#d80027")

	# Reset score entry widgets
	score_labels["0"].configure(text=scores["0"])
	score_labels["1"].configure(text=scores["1"])

	# Update name labels (for score)
	name_labels["0"].configure(text="(" + str(data["player_profiles"][names["0"]]["wins"]) + ") " + names["0"])
	name_labels["1"].configure(text=names["1"] + " (" + str(data["player_profiles"][names["1"]]["wins"]) + ")")

	# Set starter/active with fair method
	starter = set_starter_fair()
	active = starter

	# Refresh turn labels
	refresh_turn_labels()

	# Set turn marker
	set_turn_marker(active)
	
	# Set focus to active
	turn_score_entry_widgets[active].focus()


# When user clicks on change player 1 / 2
def on_change_player(player_num):
	global names
	global data


	# Load player profile 
	def load_player(p_num, name):

		# Set selected player in app settings
		data["app_settings"]["players"][p_num] = name

		names[p_num] = name

		name_labels[p_num].configure(text=name)
		new_match()
		change_player_popup.destroy()


	# Create list of all existing profiles
	profiles = []
    
	for profile in data["player_profiles"].keys():
		if profile != "Player 1" and profile != "Player 2":
			profiles.append(profile)

	# Popup window
	change_player_popup = Toplevel()
	change_player_popup.title("Change Player " + str(int(player_num) + 1))

	# Widgets for loading profile
	load_profile_label = ttk.Label(change_player_popup, text="Load Profile: ")
	load_profile_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

	# Set default value to currently active profile
	profile_name = StringVar(change_player_popup)
	profile_name.set(names[player_num])

	profiles_option_menu = OptionMenu(change_player_popup, profile_name, *profiles)
	profiles_option_menu.grid(row=0, column=1, padx=5, pady=5)

	load_button = Button(change_player_popup, text="Load", command=lambda: load_player(player_num, profile_name.get()))
	load_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)


# Create new player profile
def on_create_profile():
	# Create new player profile 
	def on_create_button_pressed(event=None):
		global data

		new_name = create_profile_entry.get()

		# If name already exists who error message
		if new_name in data["player_profiles"].keys():
			error_text = "A profile with this name already exists.\n\n" + new_name + "\n\nPlease choose another name."
			error_message = messagebox.showerror("Name taken", error_text, type="ok", default="ok")
		else:
			# Add name to profiles
			data["player_profiles"][new_name] = {}

			# Set default values for all variables of new profile
			reset_profile(new_name)

			create_player_popup.destroy()

	# Popup window
	create_player_popup = Toplevel()
	create_player_popup.title("Create Profile")

	# Widgets for creating new profile
	create_profile_label = ttk.Label(create_player_popup, text="Profile Name: ")
	create_profile_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

	create_profile_entry = ttk.Entry(create_player_popup)
	create_profile_entry.bind("<Return>", on_create_button_pressed)
	create_profile_entry.grid(row=0, column=1, padx=5, pady=5)

	create_button = ttk.Button(create_player_popup, text="Create", command=on_create_button_pressed)
	create_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

	create_profile_entry.focus()


# Popup window with list of profiles and reset button
def on_reset_profile():
	# Pop up confirm massage when reset was clicked
	def on_reset_button_clicked():
		name_to_reset = profile_name.get()
		reset_profile_popup.destroy()
		confirmation_text = "Are you sure you want to reset this player profile?\n\n" + name_to_reset + "\n\nAll stats will be reset and can not be restored."
		confirm_message = messagebox.showwarning("Reset player " + name_to_reset, confirmation_text, type="okcancel", default="cancel")
		if confirm_message:
			reset_profile(name_to_reset)
		

	# Create list of all existing profiles
	profiles = []
    
	for profile in data["player_profiles"].keys():
		if profile != "Player 1" and profile != "Player 2":
			profiles.append(profile)

	# Popup window
	reset_profile_popup = Toplevel()
	reset_profile_popup.title("Reset Profile")

	# Widgets for loading profile
	reset_profile_label = ttk.Label(reset_profile_popup, text="Reset profile: ")
	reset_profile_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

	# Set default value to "None"
	profile_name = StringVar(reset_profile_popup)
	profile_name.set("None")

	profiles_option_menu = ttk.OptionMenu(reset_profile_popup, profile_name, *profiles)
	profiles_option_menu.grid(row=0, column=1, padx=5, pady=5)

	reset_button = ttk.Button(reset_profile_popup, text="Reset", command=on_reset_button_clicked)
	reset_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)


# Used in reset profile dialog and when creating new profiles
def reset_profile(name):
	global data

	# Set default values for all variables of new profile
	data["player_profiles"][name]["closed_15"] = 0
	data["player_profiles"][name]["closed_16"] = 0
	data["player_profiles"][name]["closed_17"] = 0
	data["player_profiles"][name]["closed_18"] = 0
	data["player_profiles"][name]["closed_19"] = 0
	data["player_profiles"][name]["closed_20"] = 0
	data["player_profiles"][name]["closed_bulls"] = 0
	data["player_profiles"][name]["closed_board"] = 0
	data["player_profiles"][name]["matches"] = 0
	data["player_profiles"][name]["scores"] = []
	data["player_profiles"][name]["started"] = 0
	data["player_profiles"][name]["wins"] = 0


# Popup window with list of profiles and delete button
def on_delete_profile():
	#Pop up confirm massage when delete was clicked
	def on_delete_button_clicked():
		name_to_delete = profile_name.get()
		delete_profile_popup.destroy()
		confirmation_text = "Are you sure you want to delete this player profile?\n\n" + name_to_delete + "\n\nDeleted profiles can not be restored."
		confirm_message = messagebox.showwarning("Delete player " + name_to_delete, confirmation_text, type="okcancel", default="cancel")
		if confirm_message:
			delete_profile(name_to_delete)


	# Deletes profile from data
	def delete_profile(name):
		global data
		
		del data["player_profiles"][name]

		if data["app_settings"]["players"]["0"] == name:
			data["app_settings"]["players"]["0"] = "Player 1"

		if data["app_settings"]["players"]["1"] == name:
			data["app_settings"]["players"]["1"] = "Player 2"
		

	# Create list of all existing profiles
	profiles = []
    
	for profile in data["player_profiles"].keys():
		if profile != "Player 1" and profile != "Player 2":
			profiles.append(profile)

	# Popup window
	delete_profile_popup = Toplevel()
	delete_profile_popup.title("Delete Profile")

	# Widgets for loading profile
	delete_profile_label = ttk.Label(delete_profile_popup, text="Reset profile: ")
	delete_profile_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

	# Set default value to "None"
	profile_name = StringVar(delete_profile_popup)
	profile_name.set("None")

	profiles_option_menu = ttk.OptionMenu(delete_profile_popup, profile_name, *profiles)
	profiles_option_menu.grid(row=0, column=1, padx=5, pady=5)

	delete_button = ttk.Button(delete_profile_popup, text="Delete", command=on_delete_button_clicked)
	delete_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)



# Set turn limit to None or any option
def on_set_turn_limit():
	global turn_limit
	global turn_labels

	def on_confirm_button_clicked():
		global turn_limit

		if selected_option.get() == "None":
			turn_limit = None
		else:
			turn_limit = int(selected_option.get())

		set_turn_limit_popup.destroy()
		data["app_settings"]["turn_limit"] = turn_limit
		refresh_turn_labels()

	# List of options
	options = ["None", 5, 10, 15, 20, 25]

	# Popup window
	set_turn_limit_popup = Toplevel()
	set_turn_limit_popup.title("Set Turn Limit")

	# Widgets with options select
	set_turn_limit_label = ttk.Label(set_turn_limit_popup, text="Set Turn Limit: ")
	set_turn_limit_label.grid(row=0, column=0, sticky="W", padx=5, pady=5)

	# Set default value to "None"
	selected_option = StringVar(set_turn_limit_popup)
	selected_option.set(turn_limit)

	turn_limit_option_menu = ttk.OptionMenu(set_turn_limit_popup, selected_option, *options)
	turn_limit_option_menu.grid(row=0, column=1, padx=5, pady=5)

	confirm_button = ttk.Button(set_turn_limit_popup, text="Confirm", command=on_confirm_button_clicked)
	confirm_button.grid(row=1, column=0, padx=5, pady=5, columnspan=2)


def refresh_turn_labels():
	global turn_labels
	global turn_limit

	# If turn limit is integer
	if turn_limit:
		# Refresh turn labels in UI
		for i in ["0", "1"]:
			for j in range(turn_limit + 1, 26):
				turn_labels[i][str(j)].configure(foreground="#add5d5")
			for k in range(1, turn_limit + 1):
				turn_labels[i][str(k)].configure(foreground="#333333")
	# If turn limit is None
	else:
		for i in ["0", "1"]:
			for j in range(1, 26):
				turn_labels[i][str(j)].configure(foreground="#add5d5")

	set_turn_marker(active)


def on_new_match():
	confirm_message = messagebox.showwarning("New Match?", "Are you sure you want to start a new match?\nCurrent match progress will be lost.", type="okcancel", default="cancel")
	if confirm_message == "yes":
		new_match()


"""
INITIALIZE APP SETTINGS
"""


# Load data from data.json file
try:
    to_unicode = unicode
except NameError:
    to_unicode = str

with open("data.json") as data_file:
	data = json.load(data_file)


# Set up player names
names = {}

try:
	names["0"] = data["app_settings"]["players"]["0"]
except:
	names["0"] = "Player 1"

try:
	names["1"] = data["app_settings"]["players"]["1"]
except:
	names["1"] = "Player 2"


# Set up turn limit
try:
	turn_limit = data["app_settings"]["turn_limit"]
except:
	turn_limit = 25


"""
GLOBAL VARIABLES
"""


# Keeps track of scores of both players
scores = {}


# Current turn of both players
turns = {}

# Current active player
starter = None
active = None

# Closed target groups of both players (Also includes "board")
closed = {}

for i in ["0", "1"]:
	closed[i] = {}
	
	closed[i]["bulls"] = 0
	closed[i]["board"] = 0
	
	for j in range(20, 14, -1):
		closed[i][str(j)] = 0


# All target statuses (0 - not hit, 1 - hit)
targets = {}

for i in ["0", "1"]:
	targets[i] = {}

	targets[i]["bulls"] = [0, 0, 0]
	
	for j in range(20, 14, -1):
		targets[i][str(j)] = [0, 0, 0]


"""
CREATE APP, CREATE ROOT WINDOW, BASIC SETTINGS
"""


root = Tk()
root.geometry("1280x720")
root.configure(background="#add5d5")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.title("Cricket")
root.iconbitmap("img/logo.ico")


# When user clicks X, run on_close function
root.protocol("WM_DELETE_WINDOW", on_close)


# Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)


# Sub menu "File"
sub_menu_file = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="File", menu=sub_menu_file)

sub_menu_file.add_command(label="New Match", command=on_new_match)
sub_menu_file.add_separator()
sub_menu_file.add_command(label="Exit", command=on_close)


# Sub menu "Options"
sub_menu_options = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label="Options", menu=sub_menu_options)

sub_menu_options.add_command(label="Toggle Active Player", command=toggle_active)
sub_menu_options.add_separator()
sub_menu_options.add_command(label="Show Stats", command=show_stats)
sub_menu_options.add_separator()
sub_menu_options.add_command(label="Change Player 1", command=lambda: on_change_player("0"))
sub_menu_options.add_command(label="Change Player 2", command=lambda: on_change_player("1"))
sub_menu_options.add_separator()
sub_menu_options.add_command(label="Set Turn Limit", command=on_set_turn_limit)
sub_menu_options.add_separator()
sub_menu_options.add_command(label="Create New Profile", command=on_create_profile)
sub_menu_options.add_separator()
sub_menu_options.add_command(label="Reset Profile", command=on_reset_profile)
sub_menu_options.add_command(label="Delete Profile", command=on_delete_profile)

# Sub menu "Help"
sub_menu_help = Menu(menu_bar, tearoff = 0)

menu_bar.add_cascade(label="Help", menu=sub_menu_help)

sub_menu_help.add_command(label="Cricket Rules", command=rules)


"""
ADDING WIDGETS
"""


# Main frame surrounding player frames and turn frame
main_frame = Frame(root, background="#add5d5")
main_frame.grid(row=0, column=0)


# Player frames surrounding player name, player name, target labels and hitbuttons
player_frames = {}

player_frames["0"] = Frame(main_frame, background="#add5d5")
player_frames["0"].grid(row=0, column=0, padx=10, pady=(0, 20))

player_frames["1"] = Frame(main_frame, background="#add5d5")
player_frames["1"].grid(row=0, column=2, padx=10, pady=(0, 20))


# Player name labels at the top
name_labels = {}

name_labels["0"] = ttk.Label(player_frames["0"], text="(" + str(data["player_profiles"][names["0"]]["wins"]) + ") " + names["0"], font=("Helvetica", 40), foreground="#333333", background="#add5d5")
name_labels["0"].grid(row=0, column=1, pady=10)

name_labels["1"] = ttk.Label(player_frames["1"], text=names["1"] + " (" + str(data["player_profiles"][names["1"]]["wins"]) + ")", font=("Helvetica", 40), foreground="#333333", background="#add5d5")
name_labels["1"].grid(row=0, column=0, pady=10)


# Frames surrounding player score and turn score entry
score_frames = {}

score_frames["0"] = Frame(player_frames["0"], background="#add5d5")
score_frames["0"].grid(row=0, column=0)

score_frames["1"] = Frame(player_frames["1"], background="#add5d5")
score_frames["1"].grid(row=0, column=1)


# Player score label frames
score_label_frames = {}

score_label_frames["0"] = LabelFrame(score_frames["0"], text="Score", labelanchor="n", relief=RIDGE, fg="#333333", bg="#add5d5", font=("Helvetica", 11))
score_label_frames["0"].grid(row=0, column=1)

score_label_frames["1"] = LabelFrame(score_frames["1"], text="Score", labelanchor="n", relief=RIDGE, fg="#333333", bg="#add5d5", font=("Helvetica", 11))
score_label_frames["1"].grid(row=0, column=0)


# Player score labels
score_labels = {}

score_labels["0"] = Label(score_label_frames["0"], width=4, text="0", font=("Helvetica", 50, "bold"), foreground="#333333", background="#add5d5")
score_labels["0"].grid(row=0, column=0)

score_labels["1"] = Label(score_label_frames["1"], width=4, text="0", font=("Helvetica", 50, "bold"), foreground="#333333", background="#add5d5")
score_labels["1"].grid(row=0, column=1)


# ttk.Label frame for turn scores
turn_score_label_frames = {}

turn_score_label_frames["0"] = LabelFrame(score_frames["0"], text="Turn", labelanchor="n", relief=RIDGE, fg="#333333", bg="#add5d5", font=("Helvetica", 11))
turn_score_label_frames["0"].grid(row=0, column=0)

turn_score_label_frames["1"] = LabelFrame(score_frames["1"], text="Turn", labelanchor="n", relief=RIDGE, fg="#333333", bg="#add5d5", font=("Helvetica", 11))
turn_score_label_frames["1"].grid(row=0, column=1)


# Turn score entry widgets
turn_score_entry_widgets = {}

turn_score_entry_widgets["0"] = ttk.Entry(turn_score_label_frames["0"], width=3, justify=RIGHT, font=("Helvetica", 45, "bold"))
turn_score_entry_widgets["0"].bind('<Return>', p0_on_add_to_score)
turn_score_entry_widgets["0"].grid(row=0, column=0, padx=5, pady=4)

turn_score_entry_widgets["1"] = ttk.Entry(turn_score_label_frames["1"], width=3, justify=LEFT, font=("Helvetica", 45, "bold"))
turn_score_entry_widgets["1"].bind('<Return>', p1_on_add_to_score)
turn_score_entry_widgets["1"].grid(row=0, column=0, padx=5, pady=4)


# Frame surrounding target labels and hit buttons
target_chart_frames = {}

target_chart_frames["0"] = Frame(player_frames["0"])
target_chart_frames["0"].grid(row = 1, column = 1)

target_chart_frames["1"] = Frame(player_frames["1"])
target_chart_frames["1"].grid(row = 1, column = 0)


# Frames around target labels
target_label_frames = {}

target_label_frames["0"] = Frame(player_frames["0"], background="#add5d5")
target_label_frames["0"].grid(row=1, column=0, sticky="E")

target_label_frames["1"] = Frame(player_frames["1"], background="#add5d5")
target_label_frames["1"].grid(row=1, column=1, sticky="W")


# Target labels
target_labels = {}

target_labels["0"] = {}

j = 0

for i in range(20, 14, -1):
	target_labels["0"][str(i)] = Label(target_label_frames["0"], text=i, font=("Helvetica", 50), foreground="#333333", background="#add5d5")
	target_labels["0"][str(i)].grid(row=j, column=0, sticky="E", padx=20, pady=0)

	j += 1

target_labels["0"]["bulls"] = Label(target_label_frames["0"], text="Bulls", font=("Helvetica", 50), foreground="#333333", background="#add5d5")
target_labels["0"]["bulls"].grid(row=6, column=0, sticky="E", padx=20, pady=0)

target_labels["1"] = {}

j = 0

for i in range(20, 14, -1):
	target_labels["1"][str(i)] = Label(target_label_frames["1"], text=i, font=("Helvetica", 50), foreground="#333333", background="#add5d5")
	target_labels["1"][str(i)].grid(row=j, column=0, sticky="W", padx=20, pady=0)

	j += 1

target_labels["1"]["bulls"] = Label(target_label_frames["1"], text="Bulls", font=("Helvetica", 50), foreground="#333333", background="#add5d5")
target_labels["1"]["bulls"].grid(row=6, column=0, sticky="W", padx=20, pady=0)


# Frames surrounding all hit buttons
hitbuttons_box_frames = {}

hitbuttons_box_frames["0"] = Frame(target_chart_frames["0"])
hitbuttons_box_frames["0"].grid(row = 0, column = 1)

hitbuttons_box_frames["1"] = Frame(target_chart_frames["1"])
hitbuttons_box_frames["1"].grid(row = 1, column = 0)


# Frames surrounding groups of buttons of same value
hitbuttons_frames = {}

for i in range(2):
	hitbuttons_frames[str(i)] = {}

	hitbuttons_frames[str(i)]["bulls"] = Frame(hitbuttons_box_frames[str(i)], background="#d80027", padx=10, pady=10)
	hitbuttons_frames[str(i)]["bulls"].grid(row=6, column=0)

	k = 0

	for j in range(20, 14, -1):
		hitbuttons_frames[str(i)][str(j)] = Frame(hitbuttons_box_frames[str(i)], background="#d80027", padx=10, pady=10)
		hitbuttons_frames[str(i)][str(j)].grid(row=k, column=0)

		k += 1


# Hit button images
button_images = {}

button_images["0"] = PhotoImage(file="img/not_done.png")
button_images["1"] = PhotoImage(file="img/done.png")


# Add hit buttons into their group frames
buttons = {}

for p in ["0", "1"]:
	buttons[p] = {}

	for g in list(range(20, 14, -1)) + ["bulls"]:
		buttons[p][str(g)] = {}

		for n in range(3):
			buttons[p][str(g)][str(n)] = Button(hitbuttons_frames[p][str(g)], image=button_images["0"], command=lambda p=p, g=str(g), n=str(n): check(p, g, n), borderwidth=0, width=85, height=59)
			buttons[p][str(g)][str(n)].grid(row=0, column=n)


"""
TURN FRAME
"""


# Turn frame between player frames
turns_frame = Frame(main_frame, background="#add5d5")
turns_frame.grid(row=0, column=1, sticky="N")


# Turn indicator images
indicator_images = {}

indicator_images["0"] = PhotoImage(file="img/arrow_left.png")
indicator_images["1"] = PhotoImage(file="img/arrow_right.png")


# Turn indicator
turn_indicator = Label(turns_frame, image=indicator_images["0"], background="#add5d5", height=100)
turn_indicator.grid(row=0, column=0, columnspan=2, pady=(0, 0))


# Labelframe around turn labels
turn_labels_labelframe = LabelFrame(turns_frame, text="Turns", foreground="#333333", background="#add5d5", labelanchor="n", relief=RIDGE)
turn_labels_labelframe.grid(row=1, column=0, columnspan=2)


# Turn labels
turn_labels = {}

turn_labels["0"] = {}
turn_labels["1"] = {}

for i in range(1, 26):
	turn_labels["0"][str(i)] = ttk.Label(turn_labels_labelframe, text=str(i), justify=LEFT, foreground="#333333", background="#add5d5", font=("Helvetica", 11, "bold"))
	turn_labels["0"][str(i)].grid(row=i, column=0, sticky="W", pady=0, padx=(0, 10))

	turn_labels["1"][str(i)] = ttk.Label(turn_labels_labelframe, text=str(i), justify=RIGHT, foreground="#333333", background="#add5d5", font=("Helvetica", 11, "bold"))
	turn_labels["1"][str(i)].grid(row=i, column=1, sticky="E", pady=0, padx=(10, 0))


"""
PREPARE APP
"""


new_match()


"""
RUN APPLICATION
"""


root.mainloop()