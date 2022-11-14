import csv
import json

result = []
with open("./beginnerPRO/exam_results.csv", "r", encoding="utf8") as file:
    data = csv.DictReader(file)
    for n in data:
        if len(result) == 0:
            result.append(
                {
                    "name": n["name"],
                    "surname": n["surname"],
                    "best_score": int(n["score"]),
                    "date_and_time": n["date_and_time"],
                    "email": n["email"],
                }
            )
        else:
            for j in range(len(result)):
                if (
                    result[j]["name"] == n["name"]
                    and result[j]["surname"] == n["surname"]
                ):
                    if int(n["score"]) >= int(result[j]["best_score"]):
                        result[j]["best_score"] = int(n["score"])
                        if n["date_and_time"] > result[j]["date_and_time"]:
                            result[j]["date_and_time"] = n["date_and_time"]
                        break
                    else:
                        break
            else:
                result.append(
                    {
                        "name": n["name"],
                        "surname": n["surname"],
                        "best_score": int(n["score"]),
                        "date_and_time": n["date_and_time"],
                        "email": n["email"],
                    }
                )
result = sorted(result, key=lambda x: x["email"])
with open("./beginnerPRO/best_scores.json", "w", encoding="utf8") as f_o:
    json.dump(result, f_o, indent=3)
