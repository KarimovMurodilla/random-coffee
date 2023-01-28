from aiogram.dispatcher.filters.state import State, StatesGroup


class Reg(StatesGroup):
	check_name = State()
	change_name = State()
	get_country = State()
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