import requests
from bs4 import BeautifulSoup
import re

game_details = {
    "trending": {
        "name": [],
        "discount_pct": [],
        "discount_price": [],
        "original_price": [],
        "link": [],
        "icon": [],
    },
    "top-sellers": {
        "name": [],
        "discount_pct": [],
        "discount_price": [],
        "original_price": [],
        "link": [],
        "icon": [],
    },
    "most-popular": {
        "name": [],
        "discount_pct": [],
        "discount_price": [],
        "original_price": [],
        "link": [],
        "icon": [],
    },
    "coming-soon": {
        "name": [],
        "discount_pct": [],
        "discount_price": [],
        "original_price": [],
        "link": [],
        "icon": [],
    },
}


def get_offers(type="trending"):

    URL = "https://store.steampowered.com/specials/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    tab_content = soup.find("div", class_="tab_content_ctn sub")
    tab_categories = tab_content.find_all("div", id=True)

    for item in tab_categories:
        if "tab_content" in item["id"]:

            tab_item_names = item.find_all("div", class_="tab_item_name")
            tab_item_links = item.find_all("a", href=True)
            tab_item_disc_pct = item.find_all("div", class_="discount_pct")
            tab_item_disc_price = item.find_all("div", class_="discount_final_price")
            tab_item_ori_price = item.find_all("div", class_="discount_original_price")
            tab_item_icon = item.find_all("img", class_="tab_item_cap_img")

            for name, link, disc_pct, disc_price, ori_price, icon in zip(
                tab_item_names,
                tab_item_links,
                tab_item_disc_pct,
                tab_item_disc_price,
                tab_item_ori_price,
                tab_item_icon,
            ):
                if "NewReleases" in item["id"]:
                    game_details["trending"]["name"].append(name.text)
                    game_details["trending"]["link"].append(link["href"])
                    game_details["trending"]["discount_pct"].append(disc_pct.text)
                    game_details["trending"]["discount_price"].append(disc_price.text)
                    game_details["trending"]["original_price"].append(ori_price.text)
                    game_details["trending"]["icon"].append(icon["src"])

                if "TopSellers" in item["id"]:
                    game_details["top-sellers"]["name"].append(name.text)
                    game_details["top-sellers"]["link"].append(link["href"])
                    game_details["top-sellers"]["discount_pct"].append(disc_pct.text)
                    game_details["top-sellers"]["discount_price"].append(
                        disc_price.text
                    )
                    game_details["top-sellers"]["original_price"].append(ori_price.text)
                    game_details["top-sellers"]["icon"].append(icon["src"])

                if "ConcurrentUsers" in item["id"]:
                    game_details["most-popular"]["name"].append(name.text)
                    game_details["most-popular"]["link"].append(link["href"])
                    game_details["most-popular"]["discount_pct"].append(disc_pct.text)
                    game_details["most-popular"]["discount_price"].append(
                        disc_price.text
                    )
                    game_details["most-popular"]["original_price"].append(
                        ori_price.text
                    )
                    game_details["most-popular"]["icon"].append(icon["src"])

                if "ComingSoon" in item["id"]:
                    game_details["coming-soon"]["name"].append(name.text)
                    game_details["coming-soon"]["link"].append(link["href"])
                    game_details["coming-soon"]["discount_pct"].append(disc_pct.text)
                    game_details["coming-soon"]["discount_price"].append(
                        disc_price.text
                    )
                    game_details["coming-soon"]["original_price"].append(ori_price.text)
                    game_details["coming-soon"]["icon"].append(icon["src"])

    deals = game_details.get(type)
    return deals
