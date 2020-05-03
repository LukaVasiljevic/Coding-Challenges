#Konverter rimskih brojeva

#potrebne su dve klase- rom_to_int i int_to_rom

rom_numbers = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def int_to_rom(n):
    rom = ''
    while n > 0:
        for i, j in rom_numbers:
            while n >= i:
                rom += j
                n -= i
    return rom


def rom_to_int(rom):
    result = 0
    for romValue, romDigit in rom_numbers:
        while rom.startswith(romDigit):
            result += romValue
            rom = rom[len(rom_numbers[0]):]
    return result


num = 449
roman = 'CDXLIX'
print(rom_to_int(roman))
print(int_to_rom(num))
