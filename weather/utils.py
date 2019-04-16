
MONTHS = {"01": "Jan", "02": "Feb", "03": "Mar",
          "04": "Apr", "05": "May", "06": "Jun",
          "07": "Jul", "08": "Aug", "09": "Sep", "10": "Oct",
          "11": "Nov", "12": "Dec"}


def prepare_tmax_dataset(serialized, country):
    d_set = []
    # for country in countries:
    label = []
    data = []
    for item in serialized:
        l = "{0}-{1}".format(item.get("year"), MONTHS[item.get("month")])
        label.append(l)
        data.append(item.get("value"))
    d_set.append({"data": data, "label": country})

    return {"data_set": d_set, "label": label}


def prepare_tmin_dataset(serialized, country):
    return prepare_tmax_dataset(serialized, country)


def prepare_rainfall_dataset(serialized, country):
    return prepare_tmax_dataset(serialized, country)


