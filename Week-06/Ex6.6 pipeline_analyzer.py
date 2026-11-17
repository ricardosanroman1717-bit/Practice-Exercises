analyst = input("Analyst name:      ")
region = input("Region:            ")
n = int(input("Number of deals:    "))

if n < 1:
    raise SystemExit("Number of deals must be at least 1.")

print("\nEnter each deal (name and value):")
names = [input(f" Deal {i + 1} name:     ") for i in range(n)]
values = [float(input(f" {names[i]} value $: ")) for i in range(n)]
stages = [input(f" {names[i]} stage (Open/Won/Lost): ") for i in range(n)]

total_pipeline = sum(v for v in values)
total_won = sum(v for v, s in zip(values, stages) if s.lower() == "won")
total_open = sum(v for v, s in zip(values, stages) if s.lower() == "open")
count_won = sum(1 for s in stages if s.lower() == "won")
count_open = sum(1 for s in stages if s.lower() == "open")
largest_deal = max(v for v in values)
has_million = any(v >= 1_000_000 for v in values)
avg_deal = sum(v for v in values) / n

print(f"""
======= Sales Pipeline Report =======
Analyst : {analyst}
Region  : {region}
Deals   : {n}
-------------------------------------
Total pipeline : ${total_pipeline:,.2f}
Won revenue    : ${total_won:,.2f} ({count_won} deals)
Open pipeline  : ${total_open:,.2f} ({count_open} deals)
Avg deal size  : ${avg_deal:,.2f}
Largest deal   : ${largest_deal:,.2f}
$1M+ deal      : {'Yes' if has_million else 'No'}
=====================================
""")
