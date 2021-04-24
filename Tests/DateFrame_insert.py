# Функция для вставки строки в фрейм данных


def Insert_row(row_number, df, row_value):

    start_upper = 0
    end_upper = row_number
    start_lower = row_number
    end_lower = df.shape[0]
    upper_half = [*range(start_upper, end_upper, 1)]

    lower_half = [*range(start_lower, end_lower, 1)]
    lower_half = [x.__add__(1) for x in lower_half]
    index_ = upper_half + lower_half

    df.index = index_
    df.loc[row_number] = row_value
    df = df.sort_index()
    return df


# Давайте создадим строку, которую мы хотим вставить

row_number = 2

row_value = ['11/2/2011', 'Wrestling', 12000]

if row_number > df.index.max() + 1:

    print("Invalid row_number")

else:

    # Давайте вызовем функцию и вставим строку

    # на второй позиции

    df = Insert_row(row_number, df, row_value)

    # Распечатать обновленный фрейм данных

    print(df)