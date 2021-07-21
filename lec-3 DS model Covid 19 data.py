"""
This file contains information regarding Covid 19 data in Data Structures.
Usage of DS as model.
author: Jasleen Kaur
email: jasleenbhambra@gmail.com
Date: July 20, 2021
"""
# reference -> https://www.covid19india.org/

India = {
    "name": "India",
    "confirmed": 59566858387,
    "active": 9555553,
    "recovered": 588155197,
    "deceased": 14526237
}

Punjab = {
    "name": "Punjab",
    "confirmed": 598387,
    "active": 953,
    "recovered": 581197,
    "deceased": 16237
}

Ludhiana = {
    "name": "Ludhiana",
    "confirmed": 87234,
    "active": 221,
    "recovered": 58566,
    "deceased": 167

}

Jalandhar = {
    "name": "Jalandhar",
    "confirmed": 42534,
    "active": 241,
    "recovered": 48566,
    "deceased": 107
}

Patiala = {
    "name": "Patiala",
    "confirmed": 10234,
    "active": 201,
    "recovered": 4566,
    "deceased": 267
}

districts = [Ludhiana, Jalandhar, Patiala]

Punjab["districts"] = districts

Haryana = {
    "name": "Haryana",
    "confirmed": 5985387,
    "active": 1053,
    "recovered": 5797,
    "deceased": 26237
}

Gurugram = {
    "name": "Gurugram",
    "confirmed": 87234,
    "active": 221,
    "recovered": 58566,
    "deceased": 167

}

Hisar = {
    "name": "Hisar",
    "confirmed": 42534,
    "active": 241,
    "recovered": 48566,
    "deceased": 107
}

Sonipat = {
    "name": "Sonipat",
    "confirmed": 10234,
    "active": 201,
    "recovered": 4566,
    "deceased": 267
}

districts = [Gurugram, Hisar, Sonipat]

Haryana["districts"] = districts

India["states"] = [Punjab, Haryana]

print("Covide 19 data of India: \n", India)