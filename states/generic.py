from aiogram.dispatcher.filters.state import State, StatesGroup


# ----REGISTRATION----
class Reg(StatesGroup):
	check_name = State()
	change_name = State()
	get_country = State()
	get_place = State()
	get_age = State()
	get_job = State()
	get_sphere = State()
	get_more_spheres = State()
	other_in_search = State()
	get_emoji = State()

	# By hand
	get_place_by_hand = State()
	get_sphere_by_hand = State()
	get_many_spheres_by_hand = State()


# ----MENU----
# ---States for connect from users to admins---
class Support(StatesGroup):
	get_question = State()


# ---States for settings user---
class Settings(StatesGroup):
	get_buttons = State()


# ---One click states---
class OneClick(StatesGroup):
	any_questions = State()


# ---One click categories states---
class Questions(StatesGroup):
	step1 = State()
	step2 = State()
	step3 = State()


class NoQuestions(StatesGroup):
	step1 = State()
	step2 = State()
	step3 = State()