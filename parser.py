# parser.py
def parse(item):
    try:
        doc = item.get("document")
        if not doc:
            return None

        f = doc["fields"]

        def v(x):
            if "doubleValue" in x:
                return float(x["doubleValue"])
            if "integerValue" in x:
                return int(x["integerValue"])
            return None

        return {
            "id": doc["name"].split("/")[-1],
            "multiplier": v(f.get("multiplier", {})),
            "timestamp": v(f.get("timestamp", {})),
        }
    except:
        return None
