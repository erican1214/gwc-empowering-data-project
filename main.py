# This code is written in python
# The pandas library is used for data processing and to read data files
from numpy import block
import pandas as pd
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Libraries for printing text slowly
import sys
import time

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame
lwd = pd.read_csv("livwell175.csv")

# Print out the number of rows and columns
# print(lwd.shape)

# Country
# listOfCountries = lwd["country_name"].unique()
# print(util.vformat_list(listOfCountries))
countryOneBooleanList = lwd["country_name"] == "Niger"
countryOneData = lwd.loc[countryOneBooleanList]

countryTwoBooleanList = lwd["country_name"] == "Namibia"
countryTwoData = lwd.loc[countryTwoBooleanList]

#  basic colors:
# 'blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'


# Function to print text slowly
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print('')


# Story
print_slow(
    "Niger and Namibia are two African countries with plenty of cultural and ethnic diversity. Niger resides in West Africa, with a population of around 27 million people. Namibia resides in Southwest Africa, with a polulation of 2.6 million people (as of 2023). Both countries consist of deserts and hot climates.\n"
)
print_slow(
    ">>Press enter to see a scatterplot about women living in these countries.<<"
)
input()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Scatter plot for urban areas affecting average education years
plt.rcParams['toolbar'] = 'None'

plt.scatter(x="DM_urban_p",
            y="ED_educ_years_mean",
            data=countryOneData,
            color="green",
            label="Niger")

plt.scatter(x="DM_urban_p",
            y="ED_educ_years_mean",
            data=countryTwoData,
            color="red",
            label="Namibia")
plt.legend()

plt.title("Living in Urban Areas Affecting Average Education Years for Women")

plt.xlabel("Living in urban areas (%)")

plt.ylabel("Average years of schooling")

plt.show(block=False)
plt.pause(1)

print_slow(
    "\n>>Click the square in the top right corner of the scatterplot to have the scatterplot fit the window.<<\n"
)

print_slow(">>Press enter to see description of data<<")
input()

# Data's relevance
yearMin1 = countryOneData["year"].min()
yearMax1 = countryOneData["year"].max()
print_slow("Data from Niger is from %s to %s" % (str(yearMin1), str(yearMax1)))

yearMin2 = countryTwoData["year"].min()
yearMax2 = countryTwoData["year"].max()
print_slow("Data from Namibia is from %s to %s" %
           (str(yearMin2), str(yearMax2)) + "\n")

# Story
print_slow(
    "From the LivWell Dataset, I noticed that there is a correlation between living in urban areas and average years of education for women.\n"
)
print_slow(
    "About 25-27% of Nigerien women live in urban areas. That means that about 73-75% of women live in rural areas. Additionally, the average years of education for Nigerien women is less than 2 years.\n"
)
print_slow(
    "Contrary to that, about 40-50% of Namibian women live in urban areas. Although that is only half the population, it is a significant difference from Nigerien women. Additionally, the average years of education for Namibian women is 7-9 years, which is 5-7 years higher than for Nigerien women.\n"
)

print_slow(
    ">>Press enter when you're ready to see a possible explanation contributing to this data.<<"
)
input()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print_slow(
    "\nIn Niger, it is mandatory for children from ages 7 to 15 to have an education, so it is odd to see that the data does not reflect that for women. This may be due the fact that the vast majority of women live in rural areas in desert land, which tend to be more poor than urban areas.\n"
)

print_slow(
    "In Namibia, although it also consists of desert land, the Namibian government has also been prioritizing children's education ever since they gained their independence from South Africa in 1990. The Namibian government has also implemented adult education programs to decrease the amount of illiterate people.\n"
)

print_slow(">>Press enter for possible research questions.<<")
input()

print_slow(
    "Some research questions to look into would be:\nWhat resources does the Nigerien government need to provide good education for Nigerien girls and women?\nWhy isn't education being prioritized for girls and women?\n"
)

print_slow(
    ">>Press enter to see another scatterplot regarding women's education.<<")
input()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Scatter plot for average education years affecting average marriage age
plt.clf()
plt.scatter(x="DM_age_marr_mean",
            y="ED_educ_years_mean",
            data=countryOneData,
            color="green",
            label="Niger")

plt.scatter(x="DM_age_marr_mean",
            y="ED_educ_years_mean",
            data=countryTwoData,
            color="red",
            label="Namibia")
plt.legend()

plt.title("Average Marriage Age for Women Affecting Average Education Years")

plt.xlabel("Average age at marriage")

plt.ylabel("Average years of schooling")

plt.draw()
plt.pause(1)

print_slow(
    "\n>>Click the square in the top right corner of the scatterplot to have the scatterplot fit the window.<<\n"
)

print_slow(">>Press enter to see description of data<<")
input()

# Data's Relevance
print_slow("Data from Niger is from %s to %s" % (str(yearMin1), str(yearMax1)))
print_slow("Data from Namibia is from %s to %s" %
           (str(yearMin2), str(yearMax2)) + "\n")

# Story
print_slow(
    "Also from the LivWell Dataset, I noticed that there is a correlation between average age of marriage and average years of education.\n"
)
print_slow(
    "On average, Nigerien women were married at the age of 14-16 with an education of only 2 years or less. On the other hand, on average, Namibian women were married at the age of 22-24 with an education of 7-9 years\n"
)

print_slow(
    ">>Press enter when you're ready to see a possible explanation contributing to this data.<<"
)
input()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print_slow(
    "\nChild marriage is very prominent in Niger, and many families prioritize having their daughters married at a young age. This may be tied to familial or cultural beliefs, but a large contibuting factor is that many of these women and their families live in poverty. Therefore, they rely on the future husband's income.\n"
)

print_slow(
    "\nHowever, this is very harmful for young girls, especially if they are being married against their will. Not only will the be dependent on their future husband, their education is no longer prioritized once they are married.\n"
)

print_slow(">>Press enter for possible research questions.<<")
input()

print_slow(
    "Some research questions to look into would be:\nWhat other ways can we reduce poverty for Nigerien families without child marriage?\nHow do we break the cycle of child marriage when it is heavily tied to familial and cultural beliefs?\nHow can we support married girls and women who want to continue their education?\n"
)

print_slow(">>End of Analysis<<")
