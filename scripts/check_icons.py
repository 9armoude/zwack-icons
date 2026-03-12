import os

styles = ["outline", "filled", "broken"]
base = "icons"

icons = {}

for style in styles:
    path = os.path.join(base, style)
    if not os.path.exists(path):
        continue

    for f in os.listdir(path):
        if f.endswith(".svg"):
            name = f.replace(".svg", "")
            icons.setdefault(name, {})
            icons[name][style] = True

print("| Icon | " + " | ".join(styles) + " |")
print("|---|" + "|".join(["---"] * len(styles)) + "|")

for icon in sorted(icons):
    row = [icon]
    for style in styles:
        row.append("✓" if icons[icon].get(style) else "✗")
    print("| " + " | ".join(row) + " |")