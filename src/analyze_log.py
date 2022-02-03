from .utils.analyze_log_utils import (
    read_file,
    write_file,
    get_data_per_customer,
    get_most_requested_dish_per_customer,
    get_food_quantity_per_customer,
    get_dishes_did_never_order_customer,
    get_days_never_went_customer,
)


def analyze_log(path_to_file):
    data = read_file(path_to_file)

    path_to_file = "data/mkt_campaign.txt"
    write_file(
        path_to_file,
        [
            get_most_requested_dish_per_customer(
                get_data_per_customer("maria", data)
            ),
            get_food_quantity_per_customer(
                get_data_per_customer("arnaldo", data), "hamburguer"
            ),
            get_dishes_did_never_order_customer(
                get_data_per_customer("joao", data), data
            ),
            get_days_never_went_customer(
                get_data_per_customer("joao", data), data
            ),
        ],
    )
