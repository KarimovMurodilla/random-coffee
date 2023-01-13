from aiogram.dispatcher.filters.state import State, StatesGroup


class Reg(StatesGroup):
	check_name = State()
	change_name = State()
	get_country = State()
	get_place = State()
	get_place_by_hand = State()
	get_age = State()
	get_job = State()
	get_sphere = State()