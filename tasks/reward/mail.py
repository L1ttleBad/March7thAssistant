from managers.screen_manager import screen
from managers.automation_manager import auto
from managers.config_manager import config
from managers.logger_manager import logger
from managers.translate_manager import _


class Mail:
    @staticmethod
    def get_reward():
        if not config.mail_enable:
            logger.info(_("邮件奖励未开启"))
            return False
        screen.change_to('menu')
        if auto.find_element("./assets/images/menu/mail_reward.png", "image", 0.95, crop=(0.95, 0.1, 0.05, 0.6)):
            logger.hr(_("检测到邮件奖励"), 2)
            screen.change_to('mail')
            if auto.click_element("./assets/images/mail/receive_all.png", "image", 0.9):
                auto.click_element("./assets/images/base/click_close.png", "image", 0.9, max_retries=10)
            logger.info(_("邮件奖励完成"))
