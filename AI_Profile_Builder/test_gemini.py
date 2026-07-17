from utils.gemini import generate_profile


result = generate_profile(
    "Elon Musk",
    "CEO of Tesla and SpaceX",
    ["Wikipedia"]
)


print(result)