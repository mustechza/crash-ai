
def parse(doc):
    try:
        d = doc.get("document")
        if not d:
            return None

        f = d.get("fields", {})

        def get(v):
            if "doubleValue" in v:
                return float(v["doubleValue"])
            if "integerValue" in v:
                return int(v["integerValue"])
            if "stringValue" in v:
                return v["stringValue"]
            return None

        return {
            "id": d["name"].split("/")[-1],
            "multiplier": get(f.get("multiplier", {})),
            "timestamp": get(f.get("timestamp", {}))
        }

    except:
        return None
