def has_path(obj, path: str):
    parts = path.split(".")
    cur = obj
    for p in parts:
        if isinstance(cur, dict) and p in cur:
            cur = cur[p]
        else:
            return False
    return True


fields = [
    "title",
    "phoneNumbers.primaryPhone",
    "phoneNumbers.additionalPhones",
    "categories.primaryCategory",
    "categories.additionalCategories",
    "websiteUri",
    "regularHours",
    "specialHours",
    "serviceArea",
    "labels",
    "openInfo.status",
    "profile.description",
    "moreHours",
    "serviceItems",
    "storeCode",
]

data = {
    "storeCode": "Bari",
    "title": "La Yogurteria",
    "phoneNumbers": {"primaryPhone": "351 414 1478"},
    "categories": {"primaryCategory": {}, "additionalCategories": []},
    "websiteUri": "https://www.layogurteria.it/",
    "regularHours": {"periods": []},
    "serviceArea": {
        "businessType": "CUSTOMER_LOCATION_ONLY",
        "places": {},
        "regionCode": "IT",
    },
    "openInfo": {"status": "OPEN"},
    "profile": {"description": "🍦"},
    "serviceItems": [],
}

missing = [f for f in fields if not has_path(data, f)]
present = len(fields) - len(missing)
rate = present / len(fields)


print(missing, present, rate)
