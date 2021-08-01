world_languages = """English
Irish
Welsh
Spanish
French
German
Japanese
Dutch
Swedeish
Mandarin
Russian
Ukrainian
Catalan
Flemish
Afrikaans
Portuguese""".split()
sorted(world_languages,reverse = True)
world_languages.remove("Dutch")
world_languages.append("Dutch")
world_languages.sort()
language = world_languages.pop()
world_languages.append(language)
len(world_languages)
language = world_languages[15]
world_languages.remove(language)
world_languages.insert(15,language)
del world_languages[:]
print(world_languages)

