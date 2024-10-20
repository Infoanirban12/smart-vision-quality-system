import easyocr

reader = easyocr.Reader(['en'])

image_path ='/content/img_sauce.jpg'       # Path to the image

results = reader.readtext(image_path,detail=0) # detail=0 returns only the text

expiry_keywords = ['EXP', 'Expiry', 'Best before', 'Use by']
expiry_patterns = []

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
years = range(2025, 2032)
dates = [f"{day:02d}" for day in range(1, 32)]  # Assuming 1-31 as possible dates

# Adding formats
for month in months:
    for year in years:
        expiry_patterns.append(f"{month}/{year}")
        expiry_patterns.append(f"{month}-{year}")
        expiry_patterns.append(f"{month}{year}")
for date in dates:
    for month in months:
        for year in years:
            expiry_patterns.append(f"{date}/{month}/{year}")
            expiry_patterns.append(f"{date}-{month}-{year}")
            expiry_patterns.append(f"{date}{month}{year}")
            expiry_patterns.append(f"{date}.{month}.{year}")


#collecting expiry details
keyword = []
date= []

for line in results:
    # Checking if any keyword matches
    if any(keyword.lower() in line.lower() for keyword in expiry_keywords):
        keyword.append(line)
for box in results:
    # Checking if any pattern matches
    l=box.upper()
    if any(l.startswith(pattern[:3]) and l.endswith(pattern[-2:]) for pattern in expiry_patterns):
        date.append(box)

if keyword==[] and date==[]:
    print("No expiry details found.")
else:
    print("Expiry details found:")

# Printing expiry details if found
if keyword:
    for info in keyword:
        print(info)

if date:
    for info in date:
        print(info)


