def upper(arr):
    result = []
    for item in arr:
        a = item.title()
        result.append(a)
    return result

print(upper(["mavis", "senaida", "letty"]))
