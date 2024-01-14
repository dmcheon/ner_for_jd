from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import time
from tqdm import tqdm.notebook.tqdm as tqdm
import json

def get_web_page(url):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        return True, webpage
    except HTTPError as e:
        # Handle HTTP errors
        return False, ('HTTPError: ', e.code, url)
    except URLError as e:
        # Handle URL errors (e.g., the server could not be found)
        return False, ('URLError: ', e.reason, url)
    except Exception as e:
        # Handle other exceptions such as trying to decode a webpage with the wrong character set
        return False, ('General Error: ', e)
    else:
        return False, ('Request - unknown error!')

def parse_post_list(response):
    commonURL = 'https://academicjobsonline.org'
    post_list = []

    soup = BeautifulSoup(response.decode("UTF-8"), 'html.parser')

    job_posts = soup.find_all('div', class_='clr')

    for post in job_posts:
        university = post.find('b').find_all('a')[0].text
        if (len(post.find('b').find_all('a'))>1):
          department = post.find('b').find_all('a')[1].text
        else:
          department = ''
        job_details = post.find_all('li')

        for job_detail in job_details:
            job_code = job_detail.find('a').text
            job_title = job_detail.text.split(']')[1].strip().replace('\xa0', ' ').split('(')[0]
            try:
              deadline = job_detail.find('span', class_='purplesml').text.split('(')[1].strip().split('deadline')[1].strip().split(')')[0]
            except:
              deadline = ''
            apply_link = commonURL + job_detail.find('a', href=True)['href']

            post_list.append({
                  'university': university,
                  'department': department,
                  'job_code': job_code,
                  'job_title': job_title,
                  'deadline': deadline,
                  'apply_link': apply_link
                  })

    return post_list

def parse_job_post(response):
  soup = BeautifulSoup(response.decode("UTF-8"), 'html.parser')
  #Extracting job description
  job_description = soup.find('table', class_='ads').text.strip()

  return job_description


def get_description(url = 'https://academicjobsonline.org/ajo?joblist-0-0-0-0----d--'):
    message = ""

    true_or_false, response = get_web_page(url)
    if true_or_false == False:
        mail_title += " Found error "
        message += "WARNING! get_web_page function malfunction. \nDetails: \n"
        try:
            message += str(response)
        except:
            message += "Something wrong!"
            pass

    post_list = parse_post_list(response)

    for post in tqdm(post_list, total=len(post_list)):
      link = post['apply_link']
      true_or_false, response2 = get_web_page(link)

      if true_or_false == False:
        message = 'error found in ' + post['job_title']
        post['description'] = ''
        continue

      description = parse_job_post(response2)
      post['description'] = description

    return post_list

def save_json(data):
    output = dict()
    output['data'] = data

    file_path = "./data.json"
    with open(file_path, 'w', encoding='utf-8') as file:
      json.dump(output, file, indent="\t")

    return None