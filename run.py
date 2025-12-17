from checker.hasher import ImageHasher
from checker.similarity import SimilarityChecker
from checker.exif_reader import ExifReader
from checker.classifier import ImageClassifier
from checker.engine import ImageAuthenticityEngine

TARGET_IMAGE_0 = "test_images/test_image.jpeg"
TARGET_IMAGE_1 = "test_images/test_image_1.jpg"
TARGET_IMAGE_2 = "test_images/test_image_2.png"
REFERENCE_DIR = "reference_images"

hasher = ImageHasher()
similarity_checker = SimilarityChecker(hasher)
exif_reader = ExifReader()
classifier = ImageClassifier(similarity_threshold=85)

engine = ImageAuthenticityEngine(
    hasher=hasher,
    similarity_checker=similarity_checker,
    exif_reader=exif_reader,
    classifier=classifier
)

result = engine.analyze(TARGET_IMAGE_0, REFERENCE_DIR)
print(f"\nIMAGE : {TARGET_IMAGE_0}")
print("\nSimilarity Results:")
for item in result["similarities"]:
    print(f"- {item['image']}: {item['similarity']}%")
print(f"\nEXIF Metadata: {result["exif"] or "Missing"}")
print(f"\nFinal Verdict: {result["verdict"]}")
print("=============================================")

result_1 = engine.analyze(TARGET_IMAGE_1, REFERENCE_DIR)
print(f"\nIMAGE : {TARGET_IMAGE_1}")
print("\nSimilarity Results:")
for item in result_1["similarities"]:
    print(f"- {item['image']}: {item['similarity']}%")
print(f"\nEXIF Metadata: {result_1["exif"] or "Missing"}")
print(f"\nFinal Verdict: {result_1["verdict"]}")
print("=============================================")

result_2 = engine.analyze(TARGET_IMAGE_2, REFERENCE_DIR)
print(f"\nIMAGE : {TARGET_IMAGE_2}")
print("\nSimilarity Results:")
for item in result_2["similarities"]:
    print(f"- {item['image']}: {item['similarity']}%")
print(f"\nEXIF Metadata: {result_2["exif"] or "Missing"}")
print(f"\nFinal Verdict: {result_2["verdict"]}")