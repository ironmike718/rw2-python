# Dictionaries

cars = { "dodge":"suv", "chevy":"sedan", "subaru":"crossover"}

band = {
    "vocals":"Plant",
    "guitar":"Page",
}

print(cars)
print(band)

print(type(cars))
print(len(cars))

print(cars["chevy"])
print(band.get("guitar"))

print(cars.keys())
print(cars.values())
print(cars.items())

band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})

print(band)

# Nested Dictionaries

member1 = {"name":"Plant","instrument":"Vocals"}
member2 = {"name":"Page","instrument":"Guitar"}
band = {"member1":member1, "member2":member2}
print(band)

print(band["member1"]["name"])

