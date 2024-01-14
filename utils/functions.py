def output_last_tran(date_trans, descr_trans, trans_from):
    """Основная распечатка
    Сверху списка находятся самые последние операции (по дате)
    Последние 5 выполненных (EXECUTED) операций выведены на экран."""

# условия по EXECUTED
    print(f"<дата перевода> {date_trans} <описание перевода> {descr_trans}")
    print(f'<откуда>{trans_from} -> <куда>')
    print(f'<сумма перевода> <валюта>')


def get_format_date():
    """Дата перевода представлена в формате ДД.ММ.ГГГГ (пример: 14.10.2018)."""

    pass


def get_mask_number(account_number):
    """Номер карты замаскирован и не отображается целиком в формате
    XXXX XX** **** XXXX (видны первые 6 цифр и последние 4, разбито по
    блокам по 4 цифры, разделенных пробелом)"""

    if len(account_number) == 16:
        masked = account_number[:4] + " " + account_number[4:6] + "**" + " " + "****" + " " + account_number[-4:]
        return masked
    if len(account_number) == 20:
        masked = "**" + account_number[:4]
        return masked
    else:
        return "Неправильная длина номера карты"


def get_mask_account_number():
    """Номер счета замаскирован и не отображается целиком в формате  **XXXX
(видны только последние 4 цифры номера счета)."""
    pass
