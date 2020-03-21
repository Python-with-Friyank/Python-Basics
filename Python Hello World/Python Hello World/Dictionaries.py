customerdict = {"Name" : "Friyankk Parikh",
                "Cal" : 10/5,
                "Age" : 10,
                "Phone" : 987986897,
                "Address" : {
                    "Street" : "AB Street",
                    "Pin" : 98879,
                    "Landmark" : {
                        "NearBy" : "aa",
                        "OppositeTo" : "bb"
                    }
                }
                }
print(customerdict["Phone"])
print(customerdict["Address"]["Street"])
print(customerdict["Address"]["Landmark"]["OppositeTo"])