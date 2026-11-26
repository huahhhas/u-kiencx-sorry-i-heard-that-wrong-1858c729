LINE = "Sorry, I heard 'set a timer for pasta' as 'sue the Prime Minister' \u2014 I've already filed the paperwork."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(LINE)
