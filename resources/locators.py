from selenium.webdriver.common.by import By


class SearchPageLocators:
    search_field = (By.ID, "text")
    search_button = (By.CLASS_NAME, "search2__button")
    suggest_field = (By.CLASS_NAME, "mini-suggest__popup-content")
    search_result = (By.CLASS_NAME,
                     "Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl.organic__subtitle")


class ResultPageLocators:
    link = (By.PARTIAL_LINK_TEXT, 'tensor.ru')
