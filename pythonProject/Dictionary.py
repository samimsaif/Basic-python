# studentInfo = {
#     "Saif": {
#         "name": "saif",
#         "lacation": "Lakshmipur",
#         "study": 12,
#         "Group": "Science",
#         "Roll": 7,
#         "Number": 1648147680
#     },

# "Maisha": {
#     "name" : "Maisha",
#     "lacation" : "Dhaka",
#     "study" : 12,
#     "Group" : "Commerce",
#     "Roll" : 6,
#     "Number" : 1780409042
# },
# "year" : 1998
# }
# print(studentInfo["Maisha"]["Roll"])
# Accessing Item
# studentInfo['year']
# print(studentInfo['year'])
# studentInfo.get("Maisha")
# print(studentInfo.get("Maisha"))
# x = studentInfo.keys()
# print(x)
# m = studentInfo.values()
# print(m)
# Change Dictionary Items
# studentInfo = {
#     "Maisha": {
#         "name": "Maisha",
#         "lacation": "Dhaka",
#         "study": 12,
#         "Group": "Commerce",
#         "Roll": 6,
#         "Number": 1780409042
#     },
#     "year": 1998
# }
# studentInfo["year"] = 2005
# print(studentInfo["year"])
# # Update the "year" of the car by using the update() method:
# studentInfo.update({"Maisha" : "Maisha is a Doctor."})
# print(studentInfo["Maisha"])
#  Remove Dictionary Items : Pop Method
# studentInfo = {
#     "Maisha": {
#         "name": "Maisha",
#         "lacation": "Dhaka",
#         "study": 12,
#         "Group": "Commerce",
#         "Roll": 6,
#         "Number": 1780409042
#     },
#     "year": 1998
# }
# studentInfo.pop("Maisha")
# print(studentInfo)
#  Remove Dictionary Items : Pop Item Method
# studentInfo = {
#      "Maisha": {
#          "name": "Maisha",
#          "lacation": "Dhaka",
#          "study": 12,
#          "Group": "Commerce",
#          "Roll": 6,
#          "Number": 1780409042
#      },
#      "year": 1998
#  }
# studentInfo.popitem()
# studentInfo.popitem()
# print(studentInfo)
#  Print all key names in the dictionary, one by one:
# studentInfo = {
#      "Maisha": {
#          "name": "Maisha",
#          "lacation": "Dhaka",
#          "study": 12,
#          "Group": "Commerce",
#          "Roll": 6,
#          "Number": 1780409042
#      },
#      "year": 1998
#  }
# for x in studentInfo:
#     print(x)
# You can also use the values() method to return values of a dictionary:
# for x in studentInfo.values():
#     print(x)
#   Loop through both keys and values, by using the items() method:
# studentInfo = {
#      "Maisha": {
#          "name": "Maisha",
#          "lacation": "Dhaka",
#          "study": 12,
#          "Group": "Commerce",
#          "Roll": 6,
#          "Number": 1780409042
#      },
#      "year": 1998,
#     "Saif": {
#         "name": "saif",
#         "lacation": "Lakshmipur",
#         "study": 12,
#         "Group": "Science",
#         "Roll": 7,
#         "Number": 1648147680
#    }
#  }
# for item in studentInfo.items():
#     print(item)
#  Copy Dictionary
# studentInfo = {
#      "Maisha": {
#          "name": "Maisha",
#          "lacation": "Dhaka",
#          "study": 12,
#          "Group": "Commerce",
#          "Roll": 6,
#          "Number": 1780409042
#      },
#      "year": 1998,
#     "Saif": {
#         "name": "saif",
#         "lacation": "Lakshmipur",
#         "study": 12,
#         "Group": "Science",
#         "Roll": 7,
#         "Number": 1648147680
#    }
#  }
# saif = studentInfo.copy()
# print(saif)
# Copy Dictionary
saif = {
    "sum1": 20,
    "sum2": 40,
    "sum3": 60
}
# for item in saif.items():
#     print(item)
# print(saif)
# x = saif.copy()
# print(x)
# x = dict(saif)
# print(x)


