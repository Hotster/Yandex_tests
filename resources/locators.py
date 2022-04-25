from selenium.webdriver.common.by import By


class SearchPageLocators:
    search_field = (By.ID,
                    "text")
    search_button = (By.CLASS_NAME,
                     "search2__button")
    suggest_field = (By.CLASS_NAME,
                     "mini-suggest__popup-content")
    search_result = (By.CLASS_NAME,
                     "Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl.organic__subtitle")
    images_link = (By.CSS_SELECTOR,
                     "a[data-id='images']")


class ResultPageLocators:
    link = (By.PARTIAL_LINK_TEXT,
            "tensor.ru")


class ImagesMainPageLocators:
    category = (By.CSS_SELECTOR,
                ".PopularRequestList-Item.PopularRequestList-Item_pos_0 .PopularRequestList-SearchText")


class ImagesResultPageLocators:
    input_field = (By.CLASS_NAME,
                     "mini-suggest__input")
    image = (By.CLASS_NAME,
             'serp-item_pos_0')
    next_button = (By.CLASS_NAME,
             'CircleButton_type_next')
    back_button = (By.CLASS_NAME,
             'CircleButton_type_prev')
    main_image = (By.CLASS_NAME,
                  'MMImage-Origin')
    main_container = (By.CLASS_NAME,
                  'MMImageContainer')
