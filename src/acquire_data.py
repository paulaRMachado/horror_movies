
import requests
from bs4 import BeautifulSoup
import pandas as pd

#IMDB Aquisition
def imbd_section (url):
    """
    This function scrapes informaton (title, imdb_rating, US_box_office, runtime) from IMDB site using BeautifulSoup
    args: url
    return: a data frame
    """
    headers = {"Accept-Language": "en-US,en;q=0.5"}
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.content, "html.parser")

    result_titles = soup.find_all("h3", attrs = {"class": "lister-item-header"})
    result_rate = soup.find_all("div", attrs = {"class": "inline-block ratings-imdb-rating"})
    result_USbox = soup.find_all("p", attrs = {"class": "sort-num_votes-visible"})
    result_runtime = soup.find_all("span", attrs = {"class": "runtime"})

    titles = [i.getText().strip().split("\n")[1] for i in result_titles]
    rate = [i.getText().strip() for i in result_rate]
    us_box_office = [i.getText().strip().split("\n")[3][1:-1] for i in result_USbox]
    runtime = [i.getText().split(" ")[0] for i in result_runtime]

    imdb = {"title": titles,
         "imdb_rating": rate,
         "US_box_office": us_box_office,
         "runtime": runtime
    }
    return pd.DataFrame(imdb)

# 2. Running the function through different ranges
def get_IMDB():
    """
    This function compiles diferent pages from IMDB using the imdb_section function and assembles it all in one dataframe
    args: NO ARGS
    return: a data frame
    """    
    df_imdb1 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc")
    df_imdb2 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=51&ref_=adv_nxt")
    df_imdb3 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt")
    df_imdb4 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=151&ref_=adv_nxt")
    df_imdb5 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=201&ref_=adv_nxt")
    df_imdb6 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=251&ref_=adv_nxt")
    df_imdb7 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=301&ref_=adv_nxt")
    df_imdb8 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=351&ref_=adv_nxt")
    df_imdb9 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=401&ref_=adv_nxt")
    df_imdb10 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=451&ref_=adv_nxt")
    df_imdb11 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=501&ref_=adv_nxt")
    df_imdb12 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=551&ref_=adv_nxt")
    df_imdb13 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=601&ref_=adv_nxt")
    df_imdb14 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=651&ref_=adv_nxt")
    df_imdb15 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=701&ref_=adv_nxt")
    df_imdb16 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=751&ref_=adv_nxt")
    df_imdb17 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=801&ref_=adv_nxt")
    df_imdb18 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=851&ref_=adv_nxt")
    df_imdb19 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=901&ref_=adv_nxt")
    df_imdb20 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=951&ref_=adv_nxt")
    df_imdb21 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=1001&ref_=adv_nxt")
    df_imdb22 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=1051&ref_=adv_nxt")
    df_imdb23 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=1101&ref_=adv_nxt")
    df_imdb25 = imbd_section("https://www.imdb.com/search/title/?title_type=feature&genres=horror&sort=boxoffice_gross_us,desc&start=1201&ref_=adv_nxt")

    # 3. Putting the dataframe together
    imdb_df = pd.concat([df_imdb1, df_imdb2, df_imdb3, df_imdb4,df_imdb5, df_imdb6, df_imdb7, df_imdb8, df_imdb9, df_imdb10, df_imdb11, df_imdb12, df_imdb13, df_imdb14,df_imdb15, df_imdb16, df_imdb17, df_imdb18, df_imdb19, df_imdb20, df_imdb21, df_imdb22, df_imdb23, df_imdb25])
    imdb_df.to_csv("data/IMDB_info.csv")
    return imdb_df

def get_local(name):
    """This function gets a CSV from a local folder.
    args:
    :name: string. name to save the file
    returns a dataframe
    """
    # 0. Establish variables
    path = f"data/{name}.csv"
    
    # 1. We read from the path
    local_df = pd.read_csv(path)
    
    return local_df
