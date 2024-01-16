from utils import functions

def test_get_format_date():
    assert functions.get_format_date('2018-12-23T11:47:52.403285') == '23.12.2018'

def test_get_mask():
    assert functions.get_mask("МИР 8665240839126074") == "МИР 8665 24** **** 6074"

    assert functions.get_mask("Maestro 3000704277834087") == "Maestro 3000 70** **** 4087"
    assert functions.get_mask("MasterCard 9454780748494532") == "MasterCard 9454 78** **** 4532"
    assert functions.get_mask("Mast 780748494532") == "Неправильная длина номера карты/счета"
    assert functions.get_mask("Visa Classic 2842878893689012") == "Visa Classic 2842 87** **** 9012"
    assert functions.get_mask("Счет 46765464282437878125") == 'Счет **8125'

def test_open_file():
    data = functions.open_file()
    assert data is not None
    assert isinstance(data, list)

def test_executed():
    data = functions.open_file()
    new_list = functions.list_executed(data)
    assert new_list is not None
    for i in new_list:
        assert i['state'] == 'EXECUTED'

