import csv


def dict_to_csv(my_dict: dict,
                save_location: str) -> None:
    with open(save_location, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(my_dict.keys()))
        writer.writeheader()
        writer.writerows(my_dict)
