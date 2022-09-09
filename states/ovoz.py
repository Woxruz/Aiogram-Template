from aiogram.dispatcher.filters.state import State,StatesGroup

class OvozBerish(StatesGroup):
    tel_nomer = State()
    kod = State()
    # oxir = State()