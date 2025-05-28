import os
import random
from faker import Faker

import file_operations


skills = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

replacements = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠', 'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠', 'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒', 'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠', 'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋', 'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋', 'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е', 'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋', 'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠', 'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋', 'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋', 'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def mod_symbols(skill):
    for cyrillic, runic in replacements.items():
        skill = skill.replace(cyrillic, runic)
    return skill


def selected_skills():
    selected = random.sample(skills, 3)
    runic_skills = []
    for skill in selected:
        runic_skills.append(mod_symbols(skill))
    return runic_skills


def dublicate(runic_skills):
    for number in range(10):
        file_name = 'forms/charsheet_count.svg'
        file_name = file_name.replace('count', str(number+1))
        fake = Faker("ru_RU")
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        job = fake.job()
        city = fake.city()
        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)
        runic_skills = selected_skills()
        charsheet = {
            'first_name': first_name,
            'last_name': last_name,
            'job': job,
            'town': city,
            'strength': strength,
            'agility': agility,
            'endurance': endurance,
            'intelligence': intelligence,
            'luck': luck,
            'skill_1': runic_skills[0],
            'skill_2': runic_skills[1],
            'skill_3': runic_skills[2]
        }
        file_operations.render_template('charsheet.svg', file_name, charsheet)


def main():
    dublicate(selected_skills())


if __name__ == '__main__':
    os.makedirs('forms', exist_ok=True)
    main()
