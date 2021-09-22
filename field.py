field={
    'A1': ' ',
    'A2': ' ',
    'A3': ' ',
    'B1': ' ',
    'B2': ' ',
    'B3': ' ',
    'C1': ' ',
    'C2': ' ',
    'C3': ' '
}

def draw_field():
    print(f'   A B C')
    print(f'   _ _ _')
    print(f'1 |{field["A1"]}|{field["A2"]}|{field["A3"]}|')
    print('   - - - ')
    print(f'2 |{field["B1"]}|{field["B2"]}|{field["B3"]}|')
    print('   - - - ')
    print(f'3 |{field["C1"]}|{field["C2"]}|{field["C3"]}|')
    print(f'   ‾ ‾ ‾')
