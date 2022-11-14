import csv
import json

result = {}
with open("./beginnerPRO/playgrounds.csv", "r", encoding="utf8") as f:
    data = csv.DictReader(
        f, fieldnames=["ObjectName", "AdmArea", "District", "Address"], delimiter=";"
    )
    districtAdd = {}
    for n in data:
        if n["AdmArea"] == "AdmArea":
            continue
        try:
            result[n["AdmArea"]][n["District"]].append(n["Address"])
        except KeyError:
            try:
                if result[n["AdmArea"]]:
                    result[n["AdmArea"]].update({n["District"]: [n["Address"]]})
            except KeyError:
                result[n["AdmArea"]] = result.get(
                    n["AdmArea"], {n["District"]: [n["Address"]]}
                )


with open("./beginnerPRO/addresses.json", "w", encoding="utf8") as f_o:
    json.dump(result, f_o, ensure_ascii=False, indent=3)
