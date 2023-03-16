from datetime import datetime
import numpy as np
from lxml import html

def get_datetime(s:str):
    date, time = s.split(', ')
    day, month, year = date.split('.')
    hour, minute = time.split(' ')[0].split('.')
    return datetime(int(year), int(month), int(day), int(hour), int(minute))

def parse_page(page:bytes):
    # Parse the content
    root = html.fromstring(page.content)

    # xpath stuff
    banner_xpath = '/html/body/div[1]/div/div/div/div'
    successful_xpath = banner_xpath + '/p[1]/strong'
    successful_count = np.int64(root.xpath(successful_xpath)[0].text.replace('.', ''))

    successful_time_xpath = banner_xpath + '//p[1]'
    successful_time_text = root.xpath(successful_time_xpath)[0].text_content()
    if not isinstance(successful_time_text, str):
        raise Exception('Could not get text')
    s = successful_time_text.split(' (')[-1].strip('()')
    successful_time = get_datetime(s)

    paid_out_count_xpath = banner_xpath + '/p[2]/strong'
    paid_out_text = root.xpath(paid_out_count_xpath)[0].text
    if not isinstance(paid_out_text, str):
        raise Exception('Could not get text')
    paid_out_count = np.int64(paid_out_text.replace('.', ''))
    paid_out_sum = np.int64(root.xpath(paid_out_count_xpath)[1].text.replace('.', '').split(' ')[0])

    paid_out_time_xpath = banner_xpath + '//p[2]'
    paid_out_time_text = root.xpath(paid_out_time_xpath)[0].text_content()
    if not isinstance(paid_out_time_text, str):
        raise Exception('Could not get text')
    s = paid_out_time_text.split(' (')[-1].strip('()')
    paid_out_time = get_datetime(s)

    return successful_count, successful_time, paid_out_count, paid_out_sum, paid_out_time