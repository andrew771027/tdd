from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    @skip
    def test_cannot_add_empty_list_items(self):

        # Edith 前往首頁，並不小心試著提交
        # 一個空的清單項目。他在空的輸入方塊中按下Enter

        # 首頁重新整理，有一個錯誤訊息
        # 說不能有空的清單選項

        # 他在是一次，在項目中加入一些文字，現在可以動作了

        # 離譜的是，現在他決定要提交地按個空白的清單項目

        # 他在清單網頁上看到類似的警告

        # 她可以填入一些文字來修正它
        self.fail('write me!')
