import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewsFeed:
    what_xpath = "//span[@class='pdngXS brdrBlackSM postWidth brdrRadiusXSM pointer lightTxt feedHover']"
    whats_txtbox_xpath ="//div[@class='ql-editor ql-blank']"
    whatsedit_txtbox_xpath = "//div[@class='ql-editor']"
    post_xpath = "//button[text()='Post']"
    logout_xpath = "//span[text()='Log out']"
    public_xpath = "//input[@id='public']"
    employeechck_xpath = "//input[@class='PrivateSwitchBase-input css-1m9pwf3']"
    partnerchck_xpath = "(//input[@class='PrivateSwitchBase-input css-1m9pwf3'])[4]"
    statuschck_xpath = "//input[@id='activeType']"
    threedots_xpath = "//div[@class='flexAutoRow alignCntr justifyCntr']"
    archive_xpath = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1slzbpg'])[2]"
    gallery_xpath = "//input[@id='imageType']"
    image_xpath = "//div[@class='auto-grid']//div[1]//span[1]//img[1]"
    video_xpath = "//input[@id='videoType']"
    youtube_xpath = "//span[@title='Youtube Url']"
    youtubeurl_xpath = "//input[@placeholder='Paste URL here']"
    done_xpath = "//button[normalize-space()='Done']"
    threedot_xpath = "(//*[name()='svg'][@class='pointer'])[1]"
    edit_xpath = "//li[normalize-space()='Edit']"
    update_xpath = "//button[text()='Update post']"
    delete_xpath = "//li[normalize-space()='Delete']"
    deletechckboox_xpath = "//input[@name='archive']"
    deletebutton_xpath = "//button[normalize-space()='Delete']"
    bookmark_xpath = "//li[normalize-space()='Bookmark']"
    explore_xpath = "//span[@aria-label='Explore bookmarks']"
    remove_xpath = "//span[text()='Remove']"
    filter_xpath = "//span[text()='Filter']"
    all_xpath =  "//input[@id='feedsAllField']"
    self_xpath = "//input[@id='feedsSelfField']"
    apply_xpath = "//button[normalize-space()='Apply']"
    share_xpath = "//span[text()='Share']"
    whatsapp_xpath = "//button[@aria-label='whatsapp']"
    facebook_xpath = "//button[@aria-label='facebook']"
    twitter_xpath = "//button[@aria-label='twitter']"
    linkedin_xpath = "//button[@aria-label='linkedin']"
    telegram_xpath = "//button[@aria-label='telegram']"
    instagram_xpath = "//div[@class='flexCol fxdSocialMediaSlider slideIn']//div[6]//div[1]//div[1]//div[1]"
    gmail_xpath = "//div[@class='flexCol fxdSocialMediaSlider slideIn']//div[7]//div[1]//div[1]//div[1]"
    comment_xpath = "(//span[text()='Comment'])[1]"
    commenttxtare_xpath = "//textarea[@id='outlined-basic']"
    send_xpath = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation primaryBg brdrRadius50 imgAvatarSM css-191um2i']"
    cancelcmnt_xpath = "//div[@class='flexAutoRow pointer pdngRXS']"
    comments_xpath = "(//span[text()='Comment'])[2]"
    replycmnt_xpath = "//span[text()='Reply']"
    replytxt_xpath  = "//textarea[@id='outlined-adornment-weight']"
    replysend_xpath = "//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div"
    viewreply_xpath = "//legend[@class='lightTxt headingSM pointer pdngHSM']"
    commentthreedot_xpath = "//span[@class='pointer']"
    commentedit_xpath = "//div[@id='demo-positioned-menu']//li[1]"
    commenteditsend_CSS_SELECTOR = "svg[data-testid='SendIcon']"
    commentdelete_xpath = "//span[@class='flexInline pointer']"
    commentconfirmdelete_xpath = "//button[normalize-space()='Delete']"





    def __init__(self, driver):
        self.driver = driver




    def clickOnwhat(self):
        self.driver.find_element(By.XPATH,self.what_xpath).click()

    def setwhats(self,whats):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whats)

    def clickonpost(self):
        self.driver.find_element(By.XPATH,self.post_xpath).click()

    def clickonlogout(self):
        self.driver.find_element(By.XPATH,self.logout_xpath).click()

    def setwhatso(self,whatso):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whatso)


    def clickonpublic(self):
        self.driver.find_element(By.XPATH,self.public_xpath).click()

    def clickonemp(self):
        self.driver.find_element(By.XPATH,self.employeechck_xpath).click()

    def clickonpartner(self):
        self.driver.find_element(By.XPATH,self.partnerchck_xpath).click()

    def setwhatson(self,whatson):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whatson)

    def clickonstatus(self):
        self.driver.find_element(By.XPATH,self.statuschck_xpath).click()

    def clickonthreedots(self):
        self.driver.find_element(By.XPATH,self.threedots_xpath).click()

    def clickonarchive(self):
        self.driver.find_element(By.XPATH,self.archive_xpath).click()

    def setgallery(self,absolute_path1):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path1)
        time.sleep(2)

    def setgallery(self,absolute_path2):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path2)
        time.sleep(2)

    def setgallery(self,absolute_path3):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path3)
        time.sleep(2)

    def setgallery(self,absolute_path4):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path4)
        time.sleep(2)

    def setgallery(self,absolute_path5):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path5)
        time.sleep(2)

    def clickonimage(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.image_xpath).click()

    def setoneimage(self, oneimage):
        self.driver.find_element(By.XPATH, self.whats_txtbox_xpath).send_keys(oneimage)

    def setfiveimages(self, fiveimages):
        self.driver.find_element(By.XPATH, self.whats_txtbox_xpath).send_keys(fiveimages)

    def setvideo(self,absolute_pathvideo):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.video_xpath).send_keys(absolute_pathvideo)
        time.sleep(2)

    def setwhatvideo(self,whatvideo):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whatvideo)

    def setwhatvideos(self,whatvideos):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whatvideos)

    def setwhatyoutube(self,whatyoutube):
        self.driver.find_element(By.XPATH,self.whats_txtbox_xpath).send_keys(whatyoutube)

    def clickonyoutube(self):
        self.driver.find_element(By.XPATH,self.youtube_xpath).click()

    def setyoutubeurl(self,youtubeurl):
        self.driver.find_element(By.XPATH,self.youtubeurl_xpath).send_keys(youtubeurl)

    def clickondone(self):
        self.driver.find_element(By.XPATH,self.done_xpath).click()

    def clickonthreedot(self):
        self.driver.find_element(By.XPATH,self.threedot_xpath).click()

    def clickonedit(self):
        self.driver.find_element(By.XPATH,self.edit_xpath).click()

    def setwhatedit(self,whatedit):
        self.driver.find_element(By.XPATH,self.whatsedit_txtbox_xpath).send_keys(whatedit)

    def clickonupdate(self):
        self.driver.find_element(By.XPATH,self.update_xpath).click()

    def clickondelete(self):
        self.driver.find_element(By.XPATH,self.delete_xpath).click()

    def clickondeletecheckbox(self):
        self.driver.find_element(By.XPATH,self.deletechckboox_xpath).click()

    def clickondeletebutton(self):
        self.driver.find_element(By.XPATH,self.deletebutton_xpath).click()

    def clickonbookmark(self):
        self.driver.find_element(By.XPATH,self.bookmark_xpath).click()

    def clickonexplore(self):
        self.driver.find_element(By.XPATH,self.explore_xpath).click()

    def clickonremove(self):
        self.driver.find_element(By.XPATH,self.remove_xpath).click()

    def clickonfilter(self):
        self.driver.find_element(By.XPATH,self.filter_xpath).click()

    def clickonall(self):
        self.driver.find_element(By.XPATH,self.all_xpath).click()

    def clickonself(self):
        self.driver.find_element(By.XPATH,self.self_xpath).click()

    def clickonapply(self):
        self.driver.find_element(By.XPATH,self.apply_xpath).click()

    def clickonshare(self):
        self.driver.find_element(By.XPATH,self.share_xpath).click()


    def clickonwhatsapp(self):
        self.driver.find_element(By.XPATH,self.whatsapp_xpath).click()

    def clickonfacebook(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.facebook_xpath).click()

    def clickontwitter(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.twitter_xpath).click()

    def clickonlinkedin(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.linkedin_xpath).click()

    def clickontelegram(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.telegram_xpath).click()

    def clickoninstagram(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.instagram_xpath).click()

    def clickongmail(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.gmail_xpath).click()

    def clickoncomment(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.comment_xpath).click()

    def setcommenttext(self,commenttext):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.commenttxtare_xpath).send_keys(commenttext)

    def clickonsend(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.send_xpath).click()

    def clickoncancelcmnt(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,self.cancelcmnt_xpath).click()

    def clickoncomments(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.comments_xpath).click()

    def clickonreplycmnt(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replycmnt_xpath).click()

    def setreplytext(self,replytext):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replytxt_xpath).send_keys(replytext)

    def clickonreplysend(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replysend_xpath).click()

    def clickonviewreply(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.viewreply_xpath).click()

    def clickoncommentthreedot(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentthreedot_xpath).click()

    def clickoncommentedit(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentedit_xpath).click()

    def setcommentedittext(self, commentedittext):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replytxt_xpath).send_keys(commentedittext)

    def clickoncommenteditsend(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.commenteditsend_CSS_SELECTOR).click()

    def clickoncommentdelete(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentdelete_xpath).click()

    def clickoncommentconfirmdelete(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentconfirmdelete_xpath).click()












