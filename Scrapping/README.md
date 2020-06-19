Data is compiled from [Practo](https://www.practo.com/)

First run Profile Scrapper. It saves doctors profile in doctors.csv. You can change location in *line 7* of code. 

Classes in HTML pages of [Practo](https://www.practo.com/) may change. So correct thoes after inspecting the elemnts in a prfile.

*Example: name = soup_new.find(class_="c-profile__title u-bold u-d-inlineblock")*
>$ python profile_scrapper.py

Comments Scrapper takes doctors.csv as input and output the comments extracted from particular doctors profile and saves it in comments/doctorname.txt format.
>$ python comments_scrapper.py

